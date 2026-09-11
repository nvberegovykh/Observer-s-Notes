# COMPASS Quick Card — Observer's Notes Vol. 1.2

Use this as the short execution surface. The full reasoning, examples, operational models, edge cases, and references are in `VOL_1.2_COMPASS.md`.

The card uses universal technical terms. The ocean expedition belongs to the explanatory story, not to the procedure.

## One cycle

1. **Define the question** — state the claim, uncertainty, or decision and the strength of answer required.
2. **Localize the system** — state boundary, scale, observation interval, horizon, assumptions, and value premise where relevant.
3. **Record evidence** — separate observed, constrained, modeled, inferred, assumed, and unresolved information; keep provenance and freshness.
4. **Identify hard boundaries** — state viability limits, required reserves, irreversible consequences, and rare catastrophic branches.
5. **Identify recovery conditions** — record viable recovery states and test whether recovery depends on the same failure path it is supposed to survive.
6. **Map dependencies** — trace constitutive relations, external conditions, delays, substitutes, and common-cause failures.
7. **Register candidate variables** — do not add a hidden variable to the reusable model merely because one application suggests it.
8. **Project relevant futures** — report ranges or distributions at the resolution justified by evidence; keep uncertainty and unresolved frontier separate.
9. **Select the consequential uncertainty** — prioritize leverage, boundary proximity, disagreement, tail risk, and decision-sensitive unknowns.
10. **Choose one bounded next step** — observation, retrieval, simulation, test, or intervention that can materially change the model or decision.
11. **Run the preservation check** — distinguish strict preservation from rescue / least-loss conditions; include non-action when the system is already failing.
12. **Execute only the justified step** — do not execute a whole imagined sequence because its first assumptions looked plausible.
13. **Measure again** — compare the realized state with the projected range and record residuals.
14. **Update and simplify** — preserve hard constraints, contradictions, provenance, recovery state, rare consequential branches, and validated variables while removing irrelevant detail.
15. **Stop explicitly** — finish in a named terminal state rather than an open reasoning loop.

## Candidate-variable promotion

A useful progression is:

**event → state change → missing or uncertain dependency → residual → candidate variable → operational definition → test → decision effect → recurrence → promotion**

Suggested statuses:

**candidate → local → recurrent/domain → core**

A variable may also become **dormant** or **rejected**, and a previously promoted variable may be demoted.

Promotion should be justified by enough of the following to match the claim being made: operational definition, observability or defensible bounds, plausible mechanism, residual reduction, decision relevance, alternative explanations, recurrence or independent mechanism, non-duplication, semantic stability, and justified complexity cost.

## Terminal states

- **Supported** — the target claim is supported to the declared strength.
- **Decision robust** — the action class remains stable under plausible refinements.
- **Preservation blocked** — a hard margin is negative or unresolved.
- **Rescue required** — strict preservation is no longer available; least-loss comparison is required.
- **External wait** — an external dependency is the true blocker.
- **Insufficient evidence** — no justified current step can resolve the key uncertainty.
- **Model contradiction** — current assumptions cannot jointly explain the observations.
- **Terminal system state** — the selected system has no modeled continuation under the stated definition.
- **Question reframed** — the original question was drawn at the wrong boundary, scale, or level.

## Core invariant

> The strength of the claim must not exceed the strength of the evidence, the model, and the preserved ability to correct it.

In the expedition story, this is what the compass is for: not choosing the destination, but keeping orientation while the surroundings remain uncertain.
