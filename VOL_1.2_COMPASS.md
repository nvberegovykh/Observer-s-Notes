# Observer's Notes — Vol. 1.2

# COMPASS

*An ocean field book for grounded exploration*

**Extension 1**

---

## Publication note

This volume extends *Observer's Notes* without replacing its definitions.

The technical vocabulary of Vol. 1 remains authoritative: element, state, interaction, relation, structure, condition, viability domain, maintenance, recursive maintenance, generative maintenance, observer effect, value premise, and intervention keep their earlier meanings.

The ocean expedition is only the environment in which the new notes unfold. It is not a second technical vocabulary. A buoy may appear in the story; the model still speaks about an element, a measured state, a relation, uncertainty, or a reference. A reef may be present in the scene; the technical text still speaks about a boundary or constraint.

The story is allowed to make an idea easier to see. It is not allowed to establish the idea as true.

The conceptual extensions in this volume grew from post-publication working discussions between Nikita Beregovykh and ChatGPT in 2026. External references are listed at the end as neighboring formal traditions, notation sources, and grounding for specific operational claims. They are not presented as the origin of the Observer's Notes model.

· ❦ ·

> *A compass does not decide where to go. It helps preserve orientation while the surroundings move.*

## A note before sailing

A small research vessel leaves a harbor before sunrise. Not far offshore stands a weather buoy. Its light is easy to see. Its radio is not always quiet.

At first the buoy seems like a convenient reference. Later the crew discovers that its signal has noise. Then that the buoy itself can drift. Then that the current affecting the buoy also affects the vessel. Then that a second instrument disagrees. Each new observation complicates the picture, but not arbitrarily. The same environment is being revisited with a better model.

That continuity is the purpose of the expedition.

A story can hold assumptions still long enough for hidden variables to become visible. The variables do not become part of the general model merely because the story contains them. They must survive operational definition, evidence, comparison, and reuse.

The notes that follow keep the pattern of Vol. 1:

**observation → general statement → limits → field note → carry-forward rules → operational model → measurements → use → example → validation.**

The formulas are deliberately small. A formula should clarify a measurable relation, not serialize the entire model into letters.

---

## Contents

| Ref | Note |
|:---:|---|
| C1 | [The Buoy That Wouldn't Be Quiet](#c1) |
| C2 | [The Current That Wasn't on the Chart](#c2) |
| C3 | [What Must Survive the Crossing](#c3) |
| C4 | [The Water Ahead](#c4) |
| C5 | [Soundings Near the Shoal](#c5) |
| C6 | [The Return Route](#c6) |
| C7 | [The Logbook After the Storm](#c7) |
| C8 | [The Compass](#c8) |

> Vol. 1 definitions remain inherited. C1–C8 introduce only extension-specific operational terms.

---

<a id="c1"></a>

# C1 · The Buoy That Wouldn't Be Quiet

*Evidence can disagree before the system itself changes*

### Observation

*The vessel is still close enough to see the harbor lights. Ahead, the weather buoy flashes at a steady interval. Its radio packet reports position, wind, and wave height. The first reading is clean. The second differs slightly. The third differs again.*

*Nothing obvious has moved. The sea looks calm.*

The simplest response would be to average the readings and continue. That may be correct. It may also erase the first useful clue.

An observation is not identical to the state being observed. It is a state estimate produced through an instrument, method, sampling interval, calibration, and interpretation. Vol. 1 already placed the observer inside the instrument. Here the consequence becomes operational: two observations of the same selected variable can disagree without immediately telling us why.

The disagreement may come from measurement noise. It may come from time variation. It may come from different spatial locations, calibration drift, unmodeled interaction, or a mistaken assumption that both instruments are measuring the same thing.

The first task is therefore not to explain the disagreement. It is to preserve it.

· ❦ ·

A model becomes unreliable when disagreement is automatically compressed into one value. Agreement is evidence only to the extent that the methods are sufficiently independent and their scopes overlap. Repeated readings from one faulty instrument do not become independent because there are many of them.

The buoy is useful precisely because it remains in the scene. Later, if its position changes, the earlier noisy measurements can be reinterpreted. A record that seemed unimportant may become evidence of drift.

This gives Compass its first discipline: **keep observations, uncertainty, method, time, and provenance separable from the explanation placed on top of them.**

### Field note

> *A noisy reference is still a reference if its uncertainty is kept visible.*

**What to carry forward**

- Preserve disagreement before explaining it.
- Record method, time, scope, and uncertainty with a measurement.
- Many correlated observations are not many independent observations.
- Do not promote a measurement artifact into a system variable without evidence.

### Operational model

*A measurable local template, not a universal law.*

For two estimates of the same selected quantity, a simple standardized disagreement is:

$$
D = \frac{|x_1-x_2|}{\sqrt{u_1^2+u_2^2}}
$$

The value is useful only when the uncertainty terms are comparable and the estimates refer to the same quantity and interval.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $x_1,x_2$ | two estimates of the same selected quantity [native units] |
| $u_1,u_2$ | stated standard uncertainty or comparable uncertainty scale [same units as $x$] |
| $D$ | standardized disagreement [dimensionless] |

#### How to use it

1. Confirm that the two estimates refer to the same variable, scope, and relevant interval.
2. Record uncertainty before comparing values.
3. Treat a large $D$ as a reason to investigate method, time, boundary, or hidden variables—not as proof of any one cause.

**Working example.** One position estimate is 12.0 m from a reference line with 0.5 m uncertainty; another is 13.2 m with 0.6 m uncertainty. $D\approx1.54$. The estimates disagree enough to justify checking timing, calibration, and motion before collapsing them into one position.

**Limit.** A small $D$ does not prove correctness. Two methods can agree because they share the same bias.

**READ THE RESULT**

$D$ reports disagreement relative to stated uncertainty. It does not identify the cause.

**VALIDATE IT**

Repeat with a materially different method, calibration path, or observation interval. Check whether disagreement follows the instrument, the time, or the system.

---

<a id="c2"></a>

# C2 · The Current That Wasn't on the Chart

*Applications expose hidden variables through residuals*

### Observation

*By midmorning the buoy is no longer where the chart says it should be. The first explanation is instrument error. Then the vessel's own dead-reckoned position begins to differ from GPS in the same direction.*

*The buoy may not be the problem.*

A general model begins with selected variables. Real applications force those variables through sequences of actual interactions. When the realized state repeatedly falls outside the model's supported range, the mismatch is information.

A residual is the difference between a model's prediction and an observation under the same declared conditions. A residual can come from noise, a wrong parameter, a wrong boundary, a wrong scale, a wrong relation, or a missing variable.

The important move is not to invent a hidden cause. It is to ask what additional variable would have to exist for the observed chain to become coherent, and then test that candidate independently.

In the expedition, a lateral current becomes a candidate because it can affect both the buoy and the vessel in the observed direction. The story makes the candidate visible. The model still has to earn it.

· ❦ ·

Candidate variables should not enter the reusable template merely because they produce a satisfying explanation once.

A candidate becomes stronger when it can be operationally defined, measured or bounded, connected through a plausible relation, shown to reduce residuals outside the case that suggested it, and shown to matter to the decision or viability boundary.

Recurrence matters most when it crosses contexts. Recovery-path independence, observer disturbance, common-cause dependency, delay, and hidden shared resources are examples of variables that can recur across very different systems while retaining the same operational relation.

### Field note

> *A residual is not an embarrassment. It is a place where the chart and the world have stopped agreeing.*

**What to carry forward**

- A hidden variable begins as a candidate, not a fact.
- Check simpler explanations before adding model dimensions.
- Prefer variables with operational definitions and observable consequences.
- A variable becomes more reusable when it survives materially different cases.
- Previously promoted variables may later be demoted.

### Operational model

*A measurable local template for candidate-variable testing.*

Let $R_0$ be prediction error under the current model and $R_x$ the error after adding candidate variable $x$ under the same validation rule.

$$
\Delta R_x = R_0-R_x
$$

A positive $\Delta R_x$ means the candidate reduced residual error. Promotion still requires checks against overfitting, alternative explanations, and decision relevance.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $R_0$ | baseline prediction error under the existing model [declared error unit] |
| $R_x$ | prediction error after adding candidate $x$ [same unit] |
| $\Delta R_x$ | residual reduction [same unit] |

#### How to use it

1. Define the error rule before comparing models.
2. Add one candidate relation or variable where practical.
3. Test on data or cases not used to invent the candidate.
4. Record whether the candidate changes a decision, explanation boundary, or viability margin.

**Working example.** Position error averages 18 m without a current term and 6 m after adding a measured lateral-current estimate on a later segment. $\Delta R_x=12$ m. The current is locally supported, but not yet a universal variable for every navigation model.

**Limit.** Better fit alone can reward unnecessary complexity. Validation must include independent cases or an independently grounded mechanism.

**READ THE RESULT**

Positive $\Delta R_x$ supports usefulness of the candidate under the stated validation rule; it does not prove causality by itself.

**VALIDATE IT**

Test a different route, time, instrument, or system where the same candidate predicts a measurable effect before seeing the outcome.

---

<a id="c3"></a>

# C3 · What Must Survive the Crossing

*Preservation is selected continuity, not frozen material*

### Observation

*The vessel turns farther offshore. A shoal lies between the current position and the next sampling station. The boat does not need to remain on its present heading. It does need to remain capable of completing the crossing—or returning from it.*

The original Notes distinguished persistence, maintenance, viability, intervention, and generative maintenance. Preservation remained easier to misunderstand.

Preservation does not mean keeping every material component unchanged. It means retaining the selected invariants, relations, conditions, and recovery capacity required by the stated value premise over the stated interval and horizon.

A part may be replaced while the system is preserved. Material may remain while the system is lost.

A server can be replaced while a service continues. A structural member can be strengthened while a building's use and load path remain. A scientific model can change while evidence, provenance, and reproducibility are preserved.

Preservation is therefore evaluated against the selected system definition, not against visual sameness.

· ❦ ·

The evaluation should include more than immediate function. A change can preserve today's output while removing the ability to repair tomorrow's failure. It can preserve the selected subsystem while damaging a containing system. It can preserve a primary path while making the backup depend on the same failure source.

The lower-level dependency map matters.

For consequential action, preservation evaluation should normally include identity, viability, constitutive dependencies, continuity, access/control, irreplaceable state, recoverability, and verification capacity when those dimensions are relevant.

These are not new universal categories forced onto every problem. They are prompts to check whether the selected system's real dependencies have been represented.

### Field note

> *Preserve what makes continuation possible, not merely what happens to be present now.*

**What to carry forward**

- State what is being preserved and why.
- Distinguish identity preservation from viability preservation and generative preservation.
- Check lower-level and containing-system dependencies.
- A recovery path must survive the failure it is intended to recover from.
- When strict preservation is already impossible, switch to rescue / least-loss evaluation rather than pretending otherwise.

### Operational model

*A local preservation gate.*

For every declared hard condition $j$, let $\underline m_j(a)$ be the conservative lower bound of the projected post-action margin and $r_j$ the required reserve.

Strict preservation requires:

$$
\underline m_j(a) \ge r_j \qquad \text{for every hard condition } j
$$

The conditions should be checked jointly when common-cause failure is possible.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $a$ | proposed action or intervention |
| $\underline m_j(a)$ | conservative lower bound of post-action margin for condition $j$ [domain unit] |
| $r_j$ | required reserve above the failure boundary [same unit] |
| $j$ | a declared hard preservation condition |

#### How to use it

1. Define the selected system, value premise, interval, and horizon.
2. Identify hard conditions and their failure boundaries.
3. Project each margin after the action, including uncertainty.
4. Check common-cause failure and recovery-path independence.
5. If no candidate action, including non-action, satisfies the hard conditions, classify the problem as rescue / least-loss rather than strict preservation.

**Working example.** A control-system migration has positive service margin and data-integrity margin, but the only rollback requires the same credential service that the migration may disable. Recoverability remains unresolved, so strict preservation is not established even though the expected main path succeeds.

**Limit.** The gate is only as complete as the selected hard conditions. An omitted dependency can make a pass meaningless.

**READ THE RESULT**

Meeting all declared bounds supports a strict preservation claim under the current model. Failing one bound identifies the condition that blocks that claim.

**VALIDATE IT**

Test the dependency and recovery map with a materially different failure scenario, especially one involving shared resources or common authority.

---

<a id="c4"></a>

# C4 · The Water Ahead

*Interestingness is structured future potential, not raw uncertainty*

### Observation

*Beyond the buoy the route opens into several channels between islands. One route is broad and well charted. Another divides repeatedly around shallow water. A third is poorly surveyed.*

*The poorly surveyed route is not automatically the most interesting. It may simply be poorly known.*

For this volume, interestingness is local and model-relative. An element is interesting when changes in it materially reorganize a broad and structured set of reachable futures under the stated assumptions.

Raw branch count is not enough. Random noise can create many possible outputs while having little causal leverage over anything that matters. A small decision can create only a few branches while moving the entire system between different viable regions.

The useful question is not merely "how uncertain is this?" It is:

> How much does this element change the reachable future structure that matters to the present question?

This future structure can be projected onto selected dimensions: success/failure priority, cost, safety margin, ecological effect, energy, time, explanatory power, or another locally justified variable.

· ❦ ·

Projection reduces combinatorial explosion, but compression can hide structure. Two future sets can occupy the same outer interval while one fills the interval continuously and the other exists only near opposite extremes.

A useful projection therefore keeps at least:

- supported range or regions;
- distribution or occupancy inside them where justified;
- confidence / grounding quality;
- unresolved frontier;
- hard boundaries and rare consequential branches.

Unknown territory is not scored as if it already contained valuable structure. It remains uncertainty until evidence supports more.

### Field note

> *The most interesting water is not necessarily the least known. It is where a change can reorganize what becomes reachable.*

**What to carry forward**

- Interestingness is local to a question and model.
- Separate uncertainty from causal leverage.
- Keep known future structure separate from unresolved frontier.
- Rare catastrophic branches remain visible even when averages are small.
- A projection is a compression, not the future itself.

### Operational model

*A first local measure, not a universal law.*

Let $B$ describe supported breadth of reachable futures on the selected projection, $E$ describe how broadly supported futures occupy the declared outcome scale, and $L$ describe the leverage of the selected element on that projection.

First combine future diversity:

$$
D_F = w_B B + w_E E
$$

with $w_B+w_E=1$, then estimate:

$$
I = L\,D_F
$$

Report confidence and unresolved frontier separately rather than allowing ignorance to inflate $I$.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $B$ | normalized supported breadth of reachable projected states [0–1] |
| $E$ | normalized distribution evenness or occupancy breadth [0–1] |
| $w_B,w_E$ | declared comparison weights, $w_B+w_E=1$ |
| $L$ | normalized leverage/sensitivity of the selected element on the projection [0–1] |
| $D_F$ | supported future diversity [0–1] |
| $I$ | local interestingness estimate [0–1] |

When a probability or normalized occupancy distribution across fixed bins is justified, a Shannon-style evenness term can be used [R3]:

$$
E = -\frac{\sum_{k=1}^{K} p_k\ln p_k}{\ln K}, \qquad K\ge2
$$

with $0\ln0=0$.

#### How to use it

1. Declare the projection axis and horizon before comparing elements.
2. Keep binning or normalization fixed across the comparison.
3. Estimate leverage from intervention, controlled comparison, or clearly labeled sensitivity analysis.
4. Report confidence, unresolved frontier, and hard-tail conditions separately.

**Working example.** Two candidate controls have similar uncertainty. One barely changes the projected outcome range ($L=0.1$). The other shifts several outcomes across a viability threshold ($L=0.8$). The second is more interesting for the current decision even if both have similar raw entropy.

**Limit.** The score depends on projection choice and normalization. It should not be treated as an intrinsic property of the object.

**READ THE RESULT**

$I$ ranks grounded structured future leverage under the declared model. It does not rank goodness, safety, or moral importance.

**VALIDATE IT**

Repeat the ranking under at least one materially different reasonable projection or binning and check whether the ordering is stable.

---

<a id="c5"></a>

# C5 · Soundings Near the Shoal

*Resolution should increase where it can change the decision*

### Observation

*The chart shows deep water across most of the route. Near one island the depth contours crowd together. The crew does not take a sounding every meter across the ocean. They take more soundings where the keel might meet the bottom.*

Complex systems can consume unlimited attention if every variable is modeled at maximum resolution.

The alternative is not to ignore detail. It is to refine selectively.

Begin with a coarse local model. Increase resolution where uncertainty overlaps a decision boundary, where two grounded methods disagree, where small changes produce large consequences, or where a rare branch can destroy an irreplaceable condition.

Once additional detail no longer changes the decision, explanation, or boundary classification, compress again.

This resembles adaptive refinement methods in numerical simulation, which allocate finer resolution where error or solution structure requires it [R6][R7]. The analogy is about allocation of resolution, not about treating every system as a numerical mesh.

· ❦ ·

The same principle applies to reasoning.

A long logical chain is useful when each step preserves the assumptions needed by the next. It becomes wasteful when detail is added without changing a prediction, decision, or residual.

Selective refinement is what allows the general picture to remain visible while microprocesses are inspected where necessary.

### Field note

> *Take more soundings where another meter can change the route.*

**What to carry forward**

- Start coarse enough to see the whole dependency path.
- Refine near hard boundaries, strong sensitivity, disagreement, or consequential tails.
- Stop refining when plausible additional detail cannot change the action class or claim.
- Compression should remove irrelevant detail, not exceptions or provenance.

### Operational model

*A local refinement-priority heuristic.*

For region $i$, let $U_i$ describe unresolved width, $S_i$ decision sensitivity, and $C_i$ the cost or disturbance of obtaining more resolution.

$$
R_i = \frac{U_iS_i}{1+C_i}
$$

Hard constraints and catastrophic tails can override the ranking.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $U_i$ | normalized uncertainty or unresolved width in region $i$ [0–1] |
| $S_i$ | normalized decision sensitivity / leverage [0–1] |
| $C_i$ | normalized cost or disturbance of refinement [$\ge0$] |
| $R_i$ | relative refinement priority |

#### How to use it

1. Identify regions where uncertainty can change the conclusion.
2. Estimate the cost or disturbance of obtaining more information.
3. Use $R_i$ only as a priority heuristic; hard safety or preservation boundaries override it.
4. Recalculate after each new observation.

**Working example.** A broad operating region has uncertainty 0.4 but sensitivity 0.05. A narrow threshold region has uncertainty 0.15 and sensitivity 0.9. Even with less uncertainty, the threshold region deserves earlier refinement because its uncertainty can change the decision.

**Limit.** Normalized values depend on the comparison set. The heuristic is not a universal optimization law.

**READ THE RESULT**

Higher $R_i$ means additional resolution is more likely to matter relative to its cost under the stated model.

**VALIDATE IT**

After refinement, check whether the new information actually changed the projected range, decision, or residual. If not, lower the priority of similar refinements.

---

<a id="c6"></a>

# C6 · The Return Route

*Recovery is part of action, not an afterthought*

### Observation

*Weather closes in before the final station. The crew has enough fuel to continue. They also have enough fuel to return—if the inlet remains navigable.*

*A return route drawn on the chart is not useful if the same storm that creates the emergency also closes the inlet.*

Vol. 1 linked intervention to reversibility, verification, and a stopping condition. This extension makes one hidden variable explicit: **recovery-path independence**.

A recovery path is independent only to the extent that the failure it is meant to recover from does not disable the resources, authority, information, or physical route required for recovery.

Backups can share hidden dependencies. Two servers can share one power source. Two pumps can share one intake. Two administrators can depend on one identity provider. Several AI agents can share one corrupted dataset.

Counting backups is therefore weaker than mapping failure domains.

· ❦ ·

Recovery also has timing.

A path that can restore the system in twelve hours is not viable when irreversible failure occurs in two.

When strict preservation is already impossible, recovery logic becomes rescue logic. Non-action belongs in the comparison because it is also a policy with projected consequences.

### Field note

> *A return route exists only if it remains reachable when it is needed.*

**What to carry forward**

- Check shared failure domains, not only backup count.
- Compare recovery time with time to irreversible loss.
- Preserve access, authority, and irreplaceable state needed for recovery.
- Include non-action in rescue / least-loss comparisons.
- Do not call rescue a successful strict-preservation result.

### Operational model

*A simple recovery-time margin.*

Let $T_F$ be the estimated time until irreversible failure under the relevant scenario and $T_R$ the estimated time required to restore a viable state.

$$
M_R = T_F-T_R
$$

A positive margin is useful only if the recovery path itself is independent of the failure being modeled.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $T_F$ | time from the current state to irreversible failure under the selected scenario [time] |
| $T_R$ | time required to restore a viable state [time] |
| $M_R$ | recovery-time margin [time] |

#### How to use it

1. Define the failure scenario and irreversible boundary.
2. Estimate recovery time including access, authority, setup, and verification.
3. Test whether the recovery path shares the relevant failure domain.
4. Treat non-independent recovery as unresolved even when $M_R>0$.

**Working example.** Irreversible data loss is expected after 90 minutes of continued corruption; verified restore requires 40 minutes. $M_R=50$ minutes. If the restore credentials depend on the same compromised identity service, the positive time margin does not establish recoverability.

**Limit.** Time estimates can change during an incident. Recalculate when state, access, or dependency availability changes.

**READ THE RESULT**

$M_R>0$ indicates temporal room for recovery under the stated scenario. Independence and viability of the recovery path remain separate requirements.

**VALIDATE IT**

Exercise or simulate recovery from a failure domain that removes the primary path, not merely under normal operating conditions.

---

<a id="c7"></a>

# C7 · The Logbook After the Storm

*Exact external state makes exploration cumulative*

### Observation

*The vessel returns after dark. The buoy is still flashing, but the position in the notebook is not the position printed on the morning chart. The crew can reconstruct what changed because each sounding, course correction, and observation was recorded with time.*

Without the logbook, tomorrow's crew would inherit conclusions without the chain of evidence that produced them.

A reusable reasoning system needs the same continuity.

The external record should separate at least four layers:

1. observation — what was measured, retrieved, or directly tested;
2. model — the relations currently used to interpret those observations;
3. projection — what future states the model supports;
4. decision — what action follows under the declared value premise and constraints.

Keeping those layers distinct makes correction possible. A model can be replaced without erasing the observations that contradicted it.

· ❦ ·

Contradictions should also survive compression.

If two grounded methods disagree, the disagreement should be localized: shared assumptions, different methods, different scopes, and what decision the disagreement can change.

An assumption should have a revision condition. Evidence that can become stale should carry a time or version. A candidate hidden variable should retain the case that exposed it and the tests that promoted or rejected it.

This external state is useful to a person, a team, or an AI system. It is not a transcript of private reasoning. It is a compact, auditable model of what the exploration currently claims to know.

### Field note

> *A good logbook preserves enough of yesterday's uncertainty for tomorrow to correct it.*

**What to carry forward**

- Separate observations, models, projections, and decisions.
- Keep provenance and freshness with evidence.
- Preserve contradictions until evidence resolves them.
- Record why a variable was promoted or demoted.
- A summary that removes hard constraints or rare consequential branches is not a faithful compression.

### Operational model

*A residual is one trigger for revision.*

For a predicted value $\hat y_t$ and realized observation $y_t$:

$$
\delta_t = y_t-\hat y_t
$$

When the observation falls outside the model's supported uncertainty range, create a revision record rather than silently widening the model after the fact.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $\hat y_t$ | predicted value or center of predicted region at time $t$ [native units] |
| $y_t$ | realized observation at the same relevant time/scope [same units] |
| $\delta_t$ | signed residual [same units] |

#### How to use it

1. Preserve the original prediction and its uncertainty before observing the outcome.
2. Record the realized value and method.
3. If the residual is material, inspect measurement, assumption, boundary, parameter, relation, and hidden-variable explanations.
4. Version the model change that follows.

**Working example.** A model predicts a buoy drift of $4\pm2$ m; the observed displacement is 13 m. Do not rewrite the earlier range as if 13 m had always been expected. Preserve the residual and test missing-current, timing, calibration, and boundary explanations.

**Limit.** A residual can arise from noise. One outlier does not automatically justify model expansion.

**READ THE RESULT**

$\delta_t$ records the direction and magnitude of mismatch. Its significance depends on the predicted uncertainty and consequence of being wrong.

**VALIDATE IT**

Check whether the revised model improves later predictions or independent cases without erasing earlier contradictions.

---

<a id="c8"></a>

# C8 · The Compass

*The reusable tool is the cycle, not the metaphor*

### Observation

*The next morning another crew leaves the same harbor. They carry yesterday's logbook, but they are not required to follow yesterday's route. The buoy remains offshore. The current may have changed.*

The purpose of Compass is to preserve orientation while the local model changes.

It is not a single equation. It is a disciplined cycle that decides what to represent, what to leave unresolved, where to spend resolution, and when to stop.

The cycle inherits the earlier Observer model:

- localize the system;
- select elements, states, and relations;
- define identity and viability;
- map dependencies;
- preserve evidence and observer effects;
- state the value premise before optimization;
- evaluate intervention, reversibility, verification, and stopping conditions.

Vol. 1.2 adds four explicit disciplines:

1. future-space projection instead of exhaustive enumeration;
2. interestingness as structured future leverage rather than raw uncertainty;
3. preservation evaluation including recovery-path independence;
4. candidate-variable promotion from real applications without allowing storytelling to become theory.

· ❦ ·

A useful execution cycle is:

1. define the exact question or claim;
2. localize system, boundary, scale, interval, horizon, assumptions, and value premise;
3. record evidence with provenance and uncertainty;
4. map dependencies, hard boundaries, reserves, and recovery conditions;
5. project only the future dimensions relevant to the question;
6. identify consequential uncertainty, disagreement, or hidden-variable candidates;
7. choose the smallest evidence-producing next step likely to change the model or decision;
8. run preservation / rescue checks before consequential intervention;
9. execute one justified step;
10. compare the realized state with the projected range;
11. update the model, preserve contradictions, and simplify irrelevant detail;
12. stop when the claim is supported, the decision is robust, a hard uncertainty blocks action, an external dependency is the blocker, or the question must be reframed.

This cycle can be represented in a machine-readable state template, but the serialization is not itself part of the theory.

### Field note

> *The compass is useful because the map can be wrong.*

**What to carry forward**

- The question selects the local model; it is not a poetic direction variable.
- The model should be no more detailed than the decision requires.
- Every consequential loop needs new evidence, state change, or a bounded reason to repeat.
- Human and AI systems both benefit from explicit external state when it preserves provenance, uncertainty, dependencies, and stopping rules.
- The technical model remains universal; the expedition only keeps the reasoning continuous enough to see it.

### Operational model

*A reusable procedure rather than a new equation.*

Use the cycle above together with `COMPASS_STATE_TEMPLATE.yaml` for auditable state and `COMPASS_QUICK_CARD.md` for short execution.

A run should terminate explicitly as one of the following:

- **supported** — target claim supported to the declared strength;
- **decision robust** — action class stable across plausible refinements;
- **preservation blocked** — a hard margin is negative or unresolved;
- **rescue required** — strict preservation is unavailable;
- **external wait** — an external dependency is the blocker;
- **insufficient evidence** — no justified current step can resolve the key uncertainty;
- **model contradiction** — current assumptions cannot jointly explain observations;
- **terminal system state** — no modeled continuation exists under the selected definition;
- **question reframed** — the original boundary, scale, or question was wrong.

**Limit.** No procedure guarantees that all relevant variables are represented. Compass improves correction by making omissions, residuals, and revision paths visible.

**READ THE RESULT**

A completed Compass run is not "the answer." It is a bounded claim plus an auditable account of what supports it, what remains unresolved, and what would cause revision.

**VALIDATE IT**

Apply the same procedure to a materially different problem. The technical terms should transfer without importing the ocean story. If they do not, the abstraction is not yet universal enough.

---

# Working definitions added in Vol. 1.2

The following extend rather than replace Vol. 1 definitions.

| Term | Working definition |
|---|---|
| **Projection** | A selected lower-dimensional representation of reachable states used for the present question. |
| **Residual** | A recorded mismatch between an observation and the state or range supported by the current model under comparable conditions. |
| **Candidate variable** | A proposed state, condition, or relation introduced to explain a residual or dependency not adequately represented by the current model. |
| **Promotion** | The act of moving a candidate variable into a more reusable model layer after operational, evidential, mechanistic, and relevance checks. |
| **Recovery path** | A sequence of actions and required conditions capable of returning the selected system to a declared viable state after disturbance. |
| **Recovery-path independence** | The degree to which a recovery path remains available under the same failure that makes recovery necessary. |
| **Preservation evaluation** | A model-relative test of whether selected invariants, viability conditions, dependencies, and recoverability remain within declared bounds through a change. |
| **Unresolved frontier** | Evidence-backed reason to believe the modeled support may be incomplete, without inventing specific unobserved futures. |
| **Compass** | The name of the reusable exploration procedure in this volume; not a replacement for the universal technical terms above. |

---

# Validation and edge cases

The operational templates above have been checked against the following recurring failure modes:

| Edge case | Handling |
|---|---|
| One occupied outcome bin | Evenness uses a fixed declared $K\ge2$, not the number of occupied bins. |
| Zero occupancy | Use $0\ln0=0$. |
| Empty or contradictory reachable set | Mark the model infeasible/unresolved rather than reporting zero interestingness. |
| Unbounded projection axis | Declare a finite comparison scale, transform, or relevant thresholds before normalization. |
| Rare catastrophic branch | Keep a separate hard-boundary/tail condition; averages and entropy cannot erase it. |
| Low-confidence model | Uncertainty widens the reported interval/frontier; it does not automatically increase the central interestingness estimate. |
| Scenario baseline count is zero | Optionality ratios using that denominator are undefined; report counts/fractions or weighted mass instead. |
| Different scenario generators | Counts are not directly comparable without a controlled basis. |
| Already-failing system | Switch from strict preservation to rescue / least-loss comparison, including non-action. |
| Irreversible action | Do not invent rollback; require explicit irreversible consequences, stronger evidence, containment, or forward recovery where possible. |
| Common-cause dependencies | Evaluate joint failure; independent positive margins are insufficient. |
| Backup shares failure domain | Recovery-path independence is not established. |
| Short-term preservation, long-term loss | Evaluate multiple horizons and report reversal rather than averaging it away. |
| Measurement changes the system | Include observer / instrument disturbance in the model when material. |
| Association presented as causality | Use intervention language only when causal identification is justified; otherwise label sensitivity or association. |
| Several agents agree | Check shared model, data, retrieval, and assumptions before treating agreement as independent evidence. |
| Compression removes exception | Preserve hard constraints, contradictions, rare consequential branches, provenance, and recovery state. |
| Refinement repeats without new evidence | Stop or branch; repetition without state change or new evidence is not exploration. |
| Story suggests a hidden variable | Keep it a candidate until it has an operational definition and supporting evidence. |
| Variable fits one case perfectly | Check independent cases or mechanism before reusable promotion. |
| Promoted variable later becomes redundant | Demote it and preserve the model history. |
| Evidence becomes stale | Reduce confidence or measure again when the stale evidence can change the decision. |

---

# Reference map

These are grounding parallels and notation sources, not claims that Compass is a restatement of any one tradition.

- viability and preservation: [R1], [R2]
- entropy / distribution evenness: [R3]
- causal intervention notation: [R4]
- rigorous interval methods: [R5]
- adaptive refinement analogy: [R6], [R7]
- receding-horizon control analogy: [R8]
- abstraction / refinement analogy: [R9]
- systems verification and end-to-end testing: [R10]
- AI lifecycle evaluation: [R11], [R12]
- expected information / experiment selection: [R13]

## References

**[R0] Beregovykh, Nikita.** *Observer's Notes: A Field Book.* Public discussion draft, 2026. Repository: https://github.com/nvberegovykh/Observer-s-Notes

**[R1] Aubin, Jean-Pierre.** *Viability Theory.* Modern Birkhäuser Classics, 2009 edition. Springer/Birkhäuser. https://link.springer.com/book/10.1007/978-0-8176-4910-4

**[R2] Holling, C. S.** "Resilience and Stability of Ecological Systems." *Annual Review of Ecology and Systematics* 4 (1973): 1–23. DOI: 10.1146/annurev.es.04.110173.000245. https://doi.org/10.1146/annurev.es.04.110173.000245

**[R3] Shannon, Claude E.** "A Mathematical Theory of Communication." *Bell System Technical Journal* 27 (1948), parts I–II, pp. 379–423 and 623–656. DOI part I: 10.1002/j.1538-7305.1948.tb01338.x. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

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

## The extension in one passage

The buoy is still there.

At first it was a reference. Then it was noisy. Then it drifted. Then its drift helped expose a current. The current changed the route. The route approached a shoal. The shoal made additional soundings worthwhile. The weather made the return route relevant. The logbook made the next day's corrections possible.

None of those story objects became technical definitions.

The technical model remained a model of elements, states, relations, boundaries, viability, evidence, uncertainty, future projections, intervention, preservation, and revision.

That is the purpose of the story: not to rename the model, but to keep enough of the world continuous that hidden assumptions have somewhere to reveal themselves.

And that is the purpose of Compass: not to eliminate uncertainty, but to make the **question, evidence, model, boundary, uncertainty, preservation conditions, and next justified step visible at the same time**.

---

## Signature

**Nikita Beregovykh & ChatGPT 5.6 Sol, Observers Notes extension 1**
