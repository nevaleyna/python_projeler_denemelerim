# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:21:15 2026

@author: PC
"""
import time

def akilli_stok_yonetimi():
    urun_adi = "Robot Kol"
    stok_miktari = 50 
    kritik_stok = 10 
    siparis_verildi = False

    print(f"--- {urun_adi} Stok Takip Sistemi Başlatıldı ---")
    print(f"Mevcut Stok: {stok_miktari}\n")

    
    while stok_miktari > 0:
        
        stok_miktari -= 2  
        
        print(f"Üretim yapıldı. Kalan {urun_adi}: {stok_miktari}")

        
        if stok_miktari <= kritik_stok and not siparis_verildi:
            print("\n[!] UYARI: Stok kritik seviyenin altına düştü!")
            print(f"OTOMATİK İŞLEM: Tedarikçi firmaya yeni sipariş geçildi.")
            siparis_verildi = True 
        
        
        if stok_miktari <= 0:
            print("\n[X] DURDURMA: Stok tükendi! Üretim hattı durduruldu.")
            break

        time.sleep(1) 

    print("\n--- Sistem Kapatıldı ---")

akilli_stok_yonetimi()
