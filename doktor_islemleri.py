import tkinter as tk
from tkinter import messagebox
import sqlite3

def doktor_recete_paneli(oturum, root):
    if oturum.get("kullanici_tipi") != "doktor":
        messagebox.showwarning("Uyarı", "Bu işlemleri sadece doktor kullanıcıları yapabilir")
        return

    # Pencereyi temizle
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Doktor - Reçete Yazma Paneli")

    # Sadece sayı girişi için doğrulama fonksiyonu
    def only_numbers(char):
        return char.isdigit() or char == ""

    vcmd = (root.register(only_numbers), '%S')

    # Hasta TC Kimlik No
    tk.Label(root, text="Hasta TC Kimlik No:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    hasta_tc_entry = tk.Entry(root, width=30, validate='key', validatecommand=vcmd)
    hasta_tc_entry.grid(row=0, column=1, padx=5, pady=5)

    # Şikayet
    tk.Label(root, text="Şikayet:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    sikayet_text = tk.Text(root, width=30, height=4)
    sikayet_text.grid(row=1, column=1, padx=5, pady=5)

    # Reçete
    tk.Label(root, text="Reçete:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    recete_text = tk.Text(root, width=30, height=6)
    recete_text.grid(row=2, column=1, padx=5, pady=5)

    # Kaydet butonu fonksiyonu
    def kaydet_recete():
        hasta_tc = hasta_tc_entry.get().strip()
        sikayet = sikayet_text.get("1.0", "end").strip()
        recete = recete_text.get("1.0", "end").strip()

        if not hasta_tc or not sikayet or not recete:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz!")
            return

        if len(hasta_tc) != 11:
            messagebox.showerror("Hata", "Hasta TC Kimlik No 11 haneli olmalıdır!")
            return

        print(f"Reçete Kaydedildi:\nHasta TC: {hasta_tc}\nŞikayet: {sikayet}\nReçete: {recete}")
        messagebox.showinfo("Başarılı", "Reçete kaydedildi!")

        # Alanları temizle
        hasta_tc_entry.delete(0, "end")
        sikayet_text.delete("1.0", "end")
        recete_text.delete("1.0", "end")

    kaydet_btn = tk.Button(root, text="Reçete Kaydet", command=kaydet_recete)
    kaydet_btn.grid(row=3, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    # Örnek oturum (session)
    oturum = {"kullanici_tipi": "doktor"}  # Doktor rolü simülasyonu

    root = tk.Tk()
    root.geometry("400x350")

    doktor_recete_paneli(oturum, root)

    root.mainloop()
