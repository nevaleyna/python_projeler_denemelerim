# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:43:27 2026

@author: PC
"""

import random # kargo numaraları birbirinden farklı olsun diye

class Kargo:
    def __init__(self, takip_no, gonderici, alici, konum):
        self.takip_no = takip_no
        self.gonderici = gonderici
        self.alici = alici
        self.durum = "Hazırlanıyor"
        self.gecmis = [f"Kabul Edildi: {konum}"] 

    def durum_guncelle(self, yeni_konum, yeni_durum):
        self.durum = yeni_durum
        self.gecmis.append(f"{yeni_durum}: {yeni_konum}")

kargo_merkezi = {}

def ana_menu():
    while True:
        print("\n--- KARGO TAKİP SİSTEMİ ---")
        print("1. Yeni Kargo Kaydı")
        print("2. Kargo Durumu Güncelle")
        print("3. Kargo Sorgula")
        print("4. Tüm Kargoları Listele")
        print("5. Çıkış")
        
        secim = input("İşlem seçiniz (1-5): ")

        if secim == "1":
            gonderici = input("Gönderici Adı: ")
            alici = input("Alıcı Adı: ")
            cikis = input("Çıkış Şehri: ")
            # 5 haneli takip nosu üretelim
            t_no = str(random.randint(10000, 99999))
            
            yeni_kargo = Kargo(t_no, gonderici, alici, cikis)
            kargo_merkezi[t_no] = yeni_kargo
            print(f"\n Kayıt Başarılı! Takip Numaranız: {t_no}")

        elif secim == "2":
            numara = input("Güncellenecek Takip No: ")
            if numara in kargo_merkezi:
                yeni_cikis = input("Yeni Konum: ")
                yeni_durum = input("Yeni Durum (Örn: Yolda, Teslim Edildi): ")
                kargo_merkezi[numara].durum_guncelle(yeni_cikis, yeni_durum)
                print("Durum güncellendi.")
            else:
                print("Kargo bulunamadı!")

        elif secim == "3":
            numara = input("Sorgulanacak Takip No: ")
            if numara in kargo_merkezi:
                k = kargo_merkezi[numara]
                print(f"\n--- Kargo Detayı [{numara}] ---")
                print(f"Gönderici: {k.gonderici} | Alıcı: {k.alici}")
                print(f"Güncel Durum: {k.durum}")
                print("Yolculuk Geçmişi:")
                for adim in k.gecmis:
                    print(f" -> {adim}")
            else:
                print(" Geçersiz Takip No.")

        elif secim == "4":
            print("\n--- SİSTEMDEKİ TÜM KARGOLAR ---")
            for numara, k in kargo_merkezi.items():
                print(f"No: {numara} | Alıcı: {k.alici} | Durum: {k.durum}")

        elif secim == "5":
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")
