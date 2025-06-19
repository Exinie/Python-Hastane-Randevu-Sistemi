# 🏥 Doğuş Hastanesi - Hastane Randevu Otomasyon Sistemi

Bu proje, Python programlama dili kullanılarak geliştirilmiş, hasta, doktor ve yönetici rollerine sahip bir hastane otomasyon sistemidir.

**Başlangıç Tarihi:** 09.05.2025\
**Tamamlanma Tarihi:** 06.06.2025

## 📋 Proje Tanımı

Sistem, hastaların randevu almasını, doktorların randevularını yönetmesini ve yöneticilerin sistemi denetlemesini sağlar. Yapılan tüm işlemler veritabanına kayıt edilerek takip edilebilir.

## ✨ Temel Özellikler

-   **Farklı Kullanıcı Rolleri:**
    -   **Hasta:** Sisteme kayıt olabilir, uygun doktorlardan randevu alabilir ve mevcut randevularını iptal edebilir.
    -   **Doktor:** Kendisine atanmış randevuları listeleyebilir, randevuları onaylayabilir, tamamlandı olarak işaretleyebilir veya iptal edebilir.
    -   **Yönetici:** Tüm kullanıcıları (hasta, doktor, yönetici) listeleyebilir, sisteme yeni kullanıcı ekleyebilir veya mevcut kullanıcıları silebilir. Ayrıca, sistemde gerçekleşen tüm işlem kayıtlarını (logları) görüntüleyebilir ve bu kayıtları CSV formatında dışa aktarabilir.
-   **Görsel Arayüz:** Uygulamanın görsel arayüzü, Python'un standart kütüphanesi olan Tkinter kullanılarak geliştirilmiştir.
-   **Veritabanı Yönetimi:** Tüm veriler (kullanıcı bilgileri, randevular, loglar) SQLite veritabanında saklanmaktadır.
-   **Modüler Tasarım:** Proje, görevlerine göre ayrı modüllere (Python dosyalarına) bölünerek daha yönetilebilir ve okunabilir hale getirilmiştir.
-   **Raporlama ve Kayıt:** Yöneticiler, sistem loglarını `.csv` formatında dışarı aktararak raporlama yapabilir.

## 🛠️ Gerekli Kütüphaneler

requirements.txt dosyasına göz atabilirsiniz, ayrıca kurulum için:\
`python -m pip install -r requirements.txt`

## 📂 Proje Modül Yapısı

Proje, görevlerine göre aşağıdaki modüllere ayrılmıştır:

-   `main.py`: Uygulamanın ana giriş noktasıdır. Tüm Tkinter pencerelerini ve arayüz akışını yönetir.
-   `veritabani_kurulumu.py`: Programın ilk çalışmasında SQLite veritabanını ve gerekli tabloları oluşturur.
-   `oturum_islemleri.py`: Kullanıcıların (hasta, doktor, yönetici) kayıt, giriş, çıkış ve oturum (session) yönetimi işlemlerini gerçekleştirir.
-   `hasta_islemleri.py`: Hastaların randevu alma, listeleme ve iptal etme gibi işlemlerini yönetir.
-   `doktor_islemleri.py`: Doktorların kendilerine atanan randevularını yönetmesi gibi işlemlerini yönetir.
-   `yonetici_islemleri.py`: Yöneticilerin kullanıcı yönetimi ve log işlemleri gibi yetkilerini yöneten fonksiyonları içerir.
-   `log_islemleri.py`: Sistemdeki tüm önemli işlemlerin veritabanına kaydedilmesini sağlar.
-   `veritabani.db`: Tüm uygulama verilerinin saklandığı SQLite veritabanı dosyası.

## 👥 Proje Ekibi ve Görev Dağılımı

Bu proje, bir final projesi kapsamında geliştirilmiştir. Projenin geliştirme süreci, modüler bir yaklaşımla ekip üyeleri arasında paylaştırılmıştır. Her üye, sorumlu olduğu modülün hem back-end kodlamasını hem de bu modüle ait Tkinter front-end kodlamasını üstlenmiştir.

| Ad - Soyad        | Sorumlu Olduğu Bölüm / Görev                                       |
| ----------------- | ------------------------------------------------------------------ |
| Erdem Ural        | Oturum (session) ve kullanıcı kayıt / giriş işlemleri. İşlem kaydı (log) modülü |
| Ege Yardımcı      | Veritabanı şeması oluşturulması ve kurulumu. Hasta işlem modülü |
| Yiğit Yıldız      | Doktor işlem modülü |
| Nuh Mehmet Turhan | Yönetici işlem modülü |