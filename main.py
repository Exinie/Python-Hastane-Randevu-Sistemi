import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from hasta_islemleri import HastaIslemleri
from veritabani_kurulumu import Veritabani
from oturum_islemleri import OturumIslemleri
# from doktor_islemleri import doktor_recete_paneli / Sınıfa çevirildiğinde import işlemini yeniden yazarsın.

veritabani_kurulumu_objesi = Veritabani()
oturum_objesi = OturumIslemleri()
hasta_objesi = HastaIslemleri()

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
    hasta_paneli_pencere.geometry("300x350")

    hasta_id = oturum_objesi.oturum["hasta_id"]

    randevu_listesi = hasta_objesi.randevu_listele(hasta_id)   
    
    liste_etiket = tk.Label(hasta_paneli_pencere, text = "Randevularınız:")
    liste_etiket.pack()

    liste_basligi_label = tk.Label(hasta_paneli_pencere, text = f"{'Tarih':<12}     {'Saat':<8}     {'Şikayet':<25}     {'Doktor ID':<8}", font = ("Arial", 9, "bold"))
    liste_basligi_label.pack() 

    listeislemi = tk.Listbox(hasta_paneli_pencere, width = 50, height = 10)
    for randevu in randevu_listesi:
        listeislemi.insert(tk.END, f"{randevu[0]} - {randevu[1]} - {randevu[2]} - {randevu[3]}")
    listeislemi.pack(pady = 5)
    

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_randevu_al_click():
        hasta_paneli_pencere.destroy()
        frm_hasta_randevu_al()

        
    def btn_cikis_yap_click():
        if oturum_objesi.oturumu_kapat():
            hasta_paneli_pencere.destroy()
            ana_pencere.deiconify()
            
    ''' Üst başlık metni '''
    lbl_ana_baslik = tk.Label(hasta_paneli_pencere, text="Hasta Paneli", font=("Arial", 14))
    lbl_ana_baslik.pack()

    lbl_hos_geldiniz_metni = tk.Label(hasta_paneli_pencere, text="Hoş geldiniz " + oturum_objesi.oturum["ad"] + " " + oturum_objesi.oturum["soyad"], font=("Arial", 12))
    lbl_hos_geldiniz_metni.pack(pady=20)

    ''' Metin girişleri ve işlem butonları vs '''
    tk.Button(hasta_paneli_pencere, text="Randevu Oluştur", width=15, command=btn_randevu_al_click).pack(pady=10)
    tk.Button(hasta_paneli_pencere, text="Çıkış Yap", command=btn_cikis_yap_click).pack(pady=2)
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

    ''' Doktor paneli pencere özellikleri '''
    doktor_paneli_pencere = tk.Toplevel()
    doktor_paneli_pencere.title("Doktor Paneli")
    doktor_paneli_pencere.geometry("300x250")

    ''' Buton vb öğelere tıklanınca gerçekleşecek işlemler '''
    def btn_retece_yaz_click():
        doktor_recete_paneli()

    def btn_cikis_yap_click():
        if oturum_objesi.oturumu_kapat():
            doktor_paneli_pencere.destroy()
            ana_pencere.deiconify()
            
    ''' Üst başlık metni '''  
    lbl_ana_baslik = tk.Label(doktor_paneli_pencere, text="Doktor Paneli", font=("Arial", 14))
    lbl_ana_baslik.pack()

    lbl_hos_geldiniz_metni = tk.Label(doktor_paneli_pencere, text="Hoş geldiniz " + oturum_objesi.oturum["ad"] + " " + oturum_objesi.oturum["soyad"], font=("Arial", 12))
    lbl_hos_geldiniz_metni.pack(pady=20)

    tk.Button(doktor_paneli_pencere, text="Reçete Yaz", width=15, command=btn_retece_yaz_click).pack(pady=10)
    tk.Button(doktor_paneli_pencere, text="Çıkış Yap", command=btn_cikis_yap_click).pack(pady=2)
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
        pass
    
    def btn_doktorlari_yonet_click():
        pass

    def btn_yoneticileri_yonet_click():
        pass

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

if __name__ == "__main__":
    main()