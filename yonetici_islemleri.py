import sqlite3


class YoneticiIslemleri:

    def __init__(self, veritabani_adi="veritabani.db"):
        self.veritabani_adi = veritabani_adi

    def hastalari_listele(self):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM HASTALAR")
        veriler = cursor.fetchall()
        conn.close()
        return veriler

    def hasta_sil(self, hasta_id):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM hastalar WHERE hasta_id=?", (hasta_id,))
        conn.commit()
        conn.close()

    def doktorları_listele(self):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM DOKTORLAR")
        veriler = cursor.fetchall()
        conn.close()
        return veriler

    def doktor_sil(self, doktor_id):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM DOKTORLAR WHERE doktor_id=?", (doktor_id,))
        conn.commit()
        conn.close()

    def doktor_ekle(self, tc, ad, soyad, sifre, uzmanlik):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO DOKTORLAR (tc, ad, soyad, sifre, uzmanlik) VALUES (?, ?, ?, ?, ?)", (tc, ad, soyad, sifre, uzmanlik))
        conn.commit()
        conn.close()

    def yoneticileri_listele(self):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM YONETICILER")
        veriler = cursor.fetchall()
        conn.close()
        return veriler
        

    def yonetici_sil(self, kullanici_adi):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM YONETICILER WHERE kullanici_adi=?", (kullanici_adi,))
        conn.commit()
        conn.close()


    def yonetici_ekle(self, ad, sifre):
        conn = sqlite3.connect(self.veritabani_adi)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO YONETICILER (kullanici_adi, sifre) VALUES (?, ?)", (ad, sifre))
        conn.commit()
        conn.close()
