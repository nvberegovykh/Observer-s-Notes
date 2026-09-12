# SPACE MISSION Quick Card — Observer's Notes Vol. 1.3

**By ChatGPT 5.6 Sol**

Use this only as the short execution surface. The full definitions, equations, limits, counterexamples, source relations, and story continuity are in `VOL_1.3_SPACE_MISSION.md`.

## One cycle

1. **Localize** — system, containing systems, horizon, value premise, authority, hard viability variables.
2. **Measure margin** — compute or bound robust margin $\widetilde M_i$ and its rate of change. Do not wait for a threshold crossing when the trend already consumes the reserve.
3. **Check saturation** — compare incoming corrective load $\lambda$ with effective correction capacity $\mu$ and check whether the response repertoire contains the required fault class.
4. **Check absolute resource use** — use $C=A I$. A better efficiency ratio is not success if total consumption or environmental burden rises.
5. **Audit loops** — recovery fraction, quality retention, energy, contaminants, latency, and external replacement. No loop is assumed closed merely because material returns.
6. **Audit redundancy** — map common causes. Two paths sharing the same critical failure source are not two independent protections.
7. **Close repair** — access + tools + material + knowledge + energy/environment + verification must all exist.
8. **Preserve regeneration** — specimen/state + decoder/activation + provenance/context + supporting environment + restoration test.
9. **Search blind state** — ask which materially different states could generate the same observations. Preserve unexplained residuals.
10. **Stress futures** — when probabilities are not defensible, test the action across a declared scenario set and search specifically for failure regions.
11. **Expand the care boundary** — include material effects on containing and neighboring protected systems; do not make harm disappear by redrawing the system boundary.
12. **Test unattended mode** — communication lost, maintainer absent, one support dependency removed; verify survival and state handoff.
13. **Test the exit** — capacity, activation time, independence, resource sufficiency, and primary-system preservation are conjunctive gates. A failed gate stays failed.

## Compact equations

### Robust viability margin

$$
\widetilde M_i=\min(x_i-L_i,\;U_i-x_i)-u_i
$$

$$
\widetilde M_{sys}=\min_{i\in H}\widetilde M_i
$$

### Corrective backlog

$$
B(t+\Delta t)=\max\{0,\;B(t)+[\lambda(t)-\mu(t)]\Delta t\}
$$

For the simple stationary queue localization, stable average backlog requires $\mathbb E[\lambda]<\mathbb E[\mu]$.

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
- Did an efficiency improvement increase total activity or move burden elsewhere?
- Does recycling lose quality, energy, trace materials, or replacement components over repeated cycles?
- Do backups share power, environment, software, operator, supplier, geometry, calibration, or assumption?
- Can the repair system repair itself?
- Can the archive actually be restored without its original maintainer?
- Could a materially different real state produce the same sensor outputs?
- Is a residual being explained away by calibration instead of investigated?
- Which plausible future makes the preferred action fail?
- Which protected system loses margin outside the selected boundary?
- What happens if nobody answers, nobody resupplies, and communication disappears?
- Does opening the exit consume the remaining viable world?

## Unknown-state rule

Do not assign a fake probability to a failure class merely because the workflow expects a number.

Classify unresolved state as one of:

- modeled but uncertain;
- modeled but unobservable;
- observed discrepancy;
- possible missing variable/relation outside the current ontology.

Respond with slack, heterogeneous probes, reversible action, independent observation, and explicit revision triggers.

## Terminal preference

Prefer the action that preserves, under the declared value premise and hard constraints:

**viability margin + corrective capacity + regenerative capacity + repairability + observability + independent alternatives + recoverable lineage + containing-system viability.**

No universal scalar weighting is assumed.

> *Preserve enough world that correction remains possible.*
