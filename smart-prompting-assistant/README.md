# Smart AI Prompting Assistant

This project is a web application designed to assist users in optimizing their prompts for AI interactions. It provides tools for automating prompt optimization, evaluating different prompt strategies, and improving overall AI interaction.

## Objectives

1. **Automate Prompt Optimization**: 
   - Implement algorithms to automatically refine user prompts for better performance with AI models.
   - Provide a user-friendly interface for inputting and receiving optimized prompts.

2. **Evaluate Prompt Strategies**: 
   - Develop methods to assess the effectiveness of various prompt strategies.
   - Allow users to compare and select the most effective prompts based on evaluation metrics.

3. **Improve AI Interaction**: 
   - Enhance user experience by facilitating seamless interactions with AI models.
   - Offer recommendations for prompt adjustments based on user intent and feedback.

## Project Structure

- **app/**: Contains the main application code.
  - **routes/**: Defines the routes for handling user requests.
  - **models/**: Contains data models for prompts and evaluations.
  - **services/**: Implements the core logic for prompt optimization and evaluation.
  - **static/**: Holds static files like CSS and JavaScript.
  - **templates/**: Contains HTML templates for rendering the web pages.

- **tests/**: Includes unit tests for the application components.

- **config.py**: Configuration settings for the Flask application.

- **requirements.txt**: Lists the core dependencies required for the project.

- **requirements-ai.txt**: Optional AI model dependencies (Gemini, OpenAI, etc.).

- **.env.example**: Example environment configuration file for AI models.

- **run.py**: Entry point for running the Flask application.

- **setup.bat**: Automated setup script for Windows.

- **start_app.bat**: Quick start script to run the application.

## Setup Instructions

### Prerequisites
- Windows OS
- Python 3.8 or higher installed and added to PATH
  - Download from [python.org](https://www.python.org/downloads/)
  - During installation, check "Add Python to PATH"

### Quick Setup (Recommended)

**For first-time users**, simply run the automated setup script:

1. Clone the repository:
   ```bash
   git clone https://github.com/umarb2708/Smart-AI-Prompt.git
   ```

2. Navigate to the project directory:
   ```bash
   cd smart-prompting-assistant
   ```

3. Run the setup script:
   ```bash
   setup.bat
   ```

The script will automatically:
- ✅ Check if Python is installed
- ✅ Create a virtual environment
- ✅ Install pip (if needed)
- ✅ Install all required dependencies
- ✅ Provide clear error messages if anything goes wrong

### Running the Application

After setup, you can start the application in two ways:

**Option 1: Quick Start** (Easiest)
Simply double-click `start_app.bat` or run:
```bash
start_app.bat
```

**Option 2: Manual Start**
```bash
venv\Scripts\activate
python run.py
```

Once running, open your web browser and go to `http://127.0.0.1:5000` to access the application.

### AI Model Configuration

The application supports multiple AI backends. Configure your preferred AI model by creating a `.env` file in the project root directory.

**Quick Start:** Copy the example configuration file:
```bash
copy .env.example .env
```
Then edit the `.env` file and uncomment your preferred AI provider settings.

#### Option 1: Google Gemini API

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

2. Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   AI_MODEL_TYPE=gemini
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL=gemini-pro
   PROMPT_MAX_LENGTH=8192
   ```

3. Install the Google Generative AI package:
   ```bash
   pip install google-generativeai
   ```
   Or install all optional AI dependencies:
   ```bash
   pip install -r requirements-ai.txt
   ```

#### Option 2: Local AI Models (Ollama/LM Studio)

**Using Ollama:**

1. Install Ollama from [ollama.ai](https://ollama.ai)

2. Pull a model (e.g., llama2, mistral, codellama):
   ```bash
   ollama pull llama2
   ```

3. Start Ollama server (runs on http://localhost:11434):
   ```bash
   ollama serve
   ```

4. Configure `.env` file:
   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   AI_MODEL_TYPE=ollama
   AI_MODEL_ENDPOINT=http://localhost:11434/api/generate
   OLLAMA_MODEL=llama2
   PROMPT_MAX_LENGTH=2048
   ```

**Using LM Studio:**

1. Download and install [LM Studio](https://lmstudio.ai/)

2. Download a model through LM Studio's interface

3. Start the local server in LM Studio (default: http://localhost:1234)

4. Configure `.env` file:
   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   AI_MODEL_TYPE=lmstudio
   AI_MODEL_ENDPOINT=http://localhost:1234/v1/chat/completions
   LM_STUDIO_MODEL=local-model
   PROMPT_MAX_LENGTH=4096
   ```

#### Option 3: OpenAI API

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

2. Configure `.env` file:
   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   AI_MODEL_TYPE=openai
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-3.5-turbo
   PROMPT_MAX_LENGTH=4096
   ```

3. Install the OpenAI package:
   ```bash
   pip install openai
   ```

**Note:** After creating or updating the `.env` file, restart the application for changes to take effect.

### Manual Setup (Alternative)

If you prefer to set up manually:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd smart-prompting-assistant
   ```

3. Create virtual environment:
   ```bash
   python -m venv venv --without-pip
   ```

4. Activate virtual environment:
   ```bash
   venv\Scripts\activate
   ```

5. Install pip (if needed):
   ```bash
   python get-pip.py
   ```

6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

7. Run the application:
   ```bash
   python run.py
   ```

### Troubleshooting

**Python Not Found:**
- Ensure Python is installed and added to PATH
- Restart your terminal after installing Python

**PowerShell Execution Policy Error:**
If using PowerShell and encountering script execution errors:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Virtual Environment Activation Issues:**
Use CMD instead of PowerShell, or use the batch scripts provided.

## Usage Guidelines

- Use the homepage to input your prompts and receive optimized suggestions.
- Navigate to the evaluation page to compare different prompt strategies.
- Interact with the AI using the optimized prompts provided by the application.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.
