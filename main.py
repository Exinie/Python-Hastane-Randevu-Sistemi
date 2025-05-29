import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from hasta_islemleri import HastaIslemleri
from veritabani_kurulumu import Veritabani
from oturum_islemleri import OturumIslemleri
from doktor_islemleri import DoktorIslemleri
from yonetici_islemleri import YoneticiIslemleri

veritabani_kurulumu_objesi = Veritabani()
oturum_objesi = OturumIslemleri()
hasta_objesi = HastaIslemleri()
doktor_objesi = DoktorIslemleri()
yonetici_objesi = YoneticiIslemleri()

''' Ana pencere fonksiyonuna diğer pencerelerden erişilebilmesi için tüm fonskiyonlardan ayrı olarak tanımlanmıştır.  '''
ana_pencere = tk.Tk()

# Ana pencere
def main():

    ''' Ana pencere özellikleri '''
    ana_pencere.title("Doğuş Hastanesi")
    ana_pencere.geometry("300x300")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_hasta_girisi_click():
        ana_pencere.withdraw() # Ana pencereyi gizler
        frm_hasta_giris()

    def btn_hasta_kayit_click():
        ana_pencere.withdraw()
        frm_hasta_kayit()
    
    def btn_doktor_giris_click():
        ana_pencere.withdraw()
        frm_doktor_giris()

    def btn_yonetici_giris_click():
        ana_pencere.withdraw()
        frm_yonetici_giris()
   

    ''' Üst başlık metni '''
    lblBaslik = tk.Label(ana_pencere, text="Doğuş Hastanesi", font=("Arial", 18))
    lblBaslik.pack(pady=20)  # Dikey boşluk

    ''' İşlem butonları '''
    btnHastaGirisYap = tk.Button(ana_pencere, text="Hasta Girişi", width=20, command=btn_hasta_girisi_click)
    btnHastaGirisYap.pack(pady=5)

    btnHastaKayitOl = tk.Button(ana_pencere, text="Hasta Kayıt", width=20, command=btn_hasta_kayit_click)
    btnHastaKayitOl.pack(pady=5)

    btnDoktorGirisYap = tk.Button(ana_pencere, text="Doktor Girişi", width=20, command=btn_doktor_giris_click)
    btnDoktorGirisYap.pack(pady=5)

    btnYoneticiGirisYap = tk.Button(ana_pencere, text="Yönetici Girişi", width=20, command=btn_yonetici_giris_click)
    btnYoneticiGirisYap.pack(pady=5)

    btnCikis = tk.Button(ana_pencere, text="Çıkış", width=20, command=ana_pencere.quit)
    btnCikis.pack(pady=5)

    ''' Bu pencereyi kök pencere yapmak için mainloop ile döngüye alıyoruz '''
    ana_pencere.mainloop()
# End Ana pencere

# Hasta kayıt penceresi
def frm_hasta_kayit():

    ''' Hasta kayıt pencere özellikleri '''
    hasta_kayit_pencere = tk.Toplevel() # Diğer pencerelerden önde açılmasını sağlar
    hasta_kayit_pencere.title("Hasta Kayıt")
    hasta_kayit_pencere.geometry("300x350")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_kayit_ol_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()
        ad = entry_ad.get()
        soyad = entry_soyad.get()

        gelen_cevap = oturum_objesi.hasta_kayit_et(tc_no, sifre, ad, soyad)

        if gelen_cevap == True:
            messagebox.showinfo("Bilgi", "Hasta kaydı başarılı, giriş sayfasına aktarılıyorsunuz.")
            hasta_kayit_pencere.destroy()
            frm_hasta_giris()
        elif gelen_cevap == "bos_alan_var":
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz")
        elif gelen_cevap == "gecersiz_tc_formati":
            messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numara formatı!")
        elif gelen_cevap == "zaten_kayitli":
            messagebox.showwarning("Uyarı", "Girilen TC kimlik numarası zaten kayıtlı!")

    def btn_geri_don_click():
        hasta_kayit_pencere.destroy() # Hasta kayıt penceresini sonlandırır
        ana_pencere.deiconify() # Ana pencereyi geri görünür yapar

    

    ''' Üst başlık metni '''
    lbl_baslik = tk.Label(hasta_kayit_pencere, text="Hasta Kayıt", font=("Arial", 14))
    lbl_baslik.pack()
    lbl_alt_baslik = tk.Label(hasta_kayit_pencere, text="Lütfen kayıt için istenilen bilgileri doldurunuz", font=("Arial", 12))
    lbl_alt_baslik.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(hasta_kayit_pencere, text="TC Kimlik No:").pack()
    entry_tc_no = tk.Entry(hasta_kayit_pencere)
    entry_tc_no.pack()

    tk.Label(hasta_kayit_pencere, text="Ad:").pack()
    entry_ad = tk.Entry(hasta_kayit_pencere)
    entry_ad.pack()

    tk.Label(hasta_kayit_pencere, text="Soyad:").pack()
    entry_soyad = tk.Entry(hasta_kayit_pencere)
    entry_soyad.pack()

    tk.Label(hasta_kayit_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(hasta_kayit_pencere, show="*")
    entry_sifre.pack()
    
    tk.Button(hasta_kayit_pencere, text="Kayıt Ol", width=15, command=btn_kayit_ol_click).pack(pady=10)
    tk.Button(hasta_kayit_pencere, text="Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)
# End Hasta kayıt penceresi

# Hasta giriş penceresi
def frm_hasta_giris():

    ''' Hasta giriş pencere özellikleri '''
    hasta_girisi_pencere = tk.Toplevel()
    hasta_girisi_pencere.title("Hasta Giriş")
    hasta_girisi_pencere.geometry("300x300")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_giris_yap_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()

        gelen_cevap = oturum_objesi.hasta_oturum_ac(tc_no, sifre)

        if gelen_cevap == True:
            hasta_girisi_pencere.destroy()
            frm_hasta_paneli()
        elif gelen_cevap == "bos_alan_var":
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz")
        elif gelen_cevap == "gecersiz_tc_formati":
            messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numara formatı!")
        elif gelen_cevap == "yanlis_tc_sifre":
            messagebox.showwarning("Uyarı", "TC kimlik numaranız veya şifreniz yanlış!")
    
    def btn_geri_don_click():
        hasta_girisi_pencere.destroy()
        ana_pencere.deiconify()

    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(hasta_girisi_pencere, text="Hasta Girişi", font=("Arial", 14))
    lbl_ana_baslik.pack()
    lbl_alt_baslik = tk.Label(hasta_girisi_pencere, text="Hasta kullanıcı bilgilerinizi giriniz", font=("Arial", 12))
    lbl_alt_baslik.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(hasta_girisi_pencere, text="TC Kimlik No:").pack()
    entry_tc_no = tk.Entry(hasta_girisi_pencere)
    entry_tc_no.pack()

    tk.Label(hasta_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(hasta_girisi_pencere, show="*")
    entry_sifre.pack()
    
    tk.Button(hasta_girisi_pencere, text="Giriş Yap", width=15, command=btn_giris_yap_click).pack(pady=10)
    tk.Button(hasta_girisi_pencere, text="Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)
# End Hasta giriş penceresi

# Hasta paneli
def frm_hasta_paneli():

    ''' Hasta paneli pencere özellikleri '''
    hasta_paneli_pencere = tk.Toplevel()
    hasta_paneli_pencere.title("Hasta Paneli")
    hasta_paneli_pencere.geometry("350x470")

    hasta_id = oturum_objesi.oturum["hasta_id"]

    randevu_listesi = hasta_objesi.randevu_listele(hasta_id)   
    liste_etiket = tk.Label(hasta_paneli_pencere, text = "Randevularınız:")
    liste_etiket.grid(row = 3, column = 0, columnspan = 3)

    liste_basligi_label = tk.Label(hasta_paneli_pencere, text = f"{'Tarih':<12}     {'Saat':<8}     {'Şikayet':<25}     {'Doktor ID':<8}", font = ("Arial", 9, "bold"))
    liste_basligi_label.grid(row=4, column=0, columnspan=3, pady=(5, 0)) 

    listeislemi = tk.Listbox(hasta_paneli_pencere, width = 50, height = 10)
    for randevu in randevu_listesi:
        listeislemi.insert(tk.END, f"{randevu[0]} - {randevu[1]} - {randevu[2]} - {randevu[3]} - {randevu[4]}")
    listeislemi.grid(row = 5, column = 0, columnspan = 3, padx = 10, pady = 10)
    
    
    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_randevu_al_click():
        hasta_paneli_pencere.destroy()
        frm_hasta_randevu_al()

        
    def btn_cikis_yap_click():
        if oturum_objesi.oturumu_kapat():
            hasta_paneli_pencere.destroy()
            ana_pencere.deiconify()

    def btn_randevu_iptal_et_click():
        secili_durumda = listeislemi.curselection()
        if not secili_durumda:
            messagebox.showwarning("Uyarı", "Lütfen silmek istediğiniz randevuyu seçin.")
            return

        try:
            secili_durumda = listeislemi.curselection()
            if not secili_durumda:
                messagebox.showwarning("Uyarı", "Lütfen iptal etmek istediğiniz randevuyu belirtiniz.")
                return
            
            secilen = listeislemi.get(secili_durumda[0])
            randevu_id = int(secilen.split(" - ")[0])

            sonuc = hasta_objesi.randevu_sil(randevu_id)

            if sonuc == "Randevu başarıyla iptal edilmiştir.":
               messagebox.showinfo("Başarılı", sonuc)
               hasta_paneli_pencere.destroy()
               frm_hasta_paneli()
            else:
                messagebox.showerror("Hata", sonuc)

        except Exception as hata:
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(hata)}")

        hasta_paneli_pencere.destroy()
      

    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(hasta_paneli_pencere, text="Hasta Paneli", font=("Arial", 14))
    lbl_ana_baslik.grid(row = 0, column = 0, columnspan = 3, pady = (10, 0))

    lbl_hos_geldiniz_metni = tk.Label(hasta_paneli_pencere, text="Hoş geldiniz, " + oturum_objesi.oturum["ad"] + " " + oturum_objesi.oturum["soyad"] + "!", font=("Arial", 16, "bold"))
    lbl_hos_geldiniz_metni.grid(row = 1, column = 0, columnspan = 3, pady = (5, 15))

    ''' Metin girişleri ve işlem butonları vs '''
   
    randevu_butonu = tk.Button(hasta_paneli_pencere, text="Randevu Oluştur", command=btn_randevu_al_click)
    randevu_butonu.grid(row = 8, column = 0, padx = 10, pady = 20)
    cikis_butonu = tk.Button(hasta_paneli_pencere, text="Çıkış Yap", command=btn_cikis_yap_click)
    cikis_butonu.grid(row = 8, column = 1, padx = 10, pady = 20)
    randevu_iptal_butonu = tk.Button(hasta_paneli_pencere, text="Randevuyu iptal et", command=btn_randevu_iptal_et_click)
    randevu_iptal_butonu.grid(row = 8, column = 2, padx = 10, pady = 20)
    
# End Hasta paneli

# Hasta randevu oluşturma penceresi
def frm_hasta_randevu_al():

    ''' Hasta randevu al pencere özellikleri '''
    hasta_randevu_al_pencere = tk.Toplevel()
    hasta_randevu_al_pencere.title("Randevu Al")
    hasta_randevu_al_pencere.geometry("300x350")


    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_geri_don_click():
        hasta_randevu_al_pencere.destroy()
        frm_hasta_paneli()

            
    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(hasta_randevu_al_pencere, text="Randevu Al", font=("Arial", 14))
    lbl_ana_baslik.pack()

    # Örnek doktor listesi
    doktor_listesi = hasta_objesi.doktor_listele()

    # ID ve AdSoyad eşleşmesi (basit sözlük)
    adsoyad_to_id = {f"{d[1]} {d[2]}": d[0] for d in doktor_listesi}
    doktor_adlari = list(adsoyad_to_id.keys())
    

    def btn_randevu_al_click():
        giris_yapilmis_hasta_id = oturum_objesi.oturum["hasta_id"]
        secilen_adsoyad = combobox.get()
        doktor_id = adsoyad_to_id.get(secilen_adsoyad)
        secilen_tarih = tarih_secici.get_date()
        saat_dakika = saat_spin.get() + ":" + dakika_spin.get()
        sikayet = entry_sikayet.get()

        gelen_cevap = hasta_objesi.randevu_al(giris_yapilmis_hasta_id, doktor_id, secilen_tarih, saat_dakika, sikayet)

        if gelen_cevap == True:
            messagebox.showinfo("Bilgi", "Randevunuz başarıyla alınmıştır.")
            hasta_randevu_al_pencere.destroy()
            frm_hasta_paneli()
        elif gelen_cevap == "dolu":
            messagebox.showwarning("Uyarı", "Seçtiğiniz tarihte doktorunuz meşguldür.")


    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(hasta_randevu_al_pencere, text="Doktor tercih ediniz:").pack()
    combobox = ttk.Combobox(hasta_randevu_al_pencere, values=doktor_adlari, state="readonly")
    combobox.set("Doktor Seçin")
    combobox.pack(pady=5)

    tk.Label(hasta_randevu_al_pencere, text="Tarih:").pack()
    tarih_secici = DateEntry(hasta_randevu_al_pencere, date_pattern = "dd-mm-yyyy")
    tarih_secici.pack(pady=5)

    tk.Label(hasta_randevu_al_pencere, text="Saat:").pack()
    saat_spin = tk.Spinbox(hasta_randevu_al_pencere, from_=0, to=23, width=5, format="%02.0f")
    saat_spin.pack()

    tk.Label(hasta_randevu_al_pencere, text="Dakika:").pack()
    dakika_spin = tk.Spinbox(hasta_randevu_al_pencere, from_=0, to=59, width=5, format="%02.0f")
    dakika_spin.pack(pady=5)

    tk.Label(hasta_randevu_al_pencere, text="Şikayetiniz:").pack()
    entry_sikayet = tk.Entry(hasta_randevu_al_pencere)
    entry_sikayet.pack()

    btn = tk.Button(hasta_randevu_al_pencere, text = "Randevu Al", command=btn_randevu_al_click)
    btn.pack()

    tk.Button(hasta_randevu_al_pencere, text = "Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)             
# End Hasta randevu oluşturma penceresi

# Doktor girişi penceresi
def frm_doktor_giris():

    ''' Doktor girişi pencere özellikleri '''
    doktor_girisi_pencere = tk.Toplevel()
    doktor_girisi_pencere.title("Doktor Giriş")
    doktor_girisi_pencere.geometry("300x300")
    
    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_giriş_yap_click():
        tc_no = entry_tc_no.get()
        sifre = entry_sifre.get()

        gelen_cevap = oturum_objesi.doktor_oturum_ac(tc_no, sifre)

        if gelen_cevap == True:
            doktor_girisi_pencere.destroy()
            frm_doktor_paneli()
        elif gelen_cevap == "bos_alan_var":
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz")
        elif gelen_cevap == "gecersiz_tc_formati":
            messagebox.showwarning("Uyarı", "Geçersiz TC kimlik numara formatı!")
        elif gelen_cevap == "yanlis_tc_sifre":
            messagebox.showwarning("Uyarı", "TC kimlik numaranız veya şifreniz yanlış!")
    
    def btn_geri_don_click():
        doktor_girisi_pencere.destroy()
        ana_pencere.deiconify()

    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(doktor_girisi_pencere, text="Doktor Girişi", font=("Arial", 14))
    lbl_ana_baslik.pack()
    lbl_alt_baslik = tk.Label(doktor_girisi_pencere, text="Doktor kullanıcı bilgilerinizi giriniz", font=("Arial", 12))
    lbl_alt_baslik.pack(pady=20)
            
    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(doktor_girisi_pencere, text="TC Kimlik No:").pack()
    entry_tc_no = tk.Entry(doktor_girisi_pencere)
    entry_tc_no.pack(pady=5)
            
    tk.Label(doktor_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(doktor_girisi_pencere, show="*")
    entry_sifre.pack(pady=5)
            
    tk.Button(doktor_girisi_pencere, text="Giriş Yap" , width=15, command=btn_giriş_yap_click).pack(pady=10)
    tk.Button(doktor_girisi_pencere, text="Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)
# End Doktor girişi penceresi

# Doktor paneli
def frm_doktor_paneli():
    doktor_paneli_pencere = tk.Tk()
    doktor_paneli_pencere.title("Doktor Paneli")
    doktor_paneli_pencere.geometry("1000x400")
    
    #Treeview Tablo
    tree = ttk.Treeview(doktor_paneli_pencere, columns=("randevu_id", "hasta_id", "tarih", "saat", "sikayet", "durum"), show="headings")
    for col in ("randevu_id", "hasta_id", "tarih", "saat", "sikayet", "durum"):
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=100)
    tree.pack(fill="both", expand=True)
    
    giris_yapili_doktor_id = oturum_objesi.oturum["doktor_id"]

    def randevulari_yukle():
        tree.delete(*tree.get_children())
        randevular = doktor_objesi.randevulari_listele(giris_yapili_doktor_id)
        if isinstance(randevular, list):
            for randevu in randevular:
                tree.insert("", "end", values=randevu)
        else:
            messagebox.showerror("Hata", "Veritabanı hatası oluştu.")
            
    def secili_randevu_id():
        secim = tree.selection()
        if not secim:
            messagebox.showwarning("Uyarı", "Lütfen bir randevu seçin.")
            return None
        return tree.item(secim[0])["values"][0]

    def btn_rendevu_sil_click():
        randevu_id = secili_randevu_id()
        if randevu_id:
            sonuc = doktor_objesi.randevu_sil(randevu_id)
            if sonuc == "basarili":
                messagebox.showinfo("başarılı", "Randevu Silindi.")
                randevulari_yukle()
            elif sonuc == "randevu_bulunamadi":
                messagebox.showwarning("Uyarı", "Randevu Bulunamadı.")
            else:
                messagebox.showerror("Hata", "Veritabanı hatası oluştu")
                
    def btn_randevu_onayla_click():
        randevu_id = secili_randevu_id()
        if randevu_id:
            sonuc = doktor_objesi.randevu_durum_guncelle(randevu_id, "Onaylandı")
            if sonuc == "basarili":
                messagebox.showinfo("Başarılı", "Randevu onaylandı olarak işaretlendi.")
                randevulari_yukle()
            elif sonuc == "randevu_bulunamadi":
                messagebox.showwarning("Uyarı", "Randevu bulunamadı.")
            else:
                messagebox.showerror("Hata", "Veritabanı hatası oluştu.")
    
    def btn_randevu_tamamla_click():
        randevu_id = secili_randevu_id()
        if randevu_id:
            sonuc = doktor_objesi.randevu_durum_guncelle(randevu_id, "Tamamlandı")
            if sonuc == "basarili":
                messagebox.showinfo("Başarılı", "Randevu tamamlandı olarak işaretlendi.")
                randevulari_yukle()
            elif sonuc == "randevu_bulunamadi":
                messagebox.showwarning("Uyarı", "Randevu bulunamadı.")
            else:
                messagebox.showerror("Hata", "Veritabanı hatası oluştu.")
    
    def btn_cikis_yap_click():
        if oturum_objesi.oturumu_kapat():
            doktor_paneli_pencere.destroy()
            ana_pencere.deiconify()

    # Butonlar
    tk.Button(doktor_paneli_pencere, text="Randevuyu Sil", command=btn_rendevu_sil_click).pack(pady=3)
    tk.Button(doktor_paneli_pencere, text='"Onaylandı" olarak işaretle', command=btn_randevu_onayla_click).pack(pady=3)
    tk.Button(doktor_paneli_pencere, text='"Tamamlandı" olarak işaretle', command=btn_randevu_tamamla_click).pack(pady=3)
    tk.Button(doktor_paneli_pencere, text="Çıkış Yap", command=btn_cikis_yap_click).pack(pady=2)
    
    randevulari_yukle()
    doktor_paneli_pencere.mainloop()           
    
# End Doktor paneli

def frm_yonetici_giris():

    ''' Yönetici giriş pencere özellikleri '''
    yonetici_girisi_pencere = tk.Toplevel()
    yonetici_girisi_pencere.title("Yönetici Giriş")
    yonetici_girisi_pencere.geometry("300x300")
    
    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_giriş_yap_click():
        kullanici_adi = entry_kullanici_adi.get()
        sifre = entry_sifre.get()

        gelen_cevap = oturum_objesi.yonetici_oturum_ac(kullanici_adi, sifre)

        if gelen_cevap == True:
            yonetici_girisi_pencere.destroy()
            frm_yonetici_paneli()
        elif gelen_cevap == "bos_alan_var":
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz")
        elif gelen_cevap == "yanlis_kullaniciadi_sifre":
            messagebox.showwarning("Uyarı", "Kullanıcı adınız veya şifreniz yanlış!")
    
    def btn_geri_don_click():
        yonetici_girisi_pencere.destroy()
        ana_pencere.deiconify()

    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(yonetici_girisi_pencere, text="Yönetici Girişi", font=("Arial", 14))
    lbl_ana_baslik.pack()
    lbl_alt_baslik = tk.Label(yonetici_girisi_pencere, text="Yönetici kullanıcı bilgilerinizi giriniz", font=("Arial", 12))
    lbl_alt_baslik.pack(pady=20)
            
    ''' Metin girişleri ve işlem butonları vs '''
    tk.Label(yonetici_girisi_pencere, text="Kullanıcı adı:").pack()
    entry_kullanici_adi = tk.Entry(yonetici_girisi_pencere)
    entry_kullanici_adi.pack(pady=5)
            
    tk.Label(yonetici_girisi_pencere, text="Şifre:").pack()
    entry_sifre = tk.Entry(yonetici_girisi_pencere, show="*")
    entry_sifre.pack(pady=5)
            
    tk.Button(yonetici_girisi_pencere, text="Giriş Yap" , width=15, command=btn_giriş_yap_click).pack(pady=10)
    tk.Button(yonetici_girisi_pencere, text="Geri Dön", width=15, command=btn_geri_don_click).pack(pady=10)
# End Doktor girişi penceresi

# Yönetici paneli
def frm_yonetici_paneli():

    ''' Yönetici paneli pencere özellikleri '''
    yonetici_paneli_pencere = tk.Toplevel()
    yonetici_paneli_pencere.title("Yönetici Paneli")
    yonetici_paneli_pencere.geometry("350x450")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_hastalari_yonet_click():
        yonetici_paneli_pencere.destroy()
        hastalari_yonet()
    
    def btn_doktorlari_yonet_click():
        yonetici_paneli_pencere.destroy()
        doktorları_yonet()

    def btn_yoneticileri_yonet_click():
        yonetici_paneli_pencere.destroy()
        yoneticileri_yonet()

    def btn_cikis_yap_click():
        if oturum_objesi.oturumu_kapat():
            yonetici_paneli_pencere.destroy()
            ana_pencere.deiconify()

    
    ''' Üst başlık metni '''  
    lbl_ana_baslik = tk.Label(yonetici_paneli_pencere, text="Yönetici Paneli", font=("Arial", 14))
    lbl_ana_baslik.pack()

    lbl_hos_geldiniz_metni = tk.Label(yonetici_paneli_pencere, text="Hoş geldiniz " + oturum_objesi.oturum["kullanici_adi"], font=("Arial", 12))
    lbl_hos_geldiniz_metni.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''
    tk.Button(yonetici_paneli_pencere, text="Hastaları Yönet", command=btn_hastalari_yonet_click).pack(pady=2)
    tk.Button(yonetici_paneli_pencere, text="Doktorları Yönet", command=btn_doktorlari_yonet_click).pack(pady=2)
    tk.Button(yonetici_paneli_pencere, text="Yöneticileri Yönet", command=btn_yoneticileri_yonet_click).pack(pady=2)
    tk.Button(yonetici_paneli_pencere, text="Çıkış Yap", command=btn_cikis_yap_click).pack(pady=2)

    liste = tk.Listbox(yonetici_paneli_pencere, width=40)
    liste.pack(pady=10)
# End yönetici paneli

def hastalari_yonet():
    pencere = tk.Toplevel()
    pencere.title("Hastaları Yönet")

    #hasta listesi
    liste = tk.Listbox(pencere,width=50)
    liste.pack(pady=10)

    hastalar = yonetici_objesi.hastalari_listele()
    for h in hastalar:
        liste.insert(tk.END, f"{h[0]} - {h[1]} {h[2]}")

    #seçilen hastayı silen fonksiyon
    def sil():
        secili = liste.curselection()
        if not secili:
            messagebox.showwarning("uyarı", "Lütfen silinecek hastayı seçin.")
            return
        hasta_id = hastalar[secili[0]][0]
        yonetici_objesi.hasta_sil(hasta_id)
        liste.delete(secili)

        
    def btn_geri_don_click():
        pencere.destroy()
        frm_yonetici_paneli()

    tk.Button(pencere, text="Hastayı Sil", command=sil).pack(pady=5)   
    
    tk.Button(pencere, text="Geri Dön", command=btn_geri_don_click).pack(pady=10)


def doktorları_yonet():
    pencere = tk.Toplevel()
    pencere.title("Doktorları Yönet")

    #doktor listesi
    liste = tk.Listbox(pencere, width=60)
    liste.pack(pady=10)

    doktorlar = yonetici_objesi.doktorları_listele()
    for d in doktorlar:
        liste.insert(tk.END, f"{d[0]} - {d[1]} {d[2]} - {d[4]}")

    entries = {}

 #seçilen doktoru silen fonksiyon
    def sil():
        secili = liste.curselection()
        if not secili:
            messagebox.showwarning("Uyarı", "Lütfen silinecek doktoru seçin.")
            return
        doktor_id = doktorlar[secili[0]][0]
        yonetici_objesi.doktor_sil(doktor_id)
        liste.delete(secili[0])
        messagebox.showinfo("Başarılı", "Doktor silindi.")

     # Yeni doktor ekleyen fonksiyon
    def ekle():
        veriler = [entries[x].get() for x in ["tc", "ad", "soyad", "şifre", "uzmanlık"]]
        if not all(veriler):
            messagebox.showwarning("Uyarı", "Tüm alanlar doldurulmalı.")
            return
        yonetici_objesi.doktor_ekle(*veriler)
        liste.insert(tk.END, f"{veriler[0]} - {veriler[1]} {veriler[2]} - {veriler[4]}")
        messagebox.showinfo("Başarılı", "Doktor eklendi.")

    
    tk.Button(pencere, text="Doktoru Sil", command=sil).pack(pady=5)

      #doktor ekleme alanı
    frame = tk.Frame(pencere)
    frame.pack(pady=10)

    for i, etiket in enumerate(["TC", "Ad", "Soyad", "Şifre", "Uzmanlık"]):
        tk.Label(frame, text=etiket).grid(row=i, column=0, sticky="e")
        e = tk.Entry(frame)
        e.grid(row=i, column=1)
        entries[etiket.lower()] = e


    def btn_geri_don_click():
        pencere.destroy()
        frm_yonetici_paneli()

    tk.Button(frame, text="Doktor Ekle", command=ekle).grid(row=5, columnspan=2, pady=5)

    tk.Button(pencere, text="Geri Dön", command=btn_geri_don_click).pack(pady=10)

def yoneticileri_yonet():
    pencere = tk.Toplevel()
    pencere.title("Yöneticileri Yönet")

    #yönetici listesi
    liste = tk.Listbox(pencere, width=50)
    liste.pack(pady=10)
 
    yoneticiler = yonetici_objesi.yoneticileri_listele()
    for y in yoneticiler:
        liste.insert(tk.END, f"{y[0]} - {y[1]}")

 
      #seçilen yöneticiyi silen fonksiyon
    def sil():
        secili = liste.curselection()
        if not secili:
            messagebox.showwarning("Uyarı", "Lütfen silinecek yöneticiyi seçin.")
            return
        kullanici_adi = yoneticiler[secili[0]][1]
        yonetici_objesi.yonetici_sil(kullanici_adi)
        liste.delete(secili)

    tk.Button(pencere, text="Yönetici Sil", command=sil).pack(pady=5)

#yeni yönetici ekleme alanı
    frame = tk.Frame(pencere)
    frame.pack(pady=10)

    tk.Label(frame, text="Kullanıcı Adı").grid(row=0, column=0)
    entry_ad = tk.Entry(frame)
    entry_ad.grid(row=0, column=1)

    tk.Label(frame, text="Şifre").grid(row=1, column=0)
    entry_sifre = tk.Entry(frame, show="*")
    entry_sifre.grid(row=1, column=1)

    #yeni yönetici ekleyen fonksiyon
    def ekle():
        ad = entry_ad.get()
        sifre = entry_sifre.get()
        if not ad or not sifre:
            messagebox.showwarning("Uyarı", "Alanlar boş olamaz.")
            return
        yonetici_objesi.yonetici_ekle(ad, sifre)
        liste.insert(tk.END, f"{ad}")

    def btn_geri_don_click():
        pencere.destroy()
        frm_yonetici_paneli()


    tk.Button(frame, text="Yönetici Ekle", command=ekle).grid(row=2, columnspan=2, pady=5)

    tk.Button(pencere, text="Geri Dön", command=btn_geri_don_click).pack(pady=10)

if __name__ == "__main__":
    main()