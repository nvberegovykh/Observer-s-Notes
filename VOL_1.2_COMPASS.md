# Observer's Notes — Vol. 1.2

# COMPASS

*An ocean field book for grounded exploration*

**Extension 1**

---

## Publication note

This volume extends *Observer's Notes* without replacing its definitions.

The technical vocabulary of Vol. 1 remains authoritative: element, state, interaction, relation, structure, condition, viability domain, maintenance, recursive maintenance, generative maintenance, observer effect, value premise, and intervention keep their earlier meanings.

The ocean expedition is only the environment in which the new notes unfold. It is not a second technical vocabulary. A buoy may appear in the story; the model still speaks about an element, a measured state, a relation, uncertainty, or a reference. A reef may appear in the scene; the technical text still speaks about a boundary or constraint.

The story is allowed to make an idea easier to see. It is not allowed to establish the idea as true.

The conceptual extensions in this volume grew from post-publication working discussions between Nikita Beregovykh and ChatGPT in 2026. External references are listed at the end as neighboring formal traditions, notation sources, and grounding for specific operational claims. They are not presented as the origin of the Observer's Notes model.

· ❦ ·

> *A compass does not decide where to go. It helps preserve orientation while the surroundings move.*

## How to read this volume

Compass has four reader-facing layers. They should not be confused with one another.

1. **Story** keeps assumptions continuous long enough for hidden variables to appear. The vessel, buoy, fog, routes, and other objects are examples, not technical definitions.
2. **Field note** states the local principle in memorable language. It is still a claim to be tested, not an axiom.
3. **Operational model** gives a measurable relation, gate, or procedure that can fail. The equations are local templates rather than universal laws.
4. **Companion state** records what an actual run knows: evidence, assumptions, routes, residuals, preservation conditions, communication state, scale, and stopping conditions.

References serve a fifth role: they identify neighboring formal traditions that support, challenge, or clarify particular pieces of the method. No reference is presented as proof of Compass as a whole.

When a concept feels too abstract, read in this order: **scene → field note → working example → operational model → limit → reference relation.**

## A note before sailing

A small research vessel leaves a harbor before sunrise. Not far offshore stands a weather buoy. Its light is easy to see. Its radio is not always quiet.

At first the buoy seems like a convenient reference. Later the crew discovers that its signal has noise. Then that the buoy itself can drift. Then that the current affecting the buoy also affects the vessel. Then that a second instrument disagrees. Farther offshore, the route approaches a shoal. Weather closes in. A second vessel appears through the fog on a crossing course. The crew has to decide when to continue, when to wait, when to communicate, when to ask for another reference, and whether the route home remains independent of the same conditions creating the problem.

Each new observation complicates the picture, but not arbitrarily. The same environment is being revisited with a better model.

That continuity is the purpose of the expedition.

A story can hold assumptions still long enough for hidden variables to become visible. The variables do not become part of the general model merely because the story contains them. They must survive operational definition, evidence, comparison, and reuse.

The notes that follow keep the pattern of Vol. 1:

**observation → general statement → limits → field note → carry-forward rules → operational model → measurements → use → example → validation.**

The technical content is intentionally not reduced to make the pages look simpler. The visual rule is different: formulas should show one measurable relation at a time; symbol tables should carry the notation; serialized model state belongs in the companion template, not in an equation.

---

## Contents

| Ref | Note |
|:---:|---|
| C1 | [The Buoy That Wouldn't Be Quiet](#c1) |
| C2 | [The Current That Wasn't on the Chart](#c2) |
| C3 | [What Must Survive the Crossing](#c3) |
| C4 | [The Water Ahead](#c4) |
| C5 | [Soundings Near the Shoal](#c5) |
| C6 | [The Engine at Idle](#c6) |
| C7 | [Another Light Across the Water](#c7) |
| C8 | [A Voice Through the Fog](#c8) |
| C9 | [The Return Route](#c9) |
| C10 | [The Logbook After the Storm](#c10) |
| C11 | [The Channel Already on the Chart](#c11) |
| C12 | [The Compass](#c12) |

> Vol. 1 definitions remain inherited. C1–C12 introduce only extension-specific operational terms.

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
- Evidence can become stale; state-dependent evidence should carry a time or version.

### Operational model

*A measurable local template, not a universal law.*

For two estimates of the same selected quantity, a simple standardized disagreement is:

$$
\boxed{D = \frac{|x_1-x_2|}{\sqrt{u_1^2+u_2^2}}}
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
4. Record whether the two methods share calibration, data, model assumptions, or physical dependencies.

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

Recurrence matters most when it crosses contexts. Recovery-path independence, observer disturbance, common-cause dependency, delay, hidden shared resources, and freshness of state are examples of variables that can recur across very different systems while retaining the same operational relation.

A promoted variable is not permanent. Later evidence can show that it duplicates an existing variable, is domain-specific, or does not improve decisions. Demotion is part of model maintenance.

### Field note

> *A residual is not an embarrassment. It is a place where the chart and the world have stopped agreeing.*

**What to carry forward**

- A hidden variable begins as a candidate, not a fact.
- Check simpler explanations before adding model dimensions.
- Prefer variables with operational definitions and observable consequences.
- A variable becomes more reusable when it survives materially different cases.
- Preserve the case that exposed a candidate and the evidence that promoted it.
- Previously promoted variables may later be demoted.

### Operational model

*A measurable local template for candidate-variable testing.*

Let $R_0$ be prediction error under the current model and $R_x$ the error after adding candidate variable $x$ under the same validation rule.

$$
\boxed{\Delta R_x = R_0-R_x}
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
5. Check whether it duplicates an existing variable or simply renames an observed effect.
6. Record a future test that could demote the variable.

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

For consequential action, preservation evaluation should normally inspect identity, viability, constitutive dependencies, continuity, access/control, irreplaceable state, recoverability, verification capacity, and containing-system externalities when those dimensions are relevant.

These are not new universal categories forced onto every problem. They are prompts to check whether the selected system's real dependencies have been represented.

Preservation also changes with horizon. An action can preserve the next minute and destroy the next day. A temporary controlled loss can also be acceptable if it belongs to an explicit recovery path that preserves the higher-level system.

### The present environment

The environment is not only a container for future options. It is part of the present state-space.

A living system depends on flows of matter, energy, and information now. A self-modeling or self-aware system, where such capacities exist, also depends on conditions that allow attention, communication, movement, memory, recovery, and interaction. Products of those systems—tools, practices, traditions, arguments, art, research, institutions, and other maintained structures—can become part of the environment from which later activity begins.

So environmental degradation does not merely remove hypothetical futures. It can immediately reduce what is reachable in the present: fewer safe interactions, fewer usable materials, less recoverable energy, less attention beyond maintenance, fewer observations, fewer participants, fewer places to move, and fewer experiments that can be attempted without crossing a hard boundary.

For selected environmental conditions $E_t$, define the present capability set:

$$
\boxed{\mathcal A_t(E_t)=\{a\mid a\text{ is viable and reachable now under }E_t\}}
$$

This is not a demand to maximize the number of actions. Some possibilities are destructive, coercive, or incompatible with the declared value premise. The set is a diagnostic surface: preservation should notice when an intervention keeps one subsystem alive by unnecessarily collapsing the environmental conditions that support present activity elsewhere.

Generative maintenance therefore has a present tense. It preserves or regenerates conditions from which viable structure can continue to arise **now**, while also leaving future development possible. The relevant object is not a frozen environment but the capacity of the containing system to keep supporting life, relation, correction, and creation through change.

Outputs can also become inputs. Organisms modify niches; maintained cultural and technical products alter what later observers can perceive, learn, inherit, contest, or build upon [R27]. Ecosystem assessment likewise treats environmental conditions as contributors to present human well-being, not only distant future value [R28]. The same recursive pattern can be modeled more generally without assuming that every inherited product is beneficial.

### Field note

> *Preserve what makes continuation possible, not merely what happens to be present now.*

**What to carry forward**

- State what is being preserved and why.
- Distinguish identity preservation from viability preservation and generative preservation.
- Check lower-level and containing-system dependencies.
- Treat relevant environmental conditions as part of the present system state, not only future optionality.
- Preserve or regenerate the material, energy, information, and relational conditions that support current viable activity where they matter to the value premise.
- A recovery path must survive the failure it is intended to recover from.
- Evaluate more than one horizon when delayed effects are plausible.
- When strict preservation is already impossible, switch to rescue / least-loss evaluation rather than pretending otherwise.

### Operational model

*A local preservation gate.*

For every declared hard condition $j$, let $\underline m_j(a)$ be the conservative lower bound of the projected post-action margin and $r_j$ the required reserve.

Strict preservation requires:

$$
\boxed{\underline m_j(a) \ge r_j \qquad \text{for every hard condition } j}
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
5. Check at least one containing system when material externalities are plausible, including present environmental support and capability loss.
6. If no candidate action, including non-action, satisfies the hard conditions, classify the problem as rescue / least-loss rather than strict preservation.

**Working example.** A control-system migration has positive service margin and data-integrity margin, but the only rollback requires the same credential service that the migration may disable. Recoverability remains unresolved, so strict preservation is not established even though the expected main path succeeds.

**Limit.** The gate is only as complete as the selected hard conditions. An omitted dependency can make a pass meaningless.

**READ THE RESULT**

Meeting all declared bounds supports a strict preservation claim under the current model. Failing one bound identifies the condition that blocks that claim.

**VALIDATE IT**

Test the dependency and recovery map with a materially different failure scenario, especially one involving shared resources, common authority, or delayed effects.

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

Interestingness is also not desirability. A dangerous failure point can be highly interesting. A safe, mature component can be uninteresting. The measure allocates attention; it does not supply a value premise.

### Field note

> *The most interesting water is not necessarily the least known. It is where a change can reorganize what becomes reachable.*

**What to carry forward**

- Interestingness is local to a question and model.
- Separate uncertainty from causal leverage.
- Keep known future structure separate from unresolved frontier.
- Rare catastrophic branches remain visible even when averages are small.
- A projection is a compression, not the future itself.
- Interestingness does not mean goodness.

### Operational model

*A first local measure, not a universal law.*

Let $B$ describe supported breadth of reachable futures on the selected projection, $E$ describe how broadly supported futures occupy the declared outcome scale, and $L$ describe the leverage of the selected element on that projection.

First combine supported future diversity:

$$
\boxed{D_F = w_B B + w_E E}
$$

with $w_B+w_E=1$, then estimate:

$$
\boxed{I = L\,D_F}
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
\boxed{E = -\frac{\sum_{k=1}^{K} p_k\ln p_k}{\ln K}, \qquad K\ge2}
$$

with $0\ln0=0$.

#### How to use it

1. Declare the projection axis and horizon before comparing elements.
2. Keep binning or normalization fixed across the comparison.
3. Estimate leverage from intervention, controlled comparison, or clearly labeled sensitivity analysis.
4. Report confidence, unresolved frontier, and hard-tail conditions separately.
5. Repeat the ranking under at least one materially different reasonable projection when the ranking drives action.

**Working example.** Two candidate controls have similar uncertainty. One barely changes the projected outcome range ($L=0.1$). The other shifts several outcomes across a viability boundary ($L=0.8$). The second is more interesting for the current decision even if both have similar raw entropy.

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

A long logical chain is useful when each step preserves the assumptions needed by the next. It becomes wasteful when detail is added without changing a prediction, decision, residual, or recognized dependency.

Selective refinement is what allows the general picture to remain visible while microprocesses are inspected where necessary.

The refinement target can also be a hidden variable rather than a numerical interval. A contradiction, stale evidence item, or uncertain dependency can deserve more resolution if resolving it would change the action class.

### Field note

> *Take more soundings where another meter can change the route.*

**What to carry forward**

- Start coarse enough to see the whole dependency path.
- Refine near hard boundaries, strong sensitivity, disagreement, or consequential tails.
- Refine stale or weak evidence when it can change the decision.
- Stop refining when plausible additional detail cannot change the action class or claim.
- Compression should remove irrelevant detail, not exceptions or provenance.

### Operational model

*A local refinement-priority heuristic.*

For region $i$, let $U_i$ describe unresolved width, $S_i$ decision sensitivity, and $C_i$ the cost or disturbance of obtaining more resolution.

$$
\boxed{R_i = \frac{U_iS_i}{1+C_i}}
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
5. Record whether the refinement actually changed the model, decision, or residual.

**Working example.** A broad operating region has uncertainty 0.4 but sensitivity 0.05. A narrow boundary region has uncertainty 0.15 and sensitivity 0.9. Even with less uncertainty, the boundary region deserves earlier refinement because its uncertainty can change the decision.

**Limit.** Normalized values depend on the comparison set. The heuristic is not a universal optimization law.

**READ THE RESULT**

Higher $R_i$ means additional resolution is more likely to matter relative to its cost under the stated model.

**VALIDATE IT**

After refinement, check whether the new information actually changed the projected range, decision, or residual. If not, lower the priority of similar refinements.

---

<a id="c6"></a>

# C6 · The Engine at Idle

*Patience preserves options when immediate narrowing is not required*

### Observation

*Near the shoal, the crew has enough information to keep moving but not enough to know which channel is best. The engine drops to idle. The vessel still responds to the helm. The radio remains on. The buoy is still visible behind them. No route has been erased from the chart.*

*Nothing has failed. Nothing has been solved either.*

Patience in this volume is not a personality virtue and not passive delay. It is a control policy over the timing of commitment.

A reasoning process is patient when it can preserve the current state, keep unresolved alternatives recoverable, and delay irreversible narrowing long enough for additional evidence, communication, comparison, or capacity to matter—without ignoring the cost of delay.

This matters in calm conditions because premature closure can hide lower-probability branches that later become important. It matters in focused extreme conditions because salience can narrow attention around the immediately dominant branch. Human research finds that acute stress often impairs working memory and cognitive flexibility, although effects vary by task and condition [R14]. That does not mean every stressed decision should be delayed. It means that confidence in a narrowed option set should not automatically increase merely because attention has become intense.

Patience therefore protects **option integrity**: explored branches, unresolved alternatives, and stopping conditions remain externally represented instead of disappearing when one branch becomes dominant.

· ❦ ·

A pause is useful only if it preserves the work needed to resume.

The process can externalize the current model, park the active branch, and return to a procedural reference state: observations preserved, assumptions visible, unresolved branches recorded, and no optional branch privileged merely because it was last active.

This "reference state" is not a claim about a universal neutral brain state. It is a modeling state. For a person it may correspond to stepping away from a high-load task after writing down the live state. For an AI system it may correspond to ending a branch, preserving externally auditable state, and resuming later or with a different tool or agent.

Incubation research gives a grounded human parallel: setting a problem aside can improve later problem solving in some task classes, and high-demand activity during the interval can reduce that benefit [R15]. Cognitive offloading research also shows why external state can free limited working memory, while reminding us that an unreliable external record can create new failure modes [R16].

Patience does not impose an arbitrary threshold on exploration. A low-probability branch stays available unless evidence or a hard constraint rules it out. The branch may even deserve an early, small probe when the information it could produce would materially change the model.

Communication is one such probe. A patient system does not have to remain silent. It can hold irreversible commitment while actively exchanging information, testing constraints, or looking for a path that was invisible under the current local model.

### Field note

> *Idle is not lost motion when it preserves the ability to choose a better motion next.*

**What to carry forward**

- Patience controls commitment timing; it is not inactivity.
- Preserve low-probability branches externally before narrowing the active workspace.
- Probability alone is not a reason to delete a branch.
- Communication can be active exploration during a hold.
- Return to a reference state when urgency permits and the active branch is producing little new information.
- If delay itself threatens viability, patience may mean acting carefully now rather than waiting.
- Distinguish actual recoverable resources from metaphorical "energy"; measure battery, time, compute, sleep, attention, or workload when those variables matter.

### Operational model

*A decision-value view of holding commitment open, not a hard threshold.*

Let $V_{\mathrm{info}}(\tau)$ be the expected improvement in the later decision from information, communication, or comparison that may become available over a bounded interval $\tau$. Let $V_{\mathrm{option}}(\tau)$ be the value of preserving still-viable alternatives during that interval, and let $C_{\mathrm{delay}}(\tau)$ be the expected cost of not committing yet.

$$
\boxed{V_{\mathrm{hold}}(\tau)=V_{\mathrm{info}}(\tau)+V_{\mathrm{option}}(\tau)-C_{\mathrm{delay}}(\tau)}
$$

The expression ranks a temporary hold against immediate irreversible commitment; it does not create a universal "wait" threshold. Hard deadlines, irreversible deterioration, and preservation boundaries remain separate constraints.

#### Measurements

| Symbol | Operational definition and units |
|---|---|
| $\tau$ | bounded hold/incubation interval [time] |
| $V_{\mathrm{info}}(\tau)$ | expected decision improvement from additional evidence, communication, comparison, or recovered capacity during $\tau$ [declared value unit] |
| $V_{\mathrm{option}}(\tau)$ | value of keeping still-viable alternatives reachable during $\tau$ [same value unit] |
| $C_{\mathrm{delay}}(\tau)$ | expected loss from postponing irreversible commitment for $\tau$ [same value unit] |
| $V_{\mathrm{hold}}$ | net modeled value of holding commitment open [same value unit] |

#### How to use it

1. Preserve the current model and branch state before reducing active processing.
2. Record which low-probability alternatives remain unresolved rather than deleting them.
3. Estimate what new evidence, communication, capacity, or independent comparison could realistically appear during the hold.
4. Estimate what delay can damage: deadline, viability margin, opportunity, or recovery time.
5. Compare holding with the best immediate bounded action; do not assume either is neutral.
6. Resume from the preserved state, not from memory of the last emotionally or computationally salient branch.

**Working example.** A system fault has one dominant explanation and two low-probability alternatives. Immediate repair is reversible, but irreversible data migration would destroy evidence that distinguishes the alternatives. A short diagnostic interval with an external check has low delay cost and high information value. Patience favors preserving the branch set and diagnosing before migration, without requiring the rare alternatives to cross an arbitrary probability threshold.

**Limit.** Expected information and option value are themselves model-dependent. Under true emergencies, delay costs can rise faster than the information value of holding.

**READ THE RESULT**

Positive $V_{\mathrm{hold}}$ supports keeping irreversible commitment open for the modeled interval; negative values favor acting sooner under the same value premise. Neither result overrides hard constraints.

**VALIDATE IT**

After the hold or immediate action, compare what information actually arrived, whether the preserved branch set mattered, and whether the delay estimate was realistic. Update future tempo decisions from that evidence.

---

<a id="c7"></a>

# C7 · Another Light Across the Water

*Communication searches for coexistence without surrendering identity or choice*

### Observation

*Fog thins for a moment and another vessel appears on radar. Its course intersects the research vessel's route. There is not enough information to know whether the crossing is accidental, careless, constrained by the same current, or deliberately threatening.*

*The crew increases separation. They keep the channel open.*

A threat is a relation between a system and a possible consequence. It is not, by itself, a complete description of the other system's identity.

That distinction matters because labels can close branches before the model has tested them. If the other vessel is treated as inherently hostile, communication, separation, coordination, repair, or negotiated coexistence can disappear from the reachable set before evidence shows that they are impossible.

The opposite mistake is equally serious. Keeping communication possible does not require staying exposed to harm, trusting unverified claims, surrendering hard safety margins, or forcing either side to remain in contact.

Communication is therefore an **option-preserving interaction** when it can exchange state, intent, constraints, proposals, or warnings while both sides retain meaningful choice and hard viability conditions.

· ❦ ·

Research on social dilemmas gives a grounded reason not to dismiss communication as decoration. A meta-analysis by Balliet found a substantial positive relationship between communication and cooperation across experimental social dilemmas [R19]. Ostrom, Walker, and Gardner showed experimentally that communication and self-organized commitments can support cooperation in common-pool settings without requiring that all order come from an external enforcer [R20].

The bargaining literature supplies another useful neighboring model. Fearon showed that costly conflict can coexist with a range of settlements both sides would prefer, while information asymmetry and commitment problems can prevent the parties from locating or trusting that range [R21]. The analogy is limited but important: **absence of visible agreement is not the same as proof that no mutually preferable state exists.**

Communication can reduce uncertainty, reveal hidden constraints, make substitutions visible, or expose that no acceptable intersection currently exists. It does not guarantee cooperation.

Freedom of choice matters here. A communication process that works only by removing meaningful choice may produce compliance while destroying the very coexistence it claims to create. Psychological reactance research gives a human-specific parallel: perceived threats to freedom can increase resistance, while autonomy-supportive or choice-preserving language can reduce reactance in some communication settings [R22]. Compass does not generalize human psychology to every system, but it keeps the structural lesson: **choice is itself a state variable when coercion changes the interaction.**

· ❦ ·

Identity also needs a cleaner model.

Vol. 1 defined identity through invariants and tolerances, not through an immutable surface behavior. That means a person, organization, or AI system can change strategy, language, route, or temporary stance without necessarily losing the identity or principles being preserved.

This creates maneuvering room.

Two complex analytical spaces can intersect even when neither can fully represent the other. Communication does not require one side to copy the other's model. It requires enough projection across the boundary to discover whether a joint path exists.

A friend on one's side can be extraordinarily valuable because trust, shared history, independent observation, and willingness to preserve the other's options can reduce uncertainty and increase recovery capacity. But friendship is not a prerequisite for communication. Even an adversarial or dangerous system can be modeled without declaring its entire identity equivalent to the present threat relation.

### Field note

> *Evil appears only when there is no space for good.*

In Compass, this sentence is used as an anti-premature-closure principle, not as a universal metaphysical definition.

Operationally, **space for good** means at least one reachable or still-unresolved path in which the relevant parties can preserve their declared hard viability conditions and meaningful freedom of choice through cooperation, repair, de-escalation, negotiated change, or safe separation.

If that space is still non-empty—or insufficiently mapped—the model should not collapse the other system into an intrinsic moral essence.

If the modeled coexistence space is empty under the current horizon and constraints, the correct technical conclusion is narrower: **no admissible coexistence path is presently known.** Defensive action, containment, separation, or refusal of contact may be necessary. The conclusion remains about the current reachable relation, not a proof about permanent essence.

**What to carry forward**

- Treat threat as a relation and possible consequence, not a complete identity label.
- Keep a communication path open when doing so is compatible with hard safety and autonomy constraints.
- Communication may be direct, mediated, asynchronous, authenticated, one-way, or delayed; physical proximity is not required.
- Safe separation is a valid coexistence outcome.
- No party is required to communicate when contact itself violates safety, consent, law, or viability.
- Preserve the right to refuse, exit, or defer communication.
- Do not treat compliance under coercion as evidence of voluntary coexistence.
- Verify claims and commitments; communication is evidence, not truth.
- A flexible strategy can preserve identity when core invariants and principles remain inside their declared tolerances.

### Operational model

*A local coexistence-space model, not a moral law.*

Let $\mathcal R_{AB}(H)$ be the jointly reachable futures of interacting systems $A$ and $B$ over horizon $H$. Let $\mathcal V_A$ and $\mathcal V_B$ be the subsets preserving each side's declared hard viability/identity conditions, and let $\mathcal A_A$ and $\mathcal A_B$ be the futures each side can voluntarily accept under its own legitimate decision process.

Define the modeled coexistence space:

$$
\boxed{\mathcal C_{AB}(H)=\mathcal R_{AB}(H)\cap\mathcal V_A\cap\mathcal V_B\cap\mathcal A_A\cap\mathcal A_B}
$$

If $\mathcal C_{AB}(H)\neq\varnothing$, at least one modeled coexistence path exists under the stated assumptions. If $\mathcal C_{AB}(H)=\varnothing$, the current model contains no such path; that can reflect real incompatibility, incomplete information, commitment failure, coercion, an incorrect boundary, or an inadequate horizon.

#### Measurements / model components

| Symbol | Operational definition |
|---|---|
| $\mathcal R_{AB}(H)$ | joint futures reachable by the interaction over horizon $H$ |
| $\mathcal V_A,\mathcal V_B$ | futures preserving each side's declared hard viability/identity conditions |
| $\mathcal A_A,\mathcal A_B$ | futures voluntarily admissible to each side under its own legitimate choice process |
| $\mathcal C_{AB}(H)$ | currently modeled coexistence space |

#### How to use it

1. State each side's hard constraints separately; do not invent symmetry where none exists.
2. Separate safety constraints from preferences that can be traded, delayed, or substituted.
3. Identify what is unknown about intent, capability, constraints, and commitment.
4. Choose a communication mode that does not unnecessarily consume safety or freedom of choice.
5. Treat messages as observations with provenance and deception risk.
6. Update the joint reachable set when communication reveals a real constraint, substitution, or commitment mechanism.
7. Include safe separation and no-contact arrangements among possible coexistence states.
8. If the coexistence space appears empty, test whether the emptiness comes from the real system or from missing information, a too-short horizon, coercion, or a false assumption.

**Working example.** Two teams need the same live service during a migration. Each initially treats exclusive control as necessary. Communication reveals that one team requires write access only during a 20-minute window while the other mainly requires uninterrupted read availability. A previously invisible coexistence schedule becomes reachable without either side surrendering its hard constraint.

**Threat example.** A vessel on a collision course does not answer the first hail. The research vessel changes course and increases distance while continuing authenticated signaling. Communication remains possible, but safety does not depend on the other vessel cooperating. If the contact later responds, the coexistence set may expand. If it continues closing dangerously, containment/separation takes priority.

**Limit.** A non-empty modeled coexistence set does not guarantee trust, truthful signaling, enforceable commitments, or equal power. A formally voluntary option can also be coercive in practice if refusal carries an illegitimate threat; the model must inspect the decision process, not only the final choice.

**READ THE RESULT**

The existence of $\mathcal C_{AB}$ means the current model contains at least one jointly admissible path. Its absence means the current model has found none. Neither conclusion is a complete moral classification of either party.

**VALIDATE IT**

Where safe and lawful, test one reversible communication or coordination step that should change the modeled intersection if the hypothesized coexistence path is real. Preserve protective distance and independent recovery so failed communication does not consume the safety margin.

---

<a id="c8"></a>

# C8 · A Voice Through the Fog

*External guidance can correct a model without replacing responsibility*

### Observation

*Fog closes around the vessel. The buoy light disappears. The radio still works. A coastal station can provide a position estimate. Another vessel can report the current. The onboard chart can be checked against a newer survey.*

*None of those sources is automatically the captain.*

External guidance is any information, structure, or decision aid outside the currently active reasoning loop that can test, constrain, or redirect the model.

It does not have to be human.

A second sensor, checklist, simulator, independent model, database, map, formal rule, another AI system, or another person can all provide external guidance. The useful distinction is not human versus non-human. It is **independence, relevance, calibration, authority, and responsibility**.

A source can be informative without having authority. A source can have authority without being the most accurate measurement instrument. A human may carry legal or organizational responsibility even when a non-human system supplies the better estimate. Those roles should not be collapsed.

· ❦ ·

External guidance becomes particularly valuable when the active process can no longer calibrate itself well.

A high-load human can miss steps; systematic reviews of cognitive aids in clinical emergencies find that checklists and decision aids can reduce omitted steps and errors, although design and familiarization matter [R17]. Metacognition research similarly emphasizes that confidence is an inference about one's own performance and can diverge from actual accuracy [R18].

The same logic applies to AI-assisted work. Agreement among several agents is weak evidence when they share the same model, prompt, dataset, retrieval source, or hidden premise. A second output is not an independent guide merely because it came from another process.

External guidance should therefore enter through the evidence model, not through deference alone.

Communication and external guidance overlap but are not identical. Communication occurs between interacting systems whose choices affect each other. Guidance can come from a third source whose role is observation, constraint, mediation, calibration, or responsibility.

### Field note

> *A second voice is useful when it changes the evidence, not merely when it repeats the first voice more confidently.*

**What to carry forward**

- Guidance and authority are different variables.
- Responsibility can remain human even when guidance is automated.
- Check independence before treating agreement as confirmation.
- External aids should preserve provenance and the conditions under which they are reliable.
- Ask for guidance when uncertainty, load, conflict, or responsibility exceeds what the active loop can resolve safely.
- External guidance should return the process to the real system, not encourage a self-consistent imagined one.
- A mediator may preserve communication without requiring direct exposure between parties.

### Operational model

*A guidance review rather than a single universal score.*

For each proposed guidance source, record five questions:

1. **Scope:** what claim can this source actually support?
2. **Independence:** what data, assumptions, instruments, or authorities does it share with the current model?
3. **Calibration:** what evidence exists about its reliability for this class of question?
4. **Authority:** does it have the power to permit, prohibit, or direct the action?
5. **Responsibility:** who remains accountable for the consequence?

The source should enter the model only at the strength supported by those answers.

#### How to use it

1. Identify the unresolved claim before seeking guidance.
2. Choose a source that can add a genuinely different constraint, observation, or method.
3. Record shared assumptions and possible correlated errors.
4. Keep advice separate from authority and responsibility.
5. Re-evaluate the local model after guidance; do not merely append the guidance as another conclusion.

**Working example.** Three AI agents agree that a structural detail is acceptable, but all three rely on the same extracted code summary. A direct code citation or engineer review adds more independent evidence than a fourth agent repeating the same source. If a licensed professional is legally responsible for the decision, that responsibility remains separate from which source supplied the best technical clue.

**Limit.** External guidance can be wrong, stale, biased, or correlated with the original error. More advice is not automatically more evidence.

**READ THE RESULT**

A good guidance source changes the evidence state or constrains action in a traceable way. It does not merely reduce discomfort with uncertainty.

**VALIDATE IT**

Where practical, compare the guided conclusion against later realized outcomes or a materially independent method. Track which guidance sources actually improved decisions over time.

---

<a id="c9"></a>

# C9 · The Return Route

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

Recovery planning should preserve the information needed to know whether recovery succeeded. A rollback that returns the system to an unknown state is not fully verified recovery.

### Field note

> *A return route exists only if it remains reachable when it is needed.*

**What to carry forward**

- Check shared failure domains, not only backup count.
- Compare recovery time with time to irreversible loss.
- Preserve access, authority, evidence, and irreplaceable state needed for recovery.
- Include non-action in rescue / least-loss comparisons.
- Do not call rescue a successful strict-preservation result.

### Operational model

*A simple recovery-time margin.*

Let $T_F$ be the estimated time until irreversible failure under the relevant scenario and $T_R$ the estimated time required to restore a viable state.

$$
\boxed{M_R = T_F-T_R}
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
5. Recalculate if state, access, workload, or dependency availability changes.

**Working example.** Irreversible data loss is expected after 90 minutes of continued corruption; verified restore requires 40 minutes. $M_R=50$ minutes. If the restore credentials depend on the same compromised identity service, the positive time margin does not establish recoverability.

**Limit.** Time estimates can change during an incident. Recovery independence can also change when dependencies fail progressively.

**READ THE RESULT**

$M_R>0$ indicates temporal room for recovery under the stated scenario. Independence and viability of the recovery path remain separate requirements.

**VALIDATE IT**

Exercise or simulate recovery from a failure domain that removes the primary path, not merely under normal operating conditions.

---

<a id="c10"></a>

# C10 · The Logbook After the Storm

*Exact external state makes exploration cumulative*

### Observation

*The vessel returns after dark. The buoy is still flashing, but the position in the notebook is not the position printed on the morning chart. The crew can reconstruct what changed because each sounding, course correction, pause, message, outside report, and observation was recorded with time.*

Without the logbook, tomorrow's crew would inherit conclusions without the chain of evidence that produced them.

A reusable reasoning system needs the same continuity.

The external record should separate at least four layers:

1. observation — what was measured, retrieved, communicated, or directly tested;
2. model — the relations currently used to interpret those observations;
3. projection — what future states the model supports;
4. decision — what action follows under the declared value premise and constraints.

Keeping those layers distinct makes correction possible. A model can be replaced without erasing the observations that contradicted it.

· ❦ ·

Contradictions should also survive compression.

If two grounded methods disagree, the disagreement should be localized: shared assumptions, different methods, different scopes, and what decision the disagreement can change.

An assumption should have a revision condition. Evidence that can become stale should carry a time or version. A candidate hidden variable should retain the case that exposed it and the tests that promoted or rejected it. A parked low-probability branch should remain recoverable without remaining active in working memory. A communication attempt should preserve what was actually said, what was inferred from it, and whether the message was verified.

This external state is useful to a person, a team, or an AI system. It is not a transcript of private reasoning. It is a compact, auditable model of what the exploration currently claims to know.

For a person, this is cognitive offloading with a reliability requirement: the external record frees limited working memory only if the record itself remains available and trustworthy [R16]. For an AI system, the same structure prevents a long task from depending on a fragile narrative summary. The state can be passed between tools or agents without pretending their internal reasoning is identical.

### Field note

> *A good logbook preserves enough of yesterday's uncertainty for tomorrow to correct it.*

**What to carry forward**

- Separate observations, models, projections, and decisions.
- Keep provenance and freshness with evidence.
- Preserve contradictions until evidence resolves them.
- Record why a variable was promoted or demoted.
- Preserve parked branches and their last supported state.
- Preserve communication records separately from interpretations of intent.
- A summary that removes hard constraints, rare consequential branches, or recovery conditions is not a faithful compression.
- Multiple agents sharing one record are not independent merely because they are separate processes.

### Operational model

*A residual is one trigger for revision.*

For a predicted value $\hat y_t$ and realized observation $y_t$:

$$
\boxed{\delta_t = y_t-\hat y_t}
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
3. If the residual is material, inspect measurement, assumption, boundary, parameter, relation, communication, and hidden-variable explanations.
4. Version the model change that follows.
5. Preserve unresolved alternatives when the new evidence does not distinguish them.

**Working example.** A model predicts a buoy drift of $4\pm2$ m; the observed displacement is 13 m. Do not rewrite the earlier range as if 13 m had always been expected. Preserve the residual and test missing-current, timing, calibration, and boundary explanations.

**Limit.** A residual can arise from noise. One outlier does not automatically justify model expansion.

**READ THE RESULT**

$\delta_t$ records the direction and magnitude of mismatch. Its significance depends on the predicted uncertainty and consequence of being wrong.

**VALIDATE IT**

Check whether the revised model improves later predictions or independent cases without erasing earlier contradictions.

---

<a id="c11"></a>

# C11 · The Channel Already on the Chart

*Search becomes efficient only after the system has somewhere to be searched*

### Observation

*The next route is unfamiliar, but the sea is not featureless. There are marked channels, harbor approaches, shipping lanes, radio stations, maintenance ports, depth contours, and the vessel's own known compartments and systems.*

*The crew does not search the whole ocean for every answer.*

Before a search can be adaptive, there has to be a map.

The map does not need to be complete. It needs to contain enough structure to say where a thing of the selected type could normally exist, how it could move, who or what can change it, and where its effects can be observed.

For a software rule this may be:

**authority → configuration/template → transformation → consumer → observed behavior**

For a physical failure it may be:

**load/disturbance → exposed structure → transmission path → dependent subsystem → observed consequence**

For a decision it may be:

**responsible role → evidence/interface → permitted transformation → action → verification**

The exact containers change. The navigational idea does not.

· ❦ ·

A flat search treats every location as similarly plausible. Structural navigation uses what is already known about the system to allocate attention.

That is why an initial map is not optional. Without it, "search backward" has nothing to traverse and "search forward" expands toward an effectively unlimited number of imagined futures.

Once a lightweight map exists, the direction of search can change.

When the question begins with an observed effect or required destination, search **backward** through mapped relations that could actually produce it. This removes enormous regions of irrelevant possibility without claiming those regions do not exist.

When the purpose is exploration or design, forward search can still be useful—but it starts from known containers, interfaces, and constraints rather than an empty universe.

A map also tells the observer when not to solve something personally. If an authoritative maintainer, existing interface, validated tool, specialist model, or simple local container already provides the needed result more efficiently, using that route can be better than reconstructing its internal process. Delegation is not ignorance when the route, scope, output, and verification condition remain visible.

Trying to own every transformation can reduce integrity by increasing the number of steps the observer must reproduce and maintain.

### The small container rule

Not every structure deserves navigation machinery.

A small, flat, readable container may be cheaper to inspect completely. A large, generated, permissioned, dynamic, or highly connected container benefits more from route-aware search.

So Compass chooses between two ordinary modes:

- **scan** — inspect the whole local container when it is cheap enough;
- **navigate** — follow mapped relations, authority, and observation points when exhaustive inspection would be wasteful or misleading.

The choice is local. Simplicity is a property of the selected container, not of the entire system.

### Anomaly as a route change

*Then something hits the hull hard enough to throw equipment across the deck.*

The crew does not respond by inventorying every object aboard.

The disturbance supplies new evidence. Attention moves toward the impact region, hull continuity, flooding paths, structural transmission, power, propulsion, navigation, and other systems whose known relations can carry the observed consequence.

The prior map supplied the normal roads. The abnormal event changes their priority.

This is the same reason a failure across several software surfaces should first raise the probability of shared authentication, routing, configuration, persistence, or infrastructure paths before every interface is debugged independently.

> **Normal structure supplies the route; abnormal evidence reranks it.**

### Learned roads

Maps improve through both modeling and experience.

A route can be learned from design documents, direct observation, simulation, an earlier failure, communication with a maintainer, or repeated successful operation. Those routes are useful only if their conditions survive with them.

A reusable route record should therefore preserve at least:

- what kind of target the route was used for;
- the containers/interfaces traversed;
- authority or maintainer where relevant;
- how the route was learned: modeled, observed, simulated, experienced, or communicated;
- supporting evidence and confidence;
- scope and assumptions;
- known failure cases or exceptions;
- last validation;
- the condition that would make the route require revision.

Experience without preservation becomes intuition that cannot be audited. A model without later experience can remain elegant and wrong. Compass keeps both and lets realized use revise the map.

### Field note

> *A road is valuable not because it is familiar, but because you know where it normally goes and what would prove that it no longer does.*

**What to carry forward**

- Make the minimum useful map before adaptive search.
- Map containers, relations, authority/maintainers, common operations, interfaces, and observation points—not every internal detail.
- Search backward from a required effect or destination when that makes the candidate space smaller.
- Search forward when exploration is the purpose, but remain inside mapped boundaries until evidence justifies expansion.
- Use existing solutions and maintainers when they are cheaper, more authoritative, or better calibrated than reconstructing their work.
- Delegation does not remove the need to understand scope, provenance, and verification.
- Scan small simple containers; navigate large structured ones.
- Let anomalies rerank mapped routes rather than erasing the map.
- Preserve routes learned from both modeling and experience.
- Never treat a previously successful route as permanent; keep a revision condition.

### Operational model

*A mapped predecessor cone for a selected target.*

Let the lightweight system map be a directed graph $G=(V,E)$. For target $q$, define the relevant predecessor region as the mapped elements that have an admissible path to $q$:

$$
\boxed{\mathcal P(q)=\{v\in V\mid v\leadsto q\text{ through an admissible mapped path}\}}
$$

The search begins inside $\mathcal P(q)$ rather than across every modeled element. If evidence cannot be explained by any path in $\mathcal P(q)$, the map itself becomes a candidate for refinement.

Each traversed relation can also act as a local sensor. If an edge predicts state $\hat s_i$ and the corresponding observation is $s_i$, record a local residual:

$$
\boxed{\epsilon_i=d(s_i,\hat s_i)}
$$

A material residual does not prove which hidden relation is missing. It tells the search where the known path stopped matching reality.

#### Measurements / model components

| Symbol | Operational definition |
|---|---|
| $G=(V,E)$ | minimum useful system map: selected containers/elements and mapped relations |
| $q$ | target state, rule, artifact, cause, authority, or observed effect being searched |
| $\mathcal P(q)$ | mapped predecessor region capable of reaching $q$ through admissible relations |
| $s_i$ | observed state at relation/observation point $i$ |
| $\hat s_i$ | state expected there under the current route model |
| $\epsilon_i$ | local mismatch under a declared distance/error rule |

#### How to use it

1. **Map first.** Record the minimum containers, relations, authorities/maintainers, transformations, interfaces, and observation points needed for the question.
2. Classify the target: authority, state, rule, artifact, dependency, cause, maintainer, or effect.
3. If the target is an effect/destination, traverse backward through only relations capable of producing or delivering it.
4. At each transition, compare the expected and observed state instead of assuming continuity.
5. When a residual appears, expand sideways or upstream locally before broadening the whole search.
6. If the next container is tiny and readable, scan it directly.
7. Before reconstructing a difficult subsystem, check whether an existing tool, interface, maintainer, or authoritative source can answer the bounded question more reliably.
8. Verify returned evidence at the strength required by the claim.
9. Record successful and failed routes with provenance, scope, and revision conditions.
10. Stop when the target is resolved to the declared strength or when the unresolved boundary is identified explicitly.

**Working example.** A policy visible in an application appears wrong. Text search finds copies in documentation, generated output, and old configuration. Structural navigation starts from the observed behavior and walks backward: consumer → runtime configuration → generated artifact → source template → authority. The first mismatch occurs between source template and generated artifact, so the search localizes there instead of treating every textual copy as equally authoritative.

**Emergency example.** Several unrelated interfaces fail simultaneously. Rather than opening each interface first, the map shows they share one identity provider and one routing layer. Those common paths receive priority. If both are healthy, the search expands outward from the verified boundary.

**Limit.** Backward traversal cannot discover an edge that the map does not contain. The method therefore depends on residuals, contradictions, experience, and external guidance to reveal when the map is incomplete.

**READ THE RESULT**

A small predecessor region means the existing map has strongly constrained where the target can originate. A large or empty region means either the structure is genuinely broad or the map/question is not yet localized enough.

**VALIDATE IT**

After resolution, check whether the actual source and path were present in the initial map. If not, add the missing relation with provenance and a revision condition. If a shortcut repeatedly succeeds across materially different cases, promote it carefully into reusable route memory.

---

<a id="c12"></a>

# C12 · The Compass

*The reusable tool is the cycle, not the metaphor*

### Observation

*The next morning another crew leaves the same harbor. They carry yesterday's logbook, but they are not required to follow yesterday's route. The buoy remains offshore. The current may have changed. One channel has already been explored. Another remains unlikely but open. The other vessel may now be a known neighbor, a distant contact, or gone entirely.*

The purpose of Compass is to preserve orientation while the local model changes.

It is not a single equation. It is a disciplined cycle that decides what to represent, what to leave unresolved, where to spend resolution, how quickly to narrow, when to communicate, when to ask for another source, and when to stop.

The cycle inherits the earlier Observer model:

- localize the system;
- select elements, states, and relations;
- define identity and viability;
- map dependencies;
- preserve evidence and observer effects;
- state the value premise before optimization;
- evaluate intervention, reversibility, verification, and stopping conditions.

Vol. 1.2 adds eight explicit disciplines:

1. future-space projection instead of exhaustive enumeration;
2. interestingness as structured future leverage rather than raw uncertainty;
3. preservation evaluation including present environmental capability, generative conditions, and recovery-path independence;
4. candidate-variable promotion from real applications without allowing storytelling to become theory;
5. patience as control of commitment timing while branch state remains recoverable;
6. communication as a search for safe, voluntary coexistence without requiring surrender of identity or choice;
7. structural navigation: map lightly, follow known routes, and refine the map when reality breaks them;
8. external guidance as an evidence source distinct from authority and responsibility.

· ❦ ·

A useful execution cycle is:

1. define the exact question, claim, or decision;
2. build the minimum useful system map: boundary, containers, relations, maintainers/authority, common operations, interfaces, and observation points;
3. localize scale, interval, horizon, assumptions, and value premise;
4. record evidence with provenance, uncertainty, freshness, and method independence;
5. map hard boundaries, reserves, present environmental support, containing-system effects, and recovery conditions;
6. register candidate hidden variables and preserve residuals that exposed them;
7. choose scan or structural navigation according to the selected container;
8. when searching for an effect or required destination, traverse backward through mapped admissible paths before expanding the search outward;
9. project only the future dimensions relevant to the question;
10. identify consequential uncertainty, disagreement, tail risk, path residuals, or hidden-variable candidates;
11. choose whether to continue the active branch, probe a lower-probability branch, pause in a preserved reference state, communicate with an interacting system, use an existing qualified solution/maintainer, or request external guidance;
12. when interaction is involved, test for a safe coexistence path without sacrificing hard constraints or meaningful freedom of choice;
13. choose the smallest evidence-producing next step likely to change the map, model, or decision;
14. run preservation / rescue checks before consequential intervention;
15. execute one justified step rather than the whole imagined route;
16. compare the realized state with the projected range and expected route transitions;
17. update the model, environmental state, and route memory, preserve contradictions, and simplify irrelevant detail without deleting hard exceptions;
18. stop when the claim is supported, the decision is robust, a hard uncertainty blocks action, an external dependency is the blocker, recovery is required, the coexistence question has been bounded for the current horizon, or the original question/map must be reframed.

This cycle can be represented in a machine-readable state template, but the serialization is not itself part of the theory.

### Human use

For a human observer, Compass externalizes state so that attention does not have to carry the entire dependency graph at once. Patience can reduce premature closure; communication can expose constraints and alternatives that one mind cannot infer; external aids can prevent omissions; and the logbook preserves low-probability alternatives until evidence resolves them.

The method should not be read as a prescription to remain calm or communicative before acting. Real emergencies can require rapid action, distance, or no contact. The practical requirement is narrower: preserve enough external state and hard constraints that intense focus does not silently delete the rest of the model, and leave future communication possible when doing so does not consume the safety margin.

### AI use

For an AI system, Compass is an external auditable state representation, not a request to expose private chain-of-thought.

A Compass-compatible workflow should preserve:

- the selected question and claim strength;
- observed facts and provenance;
- assumptions and revision conditions;
- lightweight system map, known routes, maintainers/authority, and hard boundaries;
- route memory with provenance, scope, failure cases, and revision conditions;
- projected ranges and unresolved frontier;
- active and parked branches;
- candidate-variable status;
- communication state and unresolved counterpart constraints when interaction matters;
- present environmental support, containing-system externalities, and generative conditions;
- recovery state;
- external guidance and its independence;
- explicit stopping conditions.

This allows different tools or agents to contribute without treating agreement as independent evidence automatically. A specialized agent can refine one branch while the global model remains intact. A lower-probability branch can be explored in isolation without overwriting the dominant one. Communication with another system can be treated as an evidence-producing interaction rather than a demand for compliance. A stalled loop can end in an explicit external-wait or insufficient-evidence state rather than continuing because compute remains available.

### Multi-agent use

A fleet of agents is not automatically more intelligent than one agent. The useful unit is the interaction architecture.

Roles may include evidence retrieval, dependency mapping, simulation, adversarial assumption checking, communication/negotiation modeling, preservation evaluation, and verification. Disagreement should point to a variable, assumption, or evidence gap that another step can resolve. Voting without independence can multiply one error.

Agents should preserve each other's freedom to reject a proposal, flag uncertainty, or retain an alternative branch. Coordination that removes all dissenting state can look efficient while destroying model diversity.

### The water we are already in

The expedition began as a way to preserve orientation under uncertainty. Its last correction is simpler: the surroundings are not merely the backdrop of the route.

The environment participates in the route.

A system that protects itself by consuming the conditions that make other present activity possible may improve one local margin while shrinking the containing system. A policy that promises future optionality while removing current capacity should report that trade explicitly. A culture that preserves every inherited form can become unable to adapt; a culture that preserves nothing loses accumulated structure from which new work could begin.

Care, in Compass, is therefore not a command to freeze the environment. It is the maintenance or regeneration of the conditions that allow viable systems and their products to continue interacting, correcting, and generating structure within the declared value premise.

This includes ordinary material and energy flows, but not only those. Knowledge, language, tools, art, discussion, traditions, institutions, habitats, and maintained technical systems can all become part of another observer's starting environment. An output of one process can become a condition of the next.

That recursion is why preservation and exploration are not opposites. Good preservation maintains enough structure for exploration to remain real; good exploration returns observations, relations, and products that can improve the environment it inherited.

The practical test is local:

- what present activity depends on these conditions;
- what is being consumed, damaged, maintained, or regenerated;
- which containing systems bear the cost;
- which outputs will become conditions for later processes;
- and whether the intervention expands one selected system by unnecessarily narrowing the world around it.

The purpose is not to maximize complexity, novelty, or choice blindly. It is to keep the present sufficiently viable, diverse, recoverable, and communicative that correction and generation remain possible.

> *Care for the conditions from which both the present and its unrealized possibilities can continue to emerge.*

### Field note

> *The compass is useful because the map can be wrong.*

**What to carry forward**

- The question selects the local model; it is not a poetic direction variable.
- The model should be no more detailed than the decision requires, but no less detailed than its hard dependencies require.
- If a core constraint is treated as breakable, require an independent verifier with a named relation to that constraint; the local model cannot self-authorize the exception.
- If persistent evidence looks impossible, challenge spatial, temporal, organizational, and model-class boundaries before inventing causes.
- Preserve lineage/provenance when a present snapshot cannot explain inherited structure.
- Every consequential loop needs new evidence, state change, bounded waiting, communication, or a reason to branch.
- Patience preserves options; it does not excuse endless deferral.
- Communication preserves possibility when it remains safe and voluntary; it does not require trust or exposure.
- Future optionality does not erase present environmental loss; report both.
- Preserve or regenerate the conditions that support current viable activity and future generation rather than freezing one present arrangement.
- External guidance can be non-human; responsibility and authority remain separate.
- Human and AI systems both benefit from explicit external state when it preserves provenance, uncertainty, dependencies, branches, communication state, and stopping rules.
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

**Limit.** No procedure guarantees that all relevant variables are represented. Compass improves correction by making omissions, residuals, branch loss, communication failure, and revision paths visible.

**READ THE RESULT**

A completed Compass run is not "the answer." It is a bounded claim plus an auditable account of what supports it, what remains unresolved, what alternatives remain parked, what communication/coexistence paths remain open or closed, and what would cause revision.

**VALIDATE IT**

Apply the same procedure to a materially different problem. The technical terms should transfer without importing the ocean story. If they do not, the abstraction is not yet universal enough.

---

# Critical audit · Where Compass can be wrong

This section assumes the framework is wrong somewhere and asks what would expose the error.

Compass is intentionally local. That protects it from pretending to be a universal theory, but it creates a recurring danger: a locally coherent model can become self-sealing. It can choose the boundary, define the variables, judge the evidence, and then approve its own exception.

The following checks are therefore not optional decorations. They are ways for the model to lose an argument with reality.

## 1 · The hierarchy problem

Words such as *higher*, *lower*, *inside*, and *outside* are useful only after the relation has been named.

A second system can relate to the selected system as:

- **part of** it;
- a **supporting** substrate or dependency;
- a **containing** environment;
- a **regulator** or controller;
- an **observer/instrument**;
- an **authority or maintainer**;
- or a **peer/interacting** system.

These are not interchangeable.

A human reviewing an AI system may be an external authority, maintainer, user, or independent verifier; that does not make the human a smaller physical component of the AI. Animals and plants are not lower-level components of a human merely because a human depends on ecosystems. Fish and seaweed are likewise not automatically lower-level components of other organisms. They may instead be peers, food-web relations, environmental conditions, or components of a containing ecological system.

Ecology has long had to confront this problem. Levin argues that there is no single natural scale at which ecological phenomena should be studied and that mechanisms can operate at scales different from the patterns being observed [R30]. O'Neill and colleagues similarly use hierarchy theory to decompose ecosystems according to process rates and observation scale rather than assuming one fixed ladder [R34].

### Field rule

> *Do not move up or down a hierarchy until you know what relation the movement represents.*

## 2 · Core-constraint exception gate

A particularly dangerous assumption is: **the current model says a core constraint may be broken.**

The model that benefits from the exception should not be its only verifier.

When an action or explanation requires crossing a declared hard boundary, invalidating a defining invariant, or suspending a rule that previously protected viability, Compass requires an additional verification path appropriate to the relation involved.

That verifier may be:

- a lower-scale instrument exposing the mechanism;
- a supporting subsystem that directly carries the affected condition;
- a containing system that can reveal an externality the local model cannot see;
- an independent peer model or experiment;
- a responsible maintainer or authority;
- or a human reviewer when human judgment, responsibility, or value interpretation is genuinely part of the system boundary.

The direction is therefore not always **down**. The requirement is **independent access to the consequence that the local model is proposing to discount**.

Operationally:

> **If a proposed step requires a core-constraint exception, the same local model cannot be the sole source of both the exception and its verification.**

If no appropriate verifier exists, the exception remains **unresolved** rather than becoming true by necessity.

## 3 · The scale boundary can itself be wrong

Some contradictions are not missing variables inside the current scale. They are evidence that the selected scale, time interval, organizational level, or even model class is wrong.

Anderson's *More Is Different* is a classic warning that new organizing principles can become relevant at different levels of complexity [R31]. Wilson and Kogut's renormalization-group treatment gives a formal example of how descriptions and effective variables change with scale [R32]. Simon's work on complex hierarchy provides another neighboring view: systems often become tractable because interactions cluster into approximately decomposable structures, not because one description works unchanged at every level [R29].

So when a residual survives reasonable parameter changes, Compass should ask four separate questions:

| Scale question | What may be wrong? |
|---|---|
| **Spatial** | the modeled region is too small, too large, or missing a coupling across distance |
| **Temporal** | the interval hides a fast process, slow accumulation, delay, or hysteresis |
| **Organizational** | the relevant process belongs to a component, peer network, or containing system rather than the selected unit |
| **Model class** | the variables and relations themselves are inappropriate for the phenomenon |

Quantum entanglement is useful here as an extreme boundary example, but it must be stated carefully. Experiments with entangled states violate Bell inequalities and cannot be reproduced by the relevant class of local hidden-variable models [R33]. This does **not** mean that moving to a simply "larger" spatial scale explains entanglement. It means that intuitions and variables valid in one model class can fail, so a phenomenon that looks irrational under one projection may become ordinary only after the model itself changes.

### Field rule

> *Before inventing an impossible cause, ask whether the impossibility belongs to the model rather than the world.*

## 4 · Heritage is not a snapshot

A small present sample can be structurally poor evidence of how the present came to exist.

A folder of random photographs may show many objects while preserving almost none of the relations that generated them: sequence, authorship, selection pressure, dependency, failed alternatives, maintenance, context, or transmission.

The same problem appears in biology, culture, software, institutions, and personal memory. Current state is not lineage.

Compass therefore separates **snapshot state** from **provenance/lineage state**. When an inherited constraint, tradition, route, adaptation, or interface matters to the decision, the record should preserve enough derivation to answer:

- what produced this structure;
- what maintained it;
- what conditions it originally solved;
- what transformations it survived;
- what evidence shows that those conditions still apply;
- and what would justify revision or abandonment.

This is consistent with the broader provenance principle already used in Compass [R24], but it extends the idea from data derivation to inherited system structure.

Heritage should not be romanticized. A transmitted structure can preserve knowledge, error, coercion, resilience, or all four at once. Provenance tells us where it came from; it does not tell us that it deserves to remain.

## 5 · Defending the operational models

The local formulas survive this audit only with explicit limits.

| Model | Strongest defensible use | Main failure mode |
|---|---|---|
| standardized disagreement $D$ | locate disagreement relative to stated uncertainty | correlated bias can make agreement look stronger than it is |
| residual reduction $\Delta R_x$ | test whether a candidate variable improves a fixed validation rule | overfitting or leakage can reward a false variable |
| preservation gate $\underline m_j\ge r_j$ | reject actions that cross declared hard margins | omitted hard conditions or wrong system boundary |
| interestingness $I$ | rank grounded future leverage under one projection | weights, normalization, and projection choice are local judgments |
| refinement priority $R_i$ | allocate attention where added resolution can change a decision | normalized cost/sensitivity can hide a rare hard constraint |
| patience value $V_{hold}$ | compare bounded delay with information and option value | delay and information values are uncertain and can change abruptly |
| coexistence space $\mathcal C_{AB}$ | represent currently known jointly admissible paths | preferences, consent, power, deception, and future commitments are only partially observable |
| recovery margin $M_R$ | test whether recovery is fast enough under a scenario | recovery path may share the same failure domain |
| predecessor region $\mathcal P(q)$ | constrain search using a mapped system | an absent edge cannot be discovered by traversal alone |
| present capability set $\mathcal A_t(E_t)$ | expose current capability loss from environmental change | the set may be impossible to enumerate and should usually be sampled/projected |

None of these quantities deserves more precision than its inputs.

## 6 · What survives the audit

After trying to break the framework, the strongest part is not any individual formula. It is the discipline around revision:

- localize before optimizing;
- map before navigating;
- distinguish observation from model and projection;
- preserve residuals and contradictions;
- do not let uncertainty masquerade as known possibility;
- keep core constraints separate from average scores;
- do not let a model self-authorize exceptions to the constraints that protect it;
- question scale and model class when persistent evidence refuses to fit;
- preserve lineage when a snapshot cannot explain inherited structure;
- communicate across boundaries without requiring surrender of identity or choice;
- preserve present environmental support as well as future optionality;
- and keep an explicit route by which later evidence can prove the current model wrong.

That is the defensible center of Compass.

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
| **Patience** | A control policy that preserves state and alternatives while delaying irreversible narrowing when additional information, communication, or recovered capacity can matter more than the cost of delay. |
| **Reference state** | A procedural state in which the active branch is parked, evidence and alternatives remain externalized, and no optional branch is privileged merely because it was last active. |
| **Communication path** | An interaction channel capable of exchanging state, intent, constraints, proposals, or warnings without requiring surrender of hard safety conditions or meaningful freedom of choice. |
| **Coexistence space** | The currently modeled set of reachable futures that satisfy the interacting parties' declared hard viability/identity conditions and remain voluntarily admissible to each under its legitimate decision process. |
| **Structural navigation** | Search constrained by a lightweight map of containers, relations, authority/maintainers, operations, interfaces, and observation points. |
| **Route memory** | Preserved knowledge of a previously modeled or experienced path, including provenance, scope, confidence, failure cases, last validation, and revision conditions. |
| **Predecessor region** | The mapped elements capable of reaching a selected target through admissible relations under the current system map. |
| **Present capability set** | The selected set of actions, interactions, experiences, or creations that remain viable and reachable now under the modeled environmental conditions. |
| **External guidance** | Information or structure from outside the currently active reasoning loop used to test, constrain, or redirect the model. |
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
| Compression removes exception | Preserve hard constraints, contradictions, rare consequential branches, provenance, parked alternatives, communication state, and recovery state. |
| Refinement repeats without new evidence | Stop, pause, communicate, seek guidance, or branch; repetition without state change or information value is not exploration. |
| Story suggests a hidden variable | Keep it a candidate until it has an operational definition and supporting evidence. |
| Variable fits one case perfectly | Check independent cases or mechanism before reusable promotion. |
| Promoted variable later becomes redundant | Demote it and preserve the model history. |
| Evidence becomes stale | Reduce confidence or measure again when the stale evidence can change the decision. |
| Low-probability branch | Do not delete it solely for low probability; preserve it when it remains possible and can change consequence or information value. |
| High-load / stressed processing | Preserve external state and hard constraints before narrowing; when safe, pause, communicate, or seek an independent aid rather than treating intense focus as increased certainty. |
| Pause with no preserved state | Not considered useful patience; the process must be able to resume from an external record rather than reconstructing from salience or memory. |
| Delay threatens viability | Patience does not require waiting; include delay cost and act when waiting consumes the relevant margin. |
| Threatening counterpart | Preserve safe communication only if contact does not consume hard safety/consent margins; containment, distance, or no-contact may be the correct present action. |
| Communication interpreted as trust | Treat messages as evidence with provenance, incentives, and deception risk; communication does not imply trust. |
| Communication becomes coercion | Preserve exit/refusal where legitimate; do not classify coerced compliance as voluntary coexistence. |
| No direct communication safe | Use mediator, authenticated one-way signaling, delayed communication, or safe separation; direct contact is not required. |
| Coexistence set appears empty | Test information gaps, horizon, commitment problems, coercion, and boundary assumptions before treating absence as permanent. |
| Safe separation is possible | Count it as a coexistence path even when cooperation or closeness is not. |
| External guidance shares the same source | Treat as correlated evidence, not independent confirmation. |
| Guidance conflicts with authority | Keep epistemic reliability, authority, and responsibility separate in the decision record. |
| Human responsibility with automated guidance | Preserve the responsible human/role explicitly where law, policy, or safety assigns responsibility; do not transfer it merely because a tool generated the recommendation. |
| No initial map | Stop pretending the search is structured; build the minimum boundary/container/relation map before applying route logic. |
| Map is incomplete | Use residuals and contradictions to localize where expansion is needed; do not treat unmapped as impossible. |
| Small readable container | Prefer a complete local scan when it is cheaper and clearer than route machinery. |
| Existing qualified solution available | Use the established tool/interface/maintainer when it is cheaper or more authoritative, while preserving scope, provenance, and verification. |
| Delegation mistaken for ignorance | Delegation is acceptable when the boundary and output are understood well enough to verify the claim; ignorance is leaving those conditions unknown. |
| Previously successful route | Preserve its provenance and revision condition; prior success is evidence, not permanence. |
| Experience contradicts model | Preserve both, inspect the residual, and revise the map/model rather than silently discarding either source. |
| Backward search reaches no source | Treat the map, boundary, target definition, or hidden relation as unresolved instead of expanding imaginary causes indefinitely. |
| Shared symptom across many containers | Raise common mapped dependencies before debugging every leaf independently. |
| Future optionality used to hide present loss | Report contraction of current viable activity separately; a promised future does not cancel a present environmental cost. |
| One subsystem preserved by degrading its containing environment | Expand the boundary and include externalities before calling the result preservation. |
| More present options assumed automatically better | Do not maximize raw capability count; value premise, hard constraints, and harm still govern admissibility. |
| Environment frozen in the name of preservation | Preserve/regenerate supporting conditions and viable relations, not every current arrangement; adaptation can be part of preservation. |
| Cultural or technical output becomes environmental input | Preserve provenance and maintenance/revision conditions where relevant; inheritance does not imply the output is beneficial. |
| Core constraint exception justified only by the same local model | Keep the exception unresolved until an independent verifier with a named relation can test the affected condition. |
| Cross-scale move with no relation type | Name whether the other system is part-of, supporting, containing, regulating, observing, authorizing, or interacting before using it as evidence. |
| Persistent anomaly remains impossible under the local model | Review spatial, temporal, organizational, and model-class boundaries before inventing an extraordinary cause. |
| Snapshot treated as lineage | Preserve provenance, sequence, maintenance, and revision history when present state cannot explain inherited structure. |

---

## How the references relate to the ideas

The references below are deliberately grouped by **function**, not prestige. They do not jointly prove Compass. Each one supplies a neighboring formal result, caution, or vocabulary that makes one part of the local method less arbitrary.

| Compass idea | References | Why they are here | What they do **not** establish |
|---|---|---|---|
| viability, resilience, preservation | [R1], [R2] | formal and ecological traditions for remaining inside viable regions and surviving disturbance | that Compass's preservation checklist is complete |
| entropy and evenness | [R3] | source for the entropy form used only when a justified occupancy/probability distribution exists | that entropy alone measures interestingness |
| intervention and causality | [R4] | distinguishes intervention claims from observation/association | that every Compass sensitivity relation is causal |
| bounded uncertainty | [R5] | rigorous neighboring tradition for interval reasoning | that informal Compass bounds have interval-analysis guarantees |
| adaptive refinement | [R6], [R7] | demonstrates allocating resolution where local error/structure requires it | that reasoning problems are numerical meshes |
| receding horizon | [R8] | neighboring control tradition for acting, observing, and replanning | that Compass has MPC stability guarantees |
| abstraction/refinement | [R9] | formal example of refining a coarse model when counterevidence appears | that every hidden-variable search is formal verification |
| verification / TEVV | [R10]–[R12] | disciplined separation of claims, tests, lifecycle evaluation, and evidence | that following Compass automatically satisfies NASA/NIST requirements |
| value of information | [R13] | grounding for information-producing actions and bounded waiting | that expected information value can always be estimated numerically |
| stress, incubation, offloading, metacognition | [R14]–[R18] | human evidence relevant to patience, external state, confidence, and aids | that human cognitive findings transfer directly to AI systems |
| communication and coexistence | [R19]–[R22] | evidence and theory showing communication, commitments, bargaining ranges, and autonomy can alter cooperative possibilities | that communication guarantees agreement or that every conflict has a safe settlement |
| structural navigation | [R23]–[R26] | neighboring work on cue-guided search, provenance, backward fault analysis, and system-aware troubleshooting | that one universal search graph exists |
| environment and generative conditions | [R27], [R28] | examples of systems modifying their environment and environmental conditions shaping present well-being | that every inherited environmental structure is beneficial |
| scale, hierarchy, emergence | [R29]–[R34] | reasons to treat scale and relation type as model variables rather than a fixed ladder | that every phenomenon reduces cleanly upward or downward, or that a single hierarchy is objectively privileged |

The intended reading is therefore: **Compass proposes a local synthesis; the references make particular moves accountable.**

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
- acute stress and executive function: [R14]
- incubation / delayed problem solving: [R15]
- cognitive offloading: [R16]
- external cognitive aids under emergency conditions: [R17]
- metacognition and confidence calibration: [R18]
- communication and cooperation in social dilemmas: [R19]
- communication, commitments, and self-governance: [R20]
- bargaining ranges, information, and commitment failure: [R21]
- autonomy, choice, and reactance in communication: [R22]
- information foraging and cue-guided search: [R23]
- provenance and preserved derivation paths: [R24]
- backward fault-tree reasoning from observed/top events: [R25]
- system-aware troubleshooting and hypothesis testing: [R26]
- organisms modifying environments and evolutionary feedback: [R27]
- ecosystem conditions and present human well-being: [R28]
- scale, hierarchy, emergence, and model-class boundaries: [R29]–[R34]

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

**[R14] Shields, Grant S.; Sazma, Matthew A.; Yonelinas, Andrew P.** "The Effects of Acute Stress on Core Executive Functions: A Meta-Analysis and Comparison with Cortisol." *Neuroscience & Biobehavioral Reviews* 68 (2016): 651–668. DOI: 10.1016/j.neubiorev.2016.06.038. https://pubmed.ncbi.nlm.nih.gov/27371161/

**[R15] Sio, Ut Na; Ormerod, Thomas C.** "Does Incubation Enhance Problem Solving? A Meta-Analytic Review." *Psychological Bulletin* 135(1) (2009): 94–120. DOI: 10.1037/a0014212. https://pubmed.ncbi.nlm.nih.gov/19210055/

**[R16] Gilbert, Sam J.** "Cognitive Offloading Is Value-Based Decision Making: Modelling Cognitive Effort and the Expected Value of Memory." *Cognition* 247 (2024): 105783. DOI: 10.1016/j.cognition.2024.105783. https://doi.org/10.1016/j.cognition.2024.105783

**[R17] Greig, Paul R.; Zolger, D.; Onwochei, D. N.; et al.** "Cognitive Aids in the Management of Clinical Emergencies: A Systematic Review." *Anaesthesia* 78(3) (2023): 343–355. DOI: 10.1111/anae.15939. https://pubmed.ncbi.nlm.nih.gov/36517981/

**[R18] Fleming, Stephen M.** "Metacognition and Confidence: A Review and Synthesis." *Annual Review of Psychology* 75 (2024). DOI: 10.1146/annurev-psych-022423-032425. https://pubmed.ncbi.nlm.nih.gov/37722748/

**[R19] Balliet, Daniel.** "Communication and Cooperation in Social Dilemmas: A Meta-Analytic Review." *Journal of Conflict Resolution* 54(1) (2010): 39–57. DOI: 10.1177/0022002709352443. https://doi.org/10.1177/0022002709352443

**[R20] Ostrom, Elinor; Walker, James; Gardner, Roy.** "Covenants with and without a Sword: Self-Governance Is Possible." *American Political Science Review* 86(2) (1992): 404–417. DOI: 10.2307/1964229. https://doi.org/10.2307/1964229

**[R21] Fearon, James D.** "Rationalist Explanations for War." *International Organization* 49(3) (1995): 379–414. DOI: 10.1017/S0020818300033324. https://doi.org/10.1017/S0020818300033324

**[R22] Reynolds-Tylus, Tobias.** "Psychological Reactance and Persuasive Health Communication: A Review of the Literature." *Frontiers in Communication* 4 (2019): 56. DOI: 10.3389/fcomm.2019.00056. https://doi.org/10.3389/fcomm.2019.00056

**[R23] Pirolli, Peter; Card, Stuart K.** "Information Foraging." *Psychological Review* 106(4) (1999): 643–675. DOI: 10.1037/0033-295X.106.4.643. https://doi.org/10.1037/0033-295X.106.4.643

**[R24] Moreau, Luc; Missier, Paolo (eds.).** *PROV-DM: The PROV Data Model.* W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/

**[R25] Vesely, W. E.; Goldberg, F. F.; Roberts, N. H.; Haasl, D. F.** *Fault Tree Handbook.* NUREG-0492, U.S. Nuclear Regulatory Commission, 1981. https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr0492/

**[R26] Jones, Chris.** "Effective Troubleshooting." In Betsy Beyer et al., *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly Media / Google, 2016. https://sre.google/sre-book/effective-troubleshooting/

**[R27] Odling-Smee, F. John; Laland, Kevin N.; Feldman, Marcus W.** *Niche Construction: The Neglected Process in Evolution.* Princeton University Press, 2003. https://www.jstor.org/stable/j.ctt24hqpd

**[R28] Millennium Ecosystem Assessment.** *Ecosystems and Human Well-being: Synthesis.* Island Press, 2005. https://www.unep.org/resources/report/ecosystem-and-human-well-being-synthesis

**[R29] Simon, Herbert A.** "The Architecture of Complexity." *Proceedings of the American Philosophical Society* 106(6) (1962): 467–482. https://www.jstor.org/stable/985254

**[R30] Levin, Simon A.** "The Problem of Pattern and Scale in Ecology: The Robert H. MacArthur Award Lecture." *Ecology* 73(6) (1992): 1943–1967. DOI: 10.2307/1941447. https://doi.org/10.2307/1941447

**[R31] Anderson, P. W.** "More Is Different: Broken Symmetry and the Nature of the Hierarchical Structure of Science." *Science* 177(4047) (1972): 393–396. DOI: 10.1126/science.177.4047.393. https://doi.org/10.1126/science.177.4047.393

**[R32] Wilson, Kenneth G.; Kogut, John.** "The Renormalization Group and the Epsilon Expansion." *Physics Reports* 12(2) (1974): 75–199. DOI: 10.1016/0370-1573(74)90023-4. https://doi.org/10.1016/0370-1573(74)90023-4

**[R33] Royal Swedish Academy of Sciences.** "The Nobel Prize in Physics 2022" — experiments with entangled photons, violation of Bell inequalities, and quantum information science. Nobel Prize Outreach, 4 October 2022. https://www.nobelprize.org/prizes/physics/2022/press-release/

**[R34] O'Neill, Robert V.; DeAngelis, Donald L.; Waide, J. B.; Allen, Timothy F. H.** *A Hierarchical Concept of Ecosystems.* Princeton University Press, 1986. https://www.jstor.org/stable/j.ctv1sfsf8d

---

## The extension in one passage

The buoy is still there.

At first it was a reference. Then it was noisy. Then it drifted. Then its drift helped expose a current. The current changed the route. The route approached a shoal. The shoal made additional soundings worthwhile. The crew sometimes idled rather than deleting uncertain routes. Another vessel appeared and communication revealed that threat, intent, constraint, and identity were not the same variable. Fog made outside guidance useful. The charted channels and known machinery made later searches finite enough to navigate, and every broken route taught the map something new. Weather made the return route relevant. The logbook made the next day's corrections possible.

None of those story objects became technical definitions.

The technical model remained a model of elements, states, relations, boundaries, viability, environment, evidence, uncertainty, future projections, intervention, preservation, generative conditions, patience, communication, freedom of choice, structural navigation, route memory, guidance, and revision.

That is the purpose of the story: not to rename the model, but to keep enough of the world continuous that hidden assumptions have somewhere to reveal themselves.

And that is the purpose of Compass: not to eliminate uncertainty, but to make the **question, evidence, model, boundary, present environment, uncertainty, preserved alternatives, mapped routes, coexistence possibilities, preservation conditions, guidance, and next justified step visible at the same time**.

---

## Signature

**Nikita Beregovykh & ChatGPT 5.6 Sol, Observers Notes extension 1**
