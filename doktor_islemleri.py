import sqlite3


class DoktorIslemleri:
    """
    Doktorlara ait randevu işlemlerini yöneten sınıf.
    """
    def __init__(self):
        """
        Veritabanı dosyasının yolunu belirler.
        """
        self.veritabani_dosyasi = "veritabani.db"

    def randevulari_listele(self, doktor_id):
        """
        Belirtilen doktora ait tüm randevuları listeler.
        """
        conn = None
        try:
            conn = sqlite3.connect(self.veritabani_dosyasi)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT randevu_id, hasta_id, tarih, saat, sikayet, durum FROM RANDEVULAR WHERE doktor_id = ?",
                (doktor_id,)
            )
            sonuc = cursor.fetchall()
            return sonuc
        except sqlite3.Error:
            return "veritabani_hatasi"
        finally:
            if conn:
                conn.close()

    def randevu_sil(self, randevu_id):
        """
        Belirtilen randevuyu veritabanından siler.
        """
        conn = None
        try:
            conn = sqlite3.connect(self.veritabani_dosyasi)
            cursor = conn.cursor()
            cursor.execute("UPDATE RANDEVULAR SET durum = 'İptal Edildi' WHERE randevu_id = ?", (randevu_id,))
            conn.commit()
            if cursor.rowcount == 0:
                return "randevu_bulunamadi"
            return "basarili"
        except sqlite3.Error:
            return "veritabani_hatasi"
        finally:
            if conn:
                conn.close()

    def randevu_durum_guncelle(self, randevu_id, yeni_durum):
        """
        Belirtilen randevunun durumunu günceller.
        """
        conn = None
        try:
            conn = sqlite3.connect(self.veritabani_dosyasi)
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE RANDEVULAR SET durum = ? WHERE randevu_id = ?",
                (yeni_durum, randevu_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                return "randevu_bulunamadi"
            return "basarili"
        except sqlite3.Error:
            return "veritabani_hatasi"
        finally:
            if conn:
                conn.close()
