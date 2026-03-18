# Smart AI Prompting Assistant - Project Report

## Introduction
Smart AI Prompting Assistant is a Flask-based web application that helps users improve the quality of prompts used with large language models. It is designed around three core outcomes:

1. Prompt optimization for better response quality.
2. Strategy-oriented prompting support (zero-shot, few-shot, chain-of-thought).
3. AI model recommendation guidance based on detected task type.

The project includes both a browser-based interface and API-style endpoints for prompt processing.

## Project Architecture
The project follows a layered Flask application structure with clear separation between request handling, domain objects, and business logic.

- Entry and configuration layer
  - `run.py`: Launches the Flask app.
  - `config.py`: Loads environment variables and AI/provider settings.

- Application factory and routing layer
  - `app/__init__.py`: Creates app instance and registers blueprints.
  - `app/routes/`: Contains web/API routes split by concern.

- Domain model layer
  - `app/models/`: Prompt and evaluation model classes.

- Service layer
  - `app/services/`: Optimization engine, model recommendation, strategy evaluation, and AI interaction abstraction.

- Presentation layer
  - `app/templates/`: Jinja2 HTML views.
  - `app/static/`: CSS and JavaScript assets.

- Validation layer
  - `tests/`: Unit/integration-style tests for models, routes, and services.

High-level request path:
User input -> Flask route -> Model creation -> Service processing -> Template rendering or JSON response.

## Module-wise Code Explanation
### 1. Entry and Configuration
- `run.py`
  - Imports and initializes the Flask application using `create_app()`.
  - Runs the app in debug mode when executed directly.

- `config.py`
  - Uses `python-dotenv` to load `.env` values.
  - Stores app-level settings (`SECRET_KEY`, `DEBUG`, `DATABASE_URI`).
  - Stores AI backend configuration:
    - `AI_MODEL_TYPE`, endpoint URL, and provider-specific keys/model names.
  - Defines global prompt constraints like `PROMPT_MAX_LENGTH`.

### 2. App Factory
- `app/__init__.py`
  - Creates Flask app instance.
  - Loads `Config` object.
  - Registers three blueprints:
    - `main`
    - `prompts_bp`
    - `evaluation_bp`

### 3. Routes
- `app/routes/main.py`
  - Provides page routes for `/`, `/optimize`, `/evaluate`, and `/interact`.
  - Includes placeholder post handlers that currently echo or pass-through values.

- `app/routes/prompts.py`
  - `/prompts` (POST JSON): accepts prompt input and returns:
    - optimized prompt result
    - model recommendation summary
  - `/handle` (POST form): used by homepage form to optimize and render `optimize.html`.
  - `/optimize` (GET): renders optimization page.
  - `/prompts/reformat` (POST JSON): returns reformatted prompt.

- `app/routes/evaluation.py`
  - `/evaluate` (GET): renders evaluation page.
  - `/evaluate` (POST JSON): evaluates strategy list and returns JSON.
  - `/evaluate/<strategy_id>` (GET): fetches one evaluation result.

### 4. Models
- `app/models/prompt.py`
  - `Prompt` class stores raw and formatted user prompt text.
  - Includes formatting helpers and compatibility properties.
  - Contains duplicate method definitions for optimization/evaluation where later placeholders override earlier methods.

- `app/models/evaluation.py`
  - `Evaluation` class stores strategies and provides:
    - `analyze()` to score each strategy
    - `evaluate_strategy()` placeholder scoring logic
    - `select_best_strategy()` to pick highest success rate

### 5. Services
- `app/services/prompt_optimizer.py`
  - Core optimization engine (`PromptOptimizer`).
  - Categorizes prompts into:
    - zero-shot
    - few-shot
    - chain-of-thought
  - Applies category-specific prompt enhancement.
  - Exposes convenience functions:
    - `optimize_prompt()`
    - `evaluate_prompt()`
    - `reformat_prompt()`

- `app/services/model_recommender.py`
  - Loads model metadata from `ai_models_database.txt`.
  - Detects prompt task types via keyword mapping.
  - Scores and returns top model recommendations with reasons.
  - Produces recommendation summary (tasks, recommendations, complexity).

- `app/services/ai_interaction.py`
  - Defines `AIInteractionService` abstraction for:
    - recommending prompt text by intent
    - interacting with model object (`generate_response`)
    - evaluating interaction success

- `app/services/strategy_evaluator.py`
  - Maintains strategy collection.
  - Evaluates all strategies and selects best one.

### 6. Frontend Templates and Static Assets
- `app/templates/index.html`
  - Main landing page and optimization form.

- `app/templates/optimize.html`
  - Displays category, original prompt, optimized prompt, and model recommendations.

- `app/templates/evaluate.html`
  - Displays strategy evaluation table.

- `app/templates/interact.html`
  - Basic AI interaction form and response container.

- `app/templates/base.html`
  - Shared layout structure with navigation and footer.

- `app/static/css/style.css`
  - Base styling for forms, layout, and result panels.

- `app/static/js/main.js`
  - Currently empty; no active global front-end behavior is defined here.

### 7. Tests
- `tests/test_models.py`, `tests/test_routes.py`, `tests/test_services.py`
  - Intended to validate model behavior, route responses, and service logic.
  - Some tests reflect earlier interfaces and may not align with current implementations.

## Working Flow
### A. Setup and Startup
1. Run `setup.bat` or `setup.ps1`.
2. Script verifies Python, creates/activates virtual environment, installs dependencies, and prepares `.env`.
3. Run `start_app.bat` or `python run.py`.
4. Flask starts at `http://127.0.0.1:5000`.

### B. Prompt Optimization Flow (Primary)
1. User enters prompt on homepage (`/`).
2. Form posts to `/handle`.
3. Route creates `Prompt` object.
4. `optimize_prompt()` in service:
   - categorizes prompt type
   - applies matching optimization strategy
5. `get_recommendation_summary()` returns best-fit AI model suggestions.
6. `optimize.html` renders:
   - prompt category + reasoning
   - original and optimized prompt
   - model recommendations and scores

### C. API-style Flow
1. Client sends JSON to `/prompts`.
2. Backend returns structured JSON with optimized prompt and recommendations.
3. Client can also call `/prompts/reformat` to normalize prompt formatting.

### D. Evaluation Flow
1. Client sends list of strategies to `/evaluate` (POST JSON).
2. Evaluation model analyzes each strategy.
3. Result JSON returns comparative strategy performance.

## Technology Stack
- Language: Python 3.8+
- Web framework: Flask 3.x
- Template engine: Jinja2
- Environment management: python-dotenv
- HTTP communication: requests
- Data/ML utilities in dependencies: numpy, pandas, scikit-learn
- Optional AI integrations: google-generativeai, openai, transformers, torch
- Deployment server: gunicorn
- Frontend: HTML, CSS, JavaScript
- Platform scripts: Windows Batch and PowerShell setup/start scripts

## Key Features
1. Prompt categorization into zero-shot, few-shot, and chain-of-thought modes.
2. Automatic prompt enhancement with strategy-specific scaffolding.
3. Prompt quality scoring and prompt reformatting utilities.
4. Model recommendation engine based on detected task type and model metadata.
5. Multi-provider readiness through environment-based AI configuration.
6. Flask blueprint-based modular architecture.
7. Browser UI and JSON API support for prompt workflows.
8. Windows-friendly setup automation with `setup.bat`, `setup.ps1`, and `start_app.bat`.

## Conclusion
The Smart AI Prompting Assistant is structured as a modular Flask application with a practical optimization core and model recommendation support. The current implementation already demonstrates a strong base for prompt engineering workflows, while some modules and tests appear to be in transition and can be further aligned for production stability.
