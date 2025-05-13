import tkinter as tk
from tkinter import messagebox
import sqlite3

'''
Bu dosyada oturum (session) işlemleri, giriş veya kayıt işlemleri gerçekleştirilir.
'''

# Giriş yapan kullanıcıya ait oturum bilgisi (dict olarak tutulur)
oturum = None

# Kullanıcı oturumu oluşturma fonksiyonu
def oturumu_baslat(kullanici_bilgisi):
    global oturum
    oturum = dict(kullanici_bilgisi)
    print(f"[+] Oturum başlatıldı: {oturum}")

def doktor_sifre_dogrula(tc_no, sifre):

    conn = sqlite3.connect('veritabani.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT tc_no FROM DOKTORLAR WHERE tc_no = ? AND sifre = ? LIMIT 1;
    ''', (tc_no, sifre))

    sonuc = cursor.fetchone()
    conn.close()

    if sonuc:
        return True
    else:
        return False

def hasta_tc_kayitli_mi(tc_no):

    conn = sqlite3.connect('veritabani.db')
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

def hasta_kayit_et(tc_no, sifre, ad, soyad):

    if tc_no.strip() and sifre.strip() and ad.strip() and soyad.strip():
        
        if len(tc_no) < 11:
            messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numarası.")
        elif hasta_tc_kayitli_mi(tc_no):
            messagebox.showwarning("Uyarı", "Girilen TC kimlik numarası zaten kayıtlı.")
        else:
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO HASTALAR (tc_no, sifre, ad, soyad) VALUES (?, ?, ?, ?)
            ''', (tc_no, sifre, ad, soyad))

            conn.commit()
            conn.close()

            messagebox.showinfo("Bilgi", "Kayıt başarılı.")
            return True
    else:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz.")
        return False

def doktor_oturum_ac(tc_no, sifre):

    if not tc_no.strip() or not sifre.strip():
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz.")
        return False
    
    if len(tc_no) != 11 or not tc_no.isdigit():
        messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numarası formatı.")
        return False
    
    try:
        conn = sqlite3.connect("veritabani.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM DOKTORLAR WHERE tc_no = ? AND sifre = ? LIMIT 1;
        ''', (tc_no, sifre))

        istenilen_kullanici_bilgisi = cursor.fetchone()
        conn.close()

        oturumu_baslat(istenilen_kullanici_bilgisi)
        messagebox.showinfo("Bilgi", "Hoş geldiniz! " + oturum["ad"] + " " + oturum["soyad"])

        return True
    except:
        messagebox.showwarning("Uyarı", "Yanlış TC kimlik numarası veya şifre.")

def hasta_oturum_ac(tc_no, sifre):
    return False

