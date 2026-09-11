# Observer's Notes — Vol. 1.2

## Extension 1: Preservation, Interestingness, Projection, and Progressive Modeling

**Status:** working extension notes. Deliberately kept in technical-note form rather than the illustrated / field-book presentation of Vol. 1.

**Purpose:** extend the operational side of the original model without replacing its definitions. The extension focuses on questions that became clearer after the first edition: what preservation actually means in a changing system; how to identify an interesting element without enumerating every future; how interval projection can compress future-space; how coarse models can be refined only where needed; and why this organization can improve reasoning for both humans and AI systems when evidence, assumptions, uncertainty, and stopping conditions remain explicit.

**Provenance:** the conceptual extensions in this document grew from post-publication working discussions between Nikita Beregovykh and ChatGPT in 2026. External references are listed separately as neighboring formal traditions, sources for mathematical notation, or grounding for specific operational claims. They are not presented as the origin of the Observer's Notes model.

---

## 0. Compatibility with Vol. 1

Vol. 1 already establishes the important base [R0]:

- select the system, purpose, scale, and interval;
- distinguish elements from relations;
- define identity by invariants and tolerances;
- define a viability domain and current margin;
- map lower-level dependencies, buffers, substitutes, delays, and thresholds;
- identify maintenance, recursive maintenance, and generative maintenance;
- state the value premise before optimization;
- attach intervention to measurement, reversibility where possible, a return path, verification, and a stopping condition.

Vol. 1 also states that preservation and generation may conflict, and that generative maintenance can require change, pruning, recombination, or the end of a structure that blocks future viability.

What remained under-specified was **preservation evaluation itself**. The word can be misread as "keep everything unchanged." That is not the intended meaning.

This extension also adds a practical method for working with systems whose future-state space is too large to enumerate. The method is based on **local projections, intervals, occupancy structure, confidence, provenance, and adaptive refinement**.

---

# 1. Preservation Evaluation

## 1.1 Preservation is selected continuity, not frozen material

Preservation is always relative to a model.

For a selected system `S`, define:

- `Θ` — declared assumptions;
- `σ` — scale;
- `Δt` — evaluation interval;
- `H` — future horizon or set of horizons;
- `I` — identity invariants and tolerances;
- `V` — viability conditions;
- `D` — constitutive dependencies;
- `W` — the value premise that explains why preservation is being evaluated.

Then preservation asks:

> After an action or disturbance, does enough of the selected organization, dependency base, and recoverability remain for the valued system to stay viable, remain identifiable, or return to an acceptable state within the declared interval and horizon?

The preserved object is therefore not necessarily the same material object.

A server can be replaced while a service is preserved. A cell replaces molecules while preserving organization. A building can receive new structural members while preserving its use and load path. A scientific model can change while preserving evidence, provenance, and the ability to reproduce earlier conclusions.

Conversely, material can remain while the system is lost. A database file may still exist while its keys, schema, credentials, or recovery path are gone. A machine may retain every component while a constitutive relation is broken.

**Preservation therefore concerns selected invariants, relations, dependencies, viability, and recoverability, not mere persistence of substance.**

This is compatible with viability theory's formal concern with trajectories that remain within constraints, while the Observer model is broader and uses viability as one component of a localized systems description rather than claiming equivalence to Aubin's framework [R1].

## 1.2 The preservation vector

A single preservation score is usually too aggressive. Start with a vector.

For a proposed action `a`, project each required preservation dimension into a post-action margin interval:

`m_j(a) = [lower_j, upper_j]`

where zero is the declared failure boundary for that dimension.

Useful dimensions include:

| Dimension | Question |
|---|---|
| Identity margin `M_I` | Are the invariants that define the selected system still within tolerance? |
| Viability margin `M_V` | Do required operating / survival conditions remain inside the viability domain? |
| Dependency margin `M_D` | Are lower-level processes, external conditions, buffers, substitutes, and interfaces still available? |
| Continuity `C` | Can the required function continue through the intervention and recovery interval? |
| Recoverability `R` | Is there an evidence-backed path to a known viable state if the action fails? |
| Access / control `A` | Will the actors or control processes required for recovery still be able to reach and change the system? |
| Irreplaceable-state integrity `K` | Are records, memory, keys, unique data, physical specimens, identity state, or other non-reconstructable dependencies protected? |
| Verification capacity `Q_V` | Can the post-action state be measured well enough to know whether preservation actually succeeded? |

The exact dimensions depend on the localized system. "Credentials" matter in a software platform; reproductive capacity may matter in a population; load-path continuity may matter in a structure. Do not force domain-specific variables into every model.

The dimensions are **not assumed independent**. If two margins can fail together because of a shared dependency, their joint failure mode must be represented explicitly rather than hidden by a vector of individually acceptable values.

## 1.3 Hard preservation gate

For any action that claims to preserve a selected system, use a gate before optimization.

For each hard preservation dimension `j`, declare a required reserve `r_j >= 0`. Logical admissibility may use `r_j = 0`; consequential systems should generally use a positive reserve when evidence and domain practice justify one.

**Gate P:**

1. Declare the system, value premise, scale, interval, horizon, identity invariants, and viability boundaries.
2. Identify constitutive dependencies and irreplaceable state.
3. For every hard preservation dimension `j`, require:

   `lower(m_j(a)) >= r_j`

   unless crossing that boundary is an explicitly accepted transformation rather than accidental loss.
4. Check joint and common-cause failures among hard dimensions.
5. Require a recovery path when recovery is physically meaningful.
6. Require the recovery path to remain reachable after the same failure that the recovery path is supposed to correct. A rollback stored behind a credential that the intervention may destroy is not a recovery path.
7. Require monitoring / verification to resolve dangerous drift before an irreversible threshold is crossed, when that is feasible.
8. State the stopping condition before action.
9. Re-evaluate after each consequential state change. Time elapsed is not evidence that the enabling condition has become true.

This is intentionally state-driven. "Wait five minutes and continue" is weaker than "continue when the required state is observed and verified."

### Emergency / already-failing exception

The gate above describes a **strict preservation claim**. It must not create the absurd result that no rescue action is allowed after the system has already crossed, or will imminently cross, a hard boundary.

If no available action, including non-action, keeps every hard margin above its required reserve, switch to **rescue / least-loss mode**:

- include non-action as a candidate;
- compare the projected losses, irreversible consequences, recoverability, and time-to-failure of the available choices;
- protect irreplaceable state and future recovery capacity where possible;
- choose the action only under the declared value premise and authority;
- do **not** describe the result as strict preservation if preservation was no longer achievable.

This distinction prevents a preservation rule from becoming a prohibition against necessary intervention.

## 1.4 Recursive preservation

Preservation must be checked across levels.

A higher-level structure can remain apparently healthy while consuming the conditions that make it possible. Short-term efficiency can reduce long-term viability margin. A system can therefore optimize itself into fragility.

For each valued higher-level function `H`, trace the active dependency path downward:

`H -> D1 -> D2 -> ... -> Dn`

Then ask for each dependency:

- Is it currently viable?
- Is there a buffer?
- Is there a substitute?
- How long is the failure delay?
- Is replacement possible after failure?
- Does the intervention reduce the ability to observe or repair it?
- Does a substitute share the same hidden failure mode as the primary dependency?

A preservation claim is incomplete if it preserves the visible top layer while silently destroying a constitutive lower layer.

The inverse also matters: preserving one subsystem can damage the larger containing system. For consequential actions, evaluate at least the selected system and any containing system that bears a material externality.

## 1.5 Preservation is not the maximization of stability

Maximum stability is not automatically desirable. A perfectly fixed system may be unable to learn, adapt, repair, or generate alternatives. Ecological work has long distinguished forms of stability from resilience, illustrating why persistence near one state and capacity to remain functional through disturbance are not identical ideas [R2].

Preservation can therefore be divided into at least three modes:

- **identity preservation** — maintain the selected invariants;
- **viability preservation** — maintain the conditions that keep the system inside its viable domain;
- **generative preservation** — maintain or expand valuable reachable viable futures.

These modes can conflict.

A repair may alter identity-relevant material while preserving function. A migration may temporarily reduce continuity while increasing recoverability. Pruning may remove one structure while improving the viability of a larger system.

The value premise decides which constraints are hard and which transformations are acceptable. The model does not derive that premise from physics.

## 1.6 Optionality as a preservation/generation check

When an action explicitly claims to preserve or expand future options, compare reachable viable states under the **same declared horizon, state representation, scenario generator, weighting rule, and sampling budget**.

Let:

- `N_R` = number of sampled reachable states;
- `N_V` = number satisfying the declared viability conditions;
- `F_V = N_V / N_R` when `N_R > 0`.

Report the paired changes:

`ΔN_V = N_V_after - N_V_before`

`ΔF_V = F_V_after - F_V_before`

This follows the caution already present in Vol. 1: a larger viable fraction can coexist with fewer viable futures, and vice versa [R0].

An optional ratio:

`O = N_V_after / N_V_before`

may be reported **only when `N_V_before > 0` and the comparison basis is held fixed**. If `N_V_before = 0`, the ratio is undefined; report the counts, fractions, or weighted viable mass instead.

Counts from differently sized or differently biased scenario samples are not directly comparable merely because both are called `N_V`.

Unknown futures must not be fabricated to improve optionality.

## 1.7 Multi-horizon preservation

An action may preserve a system over one horizon and destroy it over another.

Therefore, when delayed effects are plausible, evaluate a set of horizons:

`H = {H_short, H_operational, H_recovery, H_long}`

A short-term positive margin does not cancel a known long-term dependency loss. Conversely, a temporary controlled margin reduction may be acceptable if it is part of an explicitly modeled recovery path.

Report horizon reversals rather than averaging them away.

## 1.8 Preservation under uncertainty

Uncertainty should widen the model, not silently become confidence.

If the effect of an action on a dependency is uncertain, record an interval or unresolved boundary. For example:

`M_D(a) = [-0.15, +0.40]`

This does not mean the dependency is half-preserved. It means the current model cannot establish that the lower bound remains viable.

For hard constraints, unresolved overlap with failure is a reason to refine the model, reduce the intervention, add a buffer, or refrain from claiming strict preservation.

If measurement itself materially disturbs the system, that disturbance belongs in the model. Verification is an interaction, not a view from nowhere.

---

# 2. Interestingness as Structured Future Potential

## 2.1 Working definition

An element is interesting, within a declared local model, when its state or alteration is associated with a large and structured change in reachable future-space.

The word **local** is essential. Interestingness is not treated as an intrinsic metaphysical property. It depends on:

- the selected system;
- assumptions;
- scale;
- horizon;
- state variables;
- value / priority dimensions;
- current knowledge.

A stone can be uninteresting in a traffic model and highly interesting in a geological model. The same anomaly can become less interesting once its mechanism is well constrained.

## 2.2 Not raw branch count

Raw possibility count is insufficient.

A random-noise source can have enormous entropy while having little causal leverage over the modeled system. A small decision can have fewer branches while reorganizing the reachable state-space of an entire project.

The useful question is therefore not:

> How many futures follow this element?

but:

> How much does this element change the structure, distribution, and reachability of consequential futures under the current assumptions?

## 2.3 Priority projection and evenness

Let `F_x(T)` be the modeled set of futures reachable over horizon `T` when element `x` is relevant.

Project those futures onto a declared priority dimension `U`, for example a normalized success/failure scale:

`U in [-1, +1]`

Partition the scale into a **fixed declared number of bins `K >= 2`** before comparing elements. Do not normalize by the number of occupied bins; doing so makes the measure unstable and is undefined when only one bin is occupied.

Let `p_b` be the normalized modeled probability mass or normalized weighted occupancy in bin `b`, with:

`p_b >= 0`

`sum(p_b) = 1`

and the standard convention:

`0 * ln(0) = 0`.

A normalized Shannon-style evenness measure [R3] is:

`E_U = -sum_{b=1..K}(p_b * ln(p_b)) / ln(K)`

Then `0 <= E_U <= 1`.

`E_U` approaches 1 when occupancy is broadly distributed across the declared bins and approaches 0 when represented futures collapse into a narrow region.

If the model cannot justify probability mass, call `p_b` a declared normalized occupancy weight rather than pretending it is probability.

This **does not mean failure is desirable**. Evenness is a measurement of breadth across the declared outcome scale, not an instruction to seek harmful outcomes.

### Rare catastrophic tails

Evenness is not a safety measure.

A distribution containing one low-probability but credible catastrophic branch may have low entropy and still dominate action. Therefore keep a separate hard-threshold / tail flag:

`T_x = 1` when grounded reachable support crosses a declared hard failure boundary; otherwise `T_x = 0`.

A preservation or safety gate can override an otherwise low interestingness score.

## 2.4 Causal leverage

To distinguish consequential branching from noise, compare the projected future-space under meaningful changes in `x`.

When a causal intervention model is justified, one can write:

`C_x = distance(P(F | do(x = x1)), P(F | do(x = x0)))`

using Pearl's intervention notation [R4].

The distance rule must be declared. It may compare intervals, distributions, threshold crossings, reachable support, or another domain-appropriate structure.

If an intervention model is **not** justified, do not use `do(·)` notation as decoration. Use observational sensitivity, natural experiments, controlled comparisons, or another appropriate method and state that causal identification remains unresolved.

An element with broad futures but negligible `C_x` is uncertain, but not necessarily an important branching point.

## 2.5 Discovery frontier

Unknown territory should be represented without inventing specific futures.

Define `R_x` as an evidence-backed unresolved-frontier term. It may increase when:

- materially different models disagree;
- small assumption changes move the result strongly;
- observed data repeatedly falls near or outside modeled bounds;
- an important dependency is known but poorly resolved;
- the projection contains open boundaries that affect the decision;
- residual structure remains after the best current explanation.

Simple ignorance is not automatically discovery potential.

## 2.6 Interestingness vector before scalar score

Use a vector before collapsing to a score:

`I_vec(x) = (B_x, E_x, C_x, R_x, Q_x, T_x)`

where:

- `B_x` = normalized breadth of reachable projected intervals;
- `E_x` = occupancy / distribution evenness across fixed priority bins;
- `C_x` = causal leverage or clearly labeled sensitivity analogue;
- `R_x` = evidence-backed unresolved frontier;
- `Q_x` = grounding / confidence quality of the resolved projection;
- `T_x` = hard-threshold / catastrophic-tail flag.

The important correction is that **uncertainty must not automatically increase the central interestingness score**.

For normalized terms in `[0,1]`, one possible known-structure score is:

`I_known(x) = C_x * Q_x * (w_B*B_x + w_E*E_x)`

with:

`w_B >= 0, w_E >= 0, w_B + w_E = 1`.

Report the unresolved frontier separately:

`F_unresolved(x) = (R_x, 1 - Q_x)`.

If a single interval is required for ranking, a provisional family is:

`I_interval(x) = [I_known, min(1, I_known + C_x*w_R*R_x*(1-Q_x))]`

where `w_R` is declared and the upper term is explicitly an **uncertainty / discovery allowance**, not evidence that the element already has that much structured interestingness.

This preserves the distinction between:

- known future structure;
- and justified reason to suspect unresolved structure.

## 2.7 Binning, normalization, and empty-model edge cases

The measure depends on representation. Therefore:

- keep bin boundaries fixed across compared elements;
- run a sensitivity check with at least one materially different reasonable binning when ranking matters;
- if a projection axis is unbounded, declare a finite reference scale, robust transformation, or domain threshold before claiming normalized breadth;
- if the modeled reachable set is empty because constraints are contradictory or the model failed, do **not** report interestingness as zero; classify the model as infeasible / unresolved;
- if the system is genuinely in a terminal state with no modeled continuation, report that terminal condition separately from model failure;
- if all scenario weights are zero or cannot be normalized, `E_U` is undefined.

These conditions prevent numerical convenience from being mistaken for a property of the system.

---

# 3. Projection of Intervals

## 3.1 Why projection is necessary

Complex systems produce combinatorial explosion. Explicitly enumerating all futures quickly becomes impossible and often creates false precision.

Instead of maintaining every future `f_1 ... f_n`, project the reachable set onto a small number of dimensions relevant to the current question.

For dimension `k`:

`P_k(F) = (I_k, rho_k, q_k, r_k, prov_k)`

where:

- `I_k` = current resolved interval or union of intervals;
- `rho_k` = occupancy structure inside the resolved region;
- `q_k` = grounding / confidence of the resolved projection;
- `r_k` = evidence-backed unresolved boundary information;
- `prov_k` = provenance: measured, constrained, simulated, inferred, assumed, or open.

The interval alone is insufficient.

These two projected future sets have the same outer interval but different internal structure:

`A: dense support across [-1, +1]`

`B: support only near -1 and +1`

They should not receive the same interpretation.

## 3.2 Projection is not permission to hide assumptions

Every projection should retain:

- source variables;
- transformation rule;
- scale;
- horizon;
- thresholds;
- sampling / scenario generator;
- unresolved variables;
- provenance of measured values;
- distinction between observed, inferred, simulated, assumed, and unknown states;
- version or timestamp when the underlying state can drift.

A compact projection is useful only if the path back to its assumptions remains inspectable.

Compression that drops a rare boundary condition can be worse than no compression at all.

## 3.3 Rigorous interval enclosure versus descriptive interval

There is an important distinction.

Classical interval analysis uses interval arithmetic and related methods to compute enclosures with defined mathematical guarantees under stated assumptions [R5].

A systems-modeling interval may instead be a descriptive bound derived from scenarios, measurements, expert constraints, ensembles, or incomplete models.

Do not describe a descriptive interval as a rigorous enclosure unless it actually has the relevant guarantee.

This extension uses **interval projection** in the broader systems-modeling sense unless rigorous enclosure is explicitly established.

## 3.4 Adaptive refinement

Start coarse.

Refine only where additional resolution can change understanding or action.

The analogy to adaptive mesh refinement is useful: AMR methods allocate finer resolution where error or solution structure requires it rather than using the finest grid everywhere [R6][R7]. The Observer method borrows the resource-allocation logic, not the numerical machinery.

A useful loop is:

1. **Project** the current reachable set coarsely.
2. **Measure** breadth, occupancy, uncertainty, sensitivity, disagreement, and distance to relevant thresholds.
3. **Select** regions where more resolution can change the decision or explanation.
4. **Refine** those regions into smaller intervals, submodels, experiments, or targeted retrieval.
5. **Validate** the refinement using new evidence, a materially different method, or a controlled probe.
6. **Propagate** revised bounds upward to the larger model.
7. **Compress again** when fine detail no longer changes the higher-level conclusion.
8. **Stop** when the decision is stable under further plausible refinement, when remaining uncertainty cannot change the action class, or when no safe evidence-producing step remains.

## 3.5 A refinement priority heuristic

A local region `i` can be prioritized using a qualitative or normalized vector such as:

`R_i = (S_i, U_i, G_i, D_i, C_i)`

where:

- `S_i` = sensitivity / leverage;
- `U_i` = unresolved width or uncertainty;
- `G_i` = decision or consequence gradient across the region;
- `D_i` = disagreement among materially different models / measurements;
- `C_i` = cost or disturbance of obtaining more resolution.

A heuristic scalar, when useful, might increase with `S_i`, `U_i`, `G_i`, and `D_i`, and decrease with `C_i`.

This is **not** a universal equation. It is a reminder that refinement should be purchased where it has expected decision value. Bayesian experimental design and information-gain approaches provide an established neighboring formal tradition for valuing experiments by expected information [R13].

## 3.6 Decision-focused resolution

Resolution should be tied to the decision.

If the current margin interval is:

`M = [+0.42, +0.71]`

and the hard failure boundary is `0`, additional precision may not be worth the cost.

If the interval is:

`M = [-0.03, +0.04]`

refinement is valuable because the unresolved range crosses the decision boundary.

This avoids two common failures:

- wasting computation on already-stable regions;
- acting confidently where coarse compression hides a boundary crossing.

---

# 4. Progressive Grounded Modeling

## 4.1 Sketch before solving

A complex problem often looks difficult because every microprocess is being held at the same level of attention.

The alternative is not to ignore microprocesses. It is to place them in a lightweight structure so higher-level reasoning can remain available.

Start with a sketch:

1. system and purpose;
2. boundary, scale, interval, and horizon;
3. elements and relations;
4. identity invariants;
5. viability domain;
6. dependencies and external conditions;
7. buffers, substitutes, delays, and thresholds;
8. evidence sources and provenance;
9. action points;
10. preservation gates, cutoffs, and terminal states.

Only then fill the model with finer measurements.

A sketch is therefore a **temporary low-resolution model**, not decoration.

## 4.2 Architecture before quantification

Numbers without architecture can create the appearance of rigor while measuring the wrong system.

A useful ordering is:

`architecture -> boundaries -> relations -> measurable variables -> thresholds -> projections -> refinement -> action -> verification`

This is not a ban on early measurement. Early measurements can help discover the architecture. The rule is that quantitative confidence should not exceed structural awareness of what the numbers belong to.

A practical confidence vector can include:

- `Q_evidence` — quality of direct evidence;
- `Q_coverage` — proportion of decision-relevant dependencies represented;
- `Q_resolution` — adequacy of model resolution near relevant boundaries;
- `Q_consistency` — agreement across materially different methods;
- `Q_freshness` — whether state-dependent evidence is still current.

Do not average these blindly. A very low value in one critical dimension can dominate the decision.

Agreement between several copies of the same model, same dataset, or same hidden assumption is **not independent validation**.

## 4.3 End-to-end paths instead of local symptoms

For any user-visible or system-visible goal, trace the complete path from initiating action to terminal state.

A generic chain is:

`initiator -> authority -> input -> transformation -> dependency -> persistence -> output -> verification -> recovery`

A local component can pass every unit check while the end-to-end goal remains impossible.

Evidence therefore has levels:

- hashes / identity markers can prove artifact identity;
- builds can prove compilation;
- narrow tests can prove local behavior;
- integration tests can prove selected interfaces;
- end-to-end acceptance can demonstrate that the selected system goal remains reachable through its real dependencies.

NASA systems engineering guidance similarly distinguishes component / end-item verification, complete system integration, and end-to-end validation [R10].

Evidence should prove the claim actually being made.

## 4.4 State-driven loops, cutoffs, and terminal states

A model should distinguish:

- a local failure;
- an external wait;
- an unresolved state;
- a retryable state;
- a terminal success;
- a terminal failure requiring a different branch.

Prefer state-driven conditions over arbitrary waits.

A loop without a changing state, new evidence, bounded retry count, or cutoff is not exploration. It is repetition.

Every consequential loop should declare:

- what state change justifies another iteration;
- what new evidence the iteration can produce;
- a maximum safe or useful budget;
- a terminal condition;
- a branch for unresolved external dependency.

## 4.5 Progressive representation

Each refinement should inherit the constraints of the coarser model unless a change is explicit and justified.

A useful representation therefore keeps:

- current model;
- previous model;
- assumptions changed;
- evidence added;
- intervals narrowed or widened;
- dependencies added or removed;
- decision changed / unchanged;
- reason for stopping.

This prevents refinement from quietly becoming replacement.

## 4.6 Receding-horizon analogy

Model predictive control repeatedly solves a finite-horizon problem using the current state, applies a limited control move, observes the new state, and solves again [R8].

The Observer method is much broader and is not MPC, but the receding-horizon pattern is a useful neighboring idea:

> project far enough to choose the next bounded action, execute only the justified portion, observe the realized state, then re-project.

This reduces dependence on a single long-range forecast remaining correct after the system changes.

---

# 5. Exploration Without Destructive Blindness

## 5.1 The knife rule

Cutting can be an extremely efficient way to learn what is inside something. It can also destroy the relation that made the object interesting.

The general rule is:

> **The efficiency of a probe does not cancel the cost of the disturbance it creates.**

This applies literally in biology and materials testing, and structurally in software, organizations, ecosystems, and social systems.

A destructive probe may answer the local question while making the larger system unrecoverable.

## 5.2 Escalation ladder

When possible, explore from lower disturbance toward higher disturbance:

1. passive observation;
2. model / simulation;
3. comparison with historical or naturally occurring variation;
4. isolated or sandboxed test;
5. reversible local probe;
6. reversible system intervention with monitoring;
7. irreversible intervention only after the preservation gate, value premise, authority, and failure consequences are explicit.

This is not a requirement to be maximally conservative. Excessive caution can also destroy viability by preventing necessary action. The emergency / rescue exception in Section 1.3 remains available.

The purpose is to make disturbance and recoverability explicit rather than invisible.

## 5.3 Freedom and preservation

Agency is useful partly because it can reach states that fixed rules cannot enumerate in advance. Unbounded action, however, can consume the conditions that make future agency possible.

A stable exploratory system therefore maintains a tension:

- enough freedom to discover new states;
- enough preservation to retain the substrate, memory, repair capacity, and future optionality needed for continued exploration.

This is not a contradiction. It is a control problem across levels.

---

# 6. What Progressive Modeling Gives a Human

A human observer has limited working memory and attention. A lightweight external model can offload detail without discarding it.

The gain is not merely convenience.

A well-organized sketch can:

- keep local details connected to the general picture;
- expose missing dependencies;
- separate known state from assumed state;
- prevent one dramatic symptom from replacing the system model;
- make uncertainty visible;
- allow re-entry after interruption without reconstructing everything from memory;
- preserve earlier reasoning and evidence;
- permit coarse-to-fine attention rather than all-at-once attention;
- show which unknowns can actually change the decision.

This allows microprocesses to remain lightweight while the observer reflects on the larger structure.

A mature model may therefore become **simpler** after refinement: irrelevant detail has been tested and compressed, while the few consequential boundaries remain explicit.

---

# 7. What Progressive Modeling Can Give an AI System

The claim here should be narrow.

An AI system does not become reliable merely because it is given more context, more agents, or a larger prompt. The model must be organized so that the system can distinguish evidence, assumptions, projections, uncertainty, and terminal states.

A machine-usable Observer-style representation should expose, at minimum:

- selected system and goal;
- boundary, scale, interval, and horizon;
- entities and dependency graph;
- observed facts with provenance and timestamps where relevant;
- inferred states;
- projected states;
- unknown / unresolved states;
- hard constraints and viability margins;
- actions and expected state transitions;
- rollback / recoverability path;
- stopping conditions;
- verification tests;
- confidence and model disagreement;
- history of refinements.

This is an **external auditable state representation**. It does not require preserving or exposing private chain-of-thought.

## 7.1 Why this helps

If these fields remain explicit, an AI system can allocate reasoning effort selectively:

- coarse modeling where margins are wide and evidence agrees;
- deeper analysis near failure thresholds;
- extra retrieval where provenance is weak;
- simulation where action effects are uncertain;
- alternative models where conclusions are sensitive;
- refusal to collapse an unresolved interval into a single invented state.

The main advantage is not imitation of human cognition. It is **control of representation**.

NIST's AI Risk Management Framework emphasizes validity/reliability, safety, resilience, transparency, and evaluation across the lifecycle [R11]. NIST's 2026 TEVV-Athlon draft explicitly proposes adaptable Test, Evaluation, Verification, and Validation for varied AI systems, including agentic systems [R12]. These provide external grounding for the evaluation discipline, not for the Observer model's specific architecture.

## 7.2 Evidence-backed abstraction and refinement

A useful AI loop is:

`map -> project -> detect uncertainty / contradiction -> retrieve or test -> refine -> re-project -> verify -> stop`

The loop should terminate when:

- the required claim is verified;
- the decision is robust across plausible models;
- a hard uncertainty prevents justified action;
- an external dependency is the true blocker;
- additional refinement cannot materially change the answer.

The system should not continue simply because more computation is available.

Formal verification's abstraction/refinement tradition provides a strong neighboring example: CEGAR begins from an abstraction and refines it when a counterexample is spurious or the abstraction is insufficient [R9]. The analogy is methodological, not identity.

## 7.3 Multi-agent systems

Multiple agents are not automatically a collective intelligence. The useful unit is the **interaction architecture** among them.

If several agents are used, they should not merely generate independent answers and vote. Roles may include:

- evidence retrieval;
- dependency mapping;
- adversarial assumption checking;
- simulation / scenario generation;
- preservation evaluation;
- verification;
- synthesis.

The shared model should record disagreements rather than average them away. An agent should be able to point to a specific assumption, interval, dependency, or evidence gap whose refinement could resolve the disagreement.

Several agents using the same base model, same retrieval source, or same hidden premise are correlated. Numerical agent count must not be mistaken for independent evidence.

The benefit comes from structured interaction and preserved state, not agent count alone.

## 7.4 Compression failure modes

An AI-oriented compressed state can fail by deleting exactly the exception that matters.

Before compressing, preserve:

- hard constraints;
- boundary cases;
- unresolved contradictions;
- minority / rare but consequential branches;
- provenance links;
- recovery state;
- assumptions whose removal would change the conclusion.

A summary that removes these may be shorter while making the system less intelligent operationally.

---

# 8. Complex Application Template

Consider a coupled technical system being changed while it must remain usable. The exact domain could be a live software platform, an industrial control system, a building under phased work, a laboratory instrument, or another system with multiple dependencies.

## 8.1 Sketch

Define:

- target function `H`;
- identity invariants `I`;
- viability domain `V`;
- dependency graph `D`;
- hard preservation dimensions and reserves;
- proposed intervention `a`;
- relevant horizons.

Suppose the dependency graph contains:

`H -> control interface -> service -> persistent state -> external dependency`

with a separate recovery branch:

`recovery authority -> backup / substitute -> restoration path -> verification`

## 8.2 Preservation check

Before action, evaluate intervals for:

- service continuity;
- state integrity;
- recovery access;
- restoration time versus failure delay;
- external dependency availability;
- observability after the change;
- common-cause failure between primary and recovery paths.

If the proposed action can disable both the primary path and the recovery authority, the action fails the strict preservation gate even if the expected main-path outcome is positive.

If the system is already failing and every option crosses some boundary, switch to rescue / least-loss mode rather than pretending strict preservation remains available.

## 8.3 Future-space projection

Project candidate futures onto:

- continuity;
- recoverability;
- cost;
- performance;
- future optionality.

Use coarse intervals first.

If all candidate actions remain safely above the continuity boundary with adequate reserve, refine cost/performance only as needed.

If one candidate produces:

`recoverability margin = [-0.10, +0.50]`

that region receives priority for refinement because it crosses a hard boundary.

If the only negative branch is rare but destroys irreplaceable state, the tail flag overrides low average uncertainty.

## 8.4 Interestingness

A component with many random failures may be noisy but not strategically interesting if redundancy makes causal leverage small.

A single authority, dependency, interface, or irreversible state transition may be highly interesting even if it has only a few branches, because changing it reorganizes the reachable future-space of the whole system.

Keep known structure separate from unresolved frontier. Do not award a component a high central score merely because the model knows little about it.

## 8.5 Progressive action

Choose the smallest action that can produce useful evidence without consuming the recovery path.

After the action:

- measure the actual state;
- account for measurement disturbance if material;
- update intervals;
- compare the realized state with the predicted projection;
- preserve discrepancies as evidence;
- refine the model;
- continue only if the next state-driven gate is satisfied.

This is the same architecture whether the observer is a person, a team, or an AI-assisted system.

---

# 9. Validation and Edge-Case Checklist

This section records explicit failure modes checked during the Vol. 1.2 validation pass. It is not exhaustive for every future domain; it is a minimum test set for the current formulations.

| Edge case | Handling in Vol. 1.2 |
|---|---|
| One occupied priority bin | Entropy/evenness uses fixed `K >= 2`, not occupied-bin count; result approaches 0 rather than dividing by `ln(1)`. |
| Zero-probability / zero-occupancy bins | Use `0 ln 0 = 0`. |
| Empty or contradictory reachable set | Do not report interestingness as 0; classify model as infeasible / unresolved unless it is a genuine terminal state. |
| Unbounded projection axis | Require declared finite reference scale, transform, or decision thresholds before normalized breadth. |
| Rare catastrophic branch | Keep separate hard-threshold/tail flag; entropy or average score cannot erase it. |
| Low-confidence model | Unknowns widen the interestingness interval / frontier; they do not automatically raise the central score. |
| `N_V_before = 0` | Optionality ratio undefined; report counts/fractions/weighted mass instead. |
| Different scenario sample sizes | Counts are not directly comparable unless generator, weighting, and sampling basis are controlled. |
| Already-failing system | Switch from strict preservation to rescue / least-loss mode; include non-action baseline. |
| Irreversible action | Reversal is not falsely required; demand stronger evidence, containment, forward recovery/substitution where possible, and explicit irreversible consequences. |
| Common-cause / correlated dependencies | Evaluate joint failure modes; do not infer system safety from individually positive margins. |
| Subsystem preserved, larger system harmed | Evaluate containing systems when material externalities exist. |
| Short-term preserved, long-term harmed | Use multiple horizons and report reversals. |
| Measurement changes system | Treat verification / sensing as an interaction when disturbance is material. |
| Observational sensitivity presented as causality | Use `do(·)` only when a causal intervention model is justified; otherwise label sensitivity / association honestly. |
| Several agents agree | Agreement is not independent evidence when agents share model, data, retrieval, or assumptions. |
| Compression deletes exception | Preserve hard constraints, contradictions, rare consequential branches, provenance, and recovery state before summarization. |
| Refinement loop makes no new evidence | Stop or branch; repetition without state change, new evidence, or bounded purpose is not exploration. |
| Value premises conflict | Do not hide the conflict in a weighted average; state whose/which values and constraints are being preserved. |

The checklist should grow when new applications expose new failure modes.

---

# 10. Research Grounding and Reference Map

These are **grounding parallels and notation sources**, not claims that Observer's Notes is a restatement of any one tradition.

## 10.1 Reference map by chapter

- **Preservation / viability:** [R1], [R2]
- **Entropy / distribution evenness:** [R3]
- **Causal intervention notation:** [R4]
- **Rigorous interval methods:** [R5]
- **Adaptive refinement analogy:** [R6], [R7]
- **Receding-horizon control analogy:** [R8]
- **Abstraction/refinement analogy:** [R9]
- **Systems V&V / end-to-end testing:** [R10]
- **AI lifecycle risk and evaluation:** [R11], [R12]
- **Information-gain-oriented experimental refinement:** [R13]

## 10.2 References

**[R0] Beregovykh, Nikita.** *Observer's Notes: A Field Book.* Public discussion draft, 2026. Repository: https://github.com/nvberegovykh/Observer-s-Notes

**[R1] Aubin, Jean-Pierre.** *Viability Theory.* Modern Birkhäuser Classics, 2009 edition. Springer/Birkhäuser. https://link.springer.com/book/10.1007/978-0-8176-4910-4

**[R2] Holling, C. S.** "Resilience and Stability of Ecological Systems." *Annual Review of Ecology and Systematics* 4 (1973): 1–23. DOI: 10.1146/annurev.es.04.110173.000245. https://doi.org/10.1146/annurev.es.04.110173.000245

**[R3] Shannon, Claude E.** "A Mathematical Theory of Communication." *Bell System Technical Journal* 27 (1948), parts I–II, pp. 379–423 and 623–656. DOI part I: 10.1002/j.1538-7305.1948.tb01338.x; part II: 10.1002/j.1538-7305.1948.tb00917.x. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

**[R4] Pearl, Judea.** *Causality: Models, Reasoning, and Inference.* 2nd ed. Cambridge University Press, 2009. Intervention / `do(·)` calculus discussed in Chapter 3. https://bayes.cs.ucla.edu/BOOK-2K/

**[R5] Moore, Ramon E.; Kearfott, R. Baker; Cloud, Michael J.** *Introduction to Interval Analysis.* SIAM, 2009. DOI: 10.1137/1.9780898717716. https://doi.org/10.1137/1.9780898717716

**[R6] Berger, Marsha J.; Oliger, Joseph.** "Adaptive Mesh Refinement for Hyperbolic Partial Differential Equations." *Journal of Computational Physics* 53(3) (1984): 484–512. DOI: 10.1016/0021-9991(84)90073-1. https://doi.org/10.1016/0021-9991(84)90073-1

**[R7] Berger, Marsha J.; Colella, Phillip.** "Local Adaptive Mesh Refinement for Shock Hydrodynamics." *Journal of Computational Physics* 82(1) (1989): 64–84. DOI: 10.1016/0021-9991(89)90035-1. https://doi.org/10.1016/0021-9991(89)90035-1

**[R8] Mayne, D. Q.; Rawlings, J. B.; Rao, C. V.; Scokaert, P. O. M.** "Constrained Model Predictive Control: Stability and Optimality." *Automatica* 36(6) (2000): 789–814. DOI: 10.1016/S0005-1098(99)00214-9. https://doi.org/10.1016/S0005-1098(99)00214-9

**[R9] Clarke, Edmund M.; Grumberg, Orna; Jha, Somesh; Lu, Yuan; Veith, Helmut.** "Counterexample-Guided Abstraction Refinement." In *Computer Aided Verification (CAV 2000)*, LNCS 1855, pp. 154–169. DOI: 10.1007/10722167_15. https://doi.org/10.1007/10722167_15

**[R10] NASA.** *NASA Systems Engineering Handbook* and current verification/validation guidance, including complete-system and end-to-end integration. NASA/SP-2016-6105 Rev2; current web guidance: https://www.nasa.gov/reference/system-engineering-handbook-appendix/ and https://www.nasa.gov/reference/5-3-product-verification/

**[R11] NIST.** *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1, 2023. https://www.nist.gov/itl/ai-risk-management-framework

**[R12] NIST.** *The TEVV-Athlon Framework for Evaluating AI Systems.* Initial public draft / NIST AI 200-2 announcement, August 7, 2026; public comment period announced through October 6, 2026. https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems

**[R13] Lindley, Dennis V.** "On a Measure of the Information Provided by an Experiment." *Annals of Mathematical Statistics* 27(4) (1956): 986–1005. DOI: 10.1214/aoms/1177728069. https://doi.org/10.1214/aoms/1177728069

---

# 11. Condensed Vol. 1.2 Procedure

For a complex problem:

1. **Localize.** State system, purpose, scale, interval, horizon, and value premise.
2. **Sketch.** Map elements, relations, identity invariants, viability boundaries, and dependencies.
3. **Preserve.** Identify access, continuity, recoverability, irreplaceable state, lower-level conditions, reserves, and verification capacity before consequential action.
4. **Project.** Compress future-space into decision-relevant intervals plus occupancy, provenance, confidence, and unresolved boundaries.
5. **Find interesting regions.** Prioritize elements that produce broad, consequential, causally leveraged future structure; keep unresolved frontier separate from known score.
6. **Refine selectively.** Spend resolution where uncertainty, sensitivity, disagreement, tail risk, or threshold proximity can change the decision.
7. **Probe carefully.** Prefer the least destructive evidence-producing action that can distinguish relevant possibilities, unless emergency dynamics make delay more destructive.
8. **Act statefully.** Use gates, cutoffs, stopping conditions, and terminal states rather than blind waits or infinite loops.
9. **Verify at the level of the claim.** Artifact identity, unit behavior, integration, and end-to-end viability are different claims requiring different evidence.
10. **Re-project.** Update the local model from the observed result. Preserve discrepancies instead of smoothing them away.
11. **Stop when grounded.** End refinement when the conclusion is robust enough for the declared purpose, when remaining uncertainty cannot change the action class, or when uncertainty prevents a justified action.

The method does not require the whole world to be modeled. It requires the model to remain honest about what it includes, what it projects, what it does not know, what assumptions make the projection possible, and what would be damaged if it is wrong.

---

## Signature

**Nikita Beregovykh & ChatGPT 5.6 Sol, Observers Notes extension 1**
