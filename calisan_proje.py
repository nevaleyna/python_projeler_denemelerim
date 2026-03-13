# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:02:12 2026

@author: PC
"""

calisanlar = []
puanlar = []
ebuyuk=-1
en_basarili=""
while True:
    isim = input("Çalışan adı (Çıkış için 'q'): ")
    if isim == 'q':
        break
    
    projeler = int(input(f"{isim} kaç proje tamamladı? "))
    hatalar = int(input(f"{isim} kaç hata yaptı? "))
    # her proje 10 puan hatası varsa 5 puan silinir
    toplam_puan = (projeler * 10) - (hatalar * 5)
    
    calisanlar.append(isim)
    puanlar.append(toplam_puan)
    
    print(f"{isim} için hesaplanan performans puanı: {toplam_puan}")
    if toplam_puan> ebuyuk:
        ebuyuk=toplam_puan
        en_basarili=isim
    
    if toplam_puan >= 80:
        print("Sonuç: Yüksek Performans! ")
    elif toplam_puan <= 30:
        print("Sonuç: Destek Gerekli! ")
    else:
        print("Sonuç: Standart.")
print(f"en yüksek puan:{ebuyuk} ({en_basarili})")
print("\n--- Günlük Rapor Tamamlandı ---")

