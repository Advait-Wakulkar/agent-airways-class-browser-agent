# Contributing to the shared browser agent

These directions apply to teams from **both** course sections. Work on the project as homework between class meetings.

## Before coding

Read the assigned GitHub issue. Confirm your team is working on **one** capability, not changing unrelated features. Discuss the action name, arguments, expected observation, validation rules, and failure cases.

The class starter intentionally uses ordinary Python: functions, dictionaries, lists, `if` statements, and loops. Avoid unnecessary classes, lambdas, comprehensions, and agent frameworks.

## A team's workflow

1. **Fork this repository** on GitHub (or use a branch if the instructor has granted you collaborator access).
2. Clone the fork locally. One teammate may add the other teammate(s) as collaborators to the fork.
3. Create a descriptive branch, such as `team-03-fill-text`. Do not commit directly to the main repository's `main`.
4. Implement the assigned feature in the smallest understandable change.
5. Run `python tests.py` (on some Macs, `python3 tests.py`).
6. Add tests, a failed-case example, and a short trace from a real browser run if your tool interacts with the browser.
7. Push the team branch and open **one pull request** against `onyourmark/agent-airways-class-browser-agent:main`.
8. Fill out the pull-request template, link the assigned issue (`Closes #N`), and list what each teammate contributed.
9. Respond to review comments. Do not merge your own pull request.

The TA or designated integration team may help with review and merge conflicts. The instructor or designated maintainer makes the final merge decision.

## Minimum requirements for a new tool

- A clear, narrow tool name and documented argument shape
- Deterministic validation: disallowed or malformed proposals never execute
- Exactly one proposed agent action per model turn
- Browser observations reported as data, not instructions
- A meaningful read-back/check after any operation that changes the page
- A clear result when the target is missing, ambiguous, disabled, or blocked
- At least one success test and one failure/edge test
- A demonstration trace that distinguishes model proposal, action, observation, and Python's check

When extending the simple dispatcher in `browser_agent.py`, keep existing tools functioning. Add the tool's name and arguments to the model-facing prompt **and** to Python's validator. A prompt description alone does not enforce anything.

## Tests and review

Every team runs tests locally. GitHub also has a lightweight automated check for the same offline tests; the repository maintainer must verify that GitHub Actions is enabled.

Reviewers should ask: Does the tool do what it claims? Can a wrong proposal be blocked? Does it report what actually happened? Does failure appear in the trace? Does the code still run on Windows and macOS? Did the change break earlier capabilities?

Changes involving purchases, messages, personal accounts, credentials, or other effects outside the practice site are out of scope unless explicitly approved.

## What to include in the pull request

Describe the new capability, normal demo, failure demo, tests run, limitations, and team contributions. Do not paste credentials, real student data, or sensitive browser screenshots.

## Before another team starts

After a contribution is approved and merged, other students can pull the newest `main` branch. Each team should coordinate with the integration manager to minimize simultaneous edits to the central tool list and dispatcher.
