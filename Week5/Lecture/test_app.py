import unittest
from unittest.mock import MagicMock, patch

import app as fapp


class TestPredictApp(unittest.TestCase):

    def setUp(self):

        self.mock_model = MagicMock()
        self.mock_model.predict.return_value = [220]

        self.open_patcher = patch("builtins.open", MagicMock())
        self.pickle_patcher = patch("pickle.load", return_value=self.mock_model)

        self.open_patcher.start()
        self.pickle_patcher.start()

        fapp.model = self.mock_model
        self.client = fapp.app.test_client()

    def tearDown(self):
        self.open_patcher.stop()
        self.pickle_patcher.stop()

    def test_predict(self):
        self.mock_model.predict.return_value = {"prediction": 220}

        response = self.client.post("/model", json={"x": 100})

        data = response.get_json()
        self.assertEqual(data["prediction"], 220)
