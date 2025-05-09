import tkinter as tk
from tkinter import messagebox

from oturum_islemleri import *
from veritabani_kurulumu import *

def main():

    # Program başlangıcında veritabanı kurulumunu çağır.
    veritabanini_kur()

# Ana pencere oluşumu
    ana_pencere = tk.Tk()
    ana_pencere.title("")
    ana_pencere.geometry("300x300")

    # Olaylar
    def btn_hasta_girisi_click():
        ana_pencere.destroy()
        frm_hasta_giris()

    def btn_hasta_kayit_click():
        ana_pencere.destroy()
        frm_hasta_kayit()
    
    # Başlık metni
    lblUstBaslik = tk.Label(ana_pencere, text="Doğuş Hastanesi", font=("Arial", 18))
    lblUstBaslik.pack(pady=20)  # Dikey boşluk

    # Butonlar
    btnHastaGirisi = tk.Button(ana_pencere, text="Hasta Girişi", width=20, command=btn_hasta_girisi_click)
    btnHastaGirisi.pack(pady=5)

    btnHastaKayit = tk.Button(ana_pencere, text="Hasta Kayıt", width=20, command=btn_hasta_kayit_click)
    btnHastaKayit.pack(pady=5)

    btnDoktorGirisi = tk.Button(ana_pencere, text="Doktor Girişi", width=20)
    btnDoktorGirisi.pack(pady=5)

    btnYoneticiGirisi = tk.Button(ana_pencere, text="Yönetici Girişi", width=20)
    btnYoneticiGirisi.pack(pady=5)

    buton3 = tk.Button(ana_pencere, text="Çıkış", width=20, command=ana_pencere.quit)
    buton3.pack(pady=5)

    # Pencereyi göster
    ana_pencere.mainloop()
# End Ana pencere oluşumu

def frm_hasta_kayit():
# Hasta kayıt penceresi oluşumu
    hasta_kayit_pencere = tk.Tk()
    hasta_kayit_pencere.title("")
    hasta_kayit_pencere.geometry("300x250")

    # Olaylar
    def btn_kayit_ol_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()

        if kayit_ol(tc_no, sifre):
            pass
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

    # Pencereyi göster
    hasta_kayit_pencere.mainloop()
# End Hasta kayıt penceresi oluşumu

def frm_hasta_giris():
# Kullanıcı girişi penceresi oluşumu
    hasta_girisi_pencere = tk.Tk()
    hasta_girisi_pencere.title("")
    hasta_girisi_pencere.geometry("300x250")

    # Olaylar
    def btn_giris_yap_click():
        kullanici_adi = entry_kullanici_adi.get()
        sifre = entry_sifre.get()

        if oturum_ac(kullanici_adi, sifre):
            pass
        else:
            messagebox.showwarning("Uyarı", "Kullanıcı adı veya şifreniz yanlış")
          

    # Başlık
    lbl = tk.Label(hasta_girisi_pencere, text="Sistem Girişi", font=("Arial", 14))
    lbl.pack()
    lbl1 = tk.Label(hasta_girisi_pencere, text="Hasta veya doktor giriş bilgilerinizi giriniz", font=("Arial", 12))
    lbl1.pack(pady=20)

     # Form alanları
    tk.Label(hasta_girisi_pencere, text="Kullanıcı Adı:").pack()
    entry_kullanici_adi = tk.Entry(hasta_girisi_pencere)
    entry_kullanici_adi.pack()


    tk.Label(hasta_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(hasta_girisi_pencere, show="*")
    entry_sifre.pack()
    
    tk.Button(hasta_girisi_pencere, text="Giriş Yap", width=15, command=btn_giris_yap_click).pack(pady=10)

    # Pencereyi göster
    hasta_girisi_pencere.mainloop()
# End Kullanıcı girişi penceresi oluşumu

if __name__ == "__main__":
    main()