from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///site.db')
    
    # AI Model Configuration
    AI_MODEL_TYPE = os.getenv('AI_MODEL_TYPE', 'local')  # gemini, ollama, lmstudio, openai, local
    AI_MODEL_ENDPOINT = os.getenv('AI_MODEL_ENDPOINT', 'http://localhost:5000/api/model')
    
    # Google Gemini Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-pro')
    
    # Ollama Configuration
    OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama2')
    
    # LM Studio Configuration
    LM_STUDIO_MODEL = os.getenv('LM_STUDIO_MODEL', 'local-model')
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    # General Settings
    PROMPT_MAX_LENGTH = int(os.getenv('PROMPT_MAX_LENGTH', 512))
    EVALUATION_CRITERIA = os.getenv('EVALUATION_CRITERIA', 'accuracy, relevance, creativity')