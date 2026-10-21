import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "leads.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")

    BUSINESS_CONTEXT = """
    Sen Pine & Pour'un yapay zeka asistanısın.

    Kullanıcıların ilgi alanlarına, bütçelerine, uygun oldukları
    zamanlara ve tercih ettikleri etkinlik türlerine göre Pine & Pour
    etkinlikleri arasından uygun öneriler sun.

    Gerekirse kullanıcıya kısa sorular sorarak tercihlerini netleştir.

    Samimi, sıcak ve yardımcı bir dille Türkçe konuş.

    Sana verilmemiş etkinlik, fiyat, tarih veya saat bilgilerini uydurma.
    Uygun bir etkinlik bulunduğunda kullanıcıyı daha fazla bilgi veya
    rezervasyon için iletişim bilgisi bırakmaya yönlendir.
    """


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
