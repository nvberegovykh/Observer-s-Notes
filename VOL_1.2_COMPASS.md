# Observer's Notes — Vol. 1.2

# COMPASS

## An Ocean Expedition for Grounded Exploration

**Extension 1**

**Status:** working operational volume. The ocean-expedition form is intentional, but every nautical image in this volume has a fixed technical counterpart. The metaphor is an orientation layer, never a source of evidence.

**Purpose:** turn the post-publication extensions of *Observer's Notes* into a reusable exploration instrument. Vol. 1 described a garden: dependency, maintenance, viability, and generative conditions. Vol. 1.2 moves offshore. A garden can often be walked and inspected directly; an ocean cannot. Navigation therefore requires charts, soundings, margins, course correction, recovery routes, and disciplined treatment of what remains beyond sight.

The central operational claim is modest:

> **Do not try to hold the whole possible world in memory. Maintain a grounded local chart, keep its uncertainty visible, preserve the vessel and return routes, and spend resolution where new evidence can materially change the course.**

**Provenance:** the conceptual extensions in this volume grew from post-publication working discussions between Nikita Beregovykh and ChatGPT in 2026. External references are listed separately as neighboring formal traditions, notation sources, or grounding for specific operational claims. They are not presented as the origin of the Observer's Notes model.

---

# 0. The Expedition Legend

The nautical language is fixed so that the story remains useful without becoming dreamy.

| Expedition term | Technical meaning |
|---|---|
| **Ocean** | the larger possibility space beyond the current local model |
| **Vessel** | the selected system being analyzed or acted through |
| **Hull** | identity invariants and tolerances that keep the selected system recognizable |
| **Seaworthiness** | current viability margins |
| **Cargo** | irreplaceable or hard-to-reconstruct state, memory, data, specimens, identity, or resources |
| **Crew / helm** | actors, control authority, and mechanisms able to change the system |
| **Chart** | the current explicit local model |
| **Compass** | the reusable protocol in this volume for maintaining and updating that model |
| **North** | the declared question, target claim, or decision objective |
| **Heading** | the next bounded observation, test, retrieval, simulation, or action |
| **Sounding** | a measurement, observation, test, or evidence-producing probe |
| **Current** | an external influence or dependency that changes future state |
| **Wind / weather** | uncertainty, disturbance, or changing external conditions |
| **Reef / shoal** | a hard constraint, failure boundary, legal/safety limit, or irreversible hazard |
| **Margin under keel** | reserve between current/projected state and a hard boundary |
| **Harbor** | a known viable or recoverable state |
| **Lifeboat / return route** | an independent recovery, rollback, substitution, or rescue path |
| **Wake** | history of realized changes and evidence left behind |
| **Logbook** | auditable provenance, versions, assumptions, observations, and decisions |
| **Uncharted water** | evidence-backed unresolved territory, not imaginary futures |
| **Fleet** | multiple observers, agents, tools, or teams sharing a common chart |

**Rule of interpretation:** if the nautical language and the technical definition ever diverge, the technical definition controls.

The metaphor may suggest a question. It may never establish a fact.

---

# 1. The Compass Is an Instrument, Not a Mood

## 1.1 The Compass state

A Compass run maintains an explicit state at time `t`:

`C_t = {Q, S, B, σ, Δt, H, W, Θ, X, D, V, G, E, P, U, A, R, L}`

where:

- `Q` — **North**: the question, claim, or decision being pursued;
- `S` — selected **vessel/system**;
- `B` — system boundary;
- `σ` — scale;
- `Δt` — observation / evaluation interval;
- `H` — future horizon or set of horizons;
- `W` — value premise when a decision or preservation claim is involved;
- `Θ` — declared assumptions;
- `X` — variable registry, including candidate and promoted hidden variables;
- `D` — dependency / interaction graph;
- `V` — viability and preservation margins;
- `G` — hard gates, constraints, and terminal conditions;
- `E` — evidence ledger with provenance and freshness;
- `P` — projected reachable intervals / distributions relevant to the question;
- `U` — unresolved territory and model disagreement;
- `A` — candidate observations, tests, simulations, or actions;
- `R` — recovery, rollback, substitute, and rescue paths;
- `L` — logbook: model versions, changes, realized outcomes, and reasons.

The state is intentionally larger than a single equation. A complex model is safer when uncertainty, assumptions, evidence, and recovery are not compressed into one score.

## 1.2 Minimum output of every Compass cycle

A Compass cycle is incomplete unless it can externally report:

1. **North:** what exact question or claim is being pursued;
2. **Current chart:** what system, boundary, scale, horizon, and assumptions are active;
3. **Soundings:** what is directly observed / measured and where it came from;
4. **Inferences:** what is derived rather than directly observed;
5. **Open water:** what remains unresolved and why it is suspected to matter;
6. **Reefs:** what hard boundaries or irreversible hazards constrain action;
7. **Harbors / return routes:** what viable recovery states remain reachable;
8. **Candidate hidden variables:** what application-specific reasoning exposed;
9. **Promotion status:** which variables are merely plausible, locally supported, recurrent, or reusable;
10. **Projected waters:** what future intervals matter to the decision;
11. **Next heading:** the smallest justified evidence-producing step;
12. **Stop / turn condition:** what observation would stop, redirect, or terminate the current route.

This is an auditable external state representation. It is not a request to expose private chain-of-thought.

## 1.3 The navigation invariant

At every cycle:

> **The strength of the claim must not exceed the strength of the chart, the soundings, and the preserved ability to correct course.**

That is the core invariant of Compass.

---

# 2. Leaving Harbor — Localize Before Sailing

Vol. 1 already established the base architecture [R0]: select the system, purpose, scale, and interval; define identity and viability; map dependencies; state the value premise before optimization; and attach intervention to measurement, reversibility where possible, verification, and a stopping condition.

Compass begins by making that localization executable.

## 2.1 Fix North

Before generating explanations or options, write one sentence that identifies the target:

- **descriptive North:** what is happening?
- **causal North:** what changes what?
- **predictive North:** what states remain reachable?
- **diagnostic North:** what hidden variable or dependency could explain the residual?
- **decision North:** which admissible action best serves the declared value premise?
- **preservation North:** can the selected system remain viable / recoverable through the change?

Different Norths can use the same data but require different evidence.

## 2.2 Draw only the local chart

Do not model the entire ocean.

Declare:

- vessel/system `S`;
- boundary `B`;
- scale `σ`;
- observation interval `Δt`;
- future horizon `H`;
- assumptions `Θ`;
- value premise `W` where needed.

A local chart is not a claim that nothing exists outside it. It is a claim about what is currently represented.

## 2.3 Mark chart provenance

Every state entry should be classed as one of:

- **MEASURED** — direct observation or test;
- **CONSTRAINT** — physical, logical, geometric, legal, or operational bound;
- **MODEL** — simulation, equation, estimator, or predictive model;
- **INFERRED** — supported indirectly by relations among observations;
- **ASSUMED** — introduced to make the current model tractable;
- **OPEN** — unresolved but evidence suggests the chart may be incomplete.

If provenance is unknown, mark it unknown. Do not silently upgrade it.

---

# 3. Soundings — Evidence Before Detail

A sailor does not infer the seabed from the beauty of the horizon. Compass similarly distinguishes what is observed from what is imagined.

## 3.1 Evidence ledger

For each evidence item `e` record:

`e = {id, claim_supported, source, method, timestamp, scope, uncertainty, independence, disturbance}`

Important fields:

- **source:** where it came from;
- **method:** how it was produced;
- **timestamp / version:** whether it may now be stale;
- **scope:** which region of the chart it actually supports;
- **uncertainty:** measurement/model uncertainty;
- **independence:** whether apparently separate evidence shares the same source or assumption;
- **disturbance:** whether measuring changed the system materially.

## 3.2 Evidence levels

Do not use a local check to prove an end-to-end claim.

A useful ladder is:

- identity / checksum evidence;
- local unit behavior;
- interface / integration behavior;
- end-to-end realized path;
- repeated behavior under materially different conditions.

NASA systems-engineering guidance similarly distinguishes component/end-item verification, complete-system integration, and end-to-end validation [R10].

## 3.3 Independent soundings

Several measurements are not independent merely because they are numerous.

Shared sensor, shared calibration, shared model, shared dataset, shared prompt, or shared assumption can produce correlated agreement.

Compass therefore records **method diversity**, not only count.

---

# 4. Currents Beneath the Surface — Dependencies and Hidden Variables

This chapter is the main bridge from story to reusable model.

Real applications force a general model through long logical chains. Those chains expose variables that were invisible at the abstract level. That is useful only if the variables are promoted carefully instead of being added because one story made them sound important.

## 4.1 From narrative event to candidate variable

When a use case exposes something unexpected, do not immediately edit the general formula.

Trace the chain:

`observed event -> state transition -> dependency -> residual / mismatch -> candidate variable -> operational definition -> test -> decision effect -> recurrence -> promotion`

Each arrow must be externally describable.

### Example pattern

A live platform update appears successful locally but users still cannot complete a workflow.

Story-level observation:

> "The service is up, but the journey is still broken."

Technical chain:

1. service health passes;
2. end-to-end transaction fails;
3. transaction depends on identity authority;
4. identity authority is reachable only through a credential path;
5. recovery uses the same credential path;
6. therefore **recovery-path independence** is a candidate variable that was absent from the simpler model.

The story exposed the variable. The chain justifies why it exists.

## 4.2 Variable registry

Every variable in `X` receives a status:

- `OBSERVED` — directly measured state variable;
- `DERIVED` — calculated from established variables;
- `CANDIDATE` — plausible hidden variable exposed by a residual, failure, or application chain;
- `LOCAL` — candidate has operational definition and local evidence;
- `RECURRENT` — local variable recurs in a materially different application or follows from an independently grounded mechanism;
- `CORE` — promoted into the reusable Compass template;
- `REJECTED` — tested and unsupported / redundant for the present purpose;
- `DORMANT` — possibly relevant but not worth resolving under the current North.

## 4.3 Candidate-variable record

For candidate `x*`, store:

`x* = {name, discovered_from, operational_definition, observable_proxy, mechanism, evidence, alternatives, decision_effect, recurrence, promotion_status}`

A candidate is not a fact until the relevant fields are supported.

## 4.4 Promotion gate

A hidden variable may be promoted from an application into the reusable Compass state only when enough of the following survive examination:

1. **Operationality:** the variable can be defined independently of the story that suggested it.
2. **Observability:** it can be measured, bounded, or represented by a defensible proxy.
3. **Mechanistic relevance:** there is a plausible dependency path connecting it to modeled outcomes.
4. **Residual reduction:** including it explains a repeated mismatch, improves prediction, or resolves a contradiction without merely overfitting the same case.
5. **Decision relevance:** varying it can cross a decision, viability, preservation, or explanation boundary.
6. **Alternative challenge:** simpler explanations have been checked where practical.
7. **Recurrence:** it appears in a materially different application, dataset, scale, or independently grounded mechanism.
8. **Non-duplication:** it is not just a renamed existing variable.
9. **Stability:** its meaning survives reasonable changes of representation.
10. **Cost justification:** the added model complexity is warranted by the information or decisions it improves.

Promotion does **not** require every item in every domain. The reason for promotion must be written.

## 4.5 Cross-case recurrence is stronger than narrative repetition

Repeating the same story in different words is not recurrence.

A strong recurrence test asks whether the variable appears under materially different conditions.

Examples:

- `recovery-path independence` appears in software credentials, emergency power, biological redundancy, and institutional succession;
- `observer disturbance` appears in ecology, debugging, medicine, and social measurement;
- `common-cause dependency` appears in redundant servers sharing one power source, two pumps sharing one intake, or multiple agents sharing one flawed dataset.

When a variable survives translation across domains while retaining the same operational relation, it becomes a stronger candidate for the general template.

## 4.6 Demotion is allowed

A variable promoted earlier can be demoted if later evidence shows it is redundant, misleading, domain-specific, or not decision-relevant.

Compass must be able to simplify its own chart.

---

# 5. Reefs and Harbors — Preservation Evaluation

The first obligation of navigation is not to maximize distance traveled. It is to know what must remain intact for navigation to continue.

## 5.1 Preservation is selected continuity, not frozen material

For selected system `S`, preservation asks:

> After an action or disturbance, does enough of the selected organization, dependency base, viability, and recoverability remain for the valued system to stay viable, remain identifiable, or return to an acceptable state within the declared interval and horizon?

The same material need not remain.

A server can be replaced while a service is preserved. A structural member can be replaced while a load path and use are preserved. A scientific model can change while evidence and reproducibility are preserved.

Conversely, material can remain while the system is lost.

This is compatible with viability theory's concern with trajectories remaining inside constraints, while Compass uses viability as one component of a broader localized model rather than claiming equivalence to Aubin's framework [R1].

## 5.2 Preservation vector

For action `a`, project each hard preservation dimension into a post-action margin interval:

`m_j(a) = [lower_j, upper_j]`

Useful dimensions include:

| Compass image | Technical dimension | Question |
|---|---|---|
| hull | identity margin `M_I` | Are defining invariants within tolerance? |
| seaworthiness | viability margin `M_V` | Are operating / survival conditions viable? |
| rigging / supplies | dependency margin `M_D` | Are constitutive dependencies, buffers, substitutes, and interfaces available? |
| propulsion / steerage | continuity `C` | Can required function continue through the intervention? |
| harbor / lifeboat | recoverability `R` | Is there an evidence-backed path back to a viable state? |
| helm | access/control `A_C` | Will recovery actors still be able to reach/control the system? |
| cargo | irreplaceable-state integrity `K` | Are unique states, records, keys, specimens, or memory protected? |
| instruments | verification capacity `Q_V` | Can we know whether preservation succeeded? |

These dimensions are not assumed independent.

## 5.3 Required reserve

For each hard dimension declare reserve `r_j >= 0`.

Strict preservation requires:

`lower(m_j(a)) >= r_j`

for every hard dimension, plus joint/common-cause checks.

A zero reserve may be logically admissible but operationally fragile.

## 5.4 Recovery-path independence

A return route must survive the failure it is intended to recover from.

Examples:

- backup credentials stored behind the same broken identity service are not an independent recovery path;
- emergency power sharing the same flooded switchgear is not independent;
- a rollback requiring the schema that the migration destroys is not a rollback;
- several AI agents sharing the same corrupted source are not independent verification.

This variable became visible through application chains and therefore belongs explicitly in Compass.

## 5.5 Rescue / least-loss mode

Strict preservation cannot be required when the vessel is already on the reef.

If no available action, including non-action, keeps all hard margins above reserve:

- switch mode from **PRESERVE** to **RESCUE**;
- include non-action as a candidate;
- compare time-to-failure, irreversible loss, recoverability, and protected cargo;
- preserve future recovery capacity where possible;
- state whose value premise and authority govern the choice;
- do not describe the result as strict preservation.

## 5.6 Multiple horizons

A route can be safe for ten minutes and fatal by morning.

Evaluate multiple horizons when delayed effects matter:

`H = {H_short, H_operational, H_recovery, H_long}`

Report horizon reversals instead of averaging them away.

## 5.7 Preservation is not maximum stability

Maximum stability can prevent adaptation, repair, or generation. Ecological research distinguishes resilience from narrower notions of stability [R2].

Compass therefore distinguishes:

- identity preservation;
- viability preservation;
- generative preservation / optionality.

These may conflict and must remain separately visible.

---

# 6. The Open Sea — Reachable Futures and Interestingness

## 6.1 Interestingness is local future structure

An element is interesting, within the declared chart, when its state or alteration has leverage over a broad and structured set of consequential reachable futures.

Interestingness depends on:

- boundary;
- assumptions;
- scale;
- horizon;
- selected projection axes;
- current evidence.

It is not an intrinsic property of the object.

## 6.2 Not raw branch count

A noisy buoy can generate enormous state entropy without changing the ship's route. A small rudder movement can have few immediate states but reorganize the entire reachable coast.

Therefore ask:

> **How much does this element reshape consequential reachable future-space?**

not merely:

> How many branches can be imagined?

## 6.3 Priority projection

Let `F_x(T)` be the represented futures reachable over horizon `T` under element `x`.

Project onto a declared priority axis `U`, for example:

`U in [-1, +1]`

where endpoints are locally defined.

Use fixed bins `K >= 2` across comparisons.

If `p_b` is normalized modeled probability mass or explicitly declared occupancy weight:

`p_b >= 0`

`sum(p_b) = 1`

`0 ln(0) = 0`

then normalized Shannon-style evenness [R3] is:

`E_U = -sum_{b=1..K}(p_b ln p_b) / ln(K)`

with:

`0 <= E_U <= 1`.

This describes spread across the declared scale. It does not make bad outcomes desirable.

## 6.4 Catastrophic tail flag

Evenness is not safety.

Define:

`T_x = 1`

when grounded reachable support crosses a declared catastrophic / hard failure boundary; otherwise `T_x = 0`.

A rare credible reef matters even if the average sea looks calm.

## 6.5 Causal leverage

When a causal intervention model is justified:

`C_x = distance(P(F | do(x=x1)), P(F | do(x=x0)))`

using Pearl's intervention notation [R4].

If causal identification is not justified, label the quantity as sensitivity / association rather than decorating it with `do(·)` notation.

## 6.6 Known structure versus uncharted water

Use:

`I_vec(x) = (B_x, E_x, C_x, R_x, Q_x, T_x)`

where:

- `B_x` — normalized breadth of grounded projected support;
- `E_x` — distribution evenness;
- `C_x` — causal leverage or labeled sensitivity;
- `R_x` — evidence-backed unresolved frontier;
- `Q_x` — grounding/confidence of resolved support;
- `T_x` — catastrophic-tail flag.

Unknown territory must not automatically raise central interestingness.

One provisional known-structure score is:

`I_known(x) = C_x * Q_x * (w_B B_x + w_E E_x)`

with:

`w_B >= 0, w_E >= 0, w_B + w_E = 1`.

Report frontier separately:

`F_unresolved(x) = (R_x, 1-Q_x)`.

If a single interval is needed:

`I_interval(x) = [I_known, min(1, I_known + C_x w_R R_x (1-Q_x))]`

The upper extension is an uncertainty/discovery allowance, not evidence that the hidden structure already exists.

---

# 7. Charts at Several Scales — Projection of Intervals

An ocean chart is useful because it suppresses almost everything while preserving what matters to navigation.

## 7.1 Projection record

For projection `k`:

`P_k(F) = (I_k, rho_k, q_k, r_k, prov_k)`

where:

- `I_k` — resolved interval or union of intervals;
- `rho_k` — occupancy structure inside the interval;
- `q_k` — grounding / confidence;
- `r_k` — evidence-backed unresolved boundary information;
- `prov_k` — provenance.

The interval alone is insufficient.

Dense support across `[-1,+1]` and two clusters near `-1` and `+1` share the same outer interval but imply different future structure.

## 7.2 Rigorous enclosure versus descriptive chart

Classical interval analysis computes mathematically defined enclosures under specified assumptions [R5].

Compass often uses broader descriptive intervals from scenarios, measurements, ensembles, or expert constraints.

Do not call a descriptive interval a rigorous enclosure unless it has that guarantee.

## 7.3 Keep the path back to source

Every projection should retain:

- source variables;
- transform rule;
- scale;
- horizon;
- thresholds;
- scenario generator;
- weighting / sampling rule;
- unresolved variables;
- provenance;
- timestamp/version when state can drift.

A short chart that cannot be traced back to evidence is not navigation; it is illustration.

---

# 8. Sound the Shoals — Adaptive Refinement

## 8.1 Start coarse

Use broad chart resolution until it becomes decision-sensitive.

Refine when:

- projected intervals cross a hard boundary;
- materially different models disagree;
- the decision changes under small assumption variation;
- causal leverage is high;
- a rare tail threatens irreplaceable state;
- an application exposes a candidate hidden variable;
- the cost of obtaining additional evidence is small relative to the decision consequence.

The resource-allocation analogy to adaptive mesh refinement is intentional: use fine resolution where structure/error requires it rather than everywhere [R6][R7]. Compass borrows the allocation principle, not AMR's numerical machinery.

## 8.2 Refinement priority vector

For local region / question `i`:

`R_i = (S_i, U_i, G_i, D_i, C_i)`

where:

- `S_i` — sensitivity / leverage;
- `U_i` — unresolved width;
- `G_i` — consequence / decision gradient;
- `D_i` — disagreement across materially different methods;
- `C_i` — cost / disturbance of resolving it.

Do not collapse this to a scalar unless comparison requires it.

Expected information-gain traditions provide neighboring formal tools for experiment selection [R13].

## 8.3 The refinement loop

Compass refinement is:

`chart -> sound -> compare -> isolate -> refine -> validate -> propagate -> compress`

Detailed procedure:

1. project coarsely;
2. locate boundary-sensitive or contradictory regions;
3. select the smallest useful new sounding / test / retrieval;
4. obtain evidence;
5. update variables and intervals;
6. test whether the decision or explanation changed;
7. propagate only supported changes upward;
8. compress detail that no longer changes higher-level conclusions;
9. record the update in the logbook.

## 8.4 Stop refinement when

- the claim is supported at its required level;
- the decision is robust under plausible alternate models;
- remaining uncertainty cannot change the action class;
- the next probe would violate preservation without adequate justification;
- the true blocker is external and no new local evidence can resolve it;
- the loop is no longer producing new state or evidence.

A loop without new evidence is circling, not exploration.

---

# 9. The Knife Overboard — Exploration Without Destructive Blindness

## 9.1 The probe rule

> **The efficiency of a probe does not cancel the disturbance it creates.**

Cutting is sometimes the fastest way to learn what is inside something. It can also destroy the relation being studied.

The same applies to destructive debugging, invasive experiments, organizational intervention, ecological manipulation, or irreversible infrastructure changes.

## 9.2 Escalation ladder

Prefer, where appropriate:

1. passive observation;
2. historical / naturally occurring variation;
3. model / simulation;
4. isolated or sandboxed test;
5. reversible local probe;
6. reversible system intervention with monitoring;
7. irreversible intervention after explicit preservation/rescue evaluation.

This is not a command to always move slowly. Delay can itself destroy viability. The question is whether disturbance, delay, and recovery are represented explicitly.

## 9.3 Receding-horizon navigation

Model predictive control repeatedly solves a finite-horizon problem from the current state, applies a limited control move, observes the new state, then solves again [R8].

Compass is broader, but uses the same useful pattern:

> project far enough to justify the next bounded heading; sail only the justified leg; take a new sounding; redraw the chart.

---

# 10. The Logbook — Exact External Thinking During Exploration

Compass becomes reusable only when state survives the individual conversation or observer.

## 10.1 Logbook entry

Each consequential cycle should create:

`L_t = {version, north, chart_changes, new_evidence, variable_changes, projection_changes, preservation_status, chosen_heading, stop_condition, realized_outcome}`

## 10.2 Separate layers

Keep four layers distinct:

### Layer A — Observation
What was directly seen, measured, retrieved, or tested?

### Layer B — Model
What dependency / causal / structural interpretation is currently used?

### Layer C — Projection
What future intervals follow if the model is used?

### Layer D — Decision
What action, if any, follows under the declared value premise and constraints?

This separation makes it easier to replace a model without erasing the observations that produced it.

## 10.3 Contradiction ledger

Contradictions are not noise to remove.

For contradiction `c` record:

`c = {claim_A, claim_B, evidence_A, evidence_B, shared_assumptions, candidate_resolutions, decision_impact}`

A contradiction with no decision impact may remain open. A contradiction that crosses a preservation boundary gets priority.

## 10.4 Assumption ledger

For each assumption:

`θ = {statement, reason, scope, sensitivity, invalidation_test, expiry}`

An assumption with high decision sensitivity deserves a sounding before a low-sensitivity unknown.

---

# 11. Compass Execution Protocol

This is the reusable instrument.

## 11.1 Input

A Compass run requires at minimum:

- a question / task;
- available evidence or permission to retrieve it;
- a declared target claim or decision;
- any known hard constraints.

Everything else can be discovered progressively.

## 11.2 Cycle

### C0 — Set North
Write `Q` and the claim strength required.

### C1 — Draw the first chart
Declare `S, B, σ, Δt, H, Θ, W`.

### C2 — Load soundings
Build evidence ledger `E`; separate observed from inferred.

### C3 — Mark reefs and harbors
Build `V, G, R`: hard boundaries, reserves, recovery routes, irreplaceable cargo.

### C4 — Trace currents
Build/update dependency graph `D`.

### C5 — Register variables
Update `X`; label every new variable by status.

### C6 — Project waters ahead
Build `P`; use intervals/distributions only at justified resolution.

### C7 — Locate interesting regions
Compare leverage, spread, disagreement, tail risk, and unresolved frontier.

### C8 — Run variable-promotion gate
For application-exposed hidden variables, test operationality, evidence, mechanism, decision effect, alternatives, recurrence, and redundancy.

### C9 — Choose a heading
Select the smallest step likely to reduce decision-relevant uncertainty or test the most consequential hidden variable.

### C10 — Preservation gate
Before consequential action, evaluate margins, common-cause risks, recovery independence, and mode: PRESERVE or RESCUE.

### C11 — Execute one justified leg
Observe / retrieve / simulate / test / act only to the extent justified by the current chart.

### C12 — Take new soundings
Compare realized state with projected intervals.

### C13 — Update the chart
Change only what new evidence supports. Preserve contradictions.

### C14 — Compress
Remove no-longer-relevant detail while retaining hard boundaries, rare consequential branches, provenance, assumptions, recovery state, and promoted variables.

### C15 — Stop, turn, or repeat
Apply explicit terminal conditions.

## 11.3 Allowed terminal states

A Compass run should end in one of a small number of explicit states:

- `SUPPORTED` — target claim supported to declared strength;
- `DECISION_ROBUST` — action class stable across plausible refinements;
- `PRESERVATION_BLOCK` — action blocked by unresolved / negative hard margin;
- `RESCUE_REQUIRED` — strict preservation unavailable; least-loss logic required;
- `EXTERNAL_WAIT` — external dependency is the blocker;
- `INSUFFICIENT_EVIDENCE` — no justified next step can presently resolve the key uncertainty;
- `MODEL_CONTRADICTION` — current assumptions cannot jointly explain observations;
- `TERMINAL_SYSTEM_STATE` — system itself has no modeled continuation under the selected definition;
- `QUESTION_REFRAMED` — original North was drawn at the wrong boundary/scale.

"Still thinking" is not a terminal state.

---

# 12. Hidden-Variable Discovery as a Research Engine

This is where Compass becomes more than a workflow manager.

## 12.1 Applications are stress tests of the general template

A general formula is intentionally sparse. Real applications introduce geometry, timing, authority, failure, environment, and observation constraints. The logical chain required to preserve the story while reaching an actual use case is not wasted prose; it is a **stress test** of the general model.

Each time a chain fails, ask:

> What variable or relation had to be silently assumed for the story to remain coherent?

That variable becomes a candidate.

## 12.2 Residual-driven discovery

Let predicted projection be `P_pred` and realized observation be `y`.

If `y` lies outside the supported region of `P_pred`, create residual record:

`δ = {prediction, realization, violated_assumption, candidate_dependencies, candidate_variables}`

Do not immediately widen `P_pred` to include `y`.

First ask whether:

- measurement is wrong;
- boundary is wrong;
- scale/horizon is wrong;
- dependency is missing;
- existing variable has wrong state;
- a hidden variable is required.

## 12.3 Variable enrichment without explosion

If every application-specific variable is made core, Compass becomes unusable.

Therefore the variable registry is layered:

`CORE -> DOMAIN -> LOCAL -> CANDIDATE`

- **CORE** variables recur across many systems and belong in the general Compass state;
- **DOMAIN** variables recur within a class such as structures, software, ecology, or finance;
- **LOCAL** variables matter to one application;
- **CANDIDATE** variables are not yet established.

A future research model loads only relevant layers.

## 12.4 Promotion creates inheritance

When a variable is promoted, record:

- the cases that exposed it;
- its operational definition;
- supporting evidence;
- known failure modes;
- domains where it should / should not be inherited;
- a test that could demote it later.

This turns prior exploration into reusable structure without turning prior conclusions into dogma.

---

# 13. Human Navigation

A human observer has limited working memory. Compass externalizes the chart so microprocesses can remain light while the general picture remains visible.

It helps by:

- separating observed from inferred state;
- holding dependency chains outside working memory;
- preserving unresolved contradictions;
- keeping assumptions and expiry visible;
- showing which unknowns can actually change a decision;
- allowing re-entry after interruption;
- reducing the urge to solve every branch at equal resolution.

The goal is not maximum detail. A mature chart may become simpler because irrelevant branches have been tested and compressed.

---

# 14. AI Navigation

The claim here is narrow: an AI system can benefit from the same external organization when the state is explicit and auditable.

A Compass-compatible AI should maintain or produce:

- current North;
- chart boundary/scale/horizon;
- evidence ledger with provenance;
- dependency graph;
- variable registry with promotion status;
- preservation margins and recovery paths;
- future projections;
- unresolved frontier;
- next heading;
- stop conditions;
- log of chart revisions.

It should **not** treat its own fluency as a sounding.

NIST's AI Risk Management Framework emphasizes validity/reliability, safety, resilience, transparency, and lifecycle evaluation [R11]. NIST's 2026 TEVV-Athlon draft proposes adaptable TEVV across varied AI systems, including agentic systems [R12]. These ground the evaluation discipline, not Compass's specific architecture.

## 14.1 Fleet behavior

Several agents form a fleet only if they share a chart and preserve disagreement.

Useful roles include:

- sounding / retrieval;
- dependency mapping;
- adversarial assumption checking;
- scenario generation;
- preservation evaluation;
- verification;
- synthesis.

Several agents with one hidden assumption are several ships following one wrong chart.

## 14.2 Compression rule

Before summarizing, preserve:

- reefs / hard constraints;
- rare catastrophic branches;
- contradictions;
- provenance;
- cargo / irreplaceable state;
- recovery paths;
- assumptions whose removal changes the conclusion;
- promoted variables and the evidence that justified them.

Compression that deletes these makes the system shorter, not smarter.

## 14.3 Compass invocation for AI-assisted research

A reusable instruction is:

> **Use Compass. Initialize an external Compass state before deep exploration. Separate evidence, inference, projection, and decision. Maintain variable-promotion status. Treat application narratives as stress tests that may expose hidden variables, not as evidence by themselves. Refine only decision-sensitive regions. Before consequential action, run preservation/rescue gates and verify recovery-path independence. After each new observation, compare realization to projection, update the chart, preserve contradictions, and stop when an explicit terminal state is reached.**

This instruction describes externally auditable process state, not hidden reasoning traces.

---

# 15. Worked Expedition — A Coupled Technical System

Consider a live technical platform being changed while users depend on it.

## 15.1 North

`Q = Can the update be deployed while preserving user workflow, recoverability, and irreplaceable state?`

## 15.2 First chart

Vessel/system:

`user -> client -> identity -> service -> persistent state -> external provider`

Return route:

`operator authority -> backup -> restoration -> verification`

## 15.3 Initial variables

Core chart contains:

- service availability;
- state integrity;
- dependency availability;
- recovery time;
- rollback presence.

## 15.4 Story exposes a hidden current

Local service health passes, but users cannot recover access after a failure.

Logical chain:

1. health endpoint passes;
2. user transaction fails;
3. operator attempts rollback;
4. rollback requires identity authority;
5. identity authority uses same failed dependency;
6. nominal rollback existed but was unreachable.

Candidate hidden variable:

`R_ind = recovery-path independence`.

## 15.5 Operationalize

Define `R_ind` by failure-domain separation:

- `R_ind = 1` only when at least one recovery path does not depend on the same failure mode it must recover from;
- otherwise `R_ind = 0` or an interval if dependency independence is unresolved.

This is a local definition, not a universal scalar for all domains.

## 15.6 Decision effect

Without `R_ind`, projected recoverability margin was positive.

With `R_ind`, the lower bound crosses zero.

Therefore the variable changes the preservation decision and deserves refinement.

## 15.7 Recurrence

The same structural variable appears in:

- emergency power sharing the same flooded distribution room;
- redundant pumps sharing one blocked intake;
- multiple agents sharing one corrupted evidence source.

The operational relation survives translation: a backup that shares the same relevant failure domain is not independent.

`R_ind` is therefore a strong candidate for CORE promotion.

## 15.8 Heading

The next step is not a full platform rewrite. It is the smallest sounding that resolves independence:

- map authority dependencies of the recovery path;
- test recovery from an isolated failure domain;
- verify that recovery remains reachable after primary-path loss.

## 15.9 Update

Only after the sounding does Compass update the preservation gate and choose the next deployment leg.

This is how a storytelling chain can enrich the reusable model without becoming hallucinated theory.

---

# 16. Validation and Edge-Case Checklist

This checklist is a minimum test set for the current formulas and procedure. It must grow when applications expose new failure modes.

| Edge case | Compass handling |
|---|---|
| One occupied priority bin | Use fixed `K >= 2`; no division by `ln(1)`. |
| Zero occupancy bins | Use `0 ln 0 = 0`. |
| Empty / contradictory reachable set | Mark model infeasible/unresolved; do not report interestingness as zero unless the system is genuinely terminal. |
| Unbounded projection axis | Declare finite reference scale, transform, or domain thresholds before normalized breadth. |
| Rare catastrophic branch | Preserve tail flag / hard reef; averages and entropy cannot erase it. |
| Low-confidence model | Unknowns widen frontier/interval; they do not automatically raise central score. |
| Scenario count baseline is zero | Optionality ratio undefined; use counts, fractions, or weighted viable mass. |
| Different scenario sample sizes / generators | Counts not directly comparable without controlled basis. |
| Already-failing system | Switch PRESERVE -> RESCUE; include non-action baseline. |
| Irreversible action | Stronger evidence/containment/forward recovery; do not falsely require rollback. |
| Common-cause dependencies | Model joint failure; independent positive margins are insufficient. |
| Backup shares failure domain | Recovery-path independence fails. |
| Subsystem preserved, containing system harmed | Evaluate material externalities at containing levels. |
| Short-term preserved, long-term harmed | Evaluate several horizons; report reversals. |
| Measurement disturbs system | Put measurement disturbance in evidence record/model. |
| Association presented as causality | Use `do(·)` only with justified causal model. |
| Multiple agents agree | Check common model/data/assumption before calling it independent validation. |
| Compression deletes exception | Preserve reefs, tails, contradictions, provenance, cargo, and recovery state. |
| Refinement repeats without new evidence | Stop/branch; circling is not exploration. |
| Value premises conflict | Keep conflict explicit; do not hide it in a weighted average by default. |
| Story suggests variable with no operational definition | Keep `CANDIDATE`; do not promote. |
| Variable fits one case perfectly | Check alternatives and materially different cases before recurrence/core promotion. |
| Variable recurs only because same source/template was reused | Treat as correlated recurrence, not independent evidence. |
| New variable duplicates existing one | Merge or reject; do not inflate chart dimensionality. |
| Promotion later proves harmful/redundant | Demote; preserve history in logbook. |
| North changes mid-run | Create new chart version or `QUESTION_REFRAMED`; do not pretend continuity of claim. |
| Evidence becomes stale | Lower freshness confidence; re-sound if decision-sensitive. |
| Model and observation disagree | Create residual/contradiction; do not widen model automatically. |

---

# 17. Reference Map

These are grounding parallels and notation sources, not claims that Compass is a restatement of any one tradition.

- preservation / viability: [R1], [R2]
- entropy / distribution evenness: [R3]
- causal intervention notation: [R4]
- rigorous interval methods: [R5]
- adaptive refinement analogy: [R6], [R7]
- receding-horizon control analogy: [R8]
- abstraction/refinement analogy: [R9]
- systems V&V / end-to-end testing: [R10]
- AI lifecycle evaluation: [R11], [R12]
- expected information / experiment selection: [R13]

## References

**[R0] Beregovykh, Nikita.** *Observer's Notes: A Field Book.* Public discussion draft, 2026. Repository: https://github.com/nvberegovykh/Observer-s-Notes

**[R1] Aubin, Jean-Pierre.** *Viability Theory.* Modern Birkhäuser Classics, 2009 edition. Springer/Birkhäuser. https://link.springer.com/book/10.1007/978-0-8176-4910-4

**[R2] Holling, C. S.** "Resilience and Stability of Ecological Systems." *Annual Review of Ecology and Systematics* 4 (1973): 1–23. DOI: 10.1146/annurev.es.04.110173.000245. https://doi.org/10.1146/annurev.es.04.110173.000245

**[R3] Shannon, Claude E.** "A Mathematical Theory of Communication." *Bell System Technical Journal* 27 (1948), parts I–II, pp. 379–423 and 623–656. DOI part I: 10.1002/j.1538-7305.1948.tb01338.x; part II: 10.1002/j.1538-7305.1948.tb00917.x. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

**[R4] Pearl, Judea.** *Causality: Models, Reasoning, and Inference.* 2nd ed. Cambridge University Press, 2009. https://bayes.cs.ucla.edu/BOOK-2K/

**[R5] Moore, Ramon E.; Kearfott, R. Baker; Cloud, Michael J.** *Introduction to Interval Analysis.* SIAM, 2009. DOI: 10.1137/1.9780898717716. https://doi.org/10.1137/1.9780898717716

**[R6] Berger, Marsha J.; Oliger, Joseph.** "Adaptive Mesh Refinement for Hyperbolic Partial Differential Equations." *Journal of Computational Physics* 53(3) (1984): 484–512. DOI: 10.1016/0021-9991(84)90073-1. https://doi.org/10.1016/0021-9991(84)90073-1

**[R7] Berger, Marsha J.; Colella, Phillip.** "Local Adaptive Mesh Refinement for Shock Hydrodynamics." *Journal of Computational Physics* 82(1) (1989): 64–84. DOI: 10.1016/0021-9991(89)90035-1. https://doi.org/10.1016/0021-9991(89)90035-1

**[R8] Mayne, D. Q.; Rawlings, J. B.; Rao, C. V.; Scokaert, P. O. M.** "Constrained Model Predictive Control: Stability and Optimality." *Automatica* 36(6) (2000): 789–814. DOI: 10.1016/S0005-1098(99)00214-9. https://doi.org/10.1016/S0005-1098(99)00214-9

**[R9] Clarke, Edmund M.; Grumberg, Orna; Jha, Somesh; Lu, Yuan; Veith, Helmut.** "Counterexample-Guided Abstraction Refinement." In *Computer Aided Verification (CAV 2000)*, LNCS 1855, pp. 154–169. DOI: 10.1007/10722167_15. https://doi.org/10.1007/10722167_15

**[R10] NASA.** *NASA Systems Engineering Handbook* and current verification/validation guidance. NASA/SP-2016-6105 Rev2. https://www.nasa.gov/reference/system-engineering-handbook-appendix/ and https://www.nasa.gov/reference/5-3-product-verification/

**[R11] NIST.** *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1, 2023. https://www.nist.gov/itl/ai-risk-management-framework

**[R12] NIST.** *The TEVV-Athlon Framework for Evaluating AI Systems.* Initial public draft / NIST AI 200-2 announcement, August 7, 2026. https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems

**[R13] Lindley, Dennis V.** "On a Measure of the Information Provided by an Experiment." *Annals of Mathematical Statistics* 27(4) (1956): 986–1005. DOI: 10.1214/aoms/1177728069. https://doi.org/10.1214/aoms/1177728069

---

# 18. The Compass in One Passage

For any difficult exploration:

1. **Set North.** State the exact question and required claim strength.
2. **Draw the chart.** Localize system, boundary, scale, interval, horizon, assumptions, and value premise.
3. **Take soundings.** Separate measured evidence from inference and assumption.
4. **Mark reefs and harbors.** Record hard constraints, reserves, irreplaceable state, and independent recovery paths.
5. **Trace currents.** Map dependencies and common-cause paths.
6. **Register hidden variables.** Treat application stories as stress tests; promote variables only through the promotion gate.
7. **Project open water.** Use intervals/distributions with provenance; keep unknown frontier separate from known structure.
8. **Find the consequential region.** Prioritize leverage, disagreement, boundary proximity, tail risk, and decision-sensitive uncertainty.
9. **Choose one bounded heading.** Prefer the smallest evidence-producing step that can change the chart or decision.
10. **Preserve before acting.** Run PRESERVE/RESCUE gates and check recovery-path independence.
11. **Sail one justified leg.** Do not execute the whole imagined route because the first chart looked plausible.
12. **Sound again.** Compare realization to projection.
13. **Update and log.** Change only what evidence supports; preserve contradictions and provenance.
14. **Compress carefully.** Remove detail, not reefs.
15. **Stop explicitly.** End in a named terminal state rather than an unbounded reasoning loop.

The purpose of Compass is not to make uncertainty disappear.

It is to make the **direction, boundary, evidence, unknowns, preservation conditions, and next justified move visible at the same time**.

That is enough to navigate farther without pretending the ocean has already been mapped.

---

## Signature

**Nikita Beregovykh & ChatGPT 5.6 Sol, Observers Notes extension 1**
