
# 📄 Proje Önerisi

  

## ⚒️ Ekip Üyeleri

  

| Ad - Soyad |  Numarası |
|----------------------|-------------------|
| Erdem Ural           | 202407105086          |
| Ege Yardımcı           | 202407105063          |
| Yiğit Yıldız           | 202407105091          |
| Nuh Mehmet Turhan           | 202407105080          |

  

---

  

## 📚 Proje Tanımı

  

Hastaneler için randevu / otomasyon sistemi.

  

---

  

## 🛠️ Görev Dağılımı

  

| Ad - Soyad | Sorumlu Olduğu Bölüm / Görev       |
|----------------------|------------------------------------|
| Erdem Ural           | Kullanıcı işlemleri fonksiyonları, Tkinter arayüz kodlaması |
| Ege Yardımcı           | Veri tabanı, Vatandaş kullanıcılarının işlemlerinin fonksiyonları |
| Yiğit Yıldız           | Tkinter arayüz kodlaması, Doktor kullanıcılarının işlemlerinin fonksiyonları |
| Nuh Mehmet Turhan           | Tkinter arayüz kodlaması, Yönetici kullanıcılarının işlemlerinin fonksiyonları |

  

---

  

## ✅ Proje Gerekliliklerine Uyum ve Planlanan Uygulama

  


  

### 1. Genel Proje Çalışma Sistemi

Kullanıcı program arayüzünden işlemler yapabilecek, menüler arasında görüntülenen penceredeki butonlar veya diğer elemenler üzerinden gezinebilecek ve bu pencerelerdeki elementler üzerinden arkaplandaki API / fonksiyonlar ile veri alışverişi yapacak.

  

### 2. Veri Tabanı Kullanımı

Kullanılacak veri tabanı SQLite olacaktır. Saklanacak veriler şu şekildedir:\
Hasta, doktor kullanıcı bilgileri: rolleri, randevuları tahlil sonuçları, bilinen rahatsızlıklar / alerjiler.\
yönetici kullanıcı bilgileri.\
Log kayıtları.

  

### 3. Kullanıcı Yönetimi (Farklı Kullanıcı Tipleri)

Hasta : Hasta kullanıcı kaydı yapabilir. Randevu oluşturabilir. Tahlil sonuçlarına bakabilir.\
Doktor : Randevuları görüntüleyebilir, onaylayabilir. Hastanın sağlık bilgilerini görüntüleyebilir, hastaya ilaç yazabilir, hastaya tahlil sonucu girebilir.\
Yönetici : Tüm kullanıcıların bilgilerini, randevularını, yazılan ilaçları, tahlil sonuçlarını görüntüleyebilir, düzenleyebilir, silebilir. Log kayıtlarını görüntüleyebilir.



### 4. İşlem Kayıtları

Kullanıcıdan program arayüzünden yapılan işlem sonucu gelen veriler arka yüzde işlenecek ve görevine göre veri tabanına kaydı gerçekleştirilecek.
  


### 5. Raporlama

Kullanıcı programı çalıştıracak, daha önceden oluşturduğu kullanıcı bilgilerini girerek sisteme giriş yapacak, kullanıcı rolüne bağlı olarak tahlil sonuçlarını görüntüleyip indirme veya log kayıtlarını görüntüleyip indirme gibi işlemleri gerçekleştirecek ve bu şekilde rapor edinmiş olacak.


### 6. Grup Çalışması Kriterleri

- Veri tabanı işlemlerinin özel bir veri tabanı sınıfı üzerinden gerçekleştirilmesi.
- API entegrasyonu yapılarak gerçek zamanlı veri kullanımı.
- Projeye bir görsel arayüz eklenmesi. (Örneğin: Tkinter, PyQt, Streamlit gibi araçlarla)
- Kullanıcının sisteme dosya yükleyebilmesi, dosya kaydedebilmesi veya veri çıktısı alabilmesi. (Örneğin: PDF/CSV rapor oluşturma)
- Admin kullanıcılarının, diğer kullanıcıların yetkilerini değiştirebileceği basit bir yönetim paneli oluşturulması.
- Sistemde oturum açan kullanıcıların tüm işlemlerinin ve bu işlemlere ait tarih/saat bilgilerinin kaydedilmesi.
  


---

  

# 📌 Not:

- Bu dosya **docs/proje_onerisi.md** yolunda saklanmalıdır ardından bu taslak dosyası silinmelidir.

- Belirtilen tüm başlıklar eksiksiz doldurulmalıdır.

- Gereklilikler yüzeysel değil, projenize özgü ve uygulanabilir şekilde açıklanmalıdır.
