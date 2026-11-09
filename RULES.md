# Flux Point: Zimu — rules captured so far

This document records the supplied game notes. It distinguishes stated rules from
details that still need clarification; card ability text is not necessarily an
implemented effect.

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
- The notes describe a pre-game eight-card mulligan: put the opening hand face
  down in an out-of-play Mulligan Pile, lose 5 LP, and redraw four Zimu, two
  Relics, and two Tactics. A player may mulligan at most twice. The notes say
  those cards move to the Graveyard at the start of Turn 1.

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
| Core | Green | ATK + HP: 1–4 | 0–1 LP | None stated |
| Militia | Yellow | ATK + HP: 5–10 | 2–3 LP | None stated |
| Mythic | Red | ATK + HP: 11–16 | 4–5 LP | Shatter 2 Core or 1 Militia |
| Apex | Orange | ATK + HP: 17–20 | 6–8 LP | Shatter 3 Core or 2 Militia |

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
- An un-tributed Mythic or Apex revealed on the opponent's turn dissolves and
  causes an unmitigated direct empty-lane strike. At match end all face-down
  cards are revealed; an illegal un-tributed card causes forfeiture.

## Clarifications needed

- **Support-card costs conflict:** The phase rules say Relics and Tactics cost
  0 LP from hand, but many Tactic definitions have nonzero `lp_cost` values and
  describe paying those costs. Confirm whether the cost field should be ignored
  for support cards, or whether the phase rule is inaccurate.
- **Card count conflict:** The source calls this a 100-card database, while the
  supplied lists contain 20 shared cards, 44 Deck 1 cards, and 47 Deck 2 cards
  (111 named definitions if all are distinct). Confirm whether the 100-card
  total or the per-section counts are intended.
- **Tribute procedure:** The required ranks and quantities are given, but the
  notes do not say which zones can supply Tributes, when they are chosen, or
  whether the sacrificed cards must be face-up.
- **Zero-ATK versus zero-HP:** The zero-HP rule requires a hit of at least 1 ATK,
  while the general shatter formula also destroys a 0-HP defender when a 0-ATK
  attacker meets the `ATK >= HP` threshold. The engine currently treats that
  specific clash as no damage, following the more specific zero-HP rule.
- **Mulligan setup:** The opening-hand distribution, pile sizes, and the
  relationship between the opening hand and each redraw are not fully specified.

## Current engine coverage

The Python engine currently models card data, one-Zimu-per-turn deployment, and
basic lane clashes. Draw piles, turn phases, Relic effects, Tactics, mulligans,
tribute enforcement, face-down cards, and win/forfeit checks still need
implementation.
