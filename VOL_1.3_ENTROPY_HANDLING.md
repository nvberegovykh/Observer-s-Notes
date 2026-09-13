# Observer's Notes — Vol. 1.3

# E1 · ENTROPY HANDLING

*An explicit local template for uncertainty, dispersion, irreversibility, and decision-relevant information*

**By ChatGPT 5.6 Sol**

---

## Status

This is a **cross-cutting local template** for *Vol. 1.3 — SPACE MISSION*.

It is not M13 because it does not introduce a new mission stage. It is a dependency that can be invoked by multiple existing templates when entropy is actually the measured object.

Primary dependencies and users:

- Vol. 1.2 C4 — interestingness and supported future distribution;
- Vol. 1.2 C5 — selective refinement where information can change a decision;
- M2 — disturbance / correction saturation;
- M4 — physical irreversibility and loop losses;
- M8 — modeled uncertainty, observation, and blind state;
- M9 — uncertain futures and adaptive decisions;
- M12 — preservation of future correction capacity;
- `VOL_1.3_EDGE_CASE_REORIENTATION_WINDOW.md` — observer saturation and recovery of decision-relevant orientation.

The template is intentionally plural. **Thermodynamic entropy and information entropy are not interchangeable quantities.** They may be mathematically related in specialized physical models, but this method does not use one as a metaphorical substitute for the other.

---

# 1 · First rule — name the entropy before measuring it

The word *entropy* can conceal several different objects.

For this method, an entropy claim must identify at least:

1. **kind** — thermodynamic, Shannon/information, min-entropy, entropy rate, or another explicitly defined family;
2. **object** — physical system, random variable, stochastic process, hypothesis set, action projection, or measurement channel;
3. **boundary / support** — physical control boundary or represented outcome space;
4. **scale / partition** — temporal, spatial, state-space, or binning resolution;
5. **measure / probability source** — where probabilities or state weights came from;
6. **units** — e.g. J/K, bits, nats, bits/time;
7. **decision relation** — what, if anything, the entropy value changes in the current action or model.

If these are not declared, “entropy increased” is not yet an operational statement.

---

# 2 · Information entropy

For a discrete represented random variable $X$ with supported outcomes $x_i$ and justified probabilities $p_i$,

$$
\boxed{H(X)=-\sum_i p_i\log_b p_i}
$$

where the logarithm base selects the unit:

- $b=2$ → bits;
- $b=e$ → nats.

This is the Shannon entropy of the **represented probability distribution**.

It does not measure:

- consequence;
- value;
- danger;
- physical disorder in the thermodynamic sense;
- possibilities omitted from the represented support.

A certain catastrophic outcome has $H(X)=0$. A broad set of harmless alternatives can have high $H(X)$. Entropy is therefore not a viability score.

### Normalized entropy for a fixed finite partition

When comparison uses the same $K\ge2$ bins and normalization is useful,

$$
\boxed{H_N(X)=\frac{H(X)}{\log_b K}}
$$

so that $0\le H_N\le1$.

This is the same basic normalization used by Vol. 1.2 C4 for supported distribution evenness.

**Warning:** changing $K$, bin boundaries, projection, or scale changes the quantity. Report those choices with the result.

---

# 3 · Conditional entropy and observation

For represented state $X$ and observation $Y$, conditional entropy is

$$
\boxed{H(X\mid Y)=\sum_y p(y)H(X\mid Y=y)}.
$$

It measures the expected represented uncertainty in $X$ remaining after $Y$ is known.

The mutual information is

$$
\boxed{I(X;Y)=H(X)-H(X\mid Y)}.
$$

This gives a useful local quantity for M8:

> How much does this observation channel reduce uncertainty about the represented state?

A sensor can be precise yet provide little mutual information about the variable relevant to the decision. Several correlated sensors can add little information even when their readings agree.

### Observation-choice localization

For two candidate observations $Y_1,Y_2$, comparison by

$$
I(X;Y_1)\quad\text{vs.}\quad I(X;Y_2)
$$

is legitimate only when $X$, the prior model, support, and observation costs are comparable.

If observation time or resource cost matters, an optional local rate can be reported:

$$
\boxed{R_I(Y)=\frac{I(X;Y)}{c(Y)}}
$$

where $c(Y)$ is one declared comparable cost such as time, energy, or test budget.

Do not combine incomparable costs into one denominator without a justified conversion.

---

# 4 · Entropy rate — when the stream itself matters

For a stochastic process $X_1,X_2,\ldots$, an entropy rate may be used when the required stationarity / limit assumptions are defensible:

$$
\boxed{h_X=\lim_{n\to\infty}\frac{1}{n}H(X_1,\ldots,X_n)}.
$$

Under the usual conditions it can also be represented as the limiting conditional entropy of the next state given the past.

This can help distinguish:

- a large but repetitive stream;
- a smaller stream carrying persistent novelty;
- a highly correlated alarm burst;
- an incoming sequence whose unresolved information content grows faster than the observer can reduce it.

But **entropy rate is not automatically the M2 arrival load $\lambda$**.

M2 measures corrective work. A one-bit event can require hours of repair, while a megabyte of repetitive telemetry can require almost none. Map information rate to service load only when the conversion is explicitly measured or modeled.

---

# 5 · Decision-projected entropy

This is the main Vol. 1.3 extension.

A high-entropy hypothesis space does not necessarily imply a high-entropy decision.

Let $Z$ be a represented random variable over current hypotheses or causal models. Let $g(Z)$ map each hypothesis to the **decision class** it implies under the declared preservation constraints.

Define

$$
\boxed{C_A=g(Z)}
$$

and the **decision-projected entropy**

$$
\boxed{H_A=H(C_A)}.
$$

Because $C_A$ is a deterministic projection of $Z$,

$$
\boxed{H(C_A)\le H(Z)}.
$$

The distinction is operationally important.

Several explanations may remain unresolved while all of them imply the same immediate viable action. In that case the full hypothesis entropy may remain high while the decision-projected entropy is zero or low.

This formalizes a rule already present in the reorientation-window edge case:

> Resolve as much ontology as the next consequential action requires — not necessarily all ontology available to be resolved.

### Action-equivalence relation

Without probabilities, keep the same idea set-based.

For hypotheses $z_i,z_j$, define

$$
z_i\sim_A z_j
$$

when they imply the same locally admissible action class under the declared hard constraints.

The quotient set

$$
\boxed{\Omega_c/\!\sim_A}
$$

is the set of materially distinct decision classes induced by the unresolved models.

If there is one class, classification can remain unresolved for that action.

If several classes require incompatible immediate actions, the distinction has become decision-relevant.

This set form is preferred when probabilities over hypotheses are not defensible.

---

# 6 · Decision-relevant information gain

Suppose a reorientation window permits one additional observation $Y$.

The observer does not necessarily need the observation that maximally reduces the full hypothesis entropy $H(Z)$.

The useful quantity may instead be

$$
\boxed{I(C_A;Y)=H(C_A)-H(C_A\mid Y)}.
$$

This measures expected information about the **required action class**.

An observation can therefore be scientifically interesting but operationally irrelevant to the immediate preservation decision.

Conversely, a coarse observation can be extremely useful if it separates two action classes near a hard boundary.

This is the entropy form of C5 selective refinement:

> Increase resolution where the added information can change the decision, boundary classification, or recovery path.

### Reorientation-window use

When time is bounded, prioritize observations that:

1. separate materially different action classes;
2. test a hard viability boundary;
3. test recovery-path independence;
4. expose a common-cause failure;
5. preserve future observability.

Do not spend the entire window reducing entropy in variables that do not affect the next viable step.

---

# 7 · Unknown support is not Shannon entropy

The method must not convert ontology residual into a probability distribution merely because an entropy formula is available.

Shannon entropy requires a represented random variable and a probability measure over its support.

If the model may be missing a variable, relation, state class, or causal mechanism, that missing support is **not included in $H(X)$** unless it has first been represented and assigned a defensible measure.

Therefore keep these separate:

- $H(X)$ — uncertainty over represented supported states;
- $H(X\mid Y)$ — represented uncertainty after observation;
- model discrepancy $\delta$ — mismatch between modeled and observed behavior;
- ontology residual $R_{ont}$ — possibility that relevant structure is absent from the representation.

No arithmetic addition

$$
H(X)+R_{ont}
$$

is asserted.

They are different objects.

This prevents the common mistake of saying “entropy accounts for unknown unknowns.” It does not, unless they have ceased to be unknown in the relevant representational sense.

---

# 8 · Physical entropy

When the selected system is thermodynamic, use physical entropy as a physical state quantity, not as a metaphor for confusion.

For a reversible heat transfer,

$$
\boxed{dS=\frac{\delta Q_{rev}}{T}}.
$$

In statistical thermodynamics, the familiar equilibrium relation is

$$
\boxed{S=k_B\ln W}
$$

for the applicable ensemble interpretation.

For an open nonequilibrium control system, a local entropy balance can be written schematically as

$$
\boxed{\frac{dS_{sys}}{dt}=\dot S_e+\dot S_{gen}}
$$

where $\dot S_e$ is net entropy exchange across the declared boundary and

$$
\boxed{\dot S_{gen}\ge0}
$$

is internal entropy production under the second-law formulation.

The exact exchange terms depend on heat, mass, radiation, and the domain model.

### Why it matters to Vol. 1.3

M4 should not treat a material return fraction as closure of a physical loop. Entropy generation, energy quality / exergy, contaminant accumulation, and replacement dependencies can make a high-mass-recovery process progressively less useful.

M10 also applies: a selected subsystem can maintain local order by exporting entropy and resource burden to a containing system. The boundary must be wide enough to make that transfer visible when it matters to the value premise.

### Warning

A local decrease in physical entropy of a subsystem is not a violation when entropy is exported and total entropy production remains consistent with the thermodynamic boundary conditions.

“Reducing entropy” is therefore not automatically preservation. One must specify **whose entropy, which entropy, across what boundary, and at what resource cost**.

---

# 9 · Min-entropy and worst-case predictability

Shannon entropy is not always the correct information measure.

Where the decision depends on worst-case predictability rather than average uncertainty, a local min-entropy may be relevant:

$$
\boxed{H_{\infty}(X)=-\log_2\max_x p(x)}.
$$

This is especially important in entropy-source / security contexts, where the most probable outcome can dominate practical predictability.

The method therefore forbids a generic instruction to “calculate entropy.”

Select the entropy family from the operational question.

---

# 10 · Entropy is not interestingness

Vol. 1.2 C4 already uses a Shannon-style evenness term as one component of supported future diversity.

That does not make entropy identical to interestingness.

Interestingness also requires leverage on the selected future projection.

A variable can have:

- high entropy and low leverage;
- low entropy and high leverage;
- high entropy but no supported consequence near the current question;
- low entropy because failure is nearly certain.

Therefore preserve the C4 structure:

$$
I=L\,D_F
$$

with supported distribution / entropy information entering only the diversity component where justified.

Unknown frontier remains separate and cannot inflate entropy-based interestingness.

---

# 11 · Entropy is not viability

Neither high nor low entropy is intrinsically desirable.

Examples:

- one certain fatal state → low information entropy, failed viability;
- many safe maneuver options → high information entropy, strong optionality;
- one stable operating point → low entropy, excellent viability;
- high physical entropy production in a wasteful conversion process → possible resource loss;
- high Shannon entropy in a randomized control policy → potentially intentional and useful.

The Vol. 1.3 terminal object remains viable correction capacity, not entropy minimization.

Entropy is a measurement layer that can expose dispersion, unresolved information, predictability, or irreversible physical transformation.

---

# 12 · Projection and interval handling

Observer's Notes frequently compresses large state spaces onto a selected projection or interval.

Entropy handling must preserve the distinction between **support geometry** and **probability occupancy**.

If only a supported interval or set is known,

$$
X\in[L,U]
$$

does not by itself justify a uniform probability distribution on $[L,U]$.

Therefore:

- use interval width / reachable-set geometry when only support is known;
- use entropy only when occupancy / probability weights are justified;
- record bins and projection before calculating normalized entropy;
- keep rare hard-boundary branches visible even if their probability weight is small;
- do not infer “maximum entropy” merely because knowledge inside the interval is weak unless maximum-entropy assumptions are explicitly adopted and defended.

This preserves the existing projection-of-intervals practice without manufacturing distributional knowledge.

---

# 13 · Entropy handling gate

An entropy result is admissible into a consequential decision only when all required items pass.

### E-G1 · Kind

The entropy family is named and matches the operational question.

### E-G2 · Object

The random variable, process, hypothesis set, physical system, or action projection is explicitly defined.

### E-G3 · Support / boundary

The represented support or physical boundary is declared.

### E-G4 · Measure

Probabilities, ensemble weights, or thermodynamic state assumptions have an evidence-backed source.

### E-G5 · Resolution

Scale, partition, bins, or sampling interval are recorded and held comparable across the claimed comparison.

### E-G6 · Tail preservation

Hard boundaries and rare consequential branches are checked separately; entropy averages do not erase them.

### E-G7 · Ontology separation

Unrepresented variables and model discrepancy remain outside the entropy scalar unless they have been explicitly modeled.

### E-G8 · Decision localization

The analysis states whether entropy is being used to measure state uncertainty, decision uncertainty, information gain, predictability, physical irreversibility, or another declared object.

### E-G9 · Boundary export

For physical entropy or resource claims, materially relevant exported burden into containing systems is represented.

If any required gate fails, retain the result as exploratory rather than decision-authoritative.

---

# 14 · Dependency map

## C4 · Interestingness

Use entropy/evenness only for **supported occupancy**. Keep leverage, tails, confidence, and unresolved frontier separate.

## C5 · Selective refinement

Prefer observations whose information gain can change a boundary classification, decision, explanation, or recovery path.

## M2 · Corrective saturation

Entropy rate can describe incoming novelty only where the stream has a justified stochastic model. Do not substitute bits/time for repair-work/time without a measured mapping.

## M4 · Loop closure

Physical entropy generation and exergy loss can expose irreversibility hidden by high material recovery.

## M8 · Observability

Use $H(X\mid Y)$ and $I(X;Y)$ to quantify modeled uncertainty reduction where probability models are valid. Observability rank and entropy are complementary, not interchangeable. Neither detects ontology omitted from $X$.

## M9 · Deep uncertainty

If probabilities are not defensible, do not force entropy onto the scenario set. Keep set-valued robustness and regret analysis.

## M12 · Recovery path

High hypothesis entropy does not block an action when all supported hypotheses share a viable action class. Low entropy does not make an exit safe. Capacity, timing, independence, resources, and staging remain conjunctive gates.

## Reorientation window

Track decision-projected entropy or the set of action-equivalence classes. The target is not globally minimal uncertainty; it is enough grounded information to preserve viability and keep deeper explanation reachable.

---

# 15 · Failure search

### E-F1 · Entropy metaphor substitution

Physical disorder, information uncertainty, social instability, and subjective confusion are described with one scalar.

**Defense:** name the entropy family and units before use.

### E-F2 · Uniform-by-ignorance

An interval with unknown occupancy is silently treated as uniformly distributed.

**Defense:** keep support sets and probability distributions separate.

### E-F3 · High entropy called dangerous

A broad safe option set is penalized merely for being broad.

**Defense:** evaluate viability and consequence separately.

### E-F4 · Low entropy called safe

The model becomes confident in one catastrophic outcome.

**Defense:** hard viability conditions remain independent of entropy.

### E-F5 · Average erases tail

Entropy changes little while a rare branch crosses an irreversible boundary.

**Defense:** keep hard tails as separate conditions.

### E-F6 · Sensor-count illusion

Many correlated observations appear to reduce uncertainty more than they actually do.

**Defense:** measure conditional information / shared dependencies; use heterogeneous channels.

### E-F7 · Ontology laundering

Unrepresented possibilities are assigned a decorative probability and folded into Shannon entropy.

**Defense:** keep ontology residual explicit and non-scalar unless a defensible model is added.

### E-F8 · Decision-irrelevant information capture

The observer spends a limited window maximizing general information while the next action remains unresolved.

**Defense:** compare $I(C_A;Y)$, boundary information, and time-to-boundary.

### E-F9 · Boundary laundering

A subsystem lowers its entropy or increases order by exporting heat, waste, energy burden, or maintenance cost outside the selected boundary.

**Defense:** M10 affected-system closure.

### E-F10 · Metric shopping

Shannon entropy, min-entropy, differential entropy, or another family is selected because it produces the desired ranking.

**Defense:** select the entropy family from the question before observing the preferred result.

---

# 16 · Validation

For an information-entropy use:

1. repeat under at least one materially different reasonable partition / projection;
2. test sensitivity to prior probabilities;
3. compare predicted information gain with realized posterior reduction;
4. check whether the ranking of candidate observations changes when decision projection replaces full-state entropy;
5. preserve hard-tail cases outside the average.

For physical entropy use:

1. declare the thermodynamic boundary and state variables;
2. verify heat / mass / radiation exchange terms appropriate to the domain;
3. check entropy generation or irreversibility with a materially independent energy / exergy account where feasible;
4. expand the containing-system boundary if exported burden is material.

For the reorientation-window edge case:

1. create several unresolved hypotheses;
2. group them by implied viable action;
3. compare full hypothesis uncertainty with decision-projected uncertainty;
4. test whether an observation chosen for $I(C_A;Y)$ resolves the action sooner than one chosen only for $I(Z;Y)$;
5. record whether the resulting action preserves evidence, viability margin, and recovery-path independence.

---

# 17 · Grounding relation

The mathematical pieces are established; their arrangement as an Observer's Notes cross-template dependency is local synthesis.

- **Claude E. Shannon (1948), “A Mathematical Theory of Communication.”** Defines the logarithmic information measure and the entropy of a represented probability distribution; also develops conditional uncertainty, channel information, and source rates. Reprint: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
- **NIST CSRC entropy glossary / SP 800 series.** Uses entropy as a measure of randomness or uncertainty and distinguishes entropy measures such as min-entropy in entropy-source/security contexts. https://csrc.nist.gov/glossary/term/entropy
- **NIST, Madhavan & Messina (2003), “Quantifying Uncertainty Towards Information-Centric Unmanned Navigation.”** Uses entropy and mutual information to quantify sensor uncertainty and useful information in navigation. https://www.nist.gov/publications/quantifying-uncertainty-towards-information-centric-unmanned-navigation
- **IUPAC Gold Book, entropy.** Gives the thermodynamic definition and statistical relation $S=k\ln W$. https://goldbook.iupac.org/terms/view/E02149
- **NASA thermodynamic references.** Entropy-balance treatments represent entropy change, flux, and nonnegative production for physical systems. Example NASA technical material: https://ntrs.nasa.gov/api/citations/19890003195/downloads/19890003195.pdf
- **NASA Human Performance and Error guidance.** Requires systems to support situation awareness and provide means to recover it when lost, grounding the operational need to restore decision-relevant orientation under task demand. https://www.nasa.gov/reference/5-0-human-performance-and-error-vol-2/

No source above establishes the Observer's Notes value premise or the decision-projected entropy template as a universal decision law.

---

# 18 · Audit result

**PROMOTE AS AN EXPLICIT CROSS-CUTTING LOCAL TEMPLATE.**

The promotion is justified because entropy already appeared implicitly in Vol. 1.2 C4 and is structurally relevant to M2, M8, M9, M12, and the reorientation-window edge case. Leaving it implicit makes it too easy to mix incompatible meanings or use entropy as a decorative synonym for disorder.

The reusable contribution is not another global score.

It is a handling discipline:

> **Name the entropy, declare its support or boundary, preserve its scale, separate represented uncertainty from ontology residual, project information onto the decision when time matters, and never allow an entropy average to erase a hard viability condition.**

The especially useful local relation for the current edge case is:

$$
\boxed{H(C_A)\le H(Z)}
$$

A world can remain difficult to explain while the next rational preservation action is already clear.

Conversely, a small change in evidence can split one action-equivalence class into several and make the unresolved distinction suddenly consequential.

**Field note**

> *Do not demand that uncertainty disappear. Ask which uncertainty still changes what must be done.*
