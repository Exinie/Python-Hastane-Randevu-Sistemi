import sqlite3
import tkinter as tk
from tkinter import messagebox


def listele():
    liste.delete(0, tk.END)
    conn = sqlite3.connect("veritabani.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * from kullanicilar")
    for row in cursor.fetchall():
        liste.insert(tk.END, f"{row[0]} - {row[2]}")
    conn.close()    

def kullanici_ekle():
    ad = entry_ad.get()
    sifre = entry_sifre.get()
    yetki =combo_yetki.get()

    if not ad or not sifre or not yetki:
        messagebox.showwarning("Hata", "Tüm alanlar doldurulmalıdır.")
        return
    
    try:
        conn = sqlite3.connect("veritabani.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre, yetki) VALUES (?, ?, ?)",(ad, sifre, yetki))
        conn.commit()
        conn.close()
        messagebox.showinfo("Başarılı", "Kullanıcı eklendi.")
        listele()
    except sqlite3.IntegrityError:
        messagebox.showwarning("Hata", "Bu kullanıcı zaten var.")    
 

def kullanici_sil():
    ad = entry_ad.get()
    if not ad:
        messagebox.showwarning("Hata", "Silinecek kullanıcı adı girilmelidir.")
        return
    
    conn = sqlite3.connect("veritabani.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kullanicilar WHERE kullanici_adi=?", (ad,))
    if cursor.rowcount == 0:
        messagebox.showwarning("Hata", "Kullanıcı bulunamadı.")
    else:
        messagebox.showinfo("Başarılı", "kullanıcı silindi.")
    conn.commit()
    conn.close()
    listele()         

def kullanici_guncelle():
    ad = entry_ad.get()
    sifre = entry_sifre.get()
    yetki = combo_yetki.get()

    if not ad or not sifre or not yetki:
        messagebox.showwarning("Hata","Tüm alanlar doldurulmalıdır.")
        return

    conn = sqlite3.connect("veritabani.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE kullanicilar SET sifre=?, yetki=? WHERE kullanici_adi=?",(sifre, yetki ,ad))
    if cursor.rowcount == 0:
        messagebox.showwarning("Hata", "Kullanıcı bulunamadı.")
    else:
        messagebox.showinfo("Başarılı", "Kullanıcı güncellendi.")
    conn.commit()
    conn.close()
    listele()

