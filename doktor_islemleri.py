import tkinter as tk
from tkinter import messagebox
import sqlite3

'''
Örnek giriş yapılı kullanıcının oturumunu (session) okuyup ona göre işlem yapan kod.
oturum (session) bilgisinin içinden "kullanici_tipi" girdisinin karşılığı "doktor" değilse:
messagebox ile kullanıcı uyarılıyor ve fonksiyon False dönüyor

Oturum bilgisini main'den alıyoruz
'''

def doktor_recete_yaz(oturum):
    if oturum["kullanici_tipi"] != "doktor":
        messagebox.showwarning("Uyarı", "Bu işlemi sadece doktor kullanıcıları yapabilir!")
        return False
    else:
        # Doktor reçete yazma işlemleri
        print("Reçete yazılma işlemi gerçekleşiyor çünkü doktor rolüne sahipsiniz")
        pass