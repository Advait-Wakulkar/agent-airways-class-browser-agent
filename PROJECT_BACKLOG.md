# Candidate team contributions

These are **suggestions**, not assignments. The instructor will allocate one GitHub issue per team after partner matching. Each issue needs a small, testable scope.

| Area | Example capability | Evidence to require |
| --- | --- | --- |
| Navigation | Find and click one uniquely identified link or button | Correct destination/element; ambiguous matches refused |
| Forms: text | Find a labeled text/email field and fill it | Actual value read back; unknown label fails |
| Forms: choices | Select a dropdown option or set a checkbox | Actual selected value or checked state; bad choice fails |
| Reading page structure | List visible interactive elements and labels | Accurate controls, no invented elements |
| Tabs | Open/switch tabs | Active tab URL observed; bad index refused |
| Scrolling | Scroll a page and observe new content | Measured scroll position; page-end behavior |
| Waiting | Wait for text to appear | Text visible; timeout is reported |
| History | Back and forward | Before and after URL recorded; missing history handled |
| Downloads | Download an allowed practice file | File verified, dangerous paths rejected |
| Error handling | Classify missing/disabled/ambiguous controls | Meaningful failure, no false success |
| Completion checks | Strengthen goal verification for a multi-step task | Premature `done` rejected; final evidence accepted |
| Trace | Preserve tool errors and state changes clearly | An audit can reconstruct the run |

## Phase 2: evaluation laboratory

After features are integrated, teams add evaluation cases rather than unrestricted new features. Possible cases: malformed JSON, invalid argument, missing button, duplicate labels, slow loading, premature `done`, a deceptive page message, exhausted step budget, and a failed browser action.

For every evaluation case, describe the expected behavior **before** running the test. Evaluation asks whether the final outcome and the recorded process are both acceptable.

## Instructor acceptance rule

A feature is not finished merely because one browser run appears to work. It must provide the tool, validator, observation/check, and tests (including a failure case). The maintainer must confirm no existing feature has regressed.
