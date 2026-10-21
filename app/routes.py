from flask import Blueprint, request, jsonify, render_template

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError


# Sayfalar icin Blueprint
pages_bp = Blueprint("pages", __name__)


# API icin Blueprint
api_bp = Blueprint("api", __name__, url_prefix="/api")


# Ana sayfa
@pages_bp.route("/")
def ana_sayfa():
    return render_template("index.html")


# Yonetim paneli
@pages_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Yapay zeka sohbet endpoint'i
@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json(silent=True) or {}

    mesaj = data.get("mesaj", "").strip()
    gecmis = data.get("gecmis", [])

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj alani bos olamaz."
        }), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify({
            "basari": True,
            "cevap": cevap
        })

    except AIServiceError as hata:
        return jsonify({
            "basari": False,
            "hata": str(hata)
        }), 503


# Yeni lead kaydet
@api_bp.route("/leads", methods=["POST"])
def yeni_lead():
    data = request.get_json(silent=True) or {}

    isim = data.get("isim", "").strip()
    telefon = data.get("telefon", "").strip()
    email = data.get("email", "").strip()
    mesaj = data.get("mesaj", "").strip()

    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "Isim ve telefon zorunludur."
        }), 400

    try:
        lead_id = lead_ekle(
            isim,
            telefon,
            email,
            mesaj
        )

        return jsonify({
            "basari": True,
            "id": lead_id
        }), 201

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Kayit sirasinda bir hata olustu."
        }), 500


# Tum leadleri getir
@api_bp.route("/leads", methods=["GET"])
def leadleri_getir():
    try:
        leadler = tum_leadler()

        return jsonify({
            "basari": True,
            "leadler": leadler
        })

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Kayitlar getirilemedi."
        }), 500
