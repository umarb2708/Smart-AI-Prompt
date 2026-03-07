from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Register blueprints
    from .routes.main import main
    from .routes.prompts import prompts_bp
    from .routes.evaluation import evaluation_bp
    
    app.register_blueprint(main)
    app.register_blueprint(prompts_bp)
    app.register_blueprint(evaluation_bp)

    return app