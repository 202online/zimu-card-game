import unittest

from zimu_engine import Card, CardType, ClashEngine, PlayerBoard, Rank


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

    def test_implosion_and_invalid_lane(self):
        attacker = PlayerBoard("Attacker")
        defender = PlayerBoard("Defender")
        zero_card = Card("Zero", CardType.ZIMU, Rank.CORE)
        attacker.lanes[0].vanguard = zero_card

        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 3), "ERROR: Invalid lane.")
        self.assertEqual(ClashEngine.resolve_lane_clash(attacker, defender, 0), "IMPLODED")
        self.assertEqual(attacker.graveyard, [zero_card])


if __name__ == "__main__":
    unittest.main()
