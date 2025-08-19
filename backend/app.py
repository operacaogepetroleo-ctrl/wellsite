# backend/app.py
from __future__ import annotations
import os
from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # CORS a partir da env var; aceita lista separada por vírgula
    origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",") if o.strip()]
    CORS(app, resources={r"/api/*": {"origins": origins}})

    @app.get("/api/health")
    def health():
        return jsonify(status="ok")

    # registra suas rotas de IA
    try:
        from .api_ai import bp_ai
        app.register_blueprint(bp_ai)
    except Exception as e:
        # Deixa claro no log se deu erro de import
        app.logger.exception("Falha ao registrar blueprint api_ai: %s", e)
        raise

    return app
