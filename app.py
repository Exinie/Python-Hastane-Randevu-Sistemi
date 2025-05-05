import sqlite3
from flask import Flask, render_template, Response, session
import bcrypt
from veritabani_fonksiyonlari import *

app = Flask(__name__)

@app.route("/")
def index():
    name = "Exinie"
    return render_template('index.html', person=name)

@app.route("/kayit")
def kayit():
    # return render_template("register.html")
    kayit_sonucu = kayit_islemi()

    if kayit_sonucu:
        return ("Kayıt başarılı")
    else:
        return ("Kayıt başarısız")

@app.route("/giris")
def giris():
    return render_template("login.html")

@app.route("/admin/giris")
def yonetici_giris():
    return render_template("/admin/login.html")