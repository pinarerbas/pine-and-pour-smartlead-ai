import sqlite3
from flask import current_app


# Veritabanina baglanir
def get_db():
    db = sqlite3.connect(current_app.config["DATABASE_URL"])
    db.row_factory = sqlite3.Row
    return db


# Leads tablosunu olusturur
def init_db(app):
    with app.app_context():
        db = get_db()

        db.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        db.commit()
        db.close()


# Yeni lead kaydeder
def lead_ekle(isim, telefon, mesaj=None):
    db = get_db()

    try:
        cursor = db.execute(
            "INSERT INTO leads (isim, telefon, mesaj) VALUES (?, ?, ?)",
            (isim, telefon, mesaj)
        )

        db.commit()
        return cursor.lastrowid

    except sqlite3.Error:
        db.rollback()
        raise

    finally:
        db.close()


# Tum leadleri en yeniden eskiye getirir
def tum_leadler():
    db = get_db()

    try:
        satirlar = db.execute("""
            SELECT id, isim, telefon, mesaj, tarih
            FROM leads
            ORDER BY tarih DESC
        """).fetchall()

        return [dict(satir) for satir in satirlar]

    finally:
        db.close()
