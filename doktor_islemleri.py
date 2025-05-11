import tkinter as tk
from tkinter import messagebox
import sqlite3
# sonra ekleriz veritabanı kısmını


def doktor_oturum_ac(kullanici_adi, sifre):
    #sabit kullanıcı adi ve şifre
    if kullanici_adi == "doktor1" and sifre == "1234":
        return True:
    return False:

def frm_doktor_giris():
    # Doktor Giriş Penceresi
    doktor_girisi_pencere = tk.Tk()
    doktor_girisi_pencere.title("Doktor Girişi")
    doktor_girisi_pencere.geometry("300x250")
    
    #olaylar
    def btn_giriş_yap_click():
         kullanici_adi = entry_kullanici_adi.get()
        sifre = entry_sifre.get()
        
        
        
        #giriş işlemlerini Kontrol et
        if doktor_oturum_ac(kullanici_adi, sifre):
            messagebox.showinfo("Başarılı", "Firiş Başarılı!")
            
            #Burada Doktorun işlemlerine geçiş yaplıabilir
            
            doktor_girisi_pencere.destroy() #Giriş Penceresini Kapat
        else:
            messagebox.showwarning("Uyarı", "Kullanıcıda adı veya Şire Yanlış! Lütfen tekrar Deneyiniz.")
            
            
            #başlık
            
            lbl = tk.Label(doktor_girisi_pencere, text="Doktor Girişi", font=("Arial", 14))
            lbl.pack(pady=20)
            
            #form alanları
            tk.Label(doktor_girisi_pencere, text="Kullanıcı Adı:").pack()
            entry_kullanici_adi = tk.Entry(doktor_girisi_pencere)
            entry_kullanici_adi.pack(pady=5)
            
            tk.Label(doktor_girisi_pencere, text="Şifeniz:").pack()
            entry_sifre = tk.Entry(doktor_girisi_pencere, show="*")
            entry_sifre.pack(pady=5)
            
            tk.Button(doktor_girisi_pencere, text="Giriş Yap" , width=15, command=btn_giriş_yap_click).pack(pady=10)
            
            #pencereyi Göster
            doktor_girisi_pencere.mainloop()
            
            #ana giriş fnksiyonu iöinbde çağırabilir
            if__name__=="__main__":
                frm_doktor_giris()
        