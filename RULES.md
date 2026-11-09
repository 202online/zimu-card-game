# Flux Point: Zimu — Master Manifest Rulebook v3.0

This is the rules-and-systems reference for the physical and digital game.
Card descriptions are captured in `zimu_engine.py`; most ability text is not
implemented as executable effects yet.

## 1. Global engine rules

### Starting LP and match end

- Both players start with exactly 40 Life Points (LP).
- The match ends instantly when a scorecard reaches 0 LP.
- Redline State activates when a player's LP drops to 10 or less.

### One-Summon Cap Law and support cards

- During Phase 2, the active player has one Zimu deployment action from hand to
  the Vanguard field.
- Relics and Tactics have no turn deployment limit. Their default cost to deploy
  from hand is 0 LP unless specified otherwise by their individual activation
  or resolution text.

### Opening hand and Paid Mulligan

- Each player draws an opening hand of exactly 8 cards: 4 Zimu Combatants,
  2 Relics, and 2 Tactics.
- A player may reject that hand face-down into a temporary out-of-play Mulligan
  Pile, deduct 5 LP, and redraw the same 4 / 2 / 2 ratio.
- One mulligan starts the match at 35 LP; two mulligans start at 30 LP.
- A player may mulligan at most twice per match. When Turn 1 begins, all rejected
  hands move to the right-hand Graveyard.

### Core-Recursion Law

Use the single turn deployment action to permanently banish 3 Tactic or Relic
cards from your own Graveyard and return 1 basic Vanilla Core Zimu from your
Graveyard to your hand.

### Priority Timestamp Resolution Law

Resolve all attacking declarations and direct damage against player LP first.
If a scorecard reaches 0 LP during this initial damage wave, the match ends
instantly as a knockout. Triggered abilities, healing, and Rearguard Relic
adjustments resolve only if both players survive the raw damage wave.

## 2. Physical board and printing

### Coordinate axis

Each player controls a symmetrical 3×2 grid. Each vertical column is one
unified Column Lane.

```text
[ COMBATANT DECK ] | [ Vanguard 1 ] [ Vanguard 2 ] [ Vanguard 3 ] | [ GRAVEYARD ]
[ RELIC DECK     ] | [ Rearguard 1] [ Rearguard 2] [ Rearguard 3] | [ TACTIC DECK]
```

- Row 1 is the Vanguard Row, dedicated to Zimu.
- Row 2 is the Rearguard Row, dedicated to Relics.
- A Rearguard slot is exposed only when the Vanguard slot directly in front of
  it is empty; otherwise it cannot be attacked, targeted, or sniped.
- Once a Relic is face-up, it is locked to its column and cannot be shifted
  horizontally by a card effect.
- When a Zimu shifts lanes, it moves alone. Rearguard Relics stay in their
  columns and modify the next occupant.
- All card types use one right-hand Graveyard. Between matches, sort by card
  backs: Midnight Black (Combatants), Metallic Silver (Relics), Arcane White
  (Tactics).

### Print layout

- Full Canvas (With Bleed): 2.72" × 3.72" (816 × 1116 px at 300 DPI).
- Cut Line: 2.50" × 3.50" (750 × 1050 px).
- Safe Zone: 2.25" × 3.25" (675 × 975 px).
- All text and bottom-left ATK / HP stats must stay inside the Safe Zone.

## 3. Structural hierarchy

Zimu are balanced by Combined Stat Weight: Printed ATK + Printed HP.

| Rank | Combined stats | Face-up LP cost | Accent |
|---|---:|---:|---|
| Core | 1–4 | 0–1 | Emerald Green |
| Militia | 5–10 | 2–3 | Amber Yellow |
| Mythic | 11–16 | 4–5 | Crimson Red |
| Apex | 17–20 | 6–8 | Volcanic Orange |

- Mythic Summon Requirement: Shatter 2 friendly Core or 1 friendly Militia
  currently active on the Vanguard field.
- Apex Summon Requirement: Shatter 3 friendly Core or 2 friendly Militia
  currently active on the Vanguard field.
- Apex are textless endgame boss titans.

## 4. Threshold Combat Engine

Combat damage does not persist on cards. At the end of every phase, all
surviving cards heal to maximum health. Units are otherwise completely fine or
entirely wiped out.

### Formula 1: Direct Empty-Lane Strike

If a Zimu attacks down a column with an empty opposing Vanguard slot:

`Current LP - Attacker ATK = New LP`

### Formula 2: Successful Frontline Shatter

If `Attacker ATK >= Defender HP`, destroy the defending Zimu. Overflow pierce
damages the opponent's scorecard:

`Current LP - (Attacker ATK - Defender HP) = New LP`

**Bond Rule:** When a frontline Zimu is shattered in battle, every face-up or
face-down Relic directly behind it instantly implodes into the Graveyard.

### Formula 3: Failed Frontline Strike (Clash Penalty)

If `Attacker ATK < Defender HP`, destroy the attacking Zimu and send it to the
active player's Graveyard. Apply counter-pierce damage to the active attacker's
scorecard:

`Current LP - (Defender HP - Attacker ATK) = New LP`

The passive defender takes 0 damage and heals to full health.

### Formula 4: Law of Absolute Zero

Cards printed with exactly 0 HP are stable on the board and may attack empty
lanes safely. They are destroyed only if they engage a blocker or are struck by
a card effect with force of 1 or more ATK.

### Illegal Ambush Collapse

If an opponent's attack flips a face-down card and reveals an un-tributed Mythic
or Apex Zimu, the card implodes into the Graveyard for 0 damage. The attack
bypasses the collapsing slot and becomes a full Direct Empty-Lane Strike.

### End-of-Game Disclosure Law

When a match ends by scorecard zeroing or round time expiration, both players
reveal all face-down Ambush cards. A hidden un-tributed Mythic or Apex causes
an automatic match forfeit and disqualification.

## 5. Phase Velocity

### Phase 1: Draw

If the active player has exactly 8 cards, they do not draw. Otherwise, choose
one of the Combatant, Relic, or Tactic decks and draw its top card.

### Phase 2: Deployment

The active player may perform deployment actions in any chosen order:

- Deploy one Zimu from hand to an empty Vanguard slot, paying its printed LP
  cost to place it face-up, or set it face-down horizontally as an Ambush for
  0 LP.
- Shatter active frontline units to satisfy the Mythic or Apex Summon
  Requirement.
- Set a Relic face-down in a Rearguard slot for 0 LP, or flip a pre-existing
  face-down Relic face-up by paying its LP activation fee.
- Cast any number of Surge Tactics from hand; resolve them and place them in
  the Graveyard.
- Core-Recursion also uses the single deployment action.

### Phase 3: Clash

No more cards may be placed onto the field from hand.

1. The active player declares simultaneous attacks with all face-up friendly
   Vanguard Zimu down their respective vertical Column Lanes.
2. The defender may respond with exactly one option: play one Reflex Tactic
   from hand, or flip one face-down Rearguard Relic face-up by paying its LP
   activation fee.
3. The active player may chain one Reflex Tactic. The response window then
   closes.
4. Resolve combat math down all three Column Lanes using the Threshold Combat
   Engine and Priority Timestamp Resolution Law.

### Phase 4: End

1. Reset temporary until-end-of-turn stat modifications, ATK shifts, and Tactic
   buffers.
2. Heal surviving Zimu to maximum health.
3. If the active player has more than 8 cards, they choose and discard until
   their hand is exactly 8 cards. Then the turn transitions.

## 6. Tournament deck architecture

- Each player has exactly 48 cards in their playing pile.
- Every card name in a deck must be unique; 0 duplicates are allowed.
- Required type split: 24 Zimu Combatants, 12 Rearguard Relics, and 12 Instant
  Tactics (48 total).
- Deck 1, **Overload Blitz**, and Deck 2, **Immovable Bastion**, each contain 48
  unique cards with no overlap.
- The 4 Binder Reserves (#097–#100) are unassigned and are not part of either
  48-card deck.

## 7. Registry and implementation status

The registry contains exactly 100 profiles: Deck 1 #001–#048, Deck 2 #049–#096,
and Binder Reserves #097–#100. `CARD_REGISTRY_IDS` and `CARD_REGISTRY_BY_ID`
preserve the numbered ledger.

The engine currently implements card definitions, one-Zimu-per-turn
deployment, turn-flag reset, and single-lane Formula 1–3 resolution. Full phase
orchestration, simultaneous multi-lane attacks, response limits, face-down
cards, draw piles, mulligans, Core-Recursion, rank tribute requirements,
priority timestamp ordering, and card abilities remain to be implemented.

## Open implementation questions

- Support cards default to 0 LP to deploy unless their activation or resolution
  text says otherwise; several registry entries also list nonzero LP costs.
  Confirm whether the printed `lp_cost` field itself is the exception.
- The timing for turn-limited triggered abilities and the interaction between
  the Bond Rule and the initial raw damage knockout check must follow the
  Priority Timestamp Resolution Law.
- The round time limit and the exact implementation of a face-down Zimu's
  printed identity/tribute status are not specified.
