"""Core data and lane-clash rules for the Zimu card game."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class Rank(Enum):
    CORE = 1
    MILITIA = 2
    MYTHIC = 3
    APEX = 4


class CardType(Enum):
    ZIMU = 1
    RELIC = 2
    TACTIC = 3


@dataclass
class Card:
    name: str
    card_type: CardType
    rank: Optional[Rank] = None
    atk: int = 0
    hp: int = 0
    lp_cost: int = 0
    text: str = "Vanilla"


COMMON_CORE_POOL = {
    "Scrip": Card("Scrip", CardType.ZIMU, Rank.CORE, 1, 1, 0),
    "Mite": Card("Mite", CardType.ZIMU, Rank.CORE, 2, 1, 0),
    "Gnat": Card("Gnat", CardType.ZIMU, Rank.CORE, 2, 0, 0, "Can attack adjacent horizontally instead of forward."),
    "Vapor": Card("Vapor", CardType.ZIMU, Rank.CORE, 1, 2, 0, "When sacrificed for a summon requirement, refund +1 LP."),
    "Dart": Card("Dart", CardType.ZIMU, Rank.CORE, 4, 0, 1),
    "Needle": Card("Needle", CardType.ZIMU, Rank.CORE, 3, 1, 1, "When attacking an empty lane, draw 1 Tactic card."),
    "Sentry": Card("Sentry", CardType.ZIMU, Rank.MILITIA, 2, 5, 2, "Opposing Core unblocked attackers deal 1 less direct damage to your LP pool."),
    "Bastion-Guard": Card("Bastion-Guard", CardType.ZIMU, Rank.MILITIA, 1, 6, 2),
    "Phalanx": Card("Phalanx", CardType.ZIMU, Rank.MILITIA, 2, 6, 2),
    "Bulwark": Card("Bulwark", CardType.ZIMU, Rank.MILITIA, 1, 7, 3, "Permanently immune to enemy positioning Tactic spells."),
    "Focus": Card("Focus", CardType.RELIC, None, 0, 0, 0, "Front-row Zimu in this column gains +2 ATK."),
    "Bastion": Card("Bastion", CardType.RELIC, None, 0, 0, 0, "Front-row Zimu in this column gains +2 HP."),
    "Aegis-Sigil": Card("Aegis-Sigil", CardType.RELIC, None, 0, 0, 0, "Front-row Zimu in this column is immune to Tactic destruction."),
    "Tether": Card("Tether", CardType.RELIC, None, 0, 0, 0, "Front-row Zimu in this column cannot be shifted horizontally."),
    "Iron-Anchor": Card("Iron-Anchor", CardType.RELIC, None, 0, 0, 0, "Front-row Zimu in this column gains +1 HP."),
    "Fracture": Card("Fracture", CardType.TACTIC, None, 0, 0, 2, "Shatter one friendly active frontline Zimu to draw 3 cards immediately. [Surge]"),
    "Siphon": Card("Siphon", CardType.TACTIC, None, 0, 0, 0, "Reduce a targeted enemy monster's current HP threshold by 2 points until End Phase. [Surge]"),
    "Blood-Tax": Card("Blood-Tax", CardType.TACTIC, None, 0, 0, 0, "Melt away -2 HP threshold from a targeted enemy blocker until End Phase. [Surge]"),
    "Flash-Deploy": Card("Flash-Deploy", CardType.TACTIC, None, 0, 0, 1, "Draw 2 cards immediately from your Combatant deck. [Surge]"),
    "Shimmer": Card("Shimmer", CardType.TACTIC, None, 0, 0, 0, "Flips a friendly card face-down and shuffles its lane slot. [Surge]"),
}

CORE_POOL = COMMON_CORE_POOL

DECK_1 = [
    Card("Spark", CardType.ZIMU, Rank.CORE, 3, 1, 0), Card("Shard", CardType.ZIMU, Rank.CORE, 4, 0, 0),
    Card("Bolt", CardType.ZIMU, Rank.CORE, 3, 0, 1), Card("Flint", CardType.ZIMU, Rank.CORE, 2, 1, 0),
    Card("Twig", CardType.ZIMU, Rank.CORE, 1, 1, 0),     Card("Blink", CardType.ZIMU, Rank.CORE, 3, 1, 2, "When played, swap positions with another face-up teammate."),
    Card("Wisp", CardType.ZIMU, Rank.CORE, 2, 2, 1, "Once per turn, pay 1 LP to cancel attack and slide or swap lanes."),
    Card("Sprout", CardType.ZIMU, Rank.CORE, 1, 1, 1, "When played, deploy an additional Sprout from deck to an adjacent slot."),
    Card("Talon", CardType.ZIMU, Rank.MILITIA, 4, 1, 2, "Attacking an empty slot deals 6 direct damage instead of 4."),
    Card("Lycos", CardType.ZIMU, Rank.MILITIA, 4, 2, 3, "Spend 4 LP to resurrect Lycos from Graveyard to empty slot."),
    Card("Ruin", CardType.ZIMU, Rank.MILITIA, 4, 5, 3, "In Redline State, stats permanently mutate into [8 ATK / 2 HP]."),
    Card("Hound", CardType.ZIMU, Rank.MILITIA, 5, 2, 2),
    Card("Razor", CardType.ZIMU, Rank.MILITIA, 4, 4, 3, "While in Redline State, Razor gains +1 ATK."),
    Card("Cyclops", CardType.ZIMU, Rank.MYTHIC, 7, 5, 4),
    Card("Wyvern", CardType.ZIMU, Rank.MYTHIC, 6, 5, 4, "On successful shatter, look at opponent's hand."),
    Card("Chimera", CardType.ZIMU, Rank.MYTHIC, 5, 6, 5, "Gains +1 ATK for each unique card type in graveyard."),
    Card("Basilisk", CardType.ZIMU, Rank.MYTHIC, 6, 6, 4),
    Card("Kraken", CardType.ZIMU, Rank.APEX, 9, 8, 6),
    Card("Conduit", CardType.RELIC, None, 0, 0, 0, "Draw 1 Tactic card whenever a Tactic resolves in this column."),
    Card("Ambush-Battery", CardType.RELIC, None, 0, 0, 0, "Front Zimu gains +3 ATK on the turn it flips face-up."),
    Card("Void-Shell", CardType.RELIC, None, 0, 0, 1, "Front Zimu is immune to self-inflicted Tactic backlash damage."),
    Card("Kinetic-Core", CardType.RELIC, None, 0, 0, 1, "Siphons 2 LP from enemy to heal you when front Zimu wins a clash."),
    Card("Tribute-Altar", CardType.RELIC, None, 0, 0, 0, "Draw 1 Combatant when a card in this column is sacrificed."),
    Card("Phase-Shift", CardType.RELIC, None, 0, 0, 1, "Flip face-up to swap positions of two adjacent friendly Zimu."),
    Card("Redline-Battery", CardType.RELIC, None, 0, 0, 0, "Front Zimu gains +2 ATK / +2 HP during Redline State."),
    Card("Chrono-Anchor", CardType.RELIC, None, 0, 0, 1, "Return front Zimu to hand instead of Graveyard when destroyed."),
    Card("Catalyst", CardType.RELIC, None, 0, 0, 0, "Front Zimu requires 1 less core sacrifice for higher tiers."),
    Card("Solder", CardType.RELIC, None, 0, 0, 1, "Attach this Relic directly to a Zimu; moves with it if it slides."),
    Card("Siphon-Grid", CardType.RELIC, None, 0, 0, 2, "⚡ CLASH WINDOW. Steal 1 ATK from attacker and add to defender."),
    Card("Spikewall", CardType.RELIC, None, 0, 0, 2, "⚡ CLASH WINDOW. Adds +2 HP. Failed hit adds +2 to penalty."),
    Card("Prism", CardType.RELIC, None, 0, 0, 1, "Divert a single-target enemy spell card to an adjacent lane column."),
    Card("Overload", CardType.TACTIC, None, 0, 0, 3, "Fuse all board ATK into one strike. Backlash if pierce > 5 LP. [Surge]"),
    Card("Divert", CardType.TACTIC, None, 0, 0, 0, "⚡ CLASH WINDOW. Force attack to target adjacent lane or miss. [Reflex]"),
    Card("Surge-Gate", CardType.TACTIC, None, 0, 0, 3, "Bypass Tribute scale for turn; deploy Zimu strictly for LP cost. [Surge]"),
    Card("Redline-Surge", CardType.TACTIC, None, 0, 0, 0, "Redline only. Selected lane Zimu can attack twice this phase. [Surge]"),
    Card("Mimic", CardType.TACTIC, None, 0, 0, 1, "Copy the effect of any 0 LP Tactic card sitting in opponent's Graveyard. [Surge]"),
    Card("Blind-Strike", CardType.TACTIC, None, 0, 0, 2, "Attack a face-down Ambush card without forcing it to flip face-up. [Surge]"),
    Card("False-Step", CardType.TACTIC, None, 0, 0, 1, "⚡ CLASH WINDOW. Force attacker's ATK to match its own printed HP. [Reflex]"),
]


DECK_2 = [
    Card("Clay", CardType.ZIMU, Rank.CORE, 0, 4, 1), Card("Husk", CardType.ZIMU, Rank.CORE, 0, 3, 0),
    Card("Quartz", CardType.ZIMU, Rank.CORE, 0, 3, 1),
    Card("Pebble", CardType.ZIMU, Rank.CORE, 0, 3, 1, "When deployed, protect one friendly active Relic from disruption."),
    Card("Shell", CardType.ZIMU, Rank.CORE, 0, 4, 1),     Card("Moss", CardType.ZIMU, Rank.CORE, 1, 3, 0, "When Shattered in battle, heal your scorecard by +2 LP."),
    Card("Plank", CardType.ZIMU, Rank.CORE, 0, 4, 0),
    Card("Root", CardType.ZIMU, Rank.CORE, 1, 2, 0, "Enemy units cannot slide out of this lane column."),
    Card("Strix", CardType.ZIMU, Rank.MILITIA, 1, 4, 2), Card("Ursan", CardType.ZIMU, Rank.MILITIA, 4, 4, 3),
    Card("Cyno", CardType.ZIMU, Rank.MILITIA, 1, 4, 2, "When blocking, reduce attacker's current ATK by -2 for the turn."),
    Card("Vane", CardType.ZIMU, Rank.MILITIA, 2, 6, 3, "Absorb attacks from up to two adjacent columns simultaneously."),
    Card("Warden", CardType.ZIMU, Rank.MILITIA, 2, 6, 2, "Permanently immune to horizontal board movements/swaps."),
    Card("Sentinel", CardType.ZIMU, Rank.MILITIA, 2, 5, 3, "While active, face-down Relic sitting directly behind it cannot be sniped."),
    Card("Eclipse", CardType.ZIMU, Rank.MILITIA, 3, 5, 3, "Opponent must pay an extra +1 LP tax to cast any Tactic hand spells."),
    Card("Ironclad", CardType.ZIMU, Rank.MILITIA, 3, 6, 3),
    Card("Golem", CardType.ZIMU, Rank.MYTHIC, 2, 10, 5),
    Card("Gargoyle", CardType.ZIMU, Rank.MYTHIC, 3, 9, 5),
    Card("Apex-Hybrid", CardType.ZIMU, Rank.MYTHIC, 5, 7, 5),
    Card("Leviathan", CardType.ZIMU, Rank.APEX, 5, 13, 8),
    Card("Nexus", CardType.RELIC, None, 0, 0, 2, "Turn every single 0 LP Tactic spell into a card-drawing machine."),
    Card("Gravity-Well", CardType.RELIC, None, 0, 0, 2, "Global Domain. Permanently shaves -1 ATK off all enemy attackers."),
    Card("Renewal", CardType.RELIC, None, 0, 0, 1, "When front Zimu shatters, search and deploy a Core-rank card into that slot."),
    Card("Fort-Anchor", CardType.RELIC, None, 0, 0, 0, "Front Zimu gains +1 HP and cannot be shifted horizontally."),
    Card("Iron-Wall", CardType.RELIC, None, 0, 0, 1, "Vanguard slot is completely immune to overflow pierce damage from Mythic units."),
    Card("Stone-Sigil", CardType.RELIC, None, 0, 0, 0, "Protects front Zimu from being targeted by opponent turn Surge Tactics."),
    Card("Mirror-Weave", CardType.RELIC, None, 0, 0, 2, "⚡ CLASH WINDOW. Temporarily changes defender's ATK to match attacker's current ATK."),
    Card("Ward-Battery", CardType.RELIC, None, 0, 0, 1, "Store up to 2 unused LP points inside this card to spend on future turns."),
    Card("Core-Shield", CardType.RELIC, None, 0, 0, 0, "Front Zimu cannot be destroyed by Core-rank attackers."),
    Card("Titan-Anchor", CardType.RELIC, None, 0, 0, 2, "Front Zimu cannot be forced to destroy itself via your own cards."),
    Card("Shift-Grid", CardType.RELIC, None, 0, 0, 1, "Pay 1 LP to slide a friendly back-row Relic to an adjacent slot."),
    Card("Siphon-Gate", CardType.RELIC, None, 0, 0, 2, "Whenever an enemy unit shatters from a Clash Penalty, gain +2 LP."),
    Card("Spike-Plate", CardType.RELIC, None, 0, 0, 1, "Add +1 ATK to defender values during Clash Penalty checks."),
    Card("Absorb", CardType.TACTIC, None, 0, 0, 1, "⚡ CLASH WINDOW. Jumps defender +3 HP and drops enemy Overload cap to 0 LP. [Reflex]"),
    Card("Spike-Shield", CardType.TACTIC, None, 0, 0, 1, "⚡ CLASH WINDOW. Target friendly Zimu gains +2 HP. Blowback adds +1 to penalty. [Reflex]"),
    Card("Iron-Grip", CardType.TACTIC, None, 0, 0, 2, "⚡ CLASH WINDOW. Freeze an oncoming attacker's horizontal movements. [Reflex]"),
    Card("Stone-Wall", CardType.TACTIC, None, 0, 0, 1, "⚡ CLASH WINDOW. Nullify all incoming overflow pierce damage down a column. [Reflex]"),
    Card("Mirror-Trap", CardType.TACTIC, None, 0, 0, 2, "⚡ CLASH WINDOW. Reflect a cast enemy Tactic spell effect back at them. [Reflex]"),
]

BINDER_RESERVES = [
    Card("Banish", CardType.TACTIC, None, 0, 0, 2, "Permanently remove exactly 1 targeted card in any graveyard from the match. [Surge]"),
    Card("Backlash", CardType.TACTIC, None, 0, 0, 2, "⚡ CLASH WINDOW. Cancel attack; opponent takes monster's ATK as pure LP damage. [Reflex]"),
    Card("Grid-Lock", CardType.TACTIC, None, 0, 0, 2, "Freeze a column lane; cards cannot be shifted or manipulated for a turn. [Surge]"),
    Card("Cataclysm", CardType.TACTIC, None, 0, 0, 4, "Board wipe. Instantly shatter all face-up frontline Zimu on both sides. [Surge]"),
]

MASTER_CARD_DATABASE = {
    card.name: card
    for card in (*COMMON_CORE_POOL.values(), *DECK_1, *DECK_2, *BINDER_RESERVES)
}
CARD_REGISTRY_IDS = {
    card.name: registry_id
    for registry_id, card in enumerate(MASTER_CARD_DATABASE.values(), start=1)
}
CARD_REGISTRY_BY_ID = {
    registry_id: MASTER_CARD_DATABASE[card_name]
    for card_name, registry_id in CARD_REGISTRY_IDS.items()
}


class Lane:
    def __init__(self) -> None:
        self.vanguard: Optional[Card] = None
        self.rearguard: Optional[Card] = None


class PlayerBoard:
    def __init__(self, name: str) -> None:
        self.player_name = name
        self.lp = 40
        self.lanes = [Lane(), Lane(), Lane()]
        self.hand: List[Card] = []
        self.graveyard: List[Card] = []
        self.has_summoned_this_turn = False

    @property
    def is_redline(self) -> bool:
        return self.lp <= 10

    def deploy_zimu(self, idx: int, lane_idx: int) -> str:
        if self.has_summoned_this_turn:
            return "REJECTED: One-Summon Cap."
        if not (0 <= idx < len(self.hand)):
            return "ERROR: Invalid index."
        if not (0 <= lane_idx < len(self.lanes)):
            return "ERROR: Invalid lane."

        card = self.hand[idx]
        if card.card_type != CardType.ZIMU:
            return "ERROR: Not a Zimu."
        if self.lanes[lane_idx].vanguard:
            return "REJECTED: Slot occupied."
        if self.lp <= card.lp_cost:
            return "REJECTED: Out of LP."

        self.lp -= card.lp_cost
        self.lanes[lane_idx].vanguard = self.hand.pop(idx)
        self.has_summoned_this_turn = True
        return "SUCCESS"


class ClashEngine:
    @staticmethod
    def resolve_lane_clash(att: PlayerBoard, j_def: PlayerBoard, idx: int) -> str:
        if not (0 <= idx < len(att.lanes) and 0 <= idx < len(j_def.lanes)):
            return "ERROR: Invalid lane."

        a_lane, d_lane = att.lanes[idx], j_def.lanes[idx]
        atk_c, def_c = a_lane.vanguard, d_lane.vanguard
        if not atk_c:
            return "SKIPPED"
        if not def_c:
            j_def.lp -= atk_c.atk
            return f"DIRECT STRIKE: {atk_c.atk}"
        if atk_c.atk == 0 and def_c.hp == 0:
            return "NO DAMAGE"
        if atk_c.atk >= def_c.hp:
            pierce = atk_c.atk - def_c.hp
            j_def.lp -= pierce
            j_def.graveyard.append(def_c)
            d_lane.vanguard = None
            if d_lane.rearguard:
                j_def.graveyard.append(d_lane.rearguard)
                d_lane.rearguard = None
            return "SHATTER"

        penalty = def_c.hp - atk_c.atk
        att.lp -= penalty
        att.graveyard.append(atk_c)
        a_lane.vanguard = None
        if a_lane.rearguard:
            att.graveyard.append(a_lane.rearguard)
            a_lane.rearguard = None
        return "BLOWBACK"
