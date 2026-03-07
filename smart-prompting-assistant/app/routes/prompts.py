from flask import Blueprint, request, jsonify
from app.models.prompt import Prompt
from app.services.prompt_optimizer import optimize_prompt

prompts_bp = Blueprint('prompts', __name__)

@prompts_bp.route('/prompts', methods=['POST'])
def create_prompt():
    data = request.json
    user_input = data.get('input')
    
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400
    
    prompt = Prompt(user_input)
    optimized_prompt = optimize_prompt(prompt)
    
    return jsonify({'optimized_prompt': optimized_prompt}), 200

@prompts_bp.route('/prompts/reformat', methods=['POST'])
def reformat_prompt():
    data = request.json
    prompt_text = data.get('prompt')
    
    if not prompt_text:
        return jsonify({'error': 'No prompt provided'}), 400
    
    prompt = Prompt(prompt_text)
    reformatted_prompt = prompt.reformat()
    
    return jsonify({'reformatted_prompt': reformatted_prompt}), 200