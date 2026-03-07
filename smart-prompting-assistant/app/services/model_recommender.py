import re
from typing import List, Dict, Tuple

class ModelRecommender:
    def __init__(self):
        self.models_database = []
        self.load_models_database()
        
        # Task keywords mapping
        self.task_keywords = {
            'coding': ['code', 'program', 'develop', 'debug', 'script', 'function', 'algorithm', 'software', 'api', 'bug'],
            'writing': ['write', 'essay', 'article', 'blog', 'content', 'story', 'poem', 'creative', 'draft'],
            'analysis': ['analyze', 'research', 'study', 'investigate', 'examine', 'evaluate', 'compare', 'assess'],
            'math': ['calculate', 'solve', 'math', 'equation', 'formula', 'statistics', 'probability'],
            'translation': ['translate', 'language', 'multilingual', 'localization', 'convert language'],
            'summarization': ['summarize', 'summary', 'condense', 'brief', 'overview', 'recap'],
            'image': ['image', 'picture', 'photo', 'visual', 'generate image', 'create image', 'dall-e'],
            'conversation': ['chat', 'conversation', 'talk', 'discuss', 'dialogue'],
            'reasoning': ['explain', 'reason', 'why', 'how', 'understand', 'complex', 'detailed'],
            'creative': ['creative', 'artistic', 'design', 'imagination', 'innovative', 'brainstorm'],
        }
    
    def load_models_database(self):
        """Load AI models from the database file."""
        try:
            with open('ai_models_database.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            for line in lines:
                line = line.strip()
                # Skip comments and empty lines
                if line.startswith('#') or not line or '|' not in line:
                    continue
                
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 5:
                    self.models_database.append({
                        'name': parts[0],
                        'category': parts[1],
                        'best_for': parts[2],
                        'strengths': parts[3],
                        'context': parts[4]
                    })
        except FileNotFoundError:
            # If file not found, use default models
            self._load_default_models()
    
    def _load_default_models(self):
        """Fallback default models if database file is not found."""
        self.models_database = [
            {
                'name': 'GPT-4 Turbo',
                'category': 'General Purpose',
                'best_for': 'Complex reasoning, analysis, coding',
                'strengths': 'Excellent reasoning, large context',
                'context': '128K tokens'
            },
            {
                'name': 'Claude 3 Opus',
                'category': 'Advanced Writing',
                'best_for': 'Long-form content, analysis',
                'strengths': 'Excellent writing, nuanced understanding',
                'context': '200K tokens'
            },
            {
                'name': 'Gemini Pro',
                'category': 'General Purpose',
                'best_for': 'Multi-modal tasks, long context',
                'strengths': 'Large context window, versatile',
                'context': '32K tokens'
            }
        ]
    
    def detect_task_type(self, prompt: str) -> List[str]:
        """Detect the type of task from the prompt."""
        prompt_lower = prompt.lower()
        detected_tasks = []
        
        for task_type, keywords in self.task_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_tasks.append(task_type)
        
        # Default to general if no specific task detected
        if not detected_tasks:
            detected_tasks.append('general')
        
        return detected_tasks
    
    def recommend_models(self, prompt: str, top_n: int = 3) -> List[Dict]:
        """
        Recommend AI models based on the prompt content.
        Returns top N recommended models with explanations.
        """
        detected_tasks = self.detect_task_type(prompt)
        scored_models = []
        
        for model in self.models_database:
            score = 0
            reasons = []
            
            # Score based on detected tasks
            model_text = f"{model['category']} {model['best_for']} {model['strengths']}".lower()
            
            for task in detected_tasks:
                if task in model_text or task in model['category'].lower():
                    score += 10
                    reasons.append(f"Suited for {task} tasks")
            
            # Additional scoring based on keywords in prompt
            for keyword in self.task_keywords.get(detected_tasks[0] if detected_tasks else 'general', []):
                if keyword in model_text:
                    score += 2
            
            # Boost for general purpose models if no specific task
            if 'general' in detected_tasks and 'general purpose' in model['category'].lower():
                score += 5
                reasons.append("Versatile for general tasks")
            
            # Add context window consideration for long prompts
            if len(prompt) > 1000:
                if 'large context' in model['strengths'].lower() or '100k' in model['context'].lower() or '128k' in model['context'].lower() or '200k' in model['context'].lower():
                    score += 5
                    reasons.append("Large context window for detailed tasks")
            
            if score > 0:
                scored_models.append({
                    'model': model,
                    'score': score,
                    'reasons': reasons if reasons else ['Good general-purpose option']
                })
        
        # Sort by score and return top N
        scored_models.sort(key=lambda x: x['score'], reverse=True)
        return scored_models[:top_n]
    
    def get_recommendation_summary(self, prompt: str) -> Dict:
        """
        Get a comprehensive recommendation summary.
        """
        detected_tasks = self.detect_task_type(prompt)
        recommendations = self.recommend_models(prompt, top_n=3)
        
        return {
            'detected_tasks': detected_tasks,
            'recommended_models': recommendations,
            'prompt_length': len(prompt),
            'complexity': 'high' if len(prompt) > 500 else 'medium' if len(prompt) > 200 else 'low'
        }


# Create a default instance
_recommender = ModelRecommender()

def recommend_models(prompt: str, top_n: int = 3) -> List[Dict]:
    """Standalone function to recommend models."""
    return _recommender.recommend_models(prompt, top_n)

def get_recommendation_summary(prompt: str) -> Dict:
    """Standalone function to get recommendation summary."""
    return _recommender.get_recommendation_summary(prompt)
