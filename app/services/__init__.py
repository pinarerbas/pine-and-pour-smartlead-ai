from flask import Flask, jsonify
from flask_cors import CORS

from config import DevelopmentConfig
from app.database import init_db
from app.routes import pages_bp, api_bp


def create_app():
    app = Flask(__name__)

    # Ayarlari yukle
    app.config.from_object(DevelopmentConfig)

    # CORS'u ac
    CORS(app, origins=app.config["CORS_ORIGINS"])

    # Veritabanini hazirla
    init_db(app)

    # Blueprint'leri kaydet
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)

    # Sunucu saglik kontrolu
    @app.route("/health")
    def health():
        return jsonify({
            "basari": True,
            "durum": "calisiyor"
        })

    return app
