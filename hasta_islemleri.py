import sqlite3


class HastaIslemleri:
    def randevu_al(self, hasta_id, doktor_id, tarih, saat, sikayet):
        """
        Belirtilen doktor, tarih, saat ve şikayete göre randevu alır.
        """
        try:
            # Veritabanına bağlan
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()

            # Aynı doktor, aynı tarih ve saat için zaten bir randevu var mı kontrol et
            cursor.execute('''
                SELECT * FROM RANDEVULAR
                WHERE doktor_id = ? AND tarih = ? AND saat = ?
            ''', (doktor_id, tarih, saat))
            mevcut = cursor.fetchone()

            if mevcut:
                return "dolu"

            # Randevuyu eklemek için
            cursor.execute('''
                INSERT INTO RANDEVULAR (hasta_id, doktor_id, tarih, saat, sikayet)
                VALUES (?, ?, ?, ?, ?)
            ''', (hasta_id, doktor_id, tarih, saat, sikayet))
            conn.commit()
            return True

        except Exception as hata:
            return f"Hata oluştu: {str(hata)}"

        finally:
            conn.close()

    def doktor_listele(self):
        """
        Bütün doktorları listelemek adına yazılmış bir fonksiyondur.
        """
        try:
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()

            cursor.execute('''
                SELECT doktor_id, ad, soyad FROM DOKTORLAR
            ''')

            doktorlar = cursor.fetchall()
            return doktorlar

        except Exception as hata:
            return f"Hata oluştu: {str(hata)}"

        finally:
            conn.close()

    def randevu_listele(self, hasta_id):
        """
        Bütün randevuları listelemek adına yazılmış bir fonksiyondur.
        """
        try:
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()

            cursor.execute('''
                SELECT randevu_id, tarih, saat, sikayet, doktor_id FROM RANDEVULAR WHERE hasta_id = ?
            ''', (hasta_id,))

            randevu_listesi = cursor.fetchall()
            return randevu_listesi

        except Exception as hata:
            return f"Hata oluştu: {str(hata)}"

        finally:
            conn.close()

    def randevu_sil(self, randevu_id):
        """
        Belirlenen randevuyu silmek için oluşturulmuş bir fonksiyondur.
        """
        try:
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()

            cursor.execute('''
                DELETE FROM RANDEVULAR WHERE randevu_id = ?
            ''', (randevu_id,))
            conn.commit()
            return "Randevu başarıyla iptal edilmiştir."

        except Exception as hata:
            return f"Hata oluştu: {str(hata)}"

        finally:
            conn.close()
