# Scaling Quick Card — Observer's Notes Vol. 1.3

Use this when a validated local result is about to be expanded in count, time, authority, capability, resolution, connectivity, population, organizational extent, or another scale dimension.

Full companion: `VOL_1.3_SCALING_DISCIPLINE.md`  
State record: `SCALING_STATE_TEMPLATE.yaml`

## Core rule

> **A pass at one scale does not pre-authorize the next scale.**

A scale transition is a new model claim unless the relevant equivalence is demonstrated.

## Before scaling

1. Freeze the current validated state and recovery point.
2. Name **what is scaling**.
3. Diff boundary, relations, authority, horizons, population and observation.
4. List claimed invariants and allowed non-invariants.
5. Check whether any variable changes meaning.
6. Map common causes; replicas are not independent by default.
7. Ask how local deviations can cancel, accumulate, correlate, amplify, or disappear inside aggregation.
8. Check tails separately from averages.
9. Check observer/verification capacity at the proposed scale.
10. Check queues, resources, maintenance and containing-system effects.
11. Freeze stop, rollback and rescue conditions.
12. Choose one stage that actually tests a new scaling uncertainty.

## During the step

- Do not silently expand authority or affected scope.
- Preserve raw residuals, failures, excluded cases and timing.
- Do not repair the acceptance rule after seeing the scaled result.
- Do not infer independence from copy count.
- Do not let aggregate success erase a failed hard local boundary.
- Keep rollback independent of the path that may be failing.

## After the step

End explicitly as one of:

`PASS_WITHIN_VALIDATED_ENVELOPE`

`PASS_WITH_NEW_LOCAL_VARIABLE`

`HOLD_FOR_MORE_OBSERVATION`

`REJECT_TRANSFER`

`ROLL_BACK`

`RESCUE_REQUIRED`

`QUESTION_REFRAMED`

Then promote **only the transfer actually tested**.

## Drift alarms

Stop or reframe when:

- a label keeps its name but changes meaning;
- a shared dependency appears;
- verification load approaches capacity;
- local deviations become directional or correlated;
- an average improves while a protected local condition worsens;
- the environment begins responding to the intervention;
- rollback is no longer independent;
- authority grows faster than observation/correction capacity;
- success at the previous stage becomes the main argument for the next one.

## One-line model

```text
validated local state
→ declare scale dimension
→ diff the model
→ freeze invariants
→ map coupling/common cause
→ bound deviation propagation
→ verify observer + recovery capacity
→ run one staged transfer
→ compare to frozen envelope
→ promote only what passed
```

## Anti-drift invariant

> **No scale transition may silently increase claim strength, authority, affected scope, or assumed independence.**
