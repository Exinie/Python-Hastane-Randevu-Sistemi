import tkinter as tk
from tkinter import messagebox
import sqlite3


def tc_kayitli_mi(tc_no):
    
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

def kayit_ol(tc_no, sifre):

    if tc_kayitli_mi(tc_no):
        messagebox.showwarning("Uyarı", "Girilen TC kimlik numarası zaten kayıtlı.")
    else:
        conn = sqlite3.connect('veritabani.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO HASTALAR (tc_no, sifre) VALUES (?, ?)
        ''', (tc_no, sifre))

        conn.commit()
        conn.close()

def oturum_ac(kullaniciadi, sifre):
    return False

    