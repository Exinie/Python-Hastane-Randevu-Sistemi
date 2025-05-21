import sqlite3

class OturumIslemleri:
    # __init__ metodu nesne oluşturulduğunda çağırılır. self = nesne (?)
    def __init__(self):
        self.veritabani_dosyasi = "veritabani.db"
        self.oturum = {}

    '''
     def veritabani_baglantisi(self):
        sqlite3.connect(self.veritabani_dosyasi)
    '''

    '''
    
    '''
    def hasta_tc_kayitli_mi(self, tc_no):
        
        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            cursor = baglanti.cursor()
            cursor.execute("SELECT tc_no FROM HASTALAR WHERE tc_no = ? LIMIT 1;", (tc_no,))
            sonuc = cursor.fetchone()
    
            if sonuc:
                baglanti.close()
                return True
            else:
                baglanti.close()
                return False
        except sqlite3.Error as e:
            baglanti.close()
            return f"Veritabanı hatası: {e}"

    '''
    
    '''
    def hasta_kayit_et(self, tc_no, sifre, ad, soyad):

        kontrol_hatalari = []

        if not tc_no.strip() or not sifre.strip() or not ad.strip() or not soyad.strip():
            kontrol_hatalari.append("Lütfen tüm alanları doldurunuz.")
    
        if len(tc_no) != 11 or not tc_no.isdigit():
            kontrol_hatalari.append("Geçersiz TC kimlik numarası formatı.")

        sonuc = self.hasta_tc_kayitli_mi(tc_no)

        if not isinstance(sonuc, bool):
            return sonuc
        elif sonuc == True:
            kontrol_hatalari.append("Hasta zaten kayıtlı.")
        
        if len(kontrol_hatalari) == 0:
            try:
                baglanti = sqlite3.connect(self.veritabani_dosyasi)
                cursor = baglanti.cursor()
                cursor.execute("INSERT INTO HASTALAR (tc_no, sifre, ad, soyad) VALUES (?, ?, ?, ?)",
                    (tc_no, sifre, ad, soyad))
                baglanti.commit()

                baglanti.close()
                return True
            except sqlite3.Error as e:
                baglanti.close()
                return f"Veritabanı hatası: {e}"
        else:
            return 
    '''
    
    '''
    def hasta_oturum_ac(self, tc_no, sifre):

        if not tc_no.strip() or not sifre.strip():
            return("Lütfen tüm alanları doldurunuz.")
        
        if len(tc_no) != 11 or not tc_no.isdigit():
            return("Geçersiz TC kimlik numarası formatı.")

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            baglanti.row_factory = sqlite3.Row
            cursor = baglanti.cursor()

            cursor.execute("SELECT * FROM HASTALAR WHERE tc_no = ? AND sifre = ? LIMIT 1;",
                (tc_no, sifre))

            girisi_basarili_kullanici_bilgisi = cursor.fetchone()
            baglanti.close()

            if girisi_basarili_kullanici_bilgisi:
                self.oturum = dict(girisi_basarili_kullanici_bilgisi)
                self.oturum.update({"kullanici_tipi" : "hasta"})
                print("Oturum (session) başarıyla oluşturuldu: \n" + self.oturum)
                baglanti.close()
                return True
            else:
                baglanti.close()
                return "Yanlış TC kimlik numarası veya şifre."
        except sqlite3.Error as e:
            baglanti.close()
            return f"Veritabanı hatası: {e}"

    '''
    
    '''
    def doktor_oturum_ac(self, tc_no, sifre):

        if not tc_no.strip() or not sifre.strip():
            return("Lütfen tüm alanları doldurunuz.")
        
        if len(tc_no) != 11 or not tc_no.isdigit():
            return("Geçersiz TC kimlik numarası formatı.")

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            baglanti.row_factory = sqlite3.Row
            cursor = baglanti.cursor()

            cursor.execute("SELECT * FROM DOKTORLAR WHERE tc_no = ? AND sifre = ? LIMIT 1;",
                (tc_no, sifre))

            girisi_basarili_kullanici_bilgisi = cursor.fetchone()
            baglanti.close()

            if girisi_basarili_kullanici_bilgisi:
                self.oturum = dict(girisi_basarili_kullanici_bilgisi)
                self.oturum.update({"kullanici_tipi" : "doktor"})
                baglanti.close()
                return True
            else:
                baglanti.close()
                return "Yanlış TC kimlik numarası veya şifre."
        except sqlite3.Error as e:
            baglanti.close()
            return f"Veritabanı hatası: {e}"
    
    '''
    
    '''
    def yonetici_oturum_ac(self, kullanici_adi, sifre):

        if not kullanici_adi.strip() or not sifre.strip():
            return("Lütfen tüm alanları doldurunuz.")

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            baglanti.row_factory = sqlite3.Row
            cursor = baglanti.cursor()

            cursor.execute("SELECT * FROM YONETICILER WHERE kullanici_adi = ? AND sifre = ? LIMIT 1;",
                (kullanici_adi, sifre))

            girisi_basarili_kullanici_bilgisi = cursor.fetchone()
            baglanti.close()

            if girisi_basarili_kullanici_bilgisi:
                self.oturum = dict(girisi_basarili_kullanici_bilgisi)
                self.oturum.update({"kullanici_tipi" : "yonetici"})
                baglanti.close()
                return True
            else:
                baglanti.close()
                return "Yanlış kullanıcı adı veya şifre."
        except sqlite3.Error as e:
            baglanti.close()
            return f"Veritabanı hatası: {e}"