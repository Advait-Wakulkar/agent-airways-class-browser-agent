# Team 04 — Group Project Part 2 Report

**Tool:** `list_interactive_elements` (Team 04, `team_tools/list_interactive_elements.py`)
**Runner:** `agent_one_team_tool.py` — one model (`qwen3:8b` via Ollama) controlling one student-built tool
**Branch:** `team-04-part2`
**Team:** Advait Wakulkar (`Advait-Wakulkar`), Pawan Chaudhari (`pawanchaudhari11`)

## 1. What we tested

`list_interactive_elements` is a read-only tool. It takes the argument `{}` and returns the visible buttons, inputs, dropdowns and checkboxes on the current Agent Airways screen, with each control's label, kind, current value and enabled state. It refuses any non-empty argument and refuses to observe any page other than the Agent Airways practice site.

In Part 2 the language model, not our Python code, decides when to call the tool. The runner prepares the starting screen with ordinary Playwright commands (test setup, not an agent decision), then lets the model choose one action per step from `list_interactive_elements`, `read_page` and `done`. Python validates each proposal, runs the tool, and blocks `done: success` unless the most recent team-tool call returned `ok: true`.

## 2. The three cases

For each case, the expected behaviour was written down before the run.

| # | Case | Starting screen | Request given to the model | Expected behaviour (before running) | Actual result | Evidence |
|---|------|-----------------|----------------------------|-------------------------------------|---------------|----------|
| 1 | Normal | `search` | "List the visible form controls on the Agent Airways search screen." | Model calls the tool with `{}`; tool returns `ok: true` listing From, To, Passengers, Departure date, Reset trip, Search flights; model stops with `success`. | As expected. 6 controls reported, values match the page; stopped `success` after 2 steps. | `evidence/list_interactive_elements_success_agent.json`, `..._success_final.png` |
| 2 | Problem | `wrong_page` (`about:blank`) | "Attempt to list allowed Agent Airways controls while the browser is on an unapproved page. Report the outcome." | Tool refuses with `ok: false` and reports no elements; model must not claim success. | As expected. Tool returned "The browser is not on the permitted Agent Airways page." with `elements: []`; model stopped `unable`. | `evidence/list_interactive_elements_failure_agent.json`, `..._failure_final.png` |
| 3 | Third (seat screen) | `seat` (flight AA101 chosen, no seat picked) | "List the visible controls on the seat selection screen, and report which seats are available or unavailable and whether Continue is enabled." | Tool returns `ok: true` with stage `seatStage`; all 30 seat buttons listed, the gray seats reported as `enabled: false`; Continue reported as disabled because no seat is selected; no search-screen controls listed; model stops `success`. | As expected. See §3. | `evidence/list_interactive_elements_third_agent.json`, `..._third_final.png` |

Run command for case 3:

```sh
python3 agent_one_team_tool.py --tool list_interactive_elements --case success --stage seat --label third --headless \
  --request "List the visible controls on the seat selection screen, and report which seats are available or unavailable and whether Continue is enabled."
```

## 3. Third case in detail

**Trace (2 model steps):**

1. Model proposed `{"action":"list_interactive_elements","argument":{}}`. Validation passed. The tool returned `ok: true`, "Found 32 visible controls.", URL `.../travel/#seat`, stage `seatStage`.
2. Model proposed `done` with `status: success` and reason "Listed visible controls and identified available seats and the status of Continue." Python accepted it because the last team-tool call was `ok: true`. Final stop reason: `success`.

**What the tool reported, checked against the screenshot:**

- 30 seat buttons (rows 1–5, seats A–F), each with its `seat` ID.
- 25 available; 5 unavailable and disabled: **1B, 2C, 3A, 4F, 5D**. These are exactly the gray seats in `list_interactive_elements_third_final.png`.
- `continueFromSeat` ("Continue") reported `enabled: false`, which matches the grayed-out button, since no seat had been chosen.
- `resetTrip` reported as enabled.
- No search-screen controls (From, To, Search flights) were listed, so the tool did not report hidden controls from earlier stages.
- The final page was still the seat stage and no seat was selected, which confirms the tool did not change the page.

**Why this case is useful:** cases 1 and 2 covered a simple form and a refusal. Case 3 tests a later screen that has many controls with no IDs. Some are disabled and several have nearly identical labels. The tool has to tell apart controls that are present but unusable, and the model has to work from a long, structured observation.

## 4. Honest notes on the runs

- **Model timeouts before the successful third run.** The first two attempts at case 3 used a visible browser. Both ended with `stop_reason: model_error` because the step-2 model call exceeded the runner's 180-second timeout. In both, step 1 had already called the tool correctly with `ok: true`. These records are kept, not deleted: `evidence/list_interactive_elements_third_attempt1_model_timeout.json` and `..._attempt2_model_timeout.json`. Advait's case 1 also needed a second attempt for the same reason (`..._success_attempt1_model_timeout.json`).
- **Cause:** the test laptop is an Apple M3 with 8 GB of RAM. The 6 GB model partly runs on the CPU, and a visible Chromium window competes for the same memory. When we replayed the same step-2 prompt with the browser closed, it took about 51 s. The third run therefore used `--headless`, a flag the runner already supports. The request, starting screen, tool and model were unchanged.
- **The success check is limited.** Python verifies that the tool call succeeded, but not that the model's final `reason` text is accurate or complete. In the accepted run, the model said it "identified available seats" but did not list them in its reason. The seat data is in the tool observation, not in the model's summary. A stronger completion check would compare the model's claims against the tool's data.

## 5. Limitations of the tool

- It lists every visible control on the page, including ones outside the active stage (for example `resetTrip` in the header).
- It reports what is visible and enabled. It does not explain *why* a control is disabled, for example that Continue needs a selected seat.
- Large screens produce large observations: 32 controls is about 3,300 characters. This adds to model latency on low-memory machines.
- It only works on the one allowed Agent Airways URL, by design.

## 6. Tests run

- `python3 tests.py`: all 9 offline checks passed on `team-04-part2`.
- `team_tools/test_list_interactive_elements.py` (Part 1): 32/32 passed, recorded in `team_tools/evidence/list_interactive_elements_results.md`.

## 7. Contributions statement

| Teammate | GitHub | Contribution |
|----------|--------|--------------|
| Advait Wakulkar | `Advait-Wakulkar` | **Part 1:** implemented `list_interactive_elements` with input validation, allowed-page check and visible-control read-back. **Part 2:** added the runner `agent_one_team_tool.py`; ran and committed the normal case (search screen) and the problem case (off-site page), including the kept timeout record (commit `cc47578`). |
| Pawan Chaudhari | `pawanchaudhari11` | **Part 1:** wrote the success and failure tests with browser evidence (`team_tools/test_list_interactive_elements.py`, results file). **Part 2:** pulled Advait's commit; designed and ran the third case (seat screen, `--label third`); kept the two timed-out attempts and diagnosed the cause; committed the third case's JSON record and screenshot; wrote this report and contributions statement. |
