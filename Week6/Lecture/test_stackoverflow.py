import unittest
from unittest.mock import MagicMock, patch

import requests
from stackoverflow import Stackoverflow


class TestStackstackoverfloe(unittest.TestCase):

    def setUp(self):
        self.client = Stackoverflow()

    @patch("stackoverflow.requests.get")
    def test_get_questions(self, mock_get):
        fake_items = [
            {"title": "srh mock test", "score": 42},
            {"title": "mock test", "score": 38},
        ]

        mock_get.return_value.json.return_value = {"items": fake_items}
        mock_get.return_value.raise_for_status = MagicMock()

        result = self.client.get_questions(tag="python")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["score"], "srh mock test")
