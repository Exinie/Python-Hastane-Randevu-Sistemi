import sqlite3

'''
Bu fonksiyon veritabanı boşsa gerekli tabloları oluşturur, ya da eksik tablo varsa onarımı gerçekleştirir.
'''

def veritabanini_kur():
    # Burda veritabanı bağlantısı kuruldu
    conn = sqlite3.connect('veritabani.db')
    cursor = conn.cursor()

    # Burda veritabanı tablolarının oluşturulma sql komutları çalıştırılıyor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DOKTORLAR (
        doktor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        soyad TEXT NOT NULL,
        uzmanlik TEXT NOT NULL,
        telefon TEXT,
        email TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HASTALAR (
        hasta_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        soyad TEXT NOT NULL,
        dogum_tarihi TEXT,
        telefon TEXT,
        adres TEXT,
        bilinen_rahatsizliklar TEXT
    )
    ''')    

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS YONETICILER (
        yonetici_id INTEGER PRIMARY KEY AUTOINCREMENT,
        kullanici_adi TEXT NOT NULL,
        pozisyon TEXT NOT NULL,
        telefon TEXT,
        email TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS RANDEVULAR (
        randevu_id INTEGER PRIMARY KEY AUTOINCREMENT,
        hasta_id INTEGER,
        doktor_id INTEGER,
        tarih TEXT NOT NULL,
        saat TEXT NOT NULL,
        durum TEXT DEFAULT 'Incelenmesi Bekleniyor',
        FOREIGN KEY (hasta_id) REFERENCES Hastalar(hasta_id),
        FOREIGN KEY (doktor_id) REFERENCES Doktorlar(doktor_id)
    )
    ''')

    # Burda her şey commitlenip kaydedildi, ardından veritabanı bağlantısı kapatıldı
    conn.commit()
    conn.close()

    print("Veritabanı oluşturuldu veya hasar görmüşse onarıldı")