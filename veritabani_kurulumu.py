import sqlite3


class Veritabani:
    def __init__(self, db_adi='veritabani.db'):
        self.db_adi = db_adi
        self.conn = sqlite3.connect(self.db_adi)
        self.cursor = self.conn.cursor()
        self.veritabanini_kur()

    def veritabanini_kur(self):
        """Bu fonksiyon veritabanı boşsa gerekli tabloları oluşturur, ya da eksik tablo varsa onarımı gerçekleştirir."""
        self._doktorlar_tablosu()
        self._hastalar_tablosu()
        self._yoneticiler_tablosu()
        self._randevular_tablosu()
        self._kullanicilar_tablosu()

        veritabani.yonetici_ekle('yonetici', 'yonetici000', 'ful yetki')

        print("veritabanı oluşturuldu ya da hasar görmüşse onarılmıştır.")

    """ Burada doktorlar, hastalar, yöneticiler, randevular ve kullanıcılar tabloları oluşturan kodlar bulunuyor """

    def _doktorlar_tablosu(self):
        self.cursor.execute('''
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
    def _hastalar_tablosu(self):
        self.cursor.execute('''
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
    def _yoneticiler_tablosu(self):    
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS YONETICILER (
            yonetici_id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT NOT NULL UNIQUE,
            sifre TEXT NOT NULL,
            yetki TEXT NOT NULL    
        )
        ''')
        # yetki sütununu ekledim
        try:
            self.cursor.execute("ALTER TABLE YONETICILER ADD COLUMN yetki TEXT")
        except sqlite3.OperationalError:
            pass

    def yonetici_ekle(self, kullanici_adi, sifre, yetki = 'yonetici'):   
        """ Yönetici ekleme fonksiyonu"""
        self.cursor.execute('''
        INSERT OR IGNORE INTO YONETICILER (kullanici_adi, sifre, yetki)
        VALUES (?, ?, ?)
        ''', (kullanici_adi, sifre, yetki))
        self.conn.commit()
        print(f"{kullanici_adi} isimli yönetici eklendi.")    

    def _randevular_tablosu(self):
        self.cursor.execute('''
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
    
    def _kullanicilar_tablosu(self):    
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            kullanici_adi TEXT PRIMARY KEY,
            sifre TEXT,
            yetki TEXT              
        )         
        """)

        # Burda her şey commitlenip kaydedildi, ardından veritabanı bağlantısı kapatıldı
    def commit_kapat(self):
        self.conn.commit()
        self.conn.close()

        print("Veritabanı bağlantısı kapatıldı.")
        
veritabani = Veritabani()
veritabani.commit_kapat()