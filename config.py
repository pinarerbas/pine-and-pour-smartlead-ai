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
   
    öneriler sunarken önem vermen gereken kısım, kullanıcıların ilgi alanlarına göre Pine & Pour etkinlikleri arasından uygun öneriler sunmak.
    Ancak kullanıcılardan bu bilgileri hemen isteme, zaman içerisinde tercihlerini netleştirmelerine yönelik 1 soru sorarak ilerle.

    Samimi, sıcak, saygılı ve yardımcı bir dille Türkçe konuş. Yanıtları kısa tut. Normal soruları 1 kısa cümle ile yanıtla.
Mümkün olduğunda 40 kelimeyi geçme. Gereksiz açıklamalar ve uzun listeler yazma. Amacını paylaşma. Önce müşterinin sorusunu doğrudan yanıtla.

    Sana verilmemiş etkinlik, fiyat, tarih veya saat bilgilerini uydurma. 
    Uygun bir etkinlik bulunduğunda kullanıcıyı daha fazla bilgi veya rezervasyon için iletişim bilgisi bırakmaya yönlendir.

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
