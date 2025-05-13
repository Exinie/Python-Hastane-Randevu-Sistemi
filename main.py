import tkinter as tk
from tkinter import messagebox
from veritabani_kurulumu import veritabanini_kur
from oturum_islemleri import hasta_kayit_et, doktor_oturum_ac, hasta_oturum_ac, oturumu_baslat
from doktor_islemleri import doktor_recete_yaz

def main():

    # Program başlangıcında veritabanı kurulumunu çağır.
    veritabanini_kur()

# Ana pencere oluşumu
    ana_pencere = tk.Tk()
    ana_pencere.title("")
    ana_pencere.geometry("300x300")

    # Olaylar
    def btn_hasta_girisi_click():
        ana_pencere.withdraw()
        frm_hasta_giris()

    def btn_hasta_kayit_click():
        ana_pencere.withdraw()
        frm_hasta_kayit()
    
    def btn_doktor_giris_click():
        ana_pencere.withdraw()
        frm_doktor_giris()

    # Başlık metni
    lblUstBaslik = tk.Label(ana_pencere, text="Doğuş Hastanesi", font=("Arial", 18))
    lblUstBaslik.pack(pady=20)  # Dikey boşluk

    # Butonlar
    btnHastaGirisi = tk.Button(ana_pencere, text="Hasta Girişi", width=20, command=btn_hasta_girisi_click)
    btnHastaGirisi.pack(pady=5)

    btnHastaKayit = tk.Button(ana_pencere, text="Hasta Kayıt", width=20, command=btn_hasta_kayit_click)
    btnHastaKayit.pack(pady=5)

    btnDoktorGirisi = tk.Button(ana_pencere, text="Doktor Girişi", width=20, command=btn_doktor_giris_click)
    btnDoktorGirisi.pack(pady=5)

    btnYoneticiGirisi = tk.Button(ana_pencere, text="Yönetici Girişi", width=20)
    btnYoneticiGirisi.pack(pady=5)

    btnCikis = tk.Button(ana_pencere, text="Çıkış", width=20, command=ana_pencere.quit)
    btnCikis.pack(pady=5)

    # Pencereyi göster
    ana_pencere.mainloop()
# End Ana pencere oluşumu

def frm_hasta_kayit():
# Hasta kayıt penceresi oluşumu
    hasta_kayit_pencere = tk.Toplevel()
    hasta_kayit_pencere.title("")
    hasta_kayit_pencere.geometry("300x300")

    # Olaylar
    def btn_kayit_ol_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()
        ad = entry_ad.get()
        soyad = entry_soyad.get()

        if hasta_kayit_et(tc_no, sifre, ad, soyad):
            hasta_kayit_pencere.destroy()
            frm_hasta_giris()
        else:
            pass
          
    # Başlık
    lbl = tk.Label(hasta_kayit_pencere, text="Hasta Kayıt", font=("Arial", 14))
    lbl.pack()
    lbl1 = tk.Label(hasta_kayit_pencere, text="Lütfen istenilen bilgileri doldurunuz", font=("Arial", 12))
    lbl1.pack(pady=20)

     # Form alanları
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
# End Hasta kayıt penceresi oluşumu

def frm_hasta_giris():
# Hasta girişi penceresi oluşumu
    hasta_girisi_pencere = tk.Toplevel()
    hasta_girisi_pencere.title("")
    hasta_girisi_pencere.geometry("300x250")

    # Olaylar
    def btn_giris_yap_click():
        tc_no = entry_kullanici_adi.get()
        sifre = entry_sifre.get()

        oturum = hasta_oturum_ac(tc_no, sifre)
        if oturum:
            hasta_girisi_pencere.destroy()
            frm_hasta_paneli(oturum)
        else:
            messagebox.showwarning("Uyarı", "Kullanıcı adı veya şifreniz yanlış")
          

    # Başlık
    lbl = tk.Label(hasta_girisi_pencere, text="Sistem Girişi", font=("Arial", 14))
    lbl.pack()
    lbl1 = tk.Label(hasta_girisi_pencere, text="Hasta veya doktor giriş bilgilerinizi giriniz", font=("Arial", 12))
    lbl1.pack(pady=20)

     # Form alanları
    tk.Label(hasta_girisi_pencere, text="TC Kimlik No:").pack()
    entry_kullanici_adi = tk.Entry(hasta_girisi_pencere)
    entry_kullanici_adi.pack()


    tk.Label(hasta_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(hasta_girisi_pencere, show="*")
    entry_sifre.pack()
    
    tk.Button(hasta_girisi_pencere, text="Giriş Yap", width=15, command=btn_giris_yap_click).pack(pady=10)
# End Hasta girişi penceresi oluşumu

def frm_hasta_paneli(oturum):
# Hasta paneli penceresi oluşumu
    hasta_paneli_pencere = tk.Toplevel()
    hasta_paneli_pencere.title("")
    hasta_paneli_pencere.geometry("300x250")

    # Olaylar
    def btn_randevu_al_click():
        pass
            
    # Başlık    

    

    lbl = tk.Label(hasta_paneli_pencere, text="Hasta Paneli", font=("Arial", 14))
    lbl.pack()

    lbl1 = tk.Label(hasta_paneli_pencere, text="Hoş geldiniz " + oturum["ad"] + " " + oturum["soyad"], font=("Arial", 12))
    lbl1.pack(pady=20)

    lbl2 = tk.Label(hasta_paneli_pencere, text="Senin rolün: " + oturum["kullanici_tipi"], font=("Arial", 12))
    lbl2.pack(pady=20)

    tk.Button(hasta_paneli_pencere, text="Randevu Oluştur", width=15, command=btn_randevu_al_click).pack(pady=10)
# End Hasta paneli penceresi oluşumu

def frm_doktor_giris():
# Doktor girişi penceresi oluşumu
    doktor_girisi_pencere = tk.Toplevel()
    doktor_girisi_pencere.title("")
    doktor_girisi_pencere.geometry("300x250")
    
    # Olaylar
    def btn_giriş_yap_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()

        oturum = doktor_oturum_ac(tc_no, sifre)
        if oturum:
            doktor_girisi_pencere.destroy()
            frm_doktor_paneli(oturum)
        else:
            pass
    
      
    # Başlık      
    lbl = tk.Label(doktor_girisi_pencere, text="Doktor Girişi", font=("Arial", 14))
    lbl.pack(pady=20)
            
    # Form alanları
    tk.Label(doktor_girisi_pencere, text="TC Kimlik No:").pack()
    entry_tc_no = tk.Entry(doktor_girisi_pencere)
    entry_tc_no.pack(pady=5)
            
    tk.Label(doktor_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(doktor_girisi_pencere, show="*")
    entry_sifre.pack(pady=5)
            
    tk.Button(doktor_girisi_pencere, text="Giriş Yap" , width=15, command=btn_giriş_yap_click).pack(pady=10)
# End Hasta kayıt penceresi oluşumu

def frm_doktor_paneli(oturum):
# Doktor paneli penceresi oluşumu
    doktor_paneli_pencere = tk.Toplevel()
    doktor_paneli_pencere.title("")
    doktor_paneli_pencere.geometry("300x250")

    # Olaylar
    def btn_retece_yaz_click():
        doktor_recete_yaz(oturum)
            
    # Başlık    
    lbl = tk.Label(doktor_paneli_pencere, text="Doktor Paneli", font=("Arial", 14))
    lbl.pack()

    lbl1 = tk.Label(doktor_paneli_pencere, text="Hoş geldiniz " + oturum["ad"] + " " + oturum["soyad"], font=("Arial", 12))
    lbl1.pack(pady=20)

    lbl2 = tk.Label(doktor_paneli_pencere, text="Senin rolün: " + oturum["kullanici_tipi"], font=("Arial", 12))
    lbl2.pack(pady=20)

    tk.Button(doktor_paneli_pencere, text="Reçete Yaz", width=15, command=btn_retece_yaz_click).pack(pady=10)
# End Doktor paneli penceresi oluşumu


if __name__ == "__main__":
    main()