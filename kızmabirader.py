# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:12:37 2026

@author: PC
"""

import random  # Zar atma mekanizması (1-6 arası rastgele sayı) için
import os      # Ekranı temizleyip haritayı hep aynı yerde göstermek için


HEDEF_KARE = 20

# Oyuncuların anlık konumları ve oyuna girip girmedikleri (6 atma şartı)
oyuncular = {
    "Oyuncu 1": {"konum": 0, "aktif_mi": False},
    "Oyuncu 2": {"konum": 0, "aktif_mi": False}
}

def haritayi_ciz():
    """Şekilsiz, sadece klavye karakterlerinden oluşan 20 karelik haritayı çizer."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı temizle
    print("\n=== METİN TABANLI KIZMA BİRADER ===")
    print(f"Hedef Kare: {HEDEF_KARE}\n")

    # İki oyuncu için de haritayı ayrı şeritler halinde çiziyoruz
    for isim, veri in oyuncular.items():
        harita_seridi = []
        for kare in range(1, HEDEF_KARE + 1):
            if veri["konum"] == kare:
                # Piyonun olduğu kareye numarasını yaz (1 veya 2)
                harita_seridi.append(isim[-1])
            else:
                # Boş kareleri nokta ile göster
                harita_seridi.append(".")
        
        # Haritayı ekrana bas
        yol_gorunumu = "".join(harita_seridi)
        print(f"{isim} Başlangıç -> [{yol_gorunumu}] -> BİTİŞ (Konum: {veri['konum']})")
    print("=" * 45)

def hamle_yap(su_anki_oyuncu, rakip_oyuncu):
    """Sırası gelen oyuncunun zar atma ve ilerleme mantığı."""
    input(f"\n {su_anki_oyuncu} zar atmak için ENTER'a basın...")
    zar = random.randint(1, 6)
    print(f" Atılan Zar: {zar}")

    veri = oyuncular[su_anki_oyuncu]
    rakip_veri = oyuncular[rakip_oyuncu]

    # --- DURUM 1: OYUNCU HENÜZ OYUNA GİRMEMİŞSE ---
    if not veri["aktif_mi"]:
        if zar == 6:
            veri["aktif_mi"] = True
            veri["konum"] = 1
            print(f" HARİKA! {su_anki_oyuncu} 6 attı ve 1. kareden oyuna girdi!")
        else:
            print(f" {su_anki_oyuncu} oyuna girmek için 6 atmalı. Sıra rakibe geçiyor.")
        return

    # --- DURUM 2: OYUNCU ZATEN OYUNDAYSA ---
    yeni_konum = veri["konum"] + zar

    # Kısıtlama Kontrolü: Hedefi aşamaz, tam basmalı
    if yeni_konum > HEDEF_KARE:
        print(f" Geçersiz hamle! Tam {HEDEF_KARE}. kareye ulaşmalısınız. {su_anki_oyuncu} hareket edemedi.")
        return

    # Konumu güncelle
    veri["konum"] = yeni_konum
    print(f" {su_anki_oyuncu}, {zar} kare ilerleyerek {veri['konum']}. kareye ulaştı.")

    # KURAL: Birbirini Yeme Kontrolü
    if veri["konum"] == rakip_veri["konum"] and rakip_veri["konum"] != 0:
        print(f" AMAN TANRIM! {su_anki_oyuncu}, {rakip_oyuncu} piyonunu YEDİ!")
        print(f" {rakip_oyuncu} başlangıç noktasına geri gönderildi ve pasifleşti!")
        rakip_veri["konum"] = 0
        rakip_veri["aktif_mi"] = False

def oyun_dongusu():
    """Oyunu başlatan ve sırayla oyuncuları döndüren ana fonksiyon."""
    sira = "Oyuncu 1"
    
    while True:
        haritayi_ciz()
        
        # Sıradaki ve rakip oyuncuyu belirle
        rakip = "Oyuncu 2" if sira == "Oyuncu 1" else "Oyuncu 1"
        
        # Hamleyi gerçekleştir
        hamle_yap(sira, rakip)
        
        # Kazanma Kontrolü
        if oyuncular[sira]["konum"] == HEDEF_KARE:
            haritayi_ciz()
            print(f"\nTEBRİKLER! {sira} tam {HEDEF_KARE}. kareye ulaşarak OYUNU KAZANDI!  ")
            break
            
        # Sırayı değiştir
        sira = rakip

if __name__ == "__main__":
    oyun_dongusu()