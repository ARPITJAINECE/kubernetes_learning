from flask import Flask
from app.api.routes import main_bp

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )
    app.register_blueprint(main_bp)
    return app
