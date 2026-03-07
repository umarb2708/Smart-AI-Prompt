from flask import Blueprint, request, jsonify, render_template, redirect, url_for
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

@prompts_bp.route('/handle', methods=['POST'])
def handle_prompt():
    user_input = request.form.get('user_input')
    
    if not user_input:
        return redirect(url_for('main.index'))
    
    prompt = Prompt(user_input)
    optimized_prompt = optimize_prompt(prompt)
    
    return render_template('optimize.html', optimized_prompts=[optimized_prompt])

@prompts_bp.route('/optimize', methods=['GET'])
def optimize():
    return render_template('optimize.html', optimized_prompts=[])

@prompts_bp.route('/prompts/reformat', methods=['POST'])
def reformat_prompt():
    data = request.json
    prompt_text = data.get('prompt')
    
    if not prompt_text:
        return jsonify({'error': 'No prompt provided'}), 400
    
    prompt = Prompt(prompt_text)
    reformatted_prompt = prompt.reformat()
    
    return jsonify({'reformatted_prompt': reformatted_prompt}), 200