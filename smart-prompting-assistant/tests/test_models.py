from app.models.prompt import Prompt
from app.models.evaluation import Evaluation
import unittest

class TestPromptModel(unittest.TestCase):
    def setUp(self):
        self.prompt = Prompt()

    def test_create_prompt(self):
        result = self.prompt.create("Test prompt")
        self.assertEqual(result, "Test prompt")

    def test_format_prompt(self):
        self.prompt.create("Test prompt")
        formatted = self.prompt.format()
        self.assertEqual(formatted, "Formatted: Test prompt")

class TestEvaluationModel(unittest.TestCase):
    def setUp(self):
        self.evaluation = Evaluation()

    def test_analyze_prompts(self):
        prompts = ["Prompt 1", "Prompt 2"]
        best_prompt = self.evaluation.analyze(prompts)
        self.assertIn(best_prompt, prompts)

    def test_select_best_strategy(self):
        strategies = ["Strategy A", "Strategy B"]
        best_strategy = self.evaluation.select_best(strategies)
        self.assertIn(best_strategy, strategies)

if __name__ == '__main__':
    unittest.main()