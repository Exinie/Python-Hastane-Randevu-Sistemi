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
        tc_no TEXT NOT NULL,
        sifre TEXT NOT NULL,
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
        tc_no TEXT NOT NULL,
        sifre TEXT NOT NULL,
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
        kullanici_adi TEXT NOT NULL UNIQUE,
        sifre TEXT NOT NULL     
    )
    ''')
    #yetki sütununu ekledim
    try:
        cursor.execute("ALTER TABLE YONETICILER ADD COLUMN yetki TEXT")
    except sqlite3.OperationalError:
        pass


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

    cursor.execute('''
    INSERT OR IGNORE INTO YONETICILER (kullanici_adi, sifre, yetki)
    VALUES ('yonetici', 'yonetici000', 'yönetici')
    ''')

    #kullanıcılar tablosu 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kullanicilar (
        kullanici_adi TEXT PRIMARY KEY,
        sifre TEXT,
        yetki TEXT              
    )         
    """)
    

    # Burda her şey commitlenip kaydedildi, ardından veritabanı bağlantısı kapatıldı
    conn.commit()
    conn.close()

    print("Veritabanı oluşturuldu veya hasar görmüşse onarıldı")