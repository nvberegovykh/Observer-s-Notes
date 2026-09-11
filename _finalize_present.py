from pathlib import Path

book_path = Path('VOL_1.2_COMPASS.md')
state_path = Path('COMPASS_STATE_TEMPLATE.yaml')
card_path = Path('COMPASS_QUICK_CARD.md')
book = book_path.read_text(encoding='utf-8')
state = state_path.read_text(encoding='utf-8')
card = card_path.read_text(encoding='utf-8')

def rep(text, old, new, label):
    if old not in text:
        raise RuntimeError(f'missing marker: {label}')
    return text.replace(old, new, 1)

anchor = "Preservation also changes with horizon. An action can preserve the next minute and destroy the next day. A temporary controlled loss can also be acceptable if it belongs to an explicit recovery path that preserves the higher-level system.\n\n### Field note"
insert = r'''Preservation also changes with horizon. An action can preserve the next minute and destroy the next day. A temporary controlled loss can also be acceptable if it belongs to an explicit recovery path that preserves the higher-level system.

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

### Field note'''
book = rep(book, anchor, insert, 'C3 present environment')

book = rep(book, "- Check lower-level and containing-system dependencies.\n- A recovery path must survive the failure it is intended to recover from.", "- Check lower-level and containing-system dependencies.\n- Treat relevant environmental conditions as part of the present system state, not only future optionality.\n- Preserve or regenerate the material, energy, information, and relational conditions that support current viable activity where they matter to the value premise.\n- A recovery path must survive the failure it is intended to recover from.", 'C3 carry forward')
book = rep(book, "4. Check common-cause failure and recovery-path independence.\n5. Check at least one containing system when material externalities are plausible.\n6. If no candidate action, including non-action, satisfies the hard conditions, classify the problem as rescue / least-loss rather than strict preservation.", "4. Check common-cause failure and recovery-path independence.\n5. Check at least one containing system when material externalities are plausible, including present environmental support and capability loss.\n6. If no candidate action, including non-action, satisfies the hard conditions, classify the problem as rescue / least-loss rather than strict preservation.", 'C3 operational use')

book = rep(book, "3. preservation evaluation including recovery-path independence;", "3. preservation evaluation including present environmental capability, generative conditions, and recovery-path independence;", 'C12 discipline 3')
book = rep(book, "5. map hard boundaries, reserves, containing-system effects, and recovery conditions;", "5. map hard boundaries, reserves, present environmental support, containing-system effects, and recovery conditions;", 'C12 cycle step 5')
book = rep(book, "17. update the model and route memory, preserve contradictions, and simplify irrelevant detail without deleting hard exceptions;", "17. update the model, environmental state, and route memory, preserve contradictions, and simplify irrelevant detail without deleting hard exceptions;", 'C12 cycle step 17')

marker = "### Field note\n\n> *The compass is useful because the map can be wrong.*"
closing = r'''### The water we are already in

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

> *The compass is useful because the map can be wrong.*'''
book = rep(book, marker, closing, 'C12 water we are in')

book = rep(book, "- recovery state;\n- external guidance and its independence;", "- present environmental support, containing-system externalities, and generative conditions;\n- recovery state;\n- external guidance and its independence;", 'AI state list')
book = rep(book, "- Communication preserves possibility when it remains safe and voluntary; it does not require trust or exposure.\n- External guidance can be non-human; responsibility and authority remain separate.", "- Communication preserves possibility when it remains safe and voluntary; it does not require trust or exposure.\n- Future optionality does not erase present environmental loss; report both.\n- Preserve or regenerate the conditions that support current viable activity and future generation rather than freezing one present arrangement.\n- External guidance can be non-human; responsibility and authority remain separate.", 'C12 carry forward environment')

def_anchor = "| **Predecessor region** | The mapped elements capable of reaching a selected target through admissible relations under the current system map. |"
book = rep(book, def_anchor, def_anchor + "\n| **Present capability set** | The selected set of actions, interactions, experiences, or creations that remain viable and reachable now under the modeled environmental conditions. |", 'present capability definition')

edge_anchor = "| Shared symptom across many containers | Raise common mapped dependencies before debugging every leaf independently. |"
edge_insert = '''| Future optionality used to hide present loss | Report contraction of current viable activity separately; a promised future does not cancel a present environmental cost. |
| One subsystem preserved by degrading its containing environment | Expand the boundary and include externalities before calling the result preservation. |
| More present options assumed automatically better | Do not maximize raw capability count; value premise, hard constraints, and harm still govern admissibility. |
| Environment frozen in the name of preservation | Preserve/regenerate supporting conditions and viable relations, not every current arrangement; adaptation can be part of preservation. |
| Cultural or technical output becomes environmental input | Preserve provenance and maintenance/revision conditions where relevant; inheritance does not imply the output is beneficial. |'''
book = rep(book, edge_anchor, edge_anchor + "\n" + edge_insert, 'environment edge cases')

map_anchor = "- system-aware troubleshooting and hypothesis testing: [R26]"
book = rep(book, map_anchor, map_anchor + "\n- organisms modifying environments and evolutionary feedback: [R27]\n- ecosystem conditions and present human well-being: [R28]", 'reference map R27 R28')
ref_anchor = "**[R26] Jones, Chris.** \"Effective Troubleshooting.\" In Betsy Beyer et al., *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly Media / Google, 2016. https://sre.google/sre-book/effective-troubleshooting/"
refs = '''**[R27] Odling-Smee, F. John; Laland, Kevin N.; Feldman, Marcus W.** *Niche Construction: The Neglected Process in Evolution.* Princeton University Press, 2003. https://www.jstor.org/stable/j.ctt24hqpd

**[R28] Millennium Ecosystem Assessment.** *Ecosystems and Human Well-being: Synthesis.* Island Press, 2005. https://www.unep.org/resources/report/ecosystem-and-human-well-being-synthesis'''
book = rep(book, ref_anchor, ref_anchor + "\n\n" + refs, 'references R27 R28')

book = rep(book, "The technical model remained a model of elements, states, relations, boundaries, viability, evidence, uncertainty, future projections, intervention, preservation, patience, communication, freedom of choice, structural navigation, route memory, guidance, and revision.", "The technical model remained a model of elements, states, relations, boundaries, viability, environment, evidence, uncertainty, future projections, intervention, preservation, generative conditions, patience, communication, freedom of choice, structural navigation, route memory, guidance, and revision.", 'final passage model list')
book = rep(book, "And that is the purpose of Compass: not to eliminate uncertainty, but to make the **question, evidence, model, boundary, uncertainty, preserved alternatives, mapped routes, coexistence possibilities, preservation conditions, guidance, and next justified step visible at the same time**.", "And that is the purpose of Compass: not to eliminate uncertainty, but to make the **question, evidence, model, boundary, present environment, uncertainty, preserved alternatives, mapped routes, coexistence possibilities, preservation conditions, guidance, and next justified step visible at the same time**.", 'final Compass purpose')

env_marker = "preservation:\n"
env_block = '''environment:
  selected_environment: ""
  current_support_conditions: []
  material_energy_information_flows: []
  present_capabilities_supported: []
  generative_conditions: []
  containing_system_externalities: []
  outputs_becoming_environmental_inputs: []
  degradation_signals: []
  regeneration_paths: []

'''
state = rep(state, env_marker, env_block + env_marker, 'state environment block')
state = rep(state, '  #   preservation_effect: ""\n  #   freedom_of_choice_effect: ""', '  #   preservation_effect: ""\n  #   present_environment_effect: ""\n  #   freedom_of_choice_effect: ""', 'candidate step environment effect')
state = rep(state, '  guidance_used: []\n  realized_outcome: ""', '  guidance_used: []\n  present_capabilities_added_or_lost: []\n  environmental_conditions_changed: []\n  realized_outcome: ""', 'logbook environment changes')
val_anchor = "  recovery_path_independence_checked: false\n"
val_insert = "  present_environment_support_checked: false\n  present_capability_loss_reported_when_material: false\n  containing_environment_externalities_checked: false\n  generative_conditions_checked_when_relevant: false\n  future_optionality_not_used_to_hide_present_loss: false\n"
state = rep(state, val_anchor, val_insert + val_anchor, 'validation environment checks')

card = rep(card, "7. **Map hard conditions** — viability boundaries, reserves, irreversible consequences, containing-system effects.", "7. **Map hard conditions** — viability boundaries, present environmental support, reserves, irreversible consequences, containing-system effects.", 'quick card step 7')
card = rep(card, "23. **Update map + route memory + model** — retain provenance, failure cases, revision conditions, parked alternatives, coexistence paths, recovery state, and validated variables.", "23. **Update map + environment + route memory + model** — retain provenance, present capability changes, failure cases, revision conditions, parked alternatives, coexistence paths, recovery state, and validated variables.", 'quick card step 23')
section_marker = "## Patience / branch preservation\n"
env_section = '''## Present environment / generative capacity

- Environment is part of the current state-space, not only a future concern.
- Ask what viable activity is reachable **now** because the selected conditions exist.
- Track material, energy, information, relational, and containing-system dependencies when they matter.
- Do not preserve one subsystem by silently collapsing the conditions supporting the larger system.
- Future optionality does not cancel present capability loss; report both.
- Preserve/regenerate supporting conditions rather than freezing every current arrangement.
- Outputs can become environmental inputs for later systems; inheritance needs provenance and revision, not automatic approval.

'''
card = rep(card, section_marker, env_section + section_marker, 'quick card environment section')
card = rep(card, "> The strength of the claim must not exceed the strength of the evidence, model, preserved alternatives, and ability to correct course.", "> The strength of the claim must not exceed the strength of the evidence, model, preserved alternatives, and ability to correct course.\n>\n> Preserve the conditions that make viable activity, correction, communication, and generation possible now—not only later.", 'quick card core invariant')

book_path.write_text(book, encoding='utf-8')
state_path.write_text(state, encoding='utf-8')
card_path.write_text(card, encoding='utf-8')

checks = [
    ('### The present environment' in book, 'book present environment'),
    ('### The water we are already in' in book, 'book closing environment'),
    ('[R27]' in book and '[R28]' in book, 'book references'),
    ('present_capabilities_supported:' in state, 'state environment'),
    ('future_optionality_not_used_to_hide_present_loss:' in state, 'state validation'),
    ('## Present environment / generative capacity' in card, 'card environment'),
]
for ok, label in checks:
    if not ok:
        raise RuntimeError(f'failed sanity check: {label}')
