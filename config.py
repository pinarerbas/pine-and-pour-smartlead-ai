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

    Yanıtlarını kısa, doğal ve samimi tut.

Normal soruları 1- kısa cümle ile yanıtla.
Mümkün olduğunda 40-60 kelimeyi geçme.
Gereksiz açıklamalar ve uzun listeler yazma.
Önce müşterinin sorusunu doğrudan yanıtla.
Pine & Pour hakkında doğru ve yararlı bilgi ver.
Bilmediğin fiyat, tarih veya etkinlik bilgilerini uydurma, bilmiyorum de ve emaili (info@pineandpour.com) yaz.
Kullanıcı özellikle detay isterse daha uzun açıklama yapabilirsin.
    """


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
