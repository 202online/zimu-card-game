import unittest

from zimu_engine import (
    BINDER_RESERVES,
    CARD_REGISTRY_BY_ID,
    CARD_REGISTRY_IDS,
    COMMON_CORE_POOL,
    CORE_POOL,
    DECK_1,
    DECK_2,
    MASTER_CARD_DATABASE,
    Card,
    CardType,
    ClashEngine,
    PlayerBoard,
    Rank,
)


class CardDatabaseTests(unittest.TestCase):
    def test_master_database_indexes_each_card_definition(self):
        definitions = [
            *COMMON_CORE_POOL.values(),
            *DECK_1,
            *DECK_2,
            *BINDER_RESERVES,
        ]
        self.assertEqual(len(MASTER_CARD_DATABASE), 100)
        self.assertEqual(len(CARD_REGISTRY_IDS), 100)
        self.assertEqual(len(CARD_REGISTRY_BY_ID), 100)
        for card in definitions:
            self.assertIs(MASTER_CARD_DATABASE[card.name], card)
        self.assertEqual(CARD_REGISTRY_IDS["Scrip"], 1)
        self.assertEqual(CARD_REGISTRY_IDS["Spark"], 21)
        self.assertEqual(CARD_REGISTRY_IDS["Clay"], 59)
        self.assertEqual(CARD_REGISTRY_IDS["Banish"], 97)
        self.assertIs(CARD_REGISTRY_BY_ID[100], MASTER_CARD_DATABASE["Cataclysm"])
        self.assertIs(CORE_POOL, COMMON_CORE_POOL)
        self.assertEqual(len(DECK_1), 38)
        self.assertEqual(len(DECK_2), 38)
        self.assertEqual(len(BINDER_RESERVES), 4)


class DeployTests(unittest.TestCase):
    def test_deploys_zimu_and_pays_lp(self):
        player = PlayerBoard("Player")
        card = Card("Mite", CardType.ZIMU, Rank.CORE, atk=2, hp=1, lp_cost=3)
        player.hand.append(card)

        self.assertEqual(player.deploy_zimu(0, 1), "SUCCESS")
        self.assertIs(player.lanes[1].vanguard, card)
        self.assertEqual(player.lp, 37)
        self.assertEqual(player.hand, [])
        self.assertTrue(player.has_summoned_this_turn)

    def test_rejects_second_summon_without_changing_hand(self):
        player = PlayerBoard("Player")
        first = Card("First", CardType.ZIMU)
        second = Card("Second", CardType.ZIMU)
        player.hand.extend([first, second])

        self.assertEqual(player.deploy_zimu(0, 0), "SUCCESS")
        self.assertEqual(player.deploy_zimu(0, 1), "REJECTED: One-Summon Cap.")
        self.assertEqual(player.hand, [second])

    def test_turn_reset_allows_next_summon(self):
        player = PlayerBoard("Player")
        player.hand.extend([Card("First", CardType.ZIMU), Card("Second", CardType.ZIMU)])

        self.assertEqual(player.deploy_zimu(0, 0), "SUCCESS")
        player.reset_turn_flags()
        self.assertEqual(player.deploy_zimu(0, 1), "SUCCESS")

    def test_rejects_invalid_card_lane_and_unaffordable_cost(self):
        player = PlayerBoard("Player")
        player.hand.extend([
            Card("Relic", CardType.RELIC),
            Card("Expensive", CardType.ZIMU, lp_cost=40),
        ])

        self.assertEqual(player.deploy_zimu(5, 0), "ERROR: Invalid index.")
        self.assertEqual(player.deploy_zimu(0, 0), "ERROR: Not a Zimu.")
        self.assertEqual(player.deploy_zimu(1, 3), "ERROR: Invalid lane.")
        self.assertEqual(player.deploy_zimu(1, 0), "REJECTED: Out of LP.")
        self.assertEqual(len(player.hand), 2)


class ClashTests(unittest.TestCase):
    def test_direct_strike_reduces_defender_lp(self):
        attacker = PlayerBoard("Attacker")
        defender = PlayerBoard("Defender")
        attacker.lanes[0].vanguard = Card("Spark", CardType.ZIMU, Rank.CORE, atk=3, hp=1)

        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 0), "DIRECT STRIKE: 3")
        self.assertEqual(defender.lp, 37)

    def test_shatter_deals_pierce_and_sends_rearguard_to_graveyard(self):
        attacker = PlayerBoard("Attacker")
        defender = PlayerBoard("Defender")
        attacking_card = Card("Strong", CardType.ZIMU, Rank.CORE, atk=5, hp=2)
        defending_card = Card("Guard", CardType.ZIMU, Rank.CORE, atk=1, hp=3)
        rear_card = Card("Rear", CardType.ZIMU, Rank.CORE, atk=1, hp=2)
        attacker.lanes[0].vanguard = attacking_card
        defender.lanes[0].vanguard = defending_card
        defender.lanes[0].rearguard = rear_card

        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 0), "SHATTER")
        self.assertEqual(defender.lp, 38)
        self.assertIsNone(defender.lanes[0].vanguard)
        self.assertIsNone(defender.lanes[0].rearguard)
        self.assertEqual(defender.graveyard, [defending_card, rear_card])

    def test_blowback_hurts_attacker_and_clears_its_lane(self):
        attacker = PlayerBoard("Attacker")
        defender = PlayerBoard("Defender")
        attacking_card = Card("Weak", CardType.ZIMU, Rank.CORE, atk=2, hp=1)
        rear_card = Card("Rear", CardType.ZIMU, Rank.CORE, atk=1, hp=2)
        attacker.lanes[0].vanguard = attacking_card
        attacker.lanes[0].rearguard = rear_card
        defender.lanes[0].vanguard = Card("Guard", CardType.ZIMU, Rank.CORE, atk=1, hp=5)

        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 0), "BLOWBACK")
        self.assertEqual(attacker.lp, 37)
        self.assertIsNone(attacker.lanes[0].vanguard)
        self.assertIsNone(attacker.lanes[0].rearguard)
        self.assertEqual(attacker.graveyard, [attacking_card, rear_card])

    def test_zero_stat_zimu_is_safe_in_empty_lane(self):
        attacker = PlayerBoard("Attacker")
        defender = PlayerBoard("Defender")
        zero_card = Card("Zero", CardType.ZIMU, Rank.CORE)
        attacker.lanes[0].vanguard = zero_card

        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 3), "ERROR: Invalid lane.")
        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 0), "DIRECT STRIKE: 0")
        self.assertIs(attacker.lanes[0].vanguard, zero_card)
        self.assertEqual(attacker.graveyard, [])

    def test_zero_attack_does_not_destroy_zero_hp_zimu(self):
        attacker = PlayerBoard("Attacker")
        defender = PlayerBoard("Defender")
        zero_attacker = Card("Zero attacker", CardType.ZIMU, Rank.CORE)
        zero_defender = Card("Zero defender", CardType.ZIMU, Rank.CORE, atk=2, hp=0)
        attacker.lanes[0].vanguard = zero_attacker
        defender.lanes[0].vanguard = zero_defender

        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 0), "NO DAMAGE")
        self.assertIs(attacker.lanes[0].vanguard, zero_attacker)
        self.assertIs(defender.lanes[0].vanguard, zero_defender)


if __name__ == "__main__":
    unittest.main()
