import tkinter as tk
from tkinter import ttk, messagebox
from veritabani_kurulumu import Veritabani
from oturum_islemleri import OturumIslemleri
# from doktor_islemleri import doktor_recete_paneli / Sınıfa çevirildiğinde import işlemini yeniden yazarsın.

veritabani_kurulumu_objesi = Veritabani()
oturum_objesi = OturumIslemleri()

''' Ana pencere fonksiyonuna diğer pencerelerden erişilebilmesi için tüm fonskiyonlardan ayrı olarak tanımlanmıştır.  '''
ana_pencere = tk.Tk()

# Ana pencere
def main():

    ''' Ana pencere özellikleri '''
    ana_pencere.title("Doğuş Hastanesi")
    ana_pencere.geometry("300x300")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_hasta_girisi_click():
        ana_pencere.withdraw() # Ana pencereyi gizler
        frm_hasta_giris()

    def btn_hasta_kayit_click():
        ana_pencere.withdraw()
        frm_hasta_kayit()
    
    def btn_doktor_giris_click():
        ana_pencere.withdraw()
        frm_doktor_giris()

    def btn_yonetici_giris_click():
        ana_pencere.withdraw()
        frm_yonetici_paneli()
   

    ''' Üst başlık metni '''
    lblBaslik = tk.Label(ana_pencere, text="Doğuş Hastanesi", font=("Arial", 18))
    lblBaslik.pack(pady=20)  # Dikey boşluk

    ''' İşlem butonları '''
    btnHastaGirisYap = tk.Button(ana_pencere, text="Hasta Girişi", width=20, command=btn_hasta_girisi_click)
    btnHastaGirisYap.pack(pady=5)

    btnHastaKayitOl = tk.Button(ana_pencere, text="Hasta Kayıt", width=20, command=btn_hasta_kayit_click)
    btnHastaKayitOl.pack(pady=5)

    btnDoktorGirisYap = tk.Button(ana_pencere, text="Doktor Girişi", width=20, command=btn_doktor_giris_click)
    btnDoktorGirisYap.pack(pady=5)

    btnYoneticiGirisYap = tk.Button(ana_pencere, text="Yönetici Girişi", width=20, command=btn_yonetici_giris_click)
    btnYoneticiGirisYap.pack(pady=5)

    btnCikis = tk.Button(ana_pencere, text="Çıkış", width=20, command=ana_pencere.quit)
    btnCikis.pack(pady=5)

    ''' Bu pencereyi kök pencere yapmak için mainloop ile döngüye alıyoruz '''
    ana_pencere.mainloop()
# End Ana pencere

# Hasta kayıt penceresi
def frm_hasta_kayit():

    ''' Hasta kayıt pencere özellikleri '''
    hasta_kayit_pencere = tk.Toplevel() # Diğer pencerelerden önde açılmasını sağlar
    hasta_kayit_pencere.title("Hasta Kayıt")
    hasta_kayit_pencere.geometry("300x350")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_kayit_ol_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()
        ad = entry_ad.get()
        soyad = entry_soyad.get()

        if oturum_objesi.hasta_kayit_et(tc_no, sifre, ad, soyad):
            messagebox.showinfo("Bilgi", "Kayıt başarılı, giriş sayfasına aktarılıyorsunuz.")
            hasta_kayit_pencere.destroy()
            frm_hasta_giris()
        else:
            pass

    def btn_geri_don_click():
        hasta_kayit_pencere.destroy() # Hasta kayıt penceresini sonlandırır
        ana_pencere.deiconify() # Ana pencereyi geri görünür yapar

    ''' Üst başlık metni '''
    lbl_baslik = tk.Label(hasta_kayit_pencere, text="Hasta Kayıt", font=("Arial", 14))
    lbl_baslik.pack()
    lbl_alt_baslik = tk.Label(hasta_kayit_pencere, text="Lütfen istenilen bilgileri doldurunuz", font=("Arial", 12))
    lbl_alt_baslik.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(hasta_kayit_pencere, text="TC Kimlik No:").pack()
    entry_tc_no = tk.Entry(hasta_kayit_pencere)
    entry_tc_no.pack()

    tk.Label(hasta_kayit_pencere, text="Ad:").pack()
    entry_ad = tk.Entry(hasta_kayit_pencere)
    entry_ad.pack()

    tk.Label(hasta_kayit_pencere, text="Soyad:").pack()
    entry_soyad = tk.Entry(hasta_kayit_pencere)
    entry_soyad.pack()

    tk.Label(hasta_kayit_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(hasta_kayit_pencere, show="*")
    entry_sifre.pack()
    
    tk.Button(hasta_kayit_pencere, text="Kayıt Ol", width=15, command=btn_kayit_ol_click).pack(pady=10)
    tk.Button(hasta_kayit_pencere, text="Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)
# End Hasta kayıt penceresi

# Hasta giriş penceresi
def frm_hasta_giris():

    ''' Hasta giriş pencere özellikleri '''
    hasta_girisi_pencere = tk.Toplevel()
    hasta_girisi_pencere.title("Hasta Giriş")
    hasta_girisi_pencere.geometry("300x300")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_giris_yap_click():
        tc_no = entry_kullanici_adi.get()
        sifre = entry_sifre.get()

        
        if oturum_objesi.hasta_oturum_ac(tc_no, sifre) == True:
            hasta_girisi_pencere.destroy()
            frm_hasta_paneli()
        else:
            messagebox.showwarning("Uyarı", "Kullanıcı adı veya şifreniz yanlış")
    
    def btn_geri_don_click():
        hasta_girisi_pencere.destroy()
        ana_pencere.deiconify()

    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(hasta_girisi_pencere, text="Hasta Girişi", font=("Arial", 14))
    lbl_ana_baslik.pack()
    lbl_alt_baslik = tk.Label(hasta_girisi_pencere, text="Hasta kullanıcı bilgilerinizi giriniz", font=("Arial", 12))
    lbl_alt_baslik.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(hasta_girisi_pencere, text="TC Kimlik No:").pack()
    entry_kullanici_adi = tk.Entry(hasta_girisi_pencere)
    entry_kullanici_adi.pack()

    tk.Label(hasta_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(hasta_girisi_pencere, show="*")
    entry_sifre.pack()
    
    tk.Button(hasta_girisi_pencere, text="Giriş Yap", width=15, command=btn_giris_yap_click).pack(pady=10)
    tk.Button(hasta_girisi_pencere, text="Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)
# End Hasta giriş penceresi

# Hasta paneli
def frm_hasta_paneli():

    ''' Hasta paneli pencere özellikleri '''
    hasta_paneli_pencere = tk.Toplevel()
    hasta_paneli_pencere.title("Hasta Paneli")
    hasta_paneli_pencere.geometry("300x350")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_randevu_al_click():
        pass
            
    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(hasta_paneli_pencere, text="Hasta Paneli", font=("Arial", 14))
    lbl_ana_baslik.pack()

    lbl_hos_geldiniz_metni = tk.Label(hasta_paneli_pencere, text="Hoş geldiniz " + oturum_objesi.oturum["ad"] + " " + oturum_objesi.oturum["soyad"], font=("Arial", 12))
    lbl_hos_geldiniz_metni.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''


    tk.Button(hasta_paneli_pencere, text="Randevu Oluştur", width=15, command=btn_randevu_al_click).pack(pady=10)
# End Hasta paneli

# Doktor girişi penceresi
def frm_doktor_giris():

    ''' Hasta paneli pencere özellikleri '''
    doktor_girisi_pencere = tk.Toplevel()
    doktor_girisi_pencere.title("Doktor Giriş")
    doktor_girisi_pencere.geometry("300x300")
    
    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_giriş_yap_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()

        oturum = oturum_objesi.doktor_oturum_ac(tc_no, sifre)
        if oturum:
            doktor_girisi_pencere.destroy()
            frm_doktor_paneli(oturum)
        else:
            pass
    
    def btn_geri_don_click():
        doktor_girisi_pencere.destroy()
        ana_pencere.deiconify()

    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(doktor_girisi_pencere, text="Doktor Girişi", font=("Arial", 14))
    lbl_ana_baslik.pack()
    lbl_alt_baslik = tk.Label(doktor_girisi_pencere, text="Doktor kullanıcı bilgilerinizi giriniz", font=("Arial", 12))
    lbl_alt_baslik.pack(pady=20)
            
    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(doktor_girisi_pencere, text="TC Kimlik No:").pack()
    entry_tc_no = tk.Entry(doktor_girisi_pencere)
    entry_tc_no.pack(pady=5)
            
    tk.Label(doktor_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(doktor_girisi_pencere, show="*")
    entry_sifre.pack(pady=5)
            
    tk.Button(doktor_girisi_pencere, text="Giriş Yap" , width=15, command=btn_giriş_yap_click).pack(pady=10)
    tk.Button(doktor_girisi_pencere, text="Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)
# End Doktor girişi penceresi

# Doktor paneli
def frm_doktor_paneli():

    ''' Hasta paneli pencere özellikleri '''
    doktor_paneli_pencere = tk.Toplevel()
    doktor_paneli_pencere.title("Doktor Paneli")
    doktor_paneli_pencere.geometry("300x250")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_retece_yaz_click():
        doktor_recete_paneli()
            
    ''' Üst başlık metni '''  
    lbl_ana_baslik = tk.Label(doktor_paneli_pencere, text="Doktor Paneli", font=("Arial", 14))
    lbl_ana_baslik.pack()

    lbl_hos_geldiniz_metni = tk.Label(doktor_paneli_pencere, text="Hoş geldiniz " + oturum_objesi.oturum["ad"] + " " + oturum_objesi.oturum["soyad"], font=("Arial", 12))
    lbl_hos_geldiniz_metni.pack(pady=20)

    tk.Button(doktor_paneli_pencere, text="Reçete Yaz", width=15, command=btn_retece_yaz_click).pack(pady=10)
# End Doktor paneli

# Yönetici paneli
def frm_yonetici_paneli():

    ''' Hasta paneli pencere özellikleri '''
    yonetici_paneli_pencere = tk.Toplevel()
    yonetici_paneli_pencere.title("Yönetici Paneli")
    yonetici_paneli_pencere.geometry("350x450")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_hastalari_yonet_click():
        pass
    
    def btn_doktorlari_yonet_click():
        pass

    def btn_yoneticileri_yonet_click():
        pass

    def btn_cikis_yap_click():
        pass
    
    ''' Üst başlık metni '''  
    lbl_ana_baslik = tk.Label(yonetici_paneli_pencere, text="Yönetici Paneli", font=("Arial", 14))
    lbl_ana_baslik.pack()

    lbl_hos_geldiniz_metni = tk.Label(yonetici_paneli_pencere, text="Hoş geldiniz " + oturum_objesi.oturum["kullanici_adi"], font=("Arial", 12))
    lbl_hos_geldiniz_metni.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''
    tk.Button(yonetici_paneli_pencere, text="Hastaları Yönet", command=btn_hastalari_yonet_click).pack(pady=2)
    tk.Button(yonetici_paneli_pencere, text="Doktorları Yönet", command=btn_doktorlari_yonet_click).pack(pady=2)
    tk.Button(yonetici_paneli_pencere, text="Yöneticileri Yönet", command=btn_yoneticileri_yonet_click).pack(pady=2)
    tk.Button(yonetici_paneli_pencere, text="Çıkış Yap", command=btn_cikis_yap_click).pack(pady=2)

    liste = tk.Listbox(yonetici_paneli_pencere, width=40)
    liste.pack(pady=10)
# End yönetici paneli

if __name__ == "__main__":
    main()