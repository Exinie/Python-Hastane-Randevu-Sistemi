import sqlite3

class DoktorIslemleri:
    def __init__(self):
        self.veritabani_dosyasi = "veritabani.db"
    def randevulari_listele(self, doktor_id):
        try:
            conn = sqlite3.connect(self.veritabani_dosyasi)
            cursor = conn.cursor()
            cursor.execute("SELECT randevu_id, hasta_id, tarih, saat, sikayet, durum FROM RANDEVULAR WHERE doktor_id = ?", (doktor_id,))
            sonuc = cursor.fetchall()
            return sonuc
        except:
            return "veritabani_hatasi"
        finally:
            conn.close()

    def randevu_sil(self, randevu_id):
        try:
            conn = sqlite3.connect(self.veritabani_dosyasi)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM RANDEVULAR WHERE randevu_id=?", (randevu_id,))
            conn.commit()
            if cursor.rowcount == 0:
                return "randevu_bulunamadi"
            return "basarili"
        except:
            return "veritabani_hatasi"
        finally:
            conn.close()

    def randevu_durum_guncelle(self, randevu_id, yeni_durum):
        try:
            conn = sqlite3.connect(self.veritabani_dosyasi)
            cursor = conn.cursor()
            cursor.execute("UPDATE RANDEVULAR SET durum=? WHERE randevu_id=?", (yeni_durum, randevu_id))
            conn.commit()
            if cursor.rowcount == 0:
                return "randevu_bulunamadi"
            return "basarili"
        except:
            return "veritabani_hatasi"
        finally:
            conn.close()
