# Observer's Notes — Vol. 1.2

## Extension 1: Preservation, Interestingness, Projection, and Progressive Modeling

**Status:** working extension notes. Deliberately kept in technical-note form rather than the illustrated / field-book presentation of Vol. 1.

**Purpose:** extend the operational side of the original model without replacing its definitions. The extension focuses on questions that became clearer after the first edition: what preservation actually means in a changing system; how to identify an interesting element without enumerating every future; how interval projection can compress future-space; how coarse models can be refined only where needed; and why this organization can improve reasoning for both humans and AI systems when evidence, assumptions, and uncertainty remain explicit.

---

## 0. Compatibility with Vol. 1

Vol. 1 already establishes the important base:

- select the system, purpose, scale, and interval;
- distinguish elements from relations;
- define identity by invariants and tolerances;
- define a viability domain and current margin;
- map lower-level dependencies, buffers, substitutes, delays, and thresholds;
- identify maintenance, recursive maintenance, and generative maintenance;
- state the value premise before optimization;
- attach intervention to measurement, reversibility, a return path, verification, and a stopping condition.

Vol. 1 also states that preservation and generation may conflict, and that generative maintenance can require change, pruning, recombination, or the end of a structure that blocks future viability.

What remained under-specified was **preservation evaluation itself**. The word can be misread as "keep everything unchanged." That is not the intended meaning.

This extension also adds a practical method for working with systems whose future-state space is too large to enumerate. The method is based on **local projections, intervals, occupancy structure, confidence, and adaptive refinement**.

---

# 1. Preservation Evaluation

## 1.1 Preservation is selected continuity, not frozen material

Preservation is always relative to a model.

For a selected system `S`, define:

- `Θ` — declared assumptions;
- `σ` — scale;
- `Δt` — evaluation interval;
- `I` — identity invariants and tolerances;
- `V` — viability conditions;
- `D` — constitutive dependencies;
- `W` — the value premise that explains why preservation is being evaluated.

Then preservation asks:

> After an action or disturbance, does enough of the selected organization, dependency base, and recoverability remain for the valued system to stay viable, remain identifiable, or return to an acceptable state within the declared interval?

The preserved object is therefore not necessarily the same material object.

A server can be replaced while a service is preserved. A cell replaces molecules while preserving organization. A building can receive new structural members while preserving its use and load path. A scientific model can change while preserving the evidence and the ability to reproduce earlier conclusions.

Conversely, material can remain while the system is lost. A database file may still exist while its keys, schema, credentials, or recovery path are gone. A biological body may remain present after viability is lost. A machine may retain every component while a constitutive relation is broken.

**Preservation therefore concerns selected invariants, relations, dependencies, and recoverability, not mere persistence of substance.**

## 1.2 The preservation vector

A single preservation score is usually too aggressive. Start with a vector.

For a proposed action `a`, project each required preservation dimension into a post-action margin interval:

`m_j(a) = [lower_j, upper_j]`

where zero is the declared failure boundary for that dimension.

Useful dimensions include:

| Dimension | Question |
|---|---|
| Identity margin `M_I` | Are the invariants that define the selected system still within tolerance? |
| Viability margin `M_V` | Do the required operating / survival conditions remain inside the viability domain? |
| Dependency margin `M_D` | Are lower-level processes, external conditions, buffers, substitutes, and interfaces still available? |
| Continuity `C` | Can the required function continue through the intervention and recovery interval? |
| Recoverability `R` | Is there an evidence-backed path to a known viable state if the action fails? |
| Access / control `A` | Will the actors or control processes required for recovery still be able to reach and change the system? |
| Irreplaceable-state integrity `K` | Are records, memory, keys, unique data, physical specimens, identity state, or other non-reconstructable dependencies protected? |
| Verification capacity `Q_V` | Can the post-action state be measured well enough to know whether preservation actually succeeded? |

The exact dimensions depend on the localized system. "Credentials" matter in a software platform; reproductive capacity may matter in a population; load-path continuity may matter in a structure. Do not force domain-specific variables into every model.

## 1.3 Hard preservation gate

For any action that claims to preserve a selected system, use a gate before optimization.

**Gate P:**

1. Declare the system, value premise, scale, interval, identity invariants, and viability boundaries.
2. Identify constitutive dependencies and irreplaceable state.
3. For every hard preservation dimension `j`, require the **lower bound** of the projected post-action margin to remain non-negative:

   `lower(m_j(a)) >= 0`

   unless crossing that boundary is an explicitly accepted transformation rather than accidental loss.
4. Require a recovery path when recovery is physically meaningful.
5. Require the recovery path to remain reachable after the same failure that the recovery path is supposed to correct. A rollback stored behind a credential that the intervention may destroy is not a recovery path.
6. Require monitoring / verification to resolve dangerous drift before an irreversible threshold is crossed, when that is feasible.
7. State the stopping condition before action.
8. Re-evaluate after each consequential state change. Time elapsed is not evidence that the enabling condition has become true.

This is intentionally state-driven. "Wait five minutes and continue" is weaker than "continue when the required state is observed and verified."

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

A preservation claim is incomplete if it preserves the visible top layer while silently destroying a constitutive lower layer.

## 1.5 Preservation is not the maximization of stability

Maximum stability is not automatically desirable. A perfectly fixed system may be unable to learn, adapt, repair, or generate alternatives.

Preservation can therefore be divided into at least three modes:

- **identity preservation** — maintain the selected invariants;
- **viability preservation** — maintain the conditions that keep the system inside its viable domain;
- **generative preservation** — maintain or expand valuable reachable viable futures.

These modes can conflict.

A repair may alter identity-relevant material while preserving function. A migration may temporarily reduce continuity while increasing recoverability. Pruning may remove one structure while improving the viability of a larger system.

The value premise decides which constraints are hard and which transformations are acceptable. The model does not derive that premise from physics.

## 1.6 Optionality as a preservation/generation check

When an action explicitly claims to preserve or expand future options, define, under a fixed horizon and scenario generator:

`O = N_V_after / N_V_before`

where `N_V` is the number of sampled reachable states that satisfy the declared viability conditions.

For a **generative-preservation claim**, a useful conservative gate is:

- `O >= 1`, and
- `M_min >= 0`, where `M_min` is the minimum required viability margin across hard constraints.

This is not a universal moral rule and not a universal optimizer. The result depends on the scenario generator, horizon, state representation, and viability model. Report the viable count **and** viable fraction, because either can improve while the other worsens.

Unknown futures must not be fabricated to improve `O`.

## 1.7 Preservation under uncertainty

Uncertainty should widen the model, not silently become confidence.

If the effect of an action on a dependency is uncertain, record an interval or unresolved boundary. For example:

`M_D(a) = [-0.15, +0.40]`

This does not mean the dependency is half-preserved. It means the current model cannot establish that the lower bound remains viable.

For hard constraints, unresolved overlap with failure is a reason to refine the model, reduce the intervention, add a buffer, or refrain from claiming preservation.

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

## 2.3 Priority projection

Let `F_x(T)` be the modeled set of futures reachable over horizon `T` when element `x` is relevant.

Project those futures onto a declared priority dimension `U`, for example a normalized success/failure scale:

`U in [-1, +1]`

Partition the scale into declared bins. The bins should be fixed before comparing elements so that sampling density does not quietly change the measure.

Let `p_b` be the fraction or modeled probability mass in priority bin `b`.

A normalized occupancy evenness can be written:

`E_U = -sum(p_b * ln(p_b)) / ln(B)`

for `B` occupied comparison bins.

`E_U` approaches 1 when occupancy is broadly distributed and approaches 0 when futures collapse into a narrow region.

This **does not mean failure is desirable**. Evenness is a measurement of breadth across the declared outcome scale, not an instruction to seek harmful outcomes.

## 2.4 Causal leverage

To distinguish consequential branching from noise, compare the projected future-space with and without a meaningful change in `x`.

Let:

`C_x = distance(P(F | do(x = x1)), P(F | do(x = x0)))`

where `P` is the chosen projection and `distance` is a declared comparison rule suitable for the domain.

In observational domains where intervention is impossible, use the strongest available causal or counterfactual method and state its limitations.

An element with broad futures but negligible `C_x` is uncertain, but not necessarily an important branching point.

## 2.5 Discovery frontier

Unknown territory should be represented without inventing specific futures.

Define `R_x` as an evidence-backed unresolved-frontier term. It should increase only when there is a reason to believe the present model is incomplete, such as:

- materially different models disagree;
- small assumption changes move the result strongly;
- observed data repeatedly falls near or outside modeled bounds;
- an important dependency is known but poorly resolved;
- the projection contains open boundaries that affect the decision.

Simple ignorance is not automatically discovery potential.

## 2.6 Interestingness vector before scalar score

Use a vector before collapsing to a score:

`I_vec(x) = (B_x, E_x, C_x, R_x, Q_x)`

where:

- `B_x` = normalized breadth of reachable projected intervals;
- `E_x` = occupancy / distribution evenness across declared priority bins;
- `C_x` = causal leverage;
- `R_x` = evidence-backed unresolved frontier;
- `Q_x` = confidence / grounding quality of the current projection.

Only if a scalar ranking is necessary should weights be declared explicitly. One possible family is:

`I_w(x) = C_x * [ Q_x * (w_B*B_x + w_E*E_x) + (1-Q_x) * w_R*R_x ]`

This form has an important property: known structured branching and unresolved frontier can both contribute, but unresolved frontier contributes only when it is supported by evidence of model incompleteness rather than imaginary branches.

The weights are local. There is no claim here that this is a universal law of interestingness.

---

# 3. Projection of Intervals

## 3.1 Why projection is necessary

Complex systems produce combinatorial explosion. Explicitly enumerating all futures quickly becomes impossible and often creates false precision.

Instead of maintaining every future `f_1 ... f_n`, project the reachable set onto a small number of dimensions relevant to the current question.

For dimension `k`:

`P_k(F) = ([l_k, u_k], rho_k, q_k, r_k-, r_k+)`

where:

- `[l_k, u_k]` = current resolved interval of reachable values;
- `rho_k` = occupancy structure inside the interval (bins, density estimate, support classes, or another local representation);
- `q_k` = grounding / confidence of the projection;
- `r_k-`, `r_k+` = unresolved lower and upper exterior territory where the model may be incomplete.

The interval alone is insufficient.

These two projected future sets have the same outer interval but different internal structure:

`A: dense support across [-1, +1]`

`B: support only near -1 and +1`

They should not receive the same interpretation.

## 3.2 Projection is not permission to hide assumptions

Every projection must carry:

- source variables;
- transformation rule;
- scale;
- horizon;
- thresholds;
- sampling / scenario generator;
- unresolved variables;
- provenance of measured values;
- distinction between observed, inferred, simulated, and unknown states.

A compact projection is useful only if the path back to its assumptions remains inspectable.

## 3.3 Interval enclosure versus descriptive interval

There is an important distinction.

A mathematically rigorous interval enclosure guarantees that the true value lies inside the interval under the stated numerical assumptions. Classical interval analysis provides methods for this in suitable numerical problems.

A systems-modeling interval may instead be a descriptive bound derived from scenarios, measurements, expert constraints, or model ensembles. It should not be described as a rigorous enclosure unless it actually has that property.

This extension uses **interval projection** in the broader systems-modeling sense unless rigorous enclosure is explicitly established.

## 3.4 Adaptive refinement

Start coarse.

Refine only where additional resolution can change understanding or action.

A useful loop is:

1. **Project** the current reachable set coarsely.
2. **Measure** breadth, occupancy, uncertainty, sensitivity, and distance to relevant thresholds.
3. **Select** regions with high leverage, high unresolved uncertainty, model disagreement, or proximity to a decision boundary.
4. **Refine** those regions into smaller intervals / submodels.
5. **Validate** the refinement using new evidence, a materially different method, or a controlled probe.
6. **Propagate** revised bounds upward to the larger model.
7. **Stop** when the decision is stable under further plausible refinement, when remaining uncertainty cannot change the action class, or when no safe evidence-producing step remains.

This resembles adaptive mesh refinement computationally: allocate resolution where the solution needs it rather than everywhere. The analogy is methodological, not an assertion that every systems model is a numerical mesh.

## 3.5 Decision-focused resolution

Resolution should be tied to the decision.

If the current interval is:

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
2. boundary, scale, and interval;
3. elements and relations;
4. identity invariants;
5. viability domain;
6. dependencies and external conditions;
7. buffers, substitutes, delays, and thresholds;
8. evidence sources;
9. action points;
10. preservation gates and terminal states.

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
- `Q_consistency` — agreement across independent or materially different methods.

Do not average these blindly. A very low value in one critical dimension can dominate the decision.

## 4.3 End-to-end paths instead of local symptoms

For any user-visible or system-visible goal, trace the complete path from initiating action to terminal state.

A generic chain is:

`initiator -> authority -> input -> transformation -> dependency -> persistence -> output -> verification -> recovery`

A local component can pass every unit check while the end-to-end goal remains impossible.

Evidence therefore has levels:

- hashes / identity markers can prove artifact integrity;
- builds can prove compilation;
- narrow tests can prove local behavior;
- only end-to-end acceptance can demonstrate that the selected system goal remains reachable through its real dependencies.

This distinction matters for both engineering and conceptual models. Evidence should prove the claim actually being made.

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

---

# 5. Exploration Without Destructive Blindness

## 5.1 The knife rule

Cutting can be an extremely efficient way to learn what is inside something. It can also destroy the relation that made the object interesting.

The general rule is:

> The efficiency of a probe does not cancel the cost of the disturbance it creates.

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
7. irreversible intervention only after the preservation gate, value premise, and failure consequences are explicit.

This is not a requirement to be maximally conservative. Excessive caution can also destroy viability by preventing necessary action. The purpose is to make disturbance and recoverability explicit rather than invisible.

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
- allow calm re-entry after interruption;
- preserve earlier reasoning so it does not need to be reconstructed from memory;
- permit coarse-to-fine attention rather than all-at-once attention;
- show which unknowns can actually change the decision.

This allows microprocesses to remain lightweight while the observer reflects on the larger structure.

---

# 7. What Progressive Modeling Can Give an AI System

The claim here should be narrow.

An AI system does not become reliable merely because it is given more context, more agents, or a larger prompt. The model must be organized so that the system can distinguish evidence, assumptions, projections, uncertainty, and terminal states.

A machine-usable Observer-style representation should therefore expose, at minimum:

- selected system and goal;
- boundary, scale, and horizon;
- entities and dependency graph;
- observed facts with provenance;
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

## 7.1 Why this helps

If these fields remain explicit, an AI system can allocate reasoning effort selectively:

- coarse modeling where margins are wide and evidence agrees;
- deeper analysis near failure thresholds;
- extra retrieval where provenance is weak;
- simulation where action effects are uncertain;
- alternative models where conclusions are sensitive;
- refusal to collapse an unresolved interval into a single invented state.

The main advantage is not imitation of human cognition. It is **control of representation**.

## 7.2 Evidence-backed abstraction and refinement

A useful AI loop is:

`map -> project -> detect uncertainty / contradiction -> retrieve or test -> refine -> re-project -> verify -> stop`

The loop should terminate when:

- the required claim is verified;
- the decision is robust across plausible models;
- a hard uncertainty prevents safe action;
- an external dependency is the true blocker;
- additional refinement cannot materially change the answer.

The system should not continue simply because more computation is available.

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

The shared model should record disagreements rather than average them away. An agent should be able to point to a specific assumption, interval, or dependency whose refinement could resolve the disagreement.

The benefit comes from structured interaction and preserved state, not agent count alone.

---

# 8. Complex Application Template

Consider a coupled technical system being changed while it must remain usable. The exact domain could be a live software platform, an industrial control system, a building under phased work, a laboratory instrument, or another system with multiple dependencies.

## 8.1 Sketch

Define:

- target function `H`;
- identity invariants `I`;
- viability domain `V`;
- dependency graph `D`;
- hard preservation dimensions;
- proposed intervention `a`.

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
- observability after the change.

If the proposed action can disable both the primary path and the recovery authority, the action fails the preservation gate even if the expected main-path outcome is positive.

## 8.3 Future-space projection

Project candidate futures onto:

- continuity;
- recoverability;
- cost;
- performance;
- future optionality.

Use coarse intervals first.

If all candidate actions remain safely above the continuity boundary, refine cost/performance only as needed.

If one candidate produces:

`recoverability margin = [-0.1, +0.5]`

that region receives priority for refinement because it crosses a hard boundary.

## 8.4 Interestingness

A component with many random failures may be noisy but not strategically interesting if redundancy makes `C_x` small.

A single authority, dependency, interface, or irreversible state transition may be highly interesting even if it has only a few branches, because changing it reorganizes the reachable future-space of the whole system.

## 8.5 Progressive action

Choose the smallest action that can produce useful evidence without consuming the recovery path.

After the action:

- measure the actual state;
- update intervals;
- compare against the predicted projection;
- preserve discrepancies as evidence;
- refine the model;
- continue only if the next state-driven gate is satisfied.

This is the same architecture whether the observer is a person, a team, or an AI-assisted system.

---

# 9. Research Grounding and Adjacent Formal Traditions

These are **grounding parallels**, not claims that Observer's Notes is a restatement of any one of them.

## 9.1 Viability theory

Jean-Pierre Aubin's viability theory studies states and trajectories that can remain inside constraints, including viability kernels, regulation, invariance, and exit behavior. This provides a formal neighboring language for the Vol. 1 concepts of viability domains and margins.

Reference: Jean-Pierre Aubin, *Viability Theory*, Springer/Birkhäuser, 2009 edition.

https://link.springer.com/book/10.1007/978-0-8176-4910-4

## 9.2 Interval analysis

Interval analysis represents uncertain numerical quantities by enclosures and propagates bounds through calculations. It is relevant to the interval-projection idea when rigorous numerical enclosure is possible, while this extension also uses looser scenario / model intervals that must not be mislabeled as rigorous interval arithmetic.

Reference: Ramon E. Moore, R. Baker Kearfott, Michael J. Cloud, *Introduction to Interval Analysis*, SIAM.

https://epubs.siam.org/doi/book/10.1137/1.9780898717716

## 9.3 Adaptive mesh refinement

Adaptive mesh refinement uses coarse resolution broadly and finer resolution in regions requiring it. The direct mathematical machinery belongs to numerical simulation, but the resource-allocation principle closely parallels the proposed adaptive refinement of a systems model.

A review hosted by Lawrence Livermore National Laboratory describes structured AMR as a hierarchy of coarse and fine regions derived from the Berger/Oliger/Colella line of work.

https://www.osti.gov/servlets/purl/952096

## 9.4 Model predictive control

Model predictive control repeatedly predicts over a finite horizon, applies a limited control move, obtains a new state estimate, and solves again under constraints. The Observer-style loop is broader and not equivalent to MPC, but the receding-horizon pattern is a useful established neighbor to "project, act locally, measure, and re-evaluate."

https://www.mathworks.com/help/mpc/gs/what-is-mpc.html

## 9.5 Abstraction and refinement

Formal verification uses abstraction/refinement techniques to begin with a coarser representation and refine it when the abstraction is insufficient or produces a spurious counterexample. Counterexample-guided abstraction refinement (CEGAR) is one established example.

Microsoft Research overview / publication:

https://www.microsoft.com/en-us/research/publication/abstract-counterexample-based-refinement-for-powerset-domains/

The analogy is again methodological: do not pay for maximum resolution everywhere; refine where the coarse model fails to support the required conclusion.

## 9.6 Systems engineering verification and validation

NASA's Systems Engineering Handbook emphasizes system architecture, requirements validation, verification methods, margins, and system-level / end-to-end validation. This supports the distinction made here between artifact identity, local checks, and actual end-to-end system viability.

https://www.nasa.gov/reference/system-engineering-handbook-appendix/

## 9.7 AI evaluation

NIST's AI Risk Management Framework treats AI risk management as a lifecycle activity involving validity, reliability, safety, resilience, transparency, and ongoing evaluation. In August 2026 NIST also released a draft TEVV-Athlon framework for structured Test, Evaluation, Verification, and Validation across varied AI systems, including agentic systems.

These sources ground the claim that AI reasoning architectures should expose evaluation, monitoring, uncertainty, and system-specific criteria rather than relying only on fluent output.

https://www.nist.gov/itl/ai-risk-management-framework

https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems

---

# 10. Condensed Vol. 1.2 Procedure

For a complex problem:

1. **Localize.** State system, purpose, scale, interval, horizon, and value premise.
2. **Sketch.** Map elements, relations, identity invariants, viability boundaries, and dependencies.
3. **Preserve.** Identify access, continuity, recoverability, irreplaceable state, lower-level conditions, and verification capacity before consequential action.
4. **Project.** Compress future-space into decision-relevant intervals plus occupancy and unresolved boundaries.
5. **Find interesting regions.** Prioritize elements that produce broad, consequential, causally leveraged future-space or evidence-backed unresolved frontier.
6. **Refine selectively.** Spend resolution where uncertainty, sensitivity, disagreement, or threshold proximity can change the decision.
7. **Probe carefully.** Prefer the least destructive evidence-producing action that can distinguish relevant possibilities.
8. **Act statefully.** Use gates, cutoffs, stopping conditions, and terminal states rather than blind waits or infinite loops.
9. **Verify end to end.** Match the strength of evidence to the strength of the claim.
10. **Re-project.** Update the local model from the observed result. Preserve discrepancies instead of smoothing them away.
11. **Stop when grounded.** End refinement when the conclusion is robust enough for the declared purpose or when remaining uncertainty prevents a justified action.

The method does not require the whole world to be modeled. It requires the model to remain honest about what it includes, what it projects, what it does not know, and what would be damaged if it is wrong.

---

## Signature

**Nikita Beregovykh & ChatGPT 5.6 Sol, Observers Notes extension 1**
