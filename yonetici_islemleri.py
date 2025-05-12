import tkinter as tk
from tkinter import ttk, messagebox


kullanicilar = {}

def kullanici_ekle():
    adi = entry_ad.get()
    sifre = entry_sifre.get()
    yetki = combo_yetki.get()
 
 if not adi or not sifre or not yetki:
        messagebox.showwarning("Hata", "Tüm alanlar doldurulmalıdır.")
        return

if adi in kullanicilar:
        messagebox.showwarning("Hata", "Bu kullanıcı zaten mevcut.")
    else:
        kullanicilar[adi] = {"sifre": sifre, "yetki": yetki}
        messagebox.showinfo("Başarılı", "Kullanıcı eklendi.")
        listele()

def kullanici_sil():
    adi = entry_ad.get()
    if adi in kullanicilar:
        del kullanicilar[adi]
        messagebox.showinfo("Silindi", "Kullanıcı silindi.")
        listele()
    else:
        messagebox.showwarning("Hata", "Kullanıcı bulunamadı.")

def kullanici_guncelle():
    adi = entry_ad.get()
    sifre = entry_sifre.get()
    yetki = combo_yetki.get()

    if adi in kullanicilar:
        if sifre:
            kullanicilar[adi]["sifre"] = sifre
        if yetki:
            kullanicilar[adi]["yetki"] = yetki
        messagebox.showinfo("Güncellendi", "Kullanıcı güncellendi.")
        listele()
    else:
        messagebox.showwarning("Hata", "Kullanıcı bulunamadı.")
        
def listele():
    liste.delete(0, tk.END)
    for k_adi, bilgi in kullanicilar.items():
        liste.insert(tk.END, f"{k_adi} - {bilgi['yetki']}")



#arayüz

pencere = tk.Tk()
pencere.title("Yönetici Kullanıcı Paneli")

tk.Label(pencere, text="Kullanıcı Adı:").pack()
entry_ad = tk.Entry(pencere)
entry_ad.pack()

tk.Label(pencere, text="Şifre:").pack()
entry_sifre = tk.Entry(pencere, show="*")
entry_sifre.pack()

tk.Label(pencere, text="Yetki:").pack()
combo_yetki = ttk.Combobox(pencere, values=["yönetici", "doktor", "hasta"])
combo_yetki.pack()

tk.Button(pencere, text="Ekle", command=kullanici_ekle).pack()
tk.Button(pencere, text="Sil", command=kullanici_sil).pack()
tk.Button(pencere, text="Güncelle", command=kullanici_guncelle).pack()
tk.Button(pencere, text="Listele", command=listele).pack()

liste = tk.Listbox(pencere, width=40)
liste.pack()

pencere.mainloop()


