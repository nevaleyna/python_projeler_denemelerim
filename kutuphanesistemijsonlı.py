# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:06:07 2026

@author: PC
"""

import json  
import os  


KUTUPHANE_LISTESI = []
DOSYA_ADI = "kutuphane.json"

def verileri_yukle():
    """Program açıldığında JSON dosyasındaki kitapları listeye yükler."""
    global KUTUPHANE_LISTESI
    # Eğer bilgisayarda bu isimde bir JSON dosyası varsa oku
    if os.path.exists(DOSYA_ADI):
        try:
            with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
                KUTUPHANE_LISTESI = json.load(dosya)
                print(f" Veriler başarıyla yüklendi! Toplam kitap sayısı: {len(KUTUPHANE_LISTESI)}")
        except Exception as e:
            print(f" Dosya okunurken bir hata oluştu: {e}")
            KUTUPHANE_LISTESI = []
    else:
        
        print(" Kayıtlı dosya bulunamadı. Yeni bir kütüphane veri tabanı oluşturuldu.")
        KUTUPHANE_LISTESI = []

def verileri_kaydet():
    """Listemizdeki güncel kitapları anlık olarak JSON dosyasına yazar."""
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            # indent=4: JSON dosyasının süslü ve okunabilir yazılmasını sağlar.
            # ensure_ascii=False: Türkçe karakterlerin bozulmasını önler.
            json.dump(KUTUPHANE_LISTESI, dosya, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f" Veriler kaydedilirken hata oluştu: {e}")

def kitap_ekle():
    """Kullanıcıdan bilgileri alıp yeni bir kitap kartı oluşturur."""
    print("\n--- YENİ KİTAP EKLE ---")
    ad = input("Kitap Adı: ").strip()
    yazar = input("Yazar Adı: ").strip()
    
    try:
        sayfa = int(input("Sayfa Sayısı: "))
    except ValueError:
        print(" Geçersiz sayfa sayısı! Kitap ekleme iptal edildi.")
        return

    
    yeni_kitap = {
        "ad": ad,
        "yazar": yazar,
        "sayfa_sayisi": sayfa,
        "odunc_verildi_mi": False  
        }
    
    KUTUPHANE_LISTESI.append(yeni_kitap)
    verileri_kaydet()  # Değişikliği anında JSON dosyasına yazıyoruz.
    print(f" '{ad}' kütüphaneye başarıyla eklendi ve JSON dosyasına kaydedildi!")

def kitaplari_listele():
    """Kütüphanedeki tüm kitapları durumlarıyla birlikte ekrana basar."""
    print("\n--- KÜTÜPHANE KİTAP LİSTESİ ---")
    if not KUTUPHANE_LISTESI:
        print("Kütüphanede henüz hiç kitap yok.")
        return

    for sira, kitap in enumerate(KUTUPHANE_LISTESI, 1):
        
        durum = " Ödünç Verildi" if kitap["odunc_verildi_mi"] else " Kütüphanede Mevcut"
        print(f"{sira}. Kitap: {kitap['ad']} | Yazar: {kitap['yazar']} | Sayfa: {kitap['sayfa_sayisi']} | Durum: {durum}")

def durum_degistir():
    """Bir kitabın ödünç verilme veya geri alınma durumunu günceller."""
    kitaplari_listele()
    if not KUTUPHANE_LISTESI:
        return
        
    aranan = input("\nDurumunu değiştirmek istediğiniz kitabın tam adını girin: ").strip().lower()
    bulundu = False

    for kitap in KUTUPHANE_LISTESI:
        
        if kitap["ad"].lower() == aranan:
           
            kitap["odunc_verildi_mi"] = not kitap["odunc_verildi_mi"]
            verileri_kaydet()  
            yeni_durum = "Ödünç Verildi" if kitap["odunc_verildi_mi"] else "Geri Alındı (Kütüphanede)"
            print(f" '{kitap['ad']}' kitabının durumu '{yeni_durum}' olarak güncellendi!")
            bulundu = True
            break

    if not bulundu:
        print(" Bu isimde bir kitap bulunamadı.")

def sistemi_sifirla():
    """Tüm verileri siler ve JSON dosyasını temizler."""
    onay = input("\n TÜM KÜTÜPHANE VERİLERİNİ SİLMEK İSTEDİĞİNİZE EMİN MİSİNİZ? (evet/hayır): ").strip().lower()
    if onay == "evet":
        global KUTUPHANE_LISTESI
        KUTUPHANE_LISTESI = []
        verileri_kaydet()
        print(" Kütüphane veri tabanı tamamen sıfırlandı!")
    else:
        print("İşlem iptal edildi.")

def ana_menu():
    """Kullanıcı arayüzü döngüsü."""
    verileri_yukle()  # Program başlarken eski verileri diskten okuyoruz.
    
    while True:
        print("\n METNİN TABANLI AKILLI KÜTÜPHANE SİSTEMİ ")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ödünç/Geri Alma Durumu Güncelle")
        print("4. Sistem Verilerini Sıfırla")
        print("5. Çıkış")
        
        secim = input("Lütfen bir işlem seçin (1-5): ").strip()
        
        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitaplari_listele()
        elif secim == "3":
            durum_degistir()
        elif secim == "4":
            sistemi_sifirla()
        elif secim == "5":
            print(" Kütüphane programından çıkılıyor. İyi günler!")
            break
        else:
            print(" Geçersiz seçim! Lütfen 1-5 arasında bir rakam girin.")

if __name__ == "__main__":
    ana_menu()