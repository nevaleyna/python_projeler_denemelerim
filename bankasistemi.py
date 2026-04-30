# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:06:08 2026

@author: PC
"""

import json
import os
dosya_adi="bankaveriler.json"
hesaplar={}
def verileri_kaydet():
    with open(dosya_adi,"w",encoding="utf-8") as dosya:
        json.dump(hesaplar,dosya,ensure_ascii=False, indent=4)
    print("veriler güvenli şekilde kaydedildi")
    
def verileri_yukle():
    global hesaplar
    if os.path.exists(dosya_adi):
        with open(dosya_adi,"r",encoding="utf-8") as dosya:
            hesaplar=json.load(dosya)
        print("mevcut veriler başarıyla yüklendi")
    else:
        print("henüz bir  veri dosyası yok,yeni bir sistem başlatılsın")

def hesap_ac():
    print("-----yeni hesap açılışı-----")
    no=input("hesap numarası :")
    if no in hesaplar:
        print("bu numara zaten kayıtlı")
    else:
        isim=input("isim girin :")
        sifre=input("şifre :")
        try:
            bakiye=float(input("ilk bakiye :"))
            hesaplar[no]={"isim":isim,"sifre":sifre,"bakiye":bakiye}
            verileri_kaydet()
            print("hesap açıldı")
        except ValueError:
            print("geçersiz tutar")
            
def bakiye_goruntule():
    no=input("hesap no:")
    if no in hesaplar:
        sifre=input("şifre giriniz :")
        if hesaplar[no]["sifre"]==sifre:
            print(f"bakiyeniz :{hesaplar[no]['bakiye']}TL")
        else:
            print("hatalı şifre girdiniz!")
    else:
        print("hesap bulunamadı")

def ana_menu():
    verileri_yukle()
    while True:
        print("----kalıcı hafızalı banka sistemi-----")
        print("1--hesap aç")
        print("2--bakiye görüntüle")
        print("3--çıkış")
        secim=input("seçiminiz (1-3) :")
        if secim=="1":
            hesap_ac()
        elif secim=="2":
            bakiye_goruntule()
        elif secim=="3":
            print("sistem kapatılıyor")
        else:
            print("geçersiz seçim ")
        
if __name__=="__main__":
    ana_menu()
             
            
            
