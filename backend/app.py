# backend/app.py
from __future__ import annotations
import os, traceback
from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",") if o.strip()]
    CORS(app, resources={r"/api/*": {"origins": origins}})

    @app.get("/api/health")
    def health():
        return jsonify(status="ok")

    # Handler simples para ver erro como JSON (útil no Render)
    @app.errorhandler(Exception)
    def handle_err(e):
        app.logger.exception("Unhandled error: %s", e)
        return jsonify(error=str(e)), 500

    # Tenta registrar a API de IA; se falhar, não derruba o /health
    try:
        from .api_ai import bp_ai
        app.register_blueprint(bp_ai)
    except Exception as e:
        app.logger.error("Falha ao registrar blueprint api_ai: %s\n%s", e, traceback.format_exc())
        # Mantém a app viva; /api/ai/* não funcionará até corrigir o erro.
        # Para inspecionar o erro via HTTP:
        @app.get("/api/ai/status")
        def ai_status():
            return jsonify(loaded=False, error=str(e)), 500

    return app
