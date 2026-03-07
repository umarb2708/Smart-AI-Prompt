class Prompt:
    def __init__(self, user_input):
        self.user_input = user_input
        self.content = user_input  # Add content attribute for compatibility
        self.formatted_prompt = self.format_prompt()

    def format_prompt(self):
        """Format the user input into a clean prompt."""
        # Clean up the input
        formatted = self.user_input.strip()
        
        # Capitalize first letter if not already
        if formatted and formatted[0].islower():
            formatted = formatted[0].upper() + formatted[1:]
        
        return formatted

    def get_prompt(self):
        """Get the formatted prompt."""
        return self.formatted_prompt
    
    def get_original(self):
        """Get the original user input."""
        return self.user_input
    
    def __str__(self):
        """Return string representation of the prompt."""
        return self.formatted_prompt
    
    def __repr__(self):
        """Return detailed representation for debugging."""
        return f"Prompt(user_input='{self.user_input}')"
    
    def optimize_prompt(self):
        """Optimize the prompt (to be implemented with AI service)."""
        from app.services.prompt_optimizer import optimize_prompt
        return optimize_prompt(self)
    
    def evaluate_prompt(self):
        """Evaluate the prompt quality."""
        from app.services.prompt_optimizer import evaluate_prompt
        return evaluate_prompt(self)

    def optimize_prompt(self):
        # Implement logic for optimizing the prompt
        pass

    def evaluate_prompt(self):
        # Implement logic for evaluating the prompt
        pass