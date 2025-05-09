import tkinter as tk
from tkinter import messagebox
import sqlite3

from main import *

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
    
def oturum_ac(kullaniciadi, sifre):
    return False

    