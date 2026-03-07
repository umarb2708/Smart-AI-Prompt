class StrategyEvaluator:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def evaluate_strategies(self):
        results = {}
        for strategy in self.strategies:
            results[strategy.name] = strategy.evaluate()
        return results

    def select_best_strategy(self, evaluation_results):
        best_strategy = max(evaluation_results, key=evaluation_results.get)
        return best_strategy