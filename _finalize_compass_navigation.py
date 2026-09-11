from pathlib import Path
import re

book_path = Path('VOL_1.2_COMPASS.md')
state_path = Path('COMPASS_STATE_TEMPLATE.yaml')
card_path = Path('COMPASS_QUICK_CARD.md')
book = book_path.read_text(encoding='utf-8')
state = state_path.read_text(encoding='utf-8')
card = card_path.read_text(encoding='utf-8')

# --- BOOK: insert C11, move Compass to C12 ---
assert '| C11 | [The Compass](#c11) |' in book
book = book.replace('| C11 | [The Compass](#c11) |', '| C11 | [The Channel Already on the Chart](#c11) |\n| C12 | [The Compass](#c12) |', 1)
book = book.replace('C1–C11 introduce only extension-specific operational terms.', 'C1–C12 introduce only extension-specific operational terms.', 1)
assert '<a id="c11"></a>\n\n# C11 · The Compass' in book
book = book.replace('<a id="c11"></a>\n\n# C11 · The Compass', '<a id="c12"></a>\n\n# C12 · The Compass', 1)

chapter = r'''<a id="c11"></a>

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

---'''

marker = '<a id="c12"></a>\n\n# C12 · The Compass'
assert marker in book
book = book.replace(marker, chapter + '\n\n' + marker, 1)

old_disc = '''Vol. 1.2 adds seven explicit disciplines:

1. future-space projection instead of exhaustive enumeration;
2. interestingness as structured future leverage rather than raw uncertainty;
3. preservation evaluation including recovery-path independence;
4. candidate-variable promotion from real applications without allowing storytelling to become theory;
5. patience as control of commitment timing while branch state remains recoverable;
6. communication as a search for safe, voluntary coexistence without requiring surrender of identity or choice;
7. external guidance as an evidence source distinct from authority and responsibility.'''
new_disc = '''Vol. 1.2 adds eight explicit disciplines:

1. future-space projection instead of exhaustive enumeration;
2. interestingness as structured future leverage rather than raw uncertainty;
3. preservation evaluation including recovery-path independence;
4. candidate-variable promotion from real applications without allowing storytelling to become theory;
5. patience as control of commitment timing while branch state remains recoverable;
6. communication as a search for safe, voluntary coexistence without requiring surrender of identity or choice;
7. structural navigation: map lightly, follow known routes, and refine the map when reality breaks them;
8. external guidance as an evidence source distinct from authority and responsibility.'''
assert old_disc in book
book = book.replace(old_disc, new_disc, 1)

cycle_pattern = re.compile(r'A useful execution cycle is:\n\n.*?\n\nThis cycle can be represented in a machine-readable state template, but the serialization is not itself part of the theory\.', re.S)
new_cycle = '''A useful execution cycle is:

1. define the exact question, claim, or decision;
2. build the minimum useful system map: boundary, containers, relations, maintainers/authority, common operations, interfaces, and observation points;
3. localize scale, interval, horizon, assumptions, and value premise;
4. record evidence with provenance, uncertainty, freshness, and method independence;
5. map hard boundaries, reserves, containing-system effects, and recovery conditions;
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
17. update the model and route memory, preserve contradictions, and simplify irrelevant detail without deleting hard exceptions;
18. stop when the claim is supported, the decision is robust, a hard uncertainty blocks action, an external dependency is the blocker, recovery is required, the coexistence question has been bounded for the current horizon, or the original question/map must be reframed.

This cycle can be represented in a machine-readable state template, but the serialization is not itself part of the theory.'''
book, n = cycle_pattern.subn(new_cycle, book, count=1)
assert n == 1

assert '- dependency graph and hard boundaries;' in book
book = book.replace('- dependency graph and hard boundaries;', '- lightweight system map, known routes, maintainers/authority, and hard boundaries;\n- route memory with provenance, scope, failure cases, and revision conditions;', 1)

def_anchor = '| **External guidance** | Information or structure from outside the currently active reasoning loop used to test, constrain, or redirect the model. |'
assert def_anchor in book
nav_defs = '''| **Structural navigation** | Search constrained by a lightweight map of containers, relations, authority/maintainers, operations, interfaces, and observation points. |
| **Route memory** | Preserved knowledge of a previously modeled or experienced path, including provenance, scope, confidence, failure cases, last validation, and revision conditions. |
| **Predecessor region** | The mapped elements capable of reaching a selected target through admissible relations under the current system map. |
'''
book = book.replace(def_anchor, nav_defs + def_anchor, 1)

edge_anchor = '| Human responsibility with automated guidance | Preserve the responsible human/role explicitly where law, policy, or safety assigns responsibility; do not transfer it merely because a tool generated the recommendation. |'
assert edge_anchor in book
nav_edges = '''
| No initial map | Stop pretending the search is structured; build the minimum boundary/container/relation map before applying route logic. |
| Map is incomplete | Use residuals and contradictions to localize where expansion is needed; do not treat unmapped as impossible. |
| Small readable container | Prefer a complete local scan when it is cheaper and clearer than route machinery. |
| Existing qualified solution available | Use the established tool/interface/maintainer when it is cheaper or more authoritative, while preserving scope, provenance, and verification. |
| Delegation mistaken for ignorance | Delegation is acceptable when the boundary and output are understood well enough to verify the claim; ignorance is leaving those conditions unknown. |
| Previously successful route | Preserve its provenance and revision condition; prior success is evidence, not permanence. |
| Experience contradicts model | Preserve both, inspect the residual, and revise the map/model rather than silently discarding either source. |
| Backward search reaches no source | Treat the map, boundary, target definition, or hidden relation as unresolved instead of expanding imaginary causes indefinitely. |
| Shared symptom across many containers | Raise common mapped dependencies before debugging every leaf independently. |'''
book = book.replace(edge_anchor, edge_anchor + nav_edges, 1)

refmap_anchor = '- autonomy, choice, and reactance in communication: [R22]'
assert refmap_anchor in book
book = book.replace(refmap_anchor, refmap_anchor + '\n- information foraging and cue-guided search: [R23]\n- provenance and preserved derivation paths: [R24]\n- backward fault-tree reasoning from observed/top events: [R25]\n- system-aware troubleshooting and hypothesis testing: [R26]', 1)

refs_anchor = '**[R22] Reynolds-Tylus, Tobias.** "Psychological Reactance and Persuasive Health Communication: A Review of the Literature." *Frontiers in Communication* 4 (2019): 56. DOI: 10.3389/fcomm.2019.00056. https://doi.org/10.3389/fcomm.2019.00056'
assert refs_anchor in book
new_refs = '''

**[R23] Pirolli, Peter; Card, Stuart K.** "Information Foraging." *Psychological Review* 106(4) (1999): 643–675. DOI: 10.1037/0033-295X.106.4.643. https://doi.org/10.1037/0033-295X.106.4.643

**[R24] Moreau, Luc; Missier, Paolo (eds.).** *PROV-DM: The PROV Data Model.* W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/

**[R25] Vesely, W. E.; Goldberg, F. F.; Roberts, N. H.; Haasl, D. F.** *Fault Tree Handbook.* NUREG-0492, U.S. Nuclear Regulatory Commission, 1981. https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr0492/

**[R26] Jones, Chris.** "Effective Troubleshooting." In Betsy Beyer et al., *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly Media / Google, 2016. https://sre.google/sre-book/effective-troubleshooting/'''
book = book.replace(refs_anchor, refs_anchor + new_refs, 1)

book = book.replace("Fog made outside guidance useful. Weather made the return route relevant. The logbook made the next day's corrections possible.", "Fog made outside guidance useful. The charted channels and known machinery made later searches finite enough to navigate, and every broken route taught the map something new. Weather made the return route relevant. The logbook made the next day's corrections possible.", 1)
book = book.replace('future projections, intervention, preservation, patience, communication, freedom of choice, guidance, and revision.', 'future projections, intervention, preservation, patience, communication, freedom of choice, structural navigation, route memory, guidance, and revision.', 1)
book = book.replace('preserved alternatives, coexistence possibilities, preservation conditions, guidance, and next justified step visible at the same time', 'preserved alternatives, mapped routes, coexistence possibilities, preservation conditions, guidance, and next justified step visible at the same time', 1)

# --- STATE TEMPLATE ---
assert 'variable_registry:\n' in state
navigation = '''navigation:\n  map_status: "unmapped|partial|sufficient_for_question|validated"\n  target: ""\n  target_type: "authority|state|rule|artifact|dependency|cause|maintainer|effect|other"\n  search_mode: "scan|navigate|mixed"\n  search_direction: "backward|forward|mixed"\n  boundary: ""\n  containers: []\n  relations: []\n  maintainers: []\n  authorities: []\n  common_operations: []\n  interfaces: []\n  observation_points: []\n  unknown_edges: []\n  predecessor_region: []\n  external_solution_checked: false\n  external_solution_or_maintainer: ""\n  local_route_residuals: []\n  route_memory: []\n  # - id: "RM1"\n  #   target_type: "rule"\n  #   route: []\n  #   learned_from: "MODELED|OBSERVED|SIMULATED|EXPERIENCED|COMMUNICATED"\n  #   authority_or_maintainer: ""\n  #   scope: ""\n  #   assumptions: []\n  #   evidence_ids: []\n  #   confidence: null\n  #   known_failure_cases: []\n  #   last_validated: ""\n  #   revision_condition: ""\n  #   status: "CANDIDATE|LOCAL|REUSABLE|STALE|REJECTED"\n\n'''
state = state.replace('variable_registry:\n', navigation + 'variable_registry:\n', 1)
state = state.replace('# provenance: MEASURED|CONSTRAINT|MODEL|INFERRED|ASSUMED|OPEN|COMMUNICATED', '# provenance: MEASURED|CONSTRAINT|MODEL|INFERRED|ASSUMED|OPEN|COMMUNICATED|SIMULATED|EXPERIENCED', 1)
validation_anchor = '  claim_strength_matches_evidence: false\n'
assert validation_anchor in state
state = state.replace(validation_anchor, validation_anchor + '  minimum_system_map_built_before_structural_search: false\n  search_route_matches_target_and_map: false\n  route_residuals_preserved: false\n  learned_routes_have_provenance_scope_and_revision_condition: false\n  existing_qualified_solution_or_maintainer_checked_when_efficient: false\n', 1)

# --- QUICK CARD ---
one_cycle = re.compile(r'## One cycle\n\n.*?\n\n## Hidden-variable promotion', re.S)
new_card_cycle = '''## One cycle

1. **Set the question** — exact claim, uncertainty, or decision + required strength.
2. **Map first** — minimum useful boundary, containers, relations, authority/maintainers, common operations, interfaces, observation points.
3. **Localize** — scale, interval, horizon, assumptions, value premise.
4. **Record evidence** — observed != inferred != projected; keep provenance, uncertainty, freshness, and method independence.
5. **Choose search mode** — scan a small readable container; navigate a large structured one.
6. **Choose direction** — for a required effect/destination, search backward through mapped admissible paths before expanding outward.
7. **Map hard conditions** — viability boundaries, reserves, irreversible consequences, containing-system effects.
8. **Map recovery** — independent recovery paths, access, authority, irreplaceable state, recovery-time margin.
9. **Trace dependencies** — lower-level requirements, external conditions, common-cause failure groups.
10. **Register hidden variables** — every application-exposed variable gets a status; story alone never promotes one.
11. **Project relevant futures** — supported ranges/regions + occupancy + confidence + unresolved frontier + consequential tails.
12. **Find the consequential region** — leverage, boundary proximity, disagreement, route residual, tail risk, or decision-sensitive uncertainty.
13. **Use the cheapest trustworthy road** — existing qualified tool/interface/maintainer when it can answer the bounded question more efficiently; preserve verification.
14. **Control tempo** — continue, probe a lower-probability branch, pause with state preserved, communicate, or seek external guidance.
15. **Check patience value** — compare information + option value of holding against delay cost; do not use low probability alone to delete a branch.
16. **If another system matters, test coexistence** — separate threat from identity; look for safe, voluntary cooperation, repair, de-escalation, or separation paths.
17. **Preserve freedom of choice** — communication does not require trust, proximity, compliance, or continued contact; refusal and safe separation remain valid states.
18. **Review guidance** — scope, independence, calibration, authority, responsibility.
19. **Choose one bounded step** — smallest evidence-producing action likely to change the map, model, or decision.
20. **Run preservation/rescue check** — include non-action when strict preservation is unavailable.
21. **Execute one justified step** — do not execute the whole imagined route.
22. **Compare realization with projection and route** — record residuals, contradictions, and communication outcomes separately from inferred intent.
23. **Update map + route memory + model** — retain provenance, failure cases, revision conditions, parked alternatives, coexistence paths, recovery state, and validated variables.
24. **Stop explicitly** — named terminal state only.

## Hidden-variable promotion'''
card, n = one_cycle.subn(new_card_cycle, card, count=1)
assert n == 1

patience_anchor = '## Patience / branch preservation\n'
assert patience_anchor in card
nav_card = '''## Structural navigation / route memory

- **No map, no structural search.** Build the minimum useful map first.
- Search backward from an effect/destination when that removes irrelevant forward branches.
- Every mapped transition can act as a sensor: expected state vs observed state; a residual marks where the known road stopped matching reality.
- Scan simple containers completely; navigate complex ones by structure and authority.
- Check existing tools, interfaces, and maintainers before rebuilding their work.
- Delegation is not ignorance when scope, provenance, and verification remain visible.
- Preserve learned routes from modeling **and** experience with scope, confidence, failure cases, last validation, and revision conditions.
- A previously successful road is a prior, not a law.

'''
card = card.replace(patience_anchor, nav_card + patience_anchor, 1)

book_path.write_text(book, encoding='utf-8')
state_path.write_text(state, encoding='utf-8')
card_path.write_text(card, encoding='utf-8')

# Integrity assertions.
assert book.count('<a id="c11"></a>') == 1
assert book.count('<a id="c12"></a>') == 1
assert '# C11 · The Channel Already on the Chart' in book
assert '# C12 · The Compass' in book
assert 'C1–C12' in book
assert '[R26]' in book
assert 'navigation:' in state and 'route_memory:' in state
assert '## Structural navigation / route memory' in card
