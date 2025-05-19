import tkinter as tk
from tkinter import messagebox
import sqlite3

'''
Bu dosyada oturum (session) işlemleri, giriş veya kayıt işlemleri gerçekleştirilir.
'''

# Kullanıcı oturumu başlatma fonksiyonu
'''
İlgili giriş yapma işleminde ki kontrollerde bir sorun çıkmazsa veritabanından kullanıcı bilgileri çekilir ve bu fonksiyona gönderilir
ardından bu dosyada global olarak tanımlanan oturum değişkenine dictionary (sözlük) olarak aktarılır

Bu oturum değişkeni diğer dosyalar tarafından okunup kullanıcının giriş yapılı olup olmadığı denetlenebilir
veya giriş yapılı olan kullanıcının rolleri okunup ona göre işlemler yapılabilir
'''

def oturumu_baslat(kullanici_bilgisi, kullanici_tipi):
    oturum = dict(kullanici_bilgisi)
    oturum["kullanici_tipi"] = kullanici_tipi
    print(f"[+] Oturum başlatıldı: {oturum}")
    return oturum
# End Kullanıcı oturumu başlatma fonksiyonu

# TC kimlik numarasına göre sistemde kayıtlı Hasta kullanıcısı var mı kontrolünü yapan fonksiyon
def hasta_tc_kayitli_mi(tc_no):

    conn = sqlite3.connect("veritabani.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT tc_no FROM HASTALAR WHERE tc_no = ? LIMIT 1;
    ''', (tc_no,))
    
    sonuc = cursor.fetchone()
    conn.close()

    if sonuc:
        return True
    else:
        return False
# End TC kimlik numarasına göre sistemde kayıtlı Hasta kullanıcısı var mı kontrolünü yapan fonksiyon

# Hasta kayıt etme fonksiyonu
def hasta_kayit_et(tc_no, sifre, ad, soyad):

    if not tc_no.strip() or not sifre.strip() or not ad.strip() or not soyad.strip():
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz.")
        return False
    
    if len(tc_no) != 11 or not tc_no.isdigit():
        messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numarası formatı.")
        return False

    if hasta_tc_kayitli_mi(tc_no):
        messagebox.showwarning("Uyarı", "Girilen TC kimlik numarası zaten kayıtlı.")
        return False
    
    try:
        conn = sqlite3.connect("veritabani.db")
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO HASTALAR (tc_no, sifre, ad, soyad) VALUES (?, ?, ?, ?);
        ''', (tc_no, sifre, ad, soyad))

        conn.commit()
        conn.close()
    
        messagebox.showinfo("Bilgi", "Kayıt başarılı. Giriş sayfasına aktarılıyorsunuz.")
        return True
    except:
        messagebox.showwarning("Uyarı", "Veritabanı hatası")
        return False
# End Hasta kayıt etme fonksiyonu

# Hasta oturum açma fonksiyonu
def hasta_oturum_ac(tc_no, sifre):
    
    if not tc_no.strip() or not sifre.strip():
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz.")
        return
    
    if len(tc_no) != 11 or not tc_no.isdigit():
        messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numarası formatı.")
        return

    try:
        conn = sqlite3.connect("veritabani.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM HASTALAR WHERE tc_no = ? AND sifre = ? LIMIT 1;
        ''', (tc_no, sifre))

        girisi_basarili_kullanici_bilgisi = cursor.fetchone()
        conn.close()

        oturum = oturumu_baslat(girisi_basarili_kullanici_bilgisi, "hasta")
        messagebox.showinfo("Bilgi", "Hoş geldiniz! " + oturum["ad"] + " " + oturum["soyad"])

        return oturum
    except:
        messagebox.showwarning("Uyarı", "Yanlış TC kimlik numarası veya şifre.")
        return
# End Hasta oturum açma fonksiyonu

# Doktor oturum açma fonksiyonu
def doktor_oturum_ac(tc_no, sifre):

    if not tc_no.strip() or not sifre.strip():
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz.")
        return
    
    if len(tc_no) != 11 or not tc_no.isdigit():
        messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numarası formatı.")
        return
    
    try:
        conn = sqlite3.connect("veritabani.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM DOKTORLAR WHERE tc_no = ? AND sifre = ? LIMIT 1;
        ''', (tc_no, sifre))

        girisi_basarili_kullanici_bilgisi = cursor.fetchone()
        conn.close()

        oturum = oturumu_baslat(girisi_basarili_kullanici_bilgisi, "doktor")
        messagebox.showinfo("Bilgi", "Hoş geldiniz! " + oturum["ad"] + " " + oturum["soyad"])

        return oturum
    except:
        messagebox.showwarning("Uyarı", "Yanlış TC kimlik numarası veya şifre.")
        return
# End Doktor oturum açma fonksiyonu

# Yönetici oturum açma fonksiyonu
def yonetici_oturum_ac(kullanici_adi, sifre):

    if not kullanici_adi.strip() or not sifre.strip():
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz.")
        return

    try:
        conn = sqlite3.connect("veritabani.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM YONETICILER WHERE kullanici_adi = ? AND sifre = ? LIMIT 1;
            ''', (kullanici_adi, sifre))
        
        giris_basarili_kullanici_bilgisi = cursor.fetchone()
        conn.close()

        oturum = oturumu_baslat(giris_basarili_kullanici_bilgisi, "yonetici")
        messagebox.showinfo("Bilgi", "Hoş geldiniz! " + oturum["kullanici_adi"])
        
        return oturum
    except:
        messagebox.showwarning("Uyarı", "Yanlış kullanıcı adı veya şifre girdiniz!")
        return
# End Yönetici oturum açma fonksiyonu