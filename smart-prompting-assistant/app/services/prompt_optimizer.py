class PromptOptimizer:
    def __init__(self):
        pass

    def optimize_prompt(self, prompt):
        # Logic to optimize the given prompt
        optimized_prompt = prompt.strip()  # Example optimization: stripping whitespace
        return optimized_prompt

    def evaluate_prompt(self, prompt):
        # Logic to evaluate the effectiveness of the prompt
        score = len(prompt)  # Example evaluation: scoring based on length
        return score

    def reformat_prompt(self, prompt):
        # Logic to reformat the prompt for better AI interaction
        reformatted_prompt = prompt.replace("?", " ?").strip()  # Example reformatting
        return reformatted_prompt


# Create a default instance
_optimizer = PromptOptimizer()

# Export standalone functions for backward compatibility
def optimize_prompt(prompt):
    """Optimize a prompt using the default optimizer instance."""
    return _optimizer.optimize_prompt(prompt.content if hasattr(prompt, 'content') else str(prompt))

def evaluate_prompt(prompt):
    """Evaluate a prompt using the default optimizer instance."""
    return _optimizer.evaluate_prompt(prompt.content if hasattr(prompt, 'content') else str(prompt))

def reformat_prompt(prompt):
    """Reformat a prompt using the default optimizer instance."""
    return _optimizer.reformat_prompt(prompt.content if hasattr(prompt, 'content') else str(prompt))