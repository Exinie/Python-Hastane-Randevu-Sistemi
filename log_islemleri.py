import sqlite3

class LogIslemleri:

    def __init__(self):

        """
        Sınıfın init metotunda diğer metodların kullanabilmesi için veritabanı dosya konumu tanımlandı.
        """

        self.veritabani_dosyasi = "veritabani.db"

    def log_kaydi_olustur(self, kullanici_turu, kullanici_id, yapilan_islem):

        """
        Yapılan işlem bilgisini ve işlemi yapan kullanıcı türünü ve id değerini alıp LOG_KAYITLARI tablosuna ekleyen metot.
        """

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            cursor = baglanti.cursor()
            cursor.execute("INSERT INTO LOG_KAYITLARI (kullanici_turu, kullanici_id, islem) VALUES (?,?,?)",
                           (kullanici_turu, kullanici_id, yapilan_islem))
            baglanti.commit()

            print(f"[LOG] {kullanici_turu}, {kullanici_id}, {yapilan_islem}")

            return True
        except sqlite3.Error as e:
            print(f"[LOG] Günlük kaydı alınamadı, hata: {e}")
            return None
        finally:
            baglanti.close()

    def log_kayitlarini_listele(self):

        """
        LOG_KAYITLARI tablosundaki tüm satırları listeyen metot.
        """

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            cursor = baglanti.cursor()
            cursor.execute("SELECT * FROM LOG_KAYITLARI")

            gelen_veriler = cursor.fetchall()

            return gelen_veriler
        except sqlite3.Error as e:
            print(f"[LOG] Günlük kayıtları listelenemedi, hata: {e}")
            return None
        finally:
            baglanti.close()