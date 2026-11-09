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


CORE_POOL = {
    "Scrip": Card("Scrip", CardType.ZIMU, Rank.CORE, 1, 1, 0),
    "Mite": Card("Mite", CardType.ZIMU, Rank.CORE, 2, 1, 0),
    "Gnat": Card("Gnat", CardType.ZIMU, Rank.CORE, 2, 0, 0, "Can attack adjacent horizontally."),
    "Vapor": Card("Vapor", CardType.ZIMU, Rank.CORE, 1, 2, 0, "Sacrifice refunds +1 LP."),
    "Dart": Card("Dart", CardType.ZIMU, Rank.CORE, 4, 0, 1),
    "Needle": Card("Needle", CardType.ZIMU, Rank.CORE, 3, 1, 1, "Attack empty draws Tactic."),
    "Sentry": Card("Sentry", CardType.ZIMU, Rank.MILITIA, 2, 5, 2, "Unblocked Core deal -1 damage."),
    "Bastion-Guard": Card("Bastion-Guard", CardType.ZIMU, Rank.MILITIA, 1, 6, 2),
    "Phalanx": Card("Phalanx", CardType.ZIMU, Rank.MILITIA, 2, 6, 2),
    "Bulwark": Card("Bulwark", CardType.ZIMU, Rank.MILITIA, 1, 7, 3, "Immune to positioning Tactics."),
    "Focus": Card("Focus", CardType.RELIC, None, 0, 0, 0, "+2 ATK down column."),
    "Bastion": Card("Bastion", CardType.RELIC, None, 0, 0, 0, "+2 HP down column."),
    "Aegis-Sigil": Card("Aegis-Sigil", CardType.RELIC, None, 0, 0, 0, "Immune to Tactic destruction."),
    "Tether": Card("Tether", CardType.RELIC, None, 0, 0, 0, "Cannot shift horizontally."),
    "Iron-Anchor": Card("Iron-Anchor", CardType.RELIC, None, 0, 0, 0, "+1 HP down column."),
    "Fracture": Card("Fracture", CardType.TACTIC, None, 0, 0, 2, "Shatter own Zimu to draw 3. [Surge]"),
    "Siphon": Card("Siphon", CardType.TACTIC, None, 0, 0, 0, "-2 enemy HP threshold. [Surge]"),
    "Blood-Tax": Card("Blood-Tax", CardType.TACTIC, None, 0, 0, 0, "-2 enemy HP threshold. [Surge]"),
    "Flash-Deploy": Card("Flash-Deploy", CardType.TACTIC, None, 0, 0, 1, "Draw 2 Zimu. [Surge]"),
    "Shimmer": Card("Shimmer", CardType.TACTIC, None, 0, 0, 0, "Flip face-down and shuffle lane. [Surge]"),
}


DECK_1 = [
    Card("Spark", CardType.ZIMU, Rank.CORE, 3, 1, 0), Card("Shard", CardType.ZIMU, Rank.CORE, 4, 0, 0),
    Card("Bolt", CardType.ZIMU, Rank.CORE, 3, 0, 1), Card("Flint", CardType.ZIMU, Rank.CORE, 2, 1, 0),
    Card("Twig", CardType.ZIMU, Rank.CORE, 1, 1, 0), Card("Blink", CardType.ZIMU, Rank.CORE, 3, 1, 2, "Swap positions."),
    Card("Wisp", CardType.ZIMU, Rank.CORE, 2, 2, 1, "Pay 1 LP to cancel attack & slide."),
    Card("Sprout", CardType.ZIMU, Rank.CORE, 1, 1, 1, "Deploy copy from deck."),
    Card("Talon", CardType.ZIMU, Rank.MILITIA, 4, 1, 2, "Empty lane deals 6 instead of 4."),
    Card("Lycos", CardType.ZIMU, Rank.MILITIA, 4, 2, 3, "Resurrect for 4 LP."),
    Card("Ruin", CardType.ZIMU, Rank.MILITIA, 4, 5, 3, "Redline becomes [8/2]."),
    Card("Hound", CardType.ZIMU, Rank.MILITIA, 5, 2, 2),
    Card("Razor", CardType.ZIMU, Rank.MILITIA, 4, 4, 3, "Redline grants +1 ATK."),
    Card("Cyclops", CardType.ZIMU, Rank.MYTHIC, 7, 5, 4),
    Card("Wyvern", CardType.ZIMU, Rank.MYTHIC, 6, 5, 4, "Shatter lets you spy hand."),
    Card("Chimera", CardType.ZIMU, Rank.MYTHIC, 5, 6, 5, "+1 ATK per type in GY."),
    Card("Basilisk", CardType.ZIMU, Rank.MYTHIC, 6, 6, 4),
    Card("Kraken", CardType.ZIMU, Rank.APEX, 9, 8, 6),
    Card("Conduit", CardType.RELIC, None, 0, 0, 0, "Draw Tactic on resolution."),
    Card("Ambush-Battery", CardType.RELIC, None, 0, 0, 0, "Reveal grants +3 ATK."),
    Card("Void-Shell", CardType.RELIC, None, 0, 0, 1, "Immune to Tactic backlash."),
    Card("Kinetic-Core", CardType.RELIC, None, 0, 0, 1, "Siphon 2 LP on clash win."),
    Card("Tribute-Altar", CardType.RELIC, None, 0, 0, 0, "Draw Zimu on sacrifice."),
    Card("Phase-Shift", CardType.RELIC, None, 0, 0, 1, "Swap adjacent Zimu."),
    Card("Redline-Battery", CardType.RELIC, None, 0, 0, 0, "+2 ATK/+2 HP in Redline."),
    Card("Chrono-Anchor", CardType.RELIC, None, 0, 0, 1, "Death returns to hand."),
    Card("Catalyst", CardType.RELIC, None, 0, 0, 0, "-1 core sacrifice req."),
    Card("Solder", CardType.RELIC, None, 0, 0, 1, "Attached to Zimu; slides with it."),
    Card("Siphon-Grid", CardType.RELIC, None, 0, 0, 2, "Steal 1 ATK from attacker."),
    Card("Spikewall", CardType.RELIC, None, 0, 0, 2, "+2 HP. Failed hit scales penalty."),
    Card("Prism", CardType.RELIC, None, 0, 0, 1, "Divert spell to adjacent lane."),
    Card("Overload", CardType.TACTIC, None, 0, 0, 3, "Fuse all board ATK. [Surge]"),
    Card("Divert", CardType.TACTIC, None, 0, 0, 0, "Reroute or miss attack. [Reflex]"),
    Card("Surge-Gate", CardType.TACTIC, None, 0, 0, 3, "Bypass Tribute costs. [Surge]"),
    Card("Redline-Surge", CardType.TACTIC, None, 0, 0, 0, "Zimu attacks twice. [Surge]"),
    Card("Mimic", CardType.TACTIC, None, 0, 0, 1, "Copy opponent GY 0-LP Tactic. [Surge]"),
    Card("Blind-Strike", CardType.TACTIC, None, 0, 0, 2, "Attack face-down directly. [Surge]"),
    Card("False-Step", CardType.TACTIC, None, 0, 0, 1, "Attacker ATK becomes its HP. [Reflex]"),
    Card("Banish", CardType.TACTIC, None, 0, 0, 2, "Remove card from GY. [Surge]"),
    Card("Backlash", CardType.TACTIC, None, 0, 0, 2, "Cancel attack; deal ATK as LP hit. [Reflex]"),
    Card("Grid-Lock", CardType.TACTIC, None, 0, 0, 2, "Freeze column operations. [Surge]"),
    Card("Recalibrate", CardType.TACTIC, None, 0, 0, 0, "Return face-up Relic to hand. [Surge]"),
    Card("Tribute-Toll", CardType.TACTIC, None, 0, 0, 1, "Force enemy Core shatter. [Surge]"),
    Card("Cataclysm", CardType.TACTIC, None, 0, 0, 4, "Shatter all face-up frontline. [Surge]"),
]


DECK_2 = [
    Card("Clay", CardType.ZIMU, Rank.CORE, 0, 4, 1), Card("Husk", CardType.ZIMU, Rank.CORE, 0, 3, 0),
    Card("Quartz", CardType.ZIMU, Rank.CORE, 0, 3, 1),
    Card("Pebble", CardType.ZIMU, Rank.CORE, 0, 3, 1, "Protect active friendly Relic."),
    Card("Shell", CardType.ZIMU, Rank.CORE, 0, 4, 1), Card("Moss", CardType.ZIMU, Rank.CORE, 1, 3, 0, "Shatter heals +2 LP."),
    Card("Plank", CardType.ZIMU, Rank.CORE, 0, 4, 0),
    Card("Root", CardType.ZIMU, Rank.CORE, 1, 2, 0, "Enemy cannot slide out of lane."),
    Card("Strix", CardType.ZIMU, Rank.MILITIA, 1, 4, 2), Card("Ursan", CardType.ZIMU, Rank.MILITIA, 4, 4, 3),
    Card("Cyno", CardType.ZIMU, Rank.MILITIA, 1, 4, 2, "Blocks give attacker -2 ATK."),
    Card("Vane", CardType.ZIMU, Rank.MILITIA, 2, 6, 3, "Absorb 2 adjacent attacks."),
    Card("Warden", CardType.ZIMU, Rank.MILITIA, 2, 6, 2, "Immune to horizontal shifts."),
    Card("Sentinel", CardType.ZIMU, Rank.MILITIA, 2, 5, 3, "Protect back Relic from snipes."),
    Card("Eclipse", CardType.ZIMU, Rank.MILITIA, 3, 5, 3, "Opponent pays +1 LP tax on Tactics."),
    Card("Ironclad", CardType.ZIMU, Rank.MILITIA, 3, 6, 3),
    Card("Golem", CardType.ZIMU, Rank.MYTHIC, 2, 10, 5),
    Card("Gargoyle", CardType.ZIMU, Rank.MYTHIC, 3, 9, 5),
    Card("Apex-Hybrid", CardType.ZIMU, Rank.MYTHIC, 5, 7, 5),
    Card("Leviathan", CardType.ZIMU, Rank.APEX, 5, 13, 8),
    Card("Nexus", CardType.RELIC, None, 0, 0, 2, "Tactics generate card draw."),
    Card("Gravity-Well", CardType.RELIC, None, 0, 0, 2, "Global -1 enemy attacker ATK."),
    Card("Renewal", CardType.RELIC, None, 0, 0, 1, "Shatter lets you deploy Core."),
    Card("Fort-Anchor", CardType.RELIC, None, 0, 0, 0, "+1 HP & lock position."),
    Card("Iron-Wall", CardType.RELIC, None, 0, 0, 1, "Immune to Mythic pierce damage."),
    Card("Stone-Sigil", CardType.RELIC, None, 0, 0, 0, "Immune to enemy turn Surge Tactics."),
    Card("Mirror-Weave", CardType.RELIC, None, 0, 0, 2, "Defender ATK mirrors attacker ATK."),
    Card("Ward-Battery", CardType.RELIC, None, 0, 0, 1, "Store up to 2 unspent LP."),
    Card("Core-Shield", CardType.RELIC, None, 0, 0, 0, "Immune to Core rank attackers."),
    Card("Titan-Anchor", CardType.RELIC, None, 0, 0, 2, "Immune to self-destruction cards."),
    Card("Shift-Grid", CardType.RELIC, None, 0, 0, 1, "Pay 1 LP to slide Relic."),
    Card("Siphon-Gate", CardType.RELIC, None, 0, 0, 2, "Gain +2 LP on penalty kills."),
    Card("Spike-Plate", CardType.RELIC, None, 0, 0, 1, "+1 ATK to penalty math."),
    Card("Absorb", CardType.TACTIC, None, 0, 0, 1, "+3 HP, drop enemy Overload cap. [Reflex]"),
    Card("Spike-Shield", CardType.TACTIC, None, 0, 0, 1, "+2 HP, blowback maps to penalty. [Reflex]"),
    Card("Iron-Grip", CardType.TACTIC, None, 0, 0, 2, "Freeze oncoming attacker movement. [Reflex]"),
    Card("Stone-Wall", CardType.TACTIC, None, 0, 0, 1, "Nullify lane pierce damage. [Reflex]"),
    Card("Mirror-Trap", CardType.TACTIC, None, 0, 0, 2, "Reflect Tactic effect back. [Reflex]"),
    Card("Grid-Freeze", CardType.TACTIC, None, 0, 0, 1, "Close column after battle. [Reflex]"),
    Card("Counter-Step", CardType.TACTIC, None, 0, 0, 0, "Swap 2 active defenders. [Reflex]"),
    Card("Retaliate", CardType.TACTIC, None, 0, 0, 2, "Deal defender HP as hit back. [Reflex]"),
    Card("Purge", CardType.TACTIC, None, 0, 0, 1, "Discard random enemy card. [Surge]"),
    Card("Nova", CardType.TACTIC, None, 0, 0, 3, "Clear all active board Relics. [Surge]"),
    Card("Mirror-Trap-Alpha", CardType.TACTIC, None, 0, 0, 2, "Steal counter-trap effect. [Reflex]"),
    Card("Blind-Block", CardType.TACTIC, None, 0, 0, 1, "Block via face-down Ambush HP. [Reflex]"),
    Card("Deflect", CardType.TACTIC, None, 0, 0, 1, "Reroute hit to highest HP cell. [Reflex]"),
    Card("Last-Stand", CardType.TACTIC, None, 0, 0, 0, "Front Zimu gains infinite HP. [Reflex]"),
]


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
        if atk_c.hp == 0 and atk_c.atk == 0:
            att.graveyard.append(atk_c)
            a_lane.vanguard = None
            return "IMPLODED"
        if not def_c:
            j_def.lp -= atk_c.atk
            return f"DIRECT STRIKE: {atk_c.atk}"
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
