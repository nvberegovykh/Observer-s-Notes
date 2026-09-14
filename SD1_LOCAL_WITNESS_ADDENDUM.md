# SD1 candidate addendum — local witness closure

**Status:** application-supported candidate for the draft `VOL_1.3_SCALING_DISCIPLINE.md`. Do not treat this as a new primitive or a merged core rule yet.

## Why this addendum exists

The initial SD1 draft requires boundary review, invariants, new relations, deviation propagation, tail preservation, observer adequacy, capacity, recovery and evidence promotion. Three materially different applications exposed one relation that deserves to be made explicit before the draft is promoted:

- cardiovascular longitudinal research;
- strong-gravity numerical-relativity research;
- production release verification.

In all three, a large-scale result could look valid while the exact local observation or transformation that materially witnessed the result was ambiguous, failed, or simply never observed.

The missing object is not “more detail everywhere.” It is **addressable local witness structure**.

---

## 1 · Local observable entity

A **local observable entity** is the smallest entity that the current question and observation system can address without a further decomposition that is material to the claim.

It is resolution-relative.

It is not claimed to be the smallest thing that exists.

A participant-exam record, one waveform mode at one extraction scope, one workflow job step, one sensor channel, or one structural connection can each be a local observable entity in different models.

The required property is addressability: the model knows what was observed, through which method, at which time or order, under which scale state, and with which provenance/uncertainty/QC boundary.

---

## 2 · Two-sided traceability

A consequential scaled claim should support two complementary traversals.

### Downward witness closure

```text
claim
-> aggregate / interface state
-> transformations
-> local observable witnesses
```

The path need not materialize every microscopic state. It must reach the local observations and transformations that materially support the claim.

### Upward impact closure

```text
local observation or transform
-> derived states
-> aggregate / interface states
-> dependent claims
```

This allows a local correction to invalidate the claims that depend on it without rewriting unrelated branches.

A large model can therefore remain sparse while preserving fine audit resolution.

---

## 3 · Observed-surface closure

A pass at one aggregate node validates only the surface actually witnessed by its descendants.

Examples:

- a green production smoke does not verify an untested UI route;
- a reproduced cohort statistic does not close an unresolved assay semantic mapping;
- a one-history numerical-relativity closure does not become a multi-history result because its error is small.

Therefore:

> **Unobserved neighboring state does not inherit an aggregate pass.**

This is a claim-scope rule, not a command to observe everything.

---

## 4 · Candidate SD1 gates

### SD-G12 · Local witness closure

A consequential scaled claim preserves an auditable path to the local observable entities and transformations that materially witness it.

Where a local hard boundary, tail, exception, exclusion, missingness state, or unresolved semantic mapping can change the claim, that local state remains addressable after aggregation.

### SD-G13 · Upward impact closure

A material revision to a local observation, semantic mapping, calibration, clock, exclusion rule, transform, or dependency can identify which larger claims become stale or invalid without requiring unrelated branches to be reinterpreted.

### SD-G14 · Observed-surface closure

The language and authority of the scaled result do not extend beyond the explicitly observed witness surface. Untested neighboring state remains `UNOBSERVED`, `UNVERIFIED`, or equivalent rather than inheriting success.

---

## 5 · What this does not require

This addendum does **not** require:

- loading every low-level value into one reasoning context;
- observing every microscopic component;
- preserving all raw values forever;
- tracing every exploratory low-consequence summary with the same burden as a consequential decision;
- treating one missing local trace as proof that the whole containing system failed.

The burden should scale with claim strength, affected scope, consequence, irreversibility and correction difficulty.

The intended architecture is hierarchical and sparse:

```text
local observation
  -> local derived state
    -> interface state
      -> cohort / history / site / subsystem state
        -> domain claim
          -> containing-system claim
```

Each level carries references and transform semantics sufficient to descend when needed.

---

## 6 · Application evidence

### Cardiovascular

The MESA baseline preparation showed that a cohort-level reproduction could be numerically close while the ApoB-assay crosswalk or CAC representation remained semantically unresolved. A local semantic mapping can therefore be a hard upstream witness segment that an aggregate cannot repair.

### Strong gravity

The current `ExtraWaveforms.h5` implementation failure localizes to source-container -> exact-waveform-group selection. Treating that loader/interface failure as negative physics evidence would be a trace error. Likewise, a one-history seven-radius closure cannot climb to the multi-history node without the additional registered witnesses.

### Production operations

The Research.LIBER production smoke verifies exact release identity and an enumerated set of API/data invariants. Its success does not prove every untested UI interaction or route. The aggregate operational result therefore needs an observed-surface boundary.

These three cases are different enough that the relation is no longer tied to one scientific domain.

---

## 7 · Failure search

### LW-F1 · Trace bureaucracy

Every harmless exploratory value is forced through a heavyweight provenance graph.

**Correction:** require full witness closure only in proportion to claim/consequence. Exploratory summaries may remain explicitly non-authoritative.

### LW-F2 · False completeness

A graph contains a path for every claim, so the model is treated as complete.

**Correction:** traceability audits represented evidence. It does not prove that relevant unrepresented variables or blind regions do not exist.

### LW-F3 · Observer common cause

All local traces are generated by one summarizer, instrumentation lineage, model, or logging path.

**Correction:** SD1 independence/common-cause checks remain active. Many trace edges through one source do not become independent evidence.

### LW-F4 · Local anomaly absolutism

One noisy local observation is allowed to veto the aggregate forever.

**Correction:** local observations remain addressable; they can still be classified as noise, artifact or invalid acquisition through a justified rule. Preservation is not automatic promotion.

### LW-F5 · Infinite descent

The observer keeps asking for a more microscopic witness even when further decomposition cannot change the claim.

**Correction:** stop at the smallest observable entity material to the current question. Locality is question-relative.

### LW-F6 · Rhetorical overreach survives technically

The trace is correct, but prose still says “the platform is verified” or “the model is validated” when only a bounded surface passed.

**Correction:** observed-surface closure applies to result language and authority, not only data structures.

---

## 8 · Audit state

**KEEP AS AN ADDENDUM TO THE DRAFT; DO NOT YET MERGE AS CORE.**

The relation has survived two scientific domains and one operational domain, and it caught distinct failure modes in each. That is enough to justify explicit testing inside SD1.

It is not yet enough to claim a universal law of scale.

Before folding SD-G12—SD-G14 into the main scaling document, check at least one physical/engineering scaling case where local hard conditions and aggregate performance can diverge—for example infrastructure load, structural redundancy/common cause, or resource regeneration. Remove or narrow any gate that does not change the decision, evidence quality, or recoverability.

> **Field note:** *See far without making the nearby disappear.*