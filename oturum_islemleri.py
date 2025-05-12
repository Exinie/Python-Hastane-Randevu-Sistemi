import tkinter as tk
from tkinter import messagebox
import sqlite3


# Oturum array listesi
oturum = []

# Kullanıcı oturumu oluşturma fonksiyonu
def oturum_oluştur(giris_yapilan_oturum_bilgileri=[]):
    oturum.append(giris_yapilan_oturum_bilgileri)
    print(f"[+] Oturum oluşturuldu: {oturum}")

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

def hasta_kayit_ol(tc_no, sifre, ad, soyad):

    if tc_no.strip() and sifre.strip() and ad.strip() and soyad.strip():
        
        if len(tc_no) < 11:
            messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numarası.")
        elif hasta_tc_kayitli_mi(tc_no):
            messagebox.showwarning("Uyarı", "Girilen TC kimlik numarası zaten kayıtlı.")
        else:
            conn = sqlite3.connect('veritabani.db')
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
   
    if tc_no.strip() and sifre.strip():

        if len(tc_no) < 11:
            messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numarası.")
        elif doktor_sifre_dogrula(tc_no, sifre):
            messagebox.showinfo("Bilgi", "Hoş geldiniz!")

            conn = sqlite3.connect('veritabani.db')
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM DOKTORLAR WHERE tc_no = ?;
            ''', (tc_no,))

            doktor_giris_yapilan_kullanici_bilgileri = cursor.fetchone()
            conn.close()

            oturum_oluştur(doktor_giris_yapilan_kullanici_bilgileri)
            return True
        else:
            messagebox.showwarning("Uyarı", "TC kimlik numarası veya şifre yanlış!")

    else:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz.")
        return False
    
def hasta_oturum_ac(tc_no, sifre):
    return False

