import tkinter as tk
from tkinter import messagebox
import sqlite3

from oturum_islemleri import oturum

def doktor_recete_yaz():

    if "Dişçi" in oturum[0]:
        print("doktormussun")

        # İŞLEMLER
    else:
        print("doktor değilsin")
