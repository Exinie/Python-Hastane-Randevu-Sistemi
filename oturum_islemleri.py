import sqlite3


class OturumIslemleri:

    def __init__(self):
        """
        Sınıfın init yapıcı metotunda diğer metodların kullanbilmesi için veritabanı dosya konumu tanımlandı.
        Session verisini depolayan oturum sözlüğü tanımlandı.
        """
        self.veritabani_dosyasi = "veritabani.db"
        self.oturum = {}

    def hasta_tc_kayitli_mi(self, tc_no):
        """
        Aldığı TC kimlik numarası değerini HASTALAR tablosunda sorgulayıp,
        gelen sonucun dolu olmasına göre True veya False döndürür.
        """
        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            cursor = baglanti.cursor()
            cursor.execute("SELECT tc_no FROM HASTALAR WHERE tc_no = ? LIMIT 1;", (tc_no,))
            sonuc = cursor.fetchone()

            if sonuc:
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"Veritabanı hatası: {e}")
            return None
        finally:
            baglanti.close()

    def hasta_kayit_et(self, tc_no, sifre, ad, soyad):
        """
        Aldığı TC kimlik numarası, şifre, ad ve soyad değerlerini önce kontrol edip,
        daha sonra HASTALAR tablosuna ekleneyen metod.
        """

        if not tc_no.strip() or not sifre.strip() or not ad.strip() or not soyad.strip():
            return "bos_alan_var"

        if len(tc_no) != 11 or not tc_no.isdigit():
            return "gecersiz_tc_formati"

        if self.hasta_tc_kayitli_mi(tc_no):
            return "zaten_kayitli"

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            cursor = baglanti.cursor()
            cursor.execute("INSERT INTO HASTALAR (tc_no, sifre, ad, soyad) VALUES (?, ?, ?, ?)",
                           (tc_no, sifre, ad, soyad))
            baglanti.commit()

            return True
        except sqlite3.Error as e:
            print(f"Veritabanı hatası: {e}")
            return None
        finally:
            baglanti.close()

    def hasta_oturum_ac(self, tc_no, sifre):
        """
        Aldığı TC kimlik numarası ve şifre değerlerini önce kontrol edip,
        daha sonra HASTALAR tablosunda bu değerlerin eşleştiği bir satır arar.
        Sonuç gelirse, gelen verileri init metotunda bulunan oturum sözlüğüne ekler,
        ardından oturum sözlüğüne "kullanici_tipi" girdisi eklenip değeri "hasta" olarak tanımlanır.
        """
        if not tc_no.strip() or not sifre.strip():
            return "bos_alan_var"

        if len(tc_no) != 11 or not tc_no.isdigit():
            return "gecersiz_tc_formati"

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            baglanti.row_factory = sqlite3.Row
            cursor = baglanti.cursor()

            cursor.execute("SELECT * FROM HASTALAR WHERE tc_no = ? AND sifre = ? LIMIT 1;",
                           (tc_no, sifre))

            girisi_basarili_kullanici_bilgisi = cursor.fetchone()

            if girisi_basarili_kullanici_bilgisi:
                self.oturum = dict(girisi_basarili_kullanici_bilgisi)
                self.oturum.update({"kullanici_tipi": "hasta"})

                print("Oturum (session) başarıyla oluşturuldu:")
                print(self.oturum)

                return True
            else:
                return "yanlis_tc_sifre"
        except sqlite3.Error as e:
            print(f"Veritabanı hatası: {e}")
            return None
        finally:
            baglanti.close()

    def doktor_oturum_ac(self, tc_no, sifre):
        """
        Aldığı TC kimlik numarası ve şifre değerlerini önce kontrol edip,
        daha sonra DOKTORLAR tablosunda bu değerlerin eşleştiği bir satır arar.
        Sonuç gelirse, gelen verileri init metotunda bulunan oturum sözlüğüne ekler,
        ardından oturum sözlüğüne "kullanici_tipi" girdisi eklenip değeri "doktor" olarak tanımlanır.
        """
        if not tc_no.strip() or not sifre.strip():
            return "bos_alan_var"

        if len(tc_no) != 11 or not tc_no.isdigit():
            return "gecersiz_tc_formati"

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            baglanti.row_factory = sqlite3.Row
            cursor = baglanti.cursor()

            cursor.execute("SELECT * FROM DOKTORLAR WHERE tc_no = ? AND sifre = ? LIMIT 1;",
                           (tc_no, sifre))

            girisi_basarili_kullanici_bilgisi = cursor.fetchone()

            if girisi_basarili_kullanici_bilgisi:
                self.oturum = dict(girisi_basarili_kullanici_bilgisi)
                self.oturum.update({"kullanici_tipi": "doktor"})

                print("Oturum (session) başarıyla oluşturuldu:")
                print(self.oturum)

                return True
            else:
                return "yanlis_tc_sifre"
        except sqlite3.Error as e:
            print(f"Veritabanı hatası: {e}")
            return None
        finally:
            baglanti.close()

    def yonetici_oturum_ac(self, kullanici_adi, sifre):
        """
        Aldığı kullanıcı adı ve şifre değerlerini önce kontrol edip,
        daha sonra YONETICILER tablosunda bu değerlerin eşleştiği bir satır arar.
        Sonuç gelirse, gelen verileri init metotunda bulunan oturum sözlüğüne ekler,
        ardından oturum sözlüğüne "kullanici_tipi" girdisi eklenip değeri "yonetici" olarak tanımlanır.
        """
        if not kullanici_adi.strip() or not sifre.strip():
            return "bos_alan_var"

        try:
            baglanti = sqlite3.connect(self.veritabani_dosyasi)
            baglanti.row_factory = sqlite3.Row
            cursor = baglanti.cursor()

            cursor.execute("SELECT * FROM YONETICILER WHERE kullanici_adi = ? AND sifre = ? LIMIT 1;",
                           (kullanici_adi, sifre))

            girisi_basarili_kullanici_bilgisi = cursor.fetchone()

            if girisi_basarili_kullanici_bilgisi:
                self.oturum = dict(girisi_basarili_kullanici_bilgisi)
                self.oturum.update({"kullanici_tipi": "yonetici"})

                print("Oturum (session) başarıyla oluşturuldu:")
                print(self.oturum)

                return True
            else:
                return "yanlis_kullaniciadi_sifre"
        except sqlite3.Error as e:
            print(f"Veritabanı hatası: {e}")
            return None
        finally:
            baglanti.close()

    def oturumu_kapat(self):
        """
        Çağırıldığında init metotundaki oturum sözlüğünü temizleyen metot.
        """
        self.oturum = {}
        print("Oturum başarıyla kapatıldı")
        return True
