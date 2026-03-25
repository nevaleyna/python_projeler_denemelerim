# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 00:35:59 2026

@author: PC
"""

import random
import time

def oyuncak_fabrikasi():
    print("---  Oyuncak Araba Kontrol Merkezi Açıldı  ---")
    print("Robot kol çalışmaya başlıyor...\n")

    while True:
    
        
        tekerlek_sayisi = random.choice([4, 4, 4, 3]) 
        
        print(f"Yeni bir araba geldi. Tekerleklerini sayıyorum...")
        time.sleep(1) #

        
        if tekerlek_sayisi == 4:
            print(f"Tam {tekerlek_sayisi} tekerleği var.")
            print(">>> Kutuya koyulabilir.")
        else:
            print(f"Bu arabanın sadece {tekerlek_sayisi} tekerleği var!")
            print(">>> Çöpe atılsın, tamir edilsin.")

        print("-" * 30)
        
        
        time.sleep(2)


if __name__ == "__main__":
    oyuncak_fabrikasi()