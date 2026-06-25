# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:22:42 2026

@author: PC
"""
import random  


KATEGORILER = {
    "Yazılım": ["python", "kodlama", "degisken", "dongu", "fonksiyon"],
    "Şehirler": ["istanbul", "izmir", "manisa", "ankara", "samsun"],
    "Hayvanlar": ["aslan", "yunus", "kartal", "kedi", "kopek"]
}

def kategori_sec():
    """Kullanıcıya kategorileri listeler ve geçerli bir seçim yapmasını sağlar."""
    while True:
        print("\n--- LÜTFEN BİR KATEGORİ SEÇİN ---")
        
        for sira, kat in enumerate(KATEGORILER.keys(), 1):
            print(f"{sira}. {kat}")
        
        secim = input("Seçiminiz (1-3): ")
        
        if secim == "1":
            return "Yazılım"
        elif secim == "2":
            return "Şehirler"
        elif secim == "3":
            return "Hayvanlar"
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

def kelime_oyunu():
    """Ana oyun döngüsünü ve mantığını yöneten fonksiyon."""
    
    secilen_kategori = kategori_sec()
    
    kelime_listesi = KATEGORILER[secilen_kategori]
    hedef_kelime = random.choice(kelime_listesi)
    
    
    tahmin_edilen_harfler = [] 
    can_hakki = 6               
    toplam_puan = 100          
    
    print(f"\nOyun Başladı! Kategori: {secilen_kategori}")
    print(f"Kelimeniz {len(hedef_kelime)} harfli. Başarılar!")

    
    while can_hakki > 0:
        
        anlik_durum = ""
        for harf in hedef_kelime:
            if harf in tahmin_edilen_harfler:
                anlik_durum += harf + " "
            else:
                anlik_durum += "_ "
        
        print(f"\nKelime: {anlik_durum}")
        print(f"Kalan Can: {can_hakki} | Mevcut Puan: {toplam_puan}")
        print("Menü: [1] Harf Tahmin Et | [2] İpucu Al (-10 Puan)")
        
        islem = input("İşleminiz: ")
        
        
        if islem == "1":
            tahmin = input("Bir harf girin: ").lower() 
            
            
            if len(tahmin) != 1 or not tahmin.isalpha():
                print("Lütfen sadece tek bir harf girin!")
                continue
                
            if tahmin in tahmin_edilen_harfler:
                print("Bu harfi zaten tahmin etmiştiniz!")
                continue
            
            
            if tahmin in hedef_kelime:
                print(f"Tebrikler! '{tahmin}' harfi kelimede var.")
                tahmin_edilen_harfler.append(tahmin)
            else:
                print(f"Maalesef, '{tahmin}' harfi kelimede yok.")
                tahmin_edilen_harfler.append(tahmin)
                can_hakki -= 1  
                toplam_puan -= 15 
        
        
        elif islem == "2":
            if toplam_puan <= 10:
                print("Yetersiz puan! İpucu alamazsınız.")
                continue
            
            
            bilinmeyen_harfler = []
            for harf in hedef_kelime:
                if harf not in tahmin_edilen_harfler:
                    bilinmeyen_harfler.append(harf)
            
            if bilinmeyen_harfler:
                
                ipucu_harfi = random.choice(bilinmeyen_harfler)
                tahmin_edilen_harfler.append(ipucu_harfi)
                toplam_puan -= 10 
                print(f"İpucu: Kelimede '{ipucu_harfi}' harfi var!")
            else:
                print("Zaten tüm harfleri açmışsınız!")
        
        else:
            print("Geçersiz işlem menüsü!")
            continue

        
        kazandi_mi = True
        for harf in hedef_kelime:
            if harf not in tahmin_edilen_harfler:
                kazandi_mi = False
                break
                
        if kazandi_mi:
            print(f"\nTEBRİKLER! Kelimeyi bildiniz: {hedef_kelime}")
            print(f"Oyunu {toplam_puan} puan ile tamamladınız! ")
            break
            
    
    if can_hakki == 0:
        print(f"\n Oyun Bitti! Canınız tükendi.")
        print(f"Doğru kelime şuydu: {hedef_kelime}")

if __name__ == "__main__":
    kelime_oyunu()