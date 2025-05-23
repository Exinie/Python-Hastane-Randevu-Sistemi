import sqlite3

class HastaIslemleri:
    def randevu_al(self, hasta_id, doktor_id, tarih, saat, sikayet):
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
    
    # randevu görüntülemek için
    def randevu_listele(self, hasta_id):
        try:
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()

            cursor.execute('''
                SELECT R.randevu_id, R.tarih, R.saat, R.durum, D.ad || ' ' || D.soyad AS doktor_adi
                FROM RANDEVULAR R
                JOIN DOKTORLAR D ON R.doktor_id = D.doktor_id
                WHERE R.hasta_id = ?
                ORDER BY R.tarih, R.saat
            ''', (hasta_id,))
        
            randevular = cursor.fetchall()
            return randevular

        except Exception as hata:
            return f"Hata oluştu: {str(hata)}"

        finally:
            conn.close()