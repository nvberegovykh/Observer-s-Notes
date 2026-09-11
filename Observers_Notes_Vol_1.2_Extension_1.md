# Observer's Notes — Vol. 1.2

## Extension 1 — Interestingness as Projected Reachable Future Structure

**Status:** working extension; intentionally not formatted as a book chapter yet.

This note extends the local operational model of *Observer's Notes*. It does not propose a universal law of curiosity, intelligence, value, or decision-making. It proposes a way to locate what is worth examining next inside a declared model without trying to enumerate every possible future.

The central idea is simple:

> **An element is interesting when, under stated local assumptions, it materially changes a broad and structured set of reachable futures, especially when those futures remain distributed across materially different outcome priorities and when unresolved structure at their boundaries may still contain discoverable alternatives.**

The word *interesting* is descriptive here, not normative. A dangerous system can be highly interesting. A safe and desirable system can be boring. Interest identifies where additional observation, modeling, or refinement may change understanding. It does not grant permission to intervene.

---

## 1. Localize before measuring

Interestingness is not treated as an intrinsic property of an object.

It is measured relative to a local model:

\[
M=(B,S_0,A,H,\Pi,C)
\]

where:

- \(B\) is the selected system boundary;
- \(S_0\) is the present state description;
- \(A\) is the declared set of assumptions;
- \(H\) is the time or process horizon;
- \(\Pi\) is the set of projections used to compress possible futures;
- \(C\) is the set of hard constraints, viability conditions, or rules that must remain visible during analysis.

This follows the earlier Notes: an element is selected for a question, a state description is built for a purpose, a structure exists at a stated scale and interval, and an observer remains inside the modeling process rather than outside it.

Change the boundary, assumptions, scale, horizon, or projection and the measured interestingness may change.

A stone may be uninteresting in a pedestrian routing model, important in a structural failure model, and extremely interesting in a geological model. None of those descriptions has to be false. They answer different local questions.

---

## 2. The unoptimized definition

Let \(x\) be an element inside the model. Let

\[
F_M(x)
\]

represent the set of futures reachable from the present state under model \(M\), while accounting for the role of \(x\).

The naive definition would ask how many futures are possible and how different they are.

That fails quickly.

Even a small real system can have an effectively uncountable or combinatorially explosive future space. Most branches differ in details that do not matter to the present question. Explicitly enumerating them wastes computation and can make the model less grounded by encouraging invented distinctions unsupported by observation.

Therefore the useful object is not the full future tree.

The useful object is a set of **projections of the future tree**.

---

## 3. Projection instead of enumeration

For each decision-relevant dimension \(j\), define a projection

\[
\pi_j:F_M(x)\rightarrow Y_j
\]

that maps complex futures onto a smaller observable or evaluative space.

Examples of projection axes include:

- probability or severity of structural failure;
- energy demand;
- cost;
- time;
- maintainability;
- ecological impact;
- safety margin;
- explanatory power of a hypothesis;
- reversibility of an action;
- compliance;
- or a local success-to-failure priority scale.

The first approximation does not need a fine distribution. It can be an interval:

\[
P_j(F_M(x))=[a_j,b_j]
\]

or, when disconnected regions matter, a union of intervals:

\[
P_j(F_M(x))=I_{j1}\cup I_{j2}\cup\dots\cup I_{jn}.
\]

This is the primary optimization: **compress futures into bounded projected regions and refine only where the compression is no longer sufficient for the question.**

---

## 4. The priority projection

One especially useful projection is an ordered priority scale:

\[
u\in[-1,1]
\]

where the exact meaning of the endpoints must be declared locally. For example:

- \(-1\): predictably unsuccessful under the selected objective;
- \(0\): neutral, indeterminate, or locally equivalent;
- \(+1\): predictably successful under the selected objective.

The scale is not universal utility. It is a local ordering for the current question.

Divide the scale into \(K\) intervals. Estimate how reachable futures occupy those intervals.

If probability estimates are justified, let \(p_k\) be the estimated mass in interval \(k\). If probabilities are not justified, use support, bounded weights, or occupancy ranges instead of pretending to know more than the evidence supports.

A normalized distribution measure can be written as

\[
E=\frac{-\sum_{k=1}^{K}p_k\log p_k}{\log K}
\]

when the \(p_k\) values are meaningful.

\(E\) approaches 0 when almost all represented futures collapse into one priority region and approaches 1 when represented futures are broadly distributed across the declared scale.

This does **not** mean that an even mixture of catastrophe and success is desirable. It means the element sits at a point where materially different outcomes remain reachable and therefore deserves more attention if the question is to understand or control the system.

Interestingness is not goodness.

---

## 5. Width is not enough

Two projected future sets may share the same outer interval while having completely different internal structure.

For example:

```text
A:  |████████████████████████████|
    -1                           +1

B:  |██                        ██|
    -1                           +1
```

Both have the same outer range. In A, reachable futures occupy much of the interval. In B, they cluster around two extremes.

Therefore every useful projection should retain, at minimum:

1. **range** — how far the reachable region extends;
2. **occupancy** — where support actually exists inside that range;
3. **distribution** — how concentrated or balanced the support is when weights are defensible;
4. **grounding status** — which portions come from measurement, constraints, models, assumptions, or unresolved territory.

A convenient representation is:

\[
P_j=\left(I_j,O_j,Q_j\right)
\]

where \(I_j\) is the interval structure, \(O_j\) is occupancy or distribution information, and \(Q_j\) is provenance and confidence information.

---

## 6. Causal leverage is the missing filter

Raw uncertainty is not enough.

A noise source can generate enormous apparent future variety while changing nothing important around it. Another element may have only a few reachable states but reorganize the future of the whole system.

Therefore the element should be measured by how much changing, fixing, removing, or perturbing it changes the projected future regions.

For projection \(j\), define a local leverage term \(L_j(x)\) as a normalized measure of change between projected futures under materially different admissible states of \(x\):

\[
L_j(x)\propto D\left(P_j(F_M\mid x=x_1),P_j(F_M\mid x=x_0)\right)
\]

where \(D\) may be an interval distance, distribution distance, threshold crossing, change in reachable support, or another domain-appropriate sensitivity measure.

The exact metric is local. The requirement is not.

> **An element should not receive a high interestingness score merely because the future around it is uncertain. It should matter to the future structure being measured.**

---

## 7. Uncertain discovery without rewarding ignorance

Unmodeled possibilities matter, but ignorance must not be mistaken for evidence of hidden richness.

The unresolved frontier \(N_j\) should therefore be increased only by identifiable reasons to believe the current projection may be incomplete, such as:

- disagreement between materially different models;
- repeated residuals between prediction and observation;
- open system boundaries with known incoming dependencies;
- sensitivity to an unresolved parameter;
- observations that repeatedly approach or exceed the current interval boundary;
- a known mechanism whose state space is not yet resolved;
- or evidence of missing relations between already observed elements.

"We do not know" alone is not enough.

Unknown territory is represented as uncertainty in the measure rather than automatically as a larger central score.

For that reason, the output should preferably be an interval:

\[
\mathcal I(x)=[\mathcal I^-(x),\mathcal I^+(x)]
\]

rather than a falsely precise point value.

A wide interestingness interval means that the present model does not yet justify a precise ranking. That uncertainty itself can become a reason to refine the model, but it remains distinct from the estimated interestingness of the element.

---

## 8. A working measure

For each projection \(j\), define bounded terms:

- \(R_j\): normalized reachable range or occupied support width;
- \(E_j\): distribution breadth across the selected priority or state intervals;
- \(L_j\): causal leverage of element \(x\) on that projection;
- \(N_j\): evidence-backed unresolved frontier;
- \(w_j\): declared importance of projection \(j\) to the local question.

A first working form is:

\[
\mathcal I(x)
=
\sum_j w_j L_j\left(\alpha R_j+\beta E_j+\gamma N_j\right)
\]

with

\[
\sum_j w_j=1
\]

and \(\alpha,\beta,\gamma\) declared before comparison where practical.

Every term should carry uncertainty bounds when the underlying data do.

This formula is deliberately provisional. Its role is to make the assumptions visible enough to test. In many applications the individual terms or their interactions will need replacement.

The invariant idea is more important than this particular equation:

> **interestingness increases when an element has leverage over a broad, internally structured, materially consequential, and not-yet-collapsed reachable future region.**

---

## 9. Interval projection as an optimization method

The model should begin coarse.

Suppose the priority projection initially gives:

\[
[-1,+1].
\]

Do not immediately subdivide it into hundreds of states.

Refine only where additional resolution can change understanding or action:

```text
[-1,-0.5]  [-0.5,0]  [0,0.4]  [0.4,0.7]  [0.7,1]
```

A projected cell should receive more attention when it combines several of the following:

- high leverage;
- large unresolved width;
- proximity to a viability, legal, safety, or performance threshold;
- disagreement between independent models;
- steep change in priority across the interval;
- high occupancy;
- an observation near or outside the predicted boundary;
- or low refinement cost relative to expected information gain.

A useful refinement priority is conceptually:

\[
\rho_k
\propto
\frac{
L_k\,U_k\,G_k\,D_k
}{C_k}
\]

where:

- \(L_k\) is leverage;
- \(U_k\) is unresolved interval width;
- \(G_k\) is consequence or decision gradient across the cell;
- \(D_k\) is evidence conflict or model disagreement;
- \(C_k\) is the estimated cost of refinement.

Again, the equation is a sketch, not a law. Its purpose is to enforce selective resolution.

Stop refining when one of these becomes true:

1. further subdivision does not change the decision or ranking;
2. the uncertainty is below the resolution required by the question;
3. the cost of refinement exceeds the value of the expected information;
4. the model reaches an external uncertainty that cannot presently be resolved;
5. or a hard viability constraint makes deeper exploration operationally irrelevant.

The loop is therefore:

> **project → bound → compare → refine only the consequential interval → test → compress again.**

This is closer to adaptive meshing than exhaustive branching.

---

## 10. Sketching is part of the method

A sketch is not decoration and does not need to be visually polished.

It is a temporary external representation of the local model.

A useful sketch may contain only:

- selected elements;
- realized or suspected relations;
- arrows showing dependency or influence;
- projected intervals;
- hard constraints;
- observed values;
- model-derived values;
- unresolved boundaries;
- and the next region selected for refinement.

The sketch should remain cheap enough to redraw.

That is important because the first model is expected to be wrong in detail.

The workflow is:

> **sketch → ground → test → refine → simplify → sketch again.**

The purpose of refinement is not to make the representation more complicated. It is to make the necessary part more precise while allowing irrelevant detail to remain compressed.

A mature model may therefore look simpler than an immature one.

---

## 11. Grounding rules

Every projected interval should make clear why it exists.

A practical provenance vocabulary is:

- **[MEASURED]** — derived directly from observation or test data;
- **[CONSTRAINT]** — bounded by physical, legal, geometric, logical, or operational limits;
- **[MODEL]** — produced by a declared simulation, equation, or predictive model;
- **[ASSUMPTION]** — introduced to make the current model solvable;
- **[INFERRED]** — supported indirectly by relations among observations;
- **[OPEN]** — unresolved boundary with evidence that the modeled support may extend beyond the current region.

For consequential use:

1. declare boundary, scale, assumptions, and horizon before interpreting the score;
2. choose projection axes before inspecting outcomes where possible;
3. tie interval bounds to observations, physical constraints, or named models;
4. compare at least one materially different measurement or modeling method when feasible;
5. test sensitivity to projection choice, binning, weights, and interval width;
6. record realized outcomes and compare them with the predicted projected region;
7. revise the model when observations repeatedly fall outside the declared bounds;
8. do not widen intervals after the fact merely to preserve the original model;
9. keep aleatory variation, model uncertainty, and missing knowledge distinct when the distinction matters;
10. do not report more numerical precision than the grounding supports.

A disagreement between two grounded methods is information. It should be localized, not averaged away automatically.

---

## 12. Complex systems: interest does not override viability

The most interesting branch may be the branch that should never be executed.

Analysis and intervention therefore remain separate.

A high \(\mathcal I(x)\) can justify:

- observing;
- simulating;
- checking assumptions;
- collecting measurements;
- comparing models;
- or designing a reversible test.

It does not by itself justify crossing a safety, legal, ecological, continuity, access, or recoverability boundary.

The earlier viability logic remains primary for action:

> **first preserve the conditions required for the system and the observer to continue; then explore inside the remaining admissible space.**

Interestingness helps allocate attention inside that space.

---

## 13. Worked application — a building control decision

Consider a building with heat pumps, ventilation, occupancy variation, envelope losses, electrical limits, maintenance constraints, and code requirements.

Let the element \(x\) be a proposed ventilation-control strategy.

A brute-force future tree would include enormous combinations of:

- weather;
- occupancy;
- equipment states;
- control timings;
- sensor errors;
- utility conditions;
- maintenance events;
- and occupant behavior.

Instead define projections:

\[
\Pi=
\{E,IAQ,C,M,R\}
\]

where:

- \(E\): annual and peak energy demand;
- \(IAQ\): indoor-air-quality performance;
- \(C\): cost;
- \(M\): maintenance burden;
- \(R\): failure or compliance risk.

Begin with grounded interval envelopes for each.

If the proposed control strategy barely changes energy use and cost but strongly changes the IAQ and failure-risk intervals, then \(L_{IAQ}\) and \(L_R\) dominate. Those projections receive refinement.

If two independent ventilation models disagree only under low-temperature/high-occupancy conditions, the model should not refine the entire annual state space. It should subdivide the projected region associated with that condition.

If the disagreement straddles a required ventilation or safety threshold, refinement priority rises sharply.

If further simulation shows both models remaining safely on the same side of the threshold, additional detail may no longer change the decision and can remain compressed.

The interesting element was not the one with the largest raw number of possible states. It was the one whose variation reorganized the consequential reachable intervals.

---

## 14. What this gives a human observer

For a human, the method reduces the requirement to hold a whole branching system in working memory.

It provides a disciplined way to externalize:

- what is assumed;
- what is observed;
- what may happen;
- which parts matter;
- where uncertainty remains;
- and what deserves the next unit of attention.

The projection prevents irrelevant detail from competing equally with consequential structure.

The intervals prevent false precision.

The sketch makes hidden assumptions easier to notice.

The refinement loop allows understanding to become precise locally without requiring the entire model to become equally detailed.

This is useful not only for solving a problem but for seeing where the problem actually is.

---

## 15. What this gives an AI system when organized correctly

An AI system faces a related scaling problem.

If every plausible branch is expanded as text, token use and model complexity grow rapidly while provenance becomes harder to preserve. Unsupported branches can begin to look equivalent to grounded ones simply because both have been represented in language.

A better external organization is to maintain a compact model state containing:

- declared assumptions;
- selected elements and dependencies;
- projection axes;
- interval bounds;
- evidence provenance;
- confidence or uncertainty ranges;
- viability gates;
- unresolved frontier markers;
- and explicit refinement targets.

This does not require exposing or preserving private chain-of-thought. It is an **auditable external state representation**, similar to a model, table, graph, simulation state, or engineering worksheet.

Used correctly, it can help an AI system:

- avoid expanding low-value branches;
- separate evidence from assumption;
- preserve continuity across long tasks;
- share a compact state between specialized agents or tools;
- detect when two models disagree;
- spend computation where a decision is actually sensitive;
- and return from detailed analysis to a simpler global representation.

The same loop applies:

> **localize → sketch externally → project → bound → ground → refine selectively → validate → compress.**

The gain is not that the AI becomes omniscient. The gain is that limited computational attention is distributed according to the structure of the problem rather than the surface quantity of possible text branches.

---

## 16. Research and discovery

The same method can be used when the system under study is not an engineered object but a research question.

Let \(x\) be a hypothesis, experiment, measurement, or unexplained observation.

Possible projections may include:

- explanatory power;
- falsifiability;
- experimental cost;
- compatibility with existing evidence;
- number of competing mechanisms eliminated;
- safety or ethical limits;
- transferability to other domains;
- and remaining unexplained residuals.

A hypothesis becomes especially interesting when testing it can reorganize several projected regions at once.

An observation becomes especially interesting when it sits near the boundary of multiple grounded models and the models predict materially different continuations.

A discovery frontier is therefore not simply the place with the least knowledge.

It is the place where **additional grounded information has high leverage over the map of reachable explanations or actions**.

---

## 17. A compact operational procedure

For practical use:

1. **Select the local system.** State boundary, present state, scale, horizon, and purpose.
2. **Declare assumptions and hard constraints.** Keep viability limits separate from preferences.
3. **Select the element \(x\).** Ask what changes if it changes.
4. **Choose projections.** Use only dimensions that can change understanding or action.
5. **Create coarse intervals.** Do not enumerate detailed futures yet.
6. **Record occupancy and provenance.** Distinguish measured, modeled, assumed, constrained, and open regions.
7. **Estimate leverage.** Compare projected futures under meaningful variations of \(x\).
8. **Map the priority distribution.** Check whether futures collapse into one region or remain broadly distributed across materially different outcomes.
9. **Mark evidence-backed open boundaries.** Unknown is not automatically interesting.
10. **Compute or qualitatively rank interestingness with uncertainty bounds.** Avoid fake precision.
11. **Refine only consequential intervals.** Favor threshold crossings, disagreement, leverage, and low-cost information gain.
12. **Validate with a materially different method where feasible.** Preserve disagreements.
13. **Compare realized outcomes with the projected regions.** Update the model rather than protecting it.
14. **Compress again.** Keep only the resolution still required by the question.

---

## 18. Current boundary of the idea

Several parts remain intentionally open:

- the best distance measure for causal leverage depends on domain;
- the correct projection axes are observer- and task-dependent;
- probability distributions are often unjustified and must not be invented;
- interaction between projections may matter more than their weighted sum;
- novelty and model disagreement require domain-specific calibration;
- and a scalar interestingness score may sometimes destroy useful structure.

For many problems, the most faithful output may therefore remain a vector or interval map rather than one number.

The measure should become scalar only when the purpose requires ranking.

This is not a weakness of the method. It is part of the grounding requirement.

---

## 19. The extension in one line

> **Interestingness is the locally grounded degree to which an element has causal leverage over a broad, structured, materially differentiated reachable future space; projection into intervals makes that future space tractable, and selective refinement spends attention only where additional resolution can change understanding or action.**

That definition is useful only while its assumptions remain visible.

---

**Nikita Beregovykh & ChatGPT 5.6 Sol, Observers Notes extension 1**
