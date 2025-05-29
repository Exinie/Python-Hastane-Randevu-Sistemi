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
        self._log_tablosu()

        self.yonetici_ekle('admin', '123')

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
            sifre TEXT NOT NULL   
        )
        ''')

    def yonetici_ekle(self, kullanici_adi, sifre):
        """ Yönetici ekleme fonksiyonu (manuel kontrol) """
        self.cursor.execute('SELECT * FROM YONETICILER WHERE kullanici_adi = ?', (kullanici_adi,))
        if self.cursor.fetchone():
            print(f"{kullanici_adi} zaten mevcut, eklenmedi.")
            return

        self.cursor.execute('''
            INSERT INTO YONETICILER (kullanici_adi, sifre)
            VALUES (?, ?)
        ''', (kullanici_adi, sifre))
        self.conn.commit()
        print(f"{kullanici_adi} isimli yönetici eklendi.")

    def _randevular_tablosu(self):
        """ Randevular tablosunu oluşturma fonksiyonu """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS RANDEVULAR (
            randevu_id INTEGER PRIMARY KEY AUTOINCREMENT,
            hasta_id INTEGER,
            doktor_id INTEGER,
            tarih TEXT NOT NULL,
            saat TEXT NOT NULL,
            sikayet TEXT,                
            durum TEXT DEFAULT 'Incelenmesi Bekleniyor',
            FOREIGN KEY (hasta_id) REFERENCES HASTALAR(hasta_id),
            FOREIGN KEY (doktor_id) REFERENCES DOKTORLAR(doktor_id)
        )
        ''')
    def _log_tablosu(self):
        """ Log kayıtları tablosu için olan kod bloğu """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS LOG_KAYITLARI (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_turu TEXT NOT NULL,
            kullanici_id INTEGER,
            islem TEXT NOT NULL,
            tarih_saat TEXT DEFAULT (datetime('now', 'localtime'))
        )
        ''')

        # Burda her şey commitlenip kaydedildi, ardından veritabanı bağlantısı kapatıldı
    #def commit_kapat(self):
        #self.conn.commit()
        #self.conn.close()

        #print("Veritabanı bağlantısı kapatıldı.")
    