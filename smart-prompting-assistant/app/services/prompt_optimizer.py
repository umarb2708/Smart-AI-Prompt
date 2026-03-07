class PromptOptimizer:
    def __init__(self):
        self.optimization_strategies = {
            'clarity': self._add_clarity,
            'structure': self._add_structure,
            'specificity': self._add_specificity,
            'context': self._add_context
        }

    def optimize_prompt(self, prompt):
        """
        Optimize a prompt by applying multiple enhancement strategies.
        """
        prompt = prompt.strip()
        
        if not prompt:
            return "Please provide a prompt to optimize."
        
        # Detect prompt type and apply appropriate optimizations
        if self._is_question(prompt):
            return self._optimize_question(prompt)
        elif self._is_instruction(prompt):
            return self._optimize_instruction(prompt)
        elif self._is_creative_request(prompt):
            return self._optimize_creative_request(prompt)
        else:
            return self._optimize_general(prompt)

    def _is_question(self, prompt):
        """Check if prompt is a question."""
        return '?' in prompt or prompt.lower().startswith(('what', 'how', 'why', 'when', 'where', 'who', 'can', 'could', 'would', 'should'))

    def _is_instruction(self, prompt):
        """Check if prompt is an instruction."""
        instruction_words = ['write', 'create', 'generate', 'make', 'build', 'explain', 'describe', 'list', 'summarize']
        return any(prompt.lower().startswith(word) for word in instruction_words)

    def _is_creative_request(self, prompt):
        """Check if prompt is a creative request."""
        creative_words = ['story', 'poem', 'essay', 'article', 'blog', 'script', 'song']
        return any(word in prompt.lower() for word in creative_words)

    def _optimize_question(self, prompt):
        """Optimize question-type prompts."""
        if not prompt.endswith('?'):
            prompt = prompt + '?'
        
        optimized = f"""Please provide a detailed and comprehensive answer to the following question:

{prompt}

Include:
- Clear explanations with examples where applicable
- Step-by-step reasoning if relevant
- Any important context or background information
- Practical implications or applications"""
        
        return optimized

    def _optimize_instruction(self, prompt):
        """Optimize instruction-type prompts."""
        optimized = f"""Task: {prompt}

Requirements:
- Provide a clear, well-structured response
- Include relevant details and examples
- Ensure accuracy and completeness
- Use professional and appropriate language

Please proceed with the task following these guidelines."""
        
        return optimized

    def _optimize_creative_request(self, prompt):
        """Optimize creative writing prompts."""
        optimized = f"""Creative Task: {prompt}

Guidelines:
- Be original and engaging
- Maintain consistency in tone and style
- Include vivid details and descriptions
- Ensure proper structure and flow
- Consider the target audience

Please create the content following these creative guidelines."""
        
        return optimized

    def _optimize_general(self, prompt):
        """Optimize general prompts."""
        optimized = f"""Request: {prompt}

Please provide:
- A comprehensive response addressing all aspects of the request
- Clear and structured information
- Relevant examples or explanations
- Accurate and helpful content

Respond in a clear, professional manner."""
        
        return optimized

    def _add_clarity(self, prompt):
        """Add clarity to the prompt."""
        return f"Please clearly explain: {prompt}"

    def _add_structure(self, prompt):
        """Add structure to the prompt."""
        return f"Provide a structured response to: {prompt}"

    def _add_specificity(self, prompt):
        """Add specificity to the prompt."""
        return f"Provide specific details about: {prompt}"

    def _add_context(self, prompt):
        """Add context to the prompt."""
        return f"With appropriate context, please address: {prompt}"

    def evaluate_prompt(self, prompt):
        """Evaluate the effectiveness of the prompt."""
        score = 0
        
        # Length check
        if len(prompt) > 10:
            score += 20
        if len(prompt) > 50:
            score += 20
        
        # Question mark check
        if '?' in prompt:
            score += 10
        
        # Specificity check
        specific_words = ['specific', 'detailed', 'explain', 'describe', 'how', 'what', 'why']
        if any(word in prompt.lower() for word in specific_words):
            score += 20
        
        # Structure check
        if any(char in prompt for char in [':', '\n', '-']):
            score += 15
        
        # Context check
        context_words = ['context', 'background', 'because', 'regarding', 'about']
        if any(word in prompt.lower() for word in context_words):
            score += 15
        
        return min(score, 100)

    def reformat_prompt(self, prompt):
        """Reformat the prompt for better AI interaction."""
        prompt = prompt.strip()
        
        # Capitalize first letter
        if prompt:
            prompt = prompt[0].upper() + prompt[1:]
        
        # Ensure proper punctuation
        if not prompt.endswith(('.', '?', '!')):
            prompt += '.'
        
        # Add spacing after punctuation
        prompt = prompt.replace('?', '? ').replace('.', '. ').replace('!', '! ')
        prompt = ' '.join(prompt.split())  # Remove extra spaces
        
        return prompt


# Create a default instance
_optimizer = PromptOptimizer()

# Export standalone functions for backward compatibility
def optimize_prompt(prompt):
    """Optimize a prompt using the default optimizer instance."""
    # Extract text from Prompt object or convert to string
    if hasattr(prompt, 'user_input'):
        prompt_text = prompt.user_input
    elif hasattr(prompt, 'formatted_prompt'):
        prompt_text = prompt.formatted_prompt
    elif hasattr(prompt, 'content'):
        prompt_text = prompt.content
    else:
        prompt_text = str(prompt)
    
    return _optimizer.optimize_prompt(prompt_text)

def evaluate_prompt(prompt):
    """Evaluate a prompt using the default optimizer instance."""
    return _optimizer.evaluate_prompt(prompt.content if hasattr(prompt, 'content') else str(prompt))

def reformat_prompt(prompt):
    """Reformat a prompt using the default optimizer instance."""
    return _optimizer.reformat_prompt(prompt.content if hasattr(prompt, 'content') else str(prompt))