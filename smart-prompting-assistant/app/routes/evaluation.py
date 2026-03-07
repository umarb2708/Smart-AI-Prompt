from flask import Blueprint, request, jsonify, render_template
from app.models.evaluation import Evaluation

evaluation_bp = Blueprint('evaluation', __name__)

@evaluation_bp.route('/evaluate', methods=['GET'])
def evaluate():
    return render_template('evaluate.html')

@evaluation_bp.route('/evaluate', methods=['POST'])
def evaluate_prompt():
    data = request.json
    prompt_strategies = data.get('strategies', [])
    
    evaluation = Evaluation()
    results = evaluation.analyze_strategies(prompt_strategies)
    
    return jsonify(results), 200

@evaluation_bp.route('/evaluate/<strategy_id>', methods=['GET'])
def get_evaluation(strategy_id):
    evaluation = Evaluation()
    result = evaluation.get_evaluation_result(strategy_id)
    
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Evaluation not found'}), 404