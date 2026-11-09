# Flux Point: Zimu — rules captured so far

This document records the supplied game notes. It distinguishes stated rules from
details that still need clarification; card ability text is not necessarily an
implemented effect.

## Latest registry intake

The complete numbered ledger has now been received. The registry is exactly 100
profiles: 20 shared Common Core cards, 38 Deck 1 exclusives (#021–#058), 38
Deck 2 exclusives (#059–#096), and 4 Binder Reserves (#097–#100). The Python
registry preserves this order and assigns those IDs in `CARD_REGISTRY_IDS`.

## Match and turn

- Each player starts at 40 Life Points (LP). A player loses when their LP reaches
  0. Redline activates at 10 LP or less.
- Each turn has four phases:
  1. **Draw:** Draw one card, choosing from the Combatant, Relic, or Tactic pile.
  2. **Deployment:** Play at most one Zimu from hand to an empty Vanguard slot;
     activate Relics and cast Surge Tactics.
  3. **Clash:** Declare lane attacks, allow defender counter-traps, then resolve
     combat.
  4. **End:** Resolve cleanup, reset turn-limited effects, and discard until the
     hand is at most eight cards.
- The notes describe a pre-game eight-card paid Mulligan: banish the opening
  hand face-down, lose 5 LP, and redraw four Zimu, two
  Relics, and two Tactics. A player may mulligan at most twice. The notes say
  those cards move to the Graveyard at the start of Turn 1.
- Relic and Tactic plays have no per-turn cap. Their LP costs are the values
  printed in their registry entries.

## Board and card locations

- Each player has three columns, each with a Vanguard (front) and Rearguard
  (back) slot. Vanguard slots hold Zimu; Rearguard slots hold Relics.
- A Rearguard card cannot be attacked, targeted, or sniped while its Vanguard
  slot is occupied. It is exposed when that Vanguard slot is empty.
- A face-up Relic is anchored to its column. A Zimu that moves lanes moves alone;
  Relics stay in place and apply to the next Zimu in their column.
- Each player has one Graveyard shared by all three card types.

## Rank and tribute scale

| Rank | Border | Printed scale | Deployment cost | Tribute requirement |
|---|---|---:|---:|---|
| Core | Emerald Green | ATK + HP: 1–4 | 0–1 LP | None stated |
| Militia | Amber Yellow | ATK + HP: 5–10 | 2–3 LP | None stated |
| Mythic | Crimson Red | ATK + HP: 11–16 | 4–5 LP | Shatter 2 active friendly Core or 1 active friendly Militia |
| Apex | Volcanic Orange | ATK + HP: 17–20 | 6–8 LP | Shatter 3 active friendly Core or 2 active friendly Militia |

These are scale descriptions from the rules notes; the engine does not yet enforce
stat ranges or tribute requirements.

## Clash resolution

- **Empty lane:** Defender loses LP equal to the attacker's ATK.
- **Successful shatter:** If attacker ATK is at least defender HP, the defender
  is destroyed. Excess ATK damages defender LP. The defender's Rearguard card in
  that column also implodes.
- **Failed strike:** If attacker ATK is below defender HP, the attacker is
  destroyed, its owner loses LP equal to defender HP minus attacker ATK, and the
  attacker's Rearguard card in that column also implodes. The defender heals
  fully (no persistent damage is currently modeled).
- **Zero HP:** A card printed with 0 HP is stable on the board and may attack an
  empty lane safely. It implodes only when engaged in battle and hit by at least
  1 ATK.
- Redline activates at 10 LP or less and can mutate card abilities.
- If an opponent's attack flips a face-down card and reveals an un-tributed
  Mythic or Apex, it implodes for 0 damage and the attack scores a full,
  unmitigated direct empty-lane strike. At match end all face-down cards are
  revealed; a hidden un-tributed Mythic or Apex causes match forfeit and
  disqualification.

## Clarifications needed

- **Tribute procedure:** The required ranks and active-field source are given,
  but the notes do not define how Catalyst changes the requirement or whether
  the tribute choice is made before or after paying LP.
- **Zero-ATK versus zero-HP:** The zero-HP rule requires a hit of at least 1 ATK,
  while the general shatter formula also destroys a 0-HP defender when a 0-ATK
  attacker meets the `ATK >= HP` threshold. The engine currently treats that
  specific clash as no damage, following the more specific zero-HP rule.
- **Mulligan setup:** The opening-hand distribution, pile sizes, and the
  relationship between the opening hand and each redraw are not fully specified.

## Current engine coverage

The Python engine models the 100-card registry, one-Zimu-per-turn deployment,
and basic lane clashes. Draw piles, turn phases, Relic effects, Tactics,
mulligans, tribute enforcement, face-down cards, and win/forfeit checks still
need implementation.
