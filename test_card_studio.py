import json
import unittest
from pathlib import Path

from design.build_catalog import build_catalog
from zimu_engine import CARD_REGISTRY_BY_ID


class CardStudioCatalogTests(unittest.TestCase):
    def test_all_cards_have_short_unique_appearances(self):
        descriptions = json.loads(
            (Path(__file__).parent / "design" / "appearances.json").read_text(encoding="utf-8")
        )
        self.assertEqual(set(descriptions), {card.name for card in CARD_REGISTRY_BY_ID.values()})
        self.assertEqual(len(descriptions), len(set(descriptions.values())))
        for name, description in descriptions.items():
            with self.subTest(name=name):
                self.assertTrue(description.strip())
                self.assertLessEqual(len(description), 90)

    def test_generated_catalog_is_current(self):
        path = Path(__file__).parent / "design" / "card-catalog.js"
        self.assertEqual(path.read_text(encoding="utf-8"), build_catalog())


if __name__ == "__main__":
    unittest.main()
