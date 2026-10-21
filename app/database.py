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

        try:
            db.execute("""
                CREATE TABLE IF NOT EXISTS leads (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isim TEXT NOT NULL,
                    telefon TEXT NOT NULL,
                    email TEXT,
                    mesaj TEXT,
                    tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Eski veritabaninda email sutunu yoksa ekle
            kolonlar = [
                satir["name"]
                for satir in db.execute(
                    "PRAGMA table_info(leads)"
                ).fetchall()
            ]

            if "email" not in kolonlar:
                db.execute(
                    "ALTER TABLE leads ADD COLUMN email TEXT"
                )

            db.commit()

        finally:
            db.close()


# Yeni lead ekler
def lead_ekle(isim, telefon, email=None, mesaj=None):
    db = get_db()

    try:
        cursor = db.execute(
            """
            INSERT INTO leads (isim, telefon, email, mesaj)
            VALUES (?, ?, ?, ?)
            """,
            (isim, telefon, email, mesaj)
        )

        db.commit()

        return cursor.lastrowid

    except sqlite3.Error:
        db.rollback()
        raise

    finally:
        db.close()


# Tum leadleri en yeniden eskiye listeler
def tum_leadler():
    db = get_db()

    try:
        satirlar = db.execute("""
            SELECT id, isim, telefon, email, mesaj, tarih
            FROM leads
            ORDER BY tarih DESC
        """).fetchall()

        return [dict(satir) for satir in satirlar]

    finally:
        db.close()
