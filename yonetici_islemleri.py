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
