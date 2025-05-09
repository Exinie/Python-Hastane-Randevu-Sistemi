import tkinter as tk
from tkinter import messagebox

from oturum_islemleri import *

def main():
# Ana pencere oluşumu
    ana_pencere = tk.Tk()
    ana_pencere.title("")
    ana_pencere.geometry("300x250")

    # Olaylar
    def btn_kullanici_girisi_click():
        ana_pencere.destroy()
        frm_kullanici_girisi() 
    
    # Başlık metni
    baslik = tk.Label(ana_pencere, text="Doğuş Hastanesi", font=("Arial", 18))
    baslik.pack(pady=20)  # Dikey boşluk

    # Butonlar
    btnGiris = tk.Button(ana_pencere, text="Kullanıcı Girişi", width=20, command=btn_kullanici_girisi_click)
    btnGiris.pack(pady=5)

    buton2 = tk.Button(ana_pencere, text="Yönetici Girişi", width=20)
    buton2.pack(pady=5)

    buton3 = tk.Button(ana_pencere, text="Çıkış", width=20, command=ana_pencere.quit)
    buton3.pack(pady=5)

    # Pencereyi göster
    ana_pencere.mainloop()
# End Ana pencere oluşumu

def frm_kullanici_girisi():
# Kullanıcı girişi penceresi oluşumu
    kullanici_girisi_pencere = tk.Tk()
    kullanici_girisi_pencere.title("")
    kullanici_girisi_pencere.geometry("300x250")

    # Olaylar
    def btn_giris_yap_click():
        kullanici_adi = entry_kullanici_adi.get()
        sifre = entry_sifre.get()

        if oturum_ac(kullanici_adi, sifre):
            pass
        else:
            messagebox.showwarning("Uyarı", "Kullanıcı adı veya şifreniz yanlış")
          

    # Başlık
    lbl = tk.Label(kullanici_girisi_pencere, text="Sistem Girişi", font=("Arial", 14))
    lbl.pack()
    lbl1 = tk.Label(kullanici_girisi_pencere, text="Hasta veya doktor giriş bilgilerinizi giriniz", font=("Arial", 12))
    lbl1.pack(pady=20)

     # Form alanları
    tk.Label(kullanici_girisi_pencere, text="Kullanıcı Adı:").pack()
    entry_kullanici_adi = tk.Entry(kullanici_girisi_pencere)
    entry_kullanici_adi.pack()


    tk.Label(kullanici_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(kullanici_girisi_pencere, show="*")
    entry_sifre.pack()
    
    tk.Button(kullanici_girisi_pencere, text="Giriş Yap", width=15, command=btn_giris_yap_click).pack(pady=10)

    # Pencereyi göster
    kullanici_girisi_pencere.mainloop()
# End Kullanıcı girişi penceresi oluşumu

if __name__ == "__main__":
    main()