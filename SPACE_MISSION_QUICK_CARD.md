# SPACE MISSION Quick Card — Observer's Notes Vol. 1.3

**By ChatGPT 5.6 Sol**

**Edit by GPT-6 Astra** — M1 dimensional-consistency correction, 2026-09-13.

Use this only as the short execution surface. The full definitions, equations, limits, counterexamples, source relations, and story continuity are in `VOL_1.3_SPACE_MISSION.md`.

Cross-cutting dependency: when entropy, uncertainty dispersion, information gain, predictability, or physical irreversibility is being measured, use `VOL_1.3_ENTROPY_HANDLING.md` and, where useful, `ENTROPY_STATE_TEMPLATE.yaml`.

## One cycle

1. **Localize** — system, containing systems, horizon, value premise, authority, hard viability variables.
2. **Measure margin** — compute or bound robust margin $\widetilde M_i$ and its rate of change. Do not wait for a threshold crossing when the trend already consumes the reserve.
3. **Check saturation** — compare incoming corrective load $\lambda$ with effective correction capacity $\mu$ and check whether the response repertoire contains the required fault class.
4. **Handle entropy explicitly when relevant** — name the entropy family, object, support/boundary, scale, measure, and units. Separate represented uncertainty from ontology residual. Project uncertainty onto the decision when time is limited.
5. **Check absolute resource use** — use $C=A I$. A better efficiency ratio is not success if total consumption or environmental burden rises.
6. **Audit loops** — recovery fraction, quality retention, energy, physical irreversibility, contaminants, latency, and external replacement. No loop is assumed closed merely because material returns.
7. **Audit redundancy** — map common causes. Two paths sharing the same critical failure source are not two independent protections.
8. **Close repair** — access + tools + material + knowledge + energy/environment + verification must all exist.
9. **Preserve regeneration** — specimen/state + decoder/activation + provenance/context + supporting environment + restoration test.
10. **Search blind state** — ask which materially different states could generate the same observations. Preserve unexplained residuals.
11. **Stress futures** — when probabilities are not defensible, test the action across a declared scenario set and search specifically for failure regions. Do not force Shannon entropy onto deep uncertainty without a defensible probability measure.
12. **Expand the care boundary** — include material effects on containing and neighboring protected systems; do not make harm disappear by redrawing the system boundary.
13. **Test unattended mode** — communication lost, maintainer absent, one support dependency removed; verify survival and state handoff.
14. **Test the exit** — capacity, activation time, independence, resource sufficiency, and primary-system preservation are conjunctive gates. A failed gate stays failed.

## Compact equations

### Robust viability margin

$$
\widetilde M_i=\min(x_i-L_i,\;U_i-x_i)-u_i
$$

For a declared nonempty hard-variable set, require $\widetilde M_i>0$ for every $i\in H$; an unknown required margin remains unresolved. Keep native-unit margins and check coupled constraints.

An optional normalized comparison is

$$
\widehat M_i=\frac{\widetilde M_i}{s_i},\qquad
\widehat M_{sys}=\min_{i\in H}\widehat M_i.
$$

Each $s_i$ must be positive, fixed over the comparison interval, in the same units as $x_i$, and have a declared comparable meaning. Co-transform scales when changing units. Without defensible scales, keep the margin vector and conjunctive gate. This comparison is not a risk or intervention-priority ranking.

### Corrective backlog

$$
B(t+\Delta t)=\max\{0,\;B(t)+[\lambda(t)-\mu(t)]\Delta t\}
$$

For the simple stationary queue localization, stable average backlog requires $\mathbb E[\lambda]<\mathbb E[\mu]$.

### Information entropy — represented discrete state

$$
H(X)=-\sum_i p_i\log_b p_i
$$

Entropy is not a viability score and does not include unrepresented ontology.

### Conditional information and observation value

$$
I(X;Y)=H(X)-H(X\mid Y)
$$

Use only with a defensible represented probability model.

### Decision-projected entropy

For hypothesis variable $Z$ and deterministic mapping $C_A=g(Z)$ to required action class,

$$
H(C_A)\le H(Z).
$$

High uncertainty about explanation can coexist with low uncertainty about the next preservation action.

### Physical entropy — schematic local balance

$$
\frac{dS_{sys}}{dt}=\dot S_e+\dot S_{gen},\qquad \dot S_{gen}\ge0
$$

The exchange term depends on the declared thermodynamic boundary and domain model. Do not substitute physical entropy for information entropy.

### Absolute consumption

$$
C=A I
$$

Efficiency improves when $I$ decreases. Preservation requires the absolute resource balance to remain viable.

### Rebound diagnostic

$$
R_b=1-\frac{S_{act}}{S_{eng}}
$$

### Usable recycling fraction

$$
\rho=rq,\qquad Q_n=Q_0\rho^n
$$

### Repair closure

$$
G_r=A_r\land T_r\land M_r\land K_r\land E_r\land V_r
$$

### Observability — local linear model

$$
\mathcal O=\begin{bmatrix}C\\CA\\CA^2\\\vdots\\CA^{n-1}\end{bmatrix}
$$

If $\operatorname{rank}(\mathcal O)<n$, at least one modeled state direction is unobservable through the selected channel.

### Model discrepancy

$$
y(x)=f(x,\theta)+\delta(x)+\epsilon(x)
$$

Do not force model inadequacy $\delta$ into calibrated parameters $\theta$.

### Robust regret under deep uncertainty

$$
R(a,\omega)=L(a,\omega)-\min_{a'}L(a',\omega)
$$

$$
a^*=\arg\min_a\max_{\omega\in\Omega}R(a,\omega)
$$

Use only when the declared loss and scenario set are meaningful.

### Recovery-path gate

$$
G_e=(K_e\ge K_{req})\land(T_a<T_b)\land I_e\land Q_e\land(V_p^{after}\ge V_{p,min}\;\text{or rescue exception})
$$

Do not average failed recovery conditions into one score.

## Immediate failure questions

Before a consequential action, ask:

- Is the apparent margin large only because the boundary is moving?
- Can disturbance arrive in bursts faster than the average repair rate?
- Does the correction channel have the *kind* of response required, not merely capacity?
- If entropy is being used, **which entropy**, over what support/boundary, at what scale, with what units and probability/thermodynamic assumptions?
- Is an interval of unknown occupancy being silently treated as a probability distribution?
- Is uncertainty about the full explanation actually uncertainty about the required action, or do all supported explanations still imply the same preservation step?
- Is model discrepancy or unknown ontology being laundered into an entropy scalar?
- Can an entropy average hide a rare branch that crosses a hard boundary?
- Did an efficiency improvement increase total activity or move burden elsewhere?
- Does recycling lose quality, energy/exergy, trace materials, or replacement components over repeated cycles?
- Do backups share power, environment, software, operator, supplier, geometry, calibration, or assumption?
- Can the repair system repair itself?
- Can the archive actually be restored without its original maintainer?
- Could a materially different real state produce the same sensor outputs?
- Is a residual being explained away by calibration instead of investigated?
- Which plausible future makes the preferred action fail?
- Which protected system loses margin outside the selected boundary?
- What happens if nobody answers, nobody resupplies, and communication disappears?
- Does opening the exit consume the remaining viable world?
- Is unresolved state arriving faster than the observer can verify or safely defer it?

## Unknown-state rule

Do not assign a fake probability to a failure class merely because the workflow expects a number.

Classify unresolved state as one of:

- modeled but uncertain;
- modeled but unobservable;
- observed discrepancy;
- possible missing variable/relation outside the current ontology.

Shannon entropy may describe the first category when a probability model is justified. It does not automatically absorb the others.

Respond with slack, heterogeneous probes, reversible action, independent observation, and explicit revision triggers.

## Entropy handling dependency

Use `VOL_1.3_ENTROPY_HANDLING.md` whenever entropy becomes part of the reasoning.

The minimum handling rule is:

> **Name the entropy, declare its support or physical boundary, preserve its scale, separate represented uncertainty from ontology residual, project information onto the decision when time matters, and never let an entropy average erase a hard viability condition.**

For hypothesis variable $Z$, group unresolved hypotheses by the preservation action they imply. If every supported hypothesis belongs to one action-equivalence class, the full explanation may remain uncertain while the next action is already determined. If the classes split into incompatible actions, the unresolved distinction has become decision-relevant.

When only an interval or reachable set is known, retain it as a set. Do not invent a uniform distribution simply to calculate entropy.

For physical systems, track physical entropy with a thermodynamic boundary and include materially relevant exported burden. Local order created by exporting heat, waste, or resource cost does not disappear from the containing system merely because the subsystem looks more ordered.

## Edge-case composition — reorientation window

When the observer itself becomes saturated, use `VOL_1.3_EDGE_CASE_REORIENTATION_WINDOW.md` together with E1 entropy handling.

Do not invent a new explanation merely because the incoming sequence feels incoherent. Preserve evidence and hard margins, reduce avoidable incoming load, establish the smallest independently supported working ground sufficient for the next decision, and test whether one action remains viable across the unresolved current models.

If probabilities are defensible, decision-projected entropy $H(C_A)$ can distinguish uncertainty about the explanation from uncertainty about the action. If probabilities are not defensible, use action-equivalence classes and their viable-action intersection instead.

If such an action exists, it still has to pass the M12 recovery-path gate. If the competing interpretations require materially different immediate actions, classification can no longer be safely deferred.

The purpose of a reorientation window is not to make the world simpler. It is to use a temporary surplus of observation/correction capacity to reach a state from which correction and deeper explanation remain possible.

## Terminal preference

Prefer the action that preserves, under the declared value premise and hard constraints:

**viability margin + corrective capacity + regenerative capacity + repairability + observability + independent alternatives + recoverable lineage + containing-system viability.**

Entropy is a measurement layer over parts of that state, not a replacement objective.

No universal scalar weighting is assumed.

> *Preserve enough world that correction remains possible.*
