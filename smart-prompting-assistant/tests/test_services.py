from app.services.prompt_optimizer import optimize_prompt
from app.services.strategy_evaluator import evaluate_strategy
import unittest

class TestServices(unittest.TestCase):

    def test_optimize_prompt(self):
        input_prompt = "How can I improve my writing skills?"
        expected_output = "What are some effective strategies to enhance my writing skills?"
        optimized_prompt = optimize_prompt(input_prompt)
        self.assertEqual(optimized_prompt, expected_output)

    def test_evaluate_strategy(self):
        strategies = [
            "Use clear and concise language.",
            "Incorporate storytelling techniques.",
            "Engage the reader with questions."
        ]
        expected_best_strategy = "Use clear and concise language."
        best_strategy = evaluate_strategy(strategies)
        self.assertEqual(best_strategy, expected_best_strategy)

if __name__ == '__main__':
    unittest.main()