# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:01:19 2026

@author: PC
"""

import json
import os
envanterdosya="envanter.json"
siparisdosya="siparisler.json"
envanter={}
siparisler=[]

def verileri_yukle():
    global envanter,siparisler
    if os.path.exists(envanterdosya):
        with open(envanterdosya,"r",encoding="utf-8") as dosya:
            envanter=json.load(dosya)
            
    if os.path.exists((siparisdosya)):
        with open(siparisdosya,"r", encoding="utf-8") as dosya:
            siparisler=json.load(dosya)
            
def verileri_kaydet():
    with open(envanterdosya,"w",encoding="utf-8") as dosya:
        json.dump(envanter,dosya,ensure_ascii=False, indent=4)
    with open(siparisdosya,"w",encoding="utf-8") as dosya:
        json.dump(siparisler,dosya, ensure_ascii=False,indent=4)
def urun_ekle():
    ad=input("ürün adı : ").title()
    fiyat=float(input("birim fiyat :"))
    stok=int(input("stok miktarını girin : "))
    envanter[ad]={"fiyat":fiyat,"stok":stok}
    verileri_kaydet()
    print(f"{ad} envantere eklendi")

def siparis_olustur():
    musteri=input("müşteri :").title()
    urun_adi=input("satın alınan ürün :").title()
    if urun_adi in envanter:
        adet=int(input("adet :"))
        if envanter[urun_adi]["stok"]>=adet:
            envanter[urun_adi]["stok"]-=adet
            toplam=adet*envanter[urun_adi]["fiyat"]
            
            yeni_siparis={"musteri":musteri,"urun":urun_adi,"adet":adet,"toplam_tutar":toplam}
            siparisler.append(yeni_siparis)
            verileri_kaydet()
            print("sipariş hazır toplam : {toplam} TL")
        else:
            print("yetersiz stok")
    else:
        print("ürün bulunamadı")

def rapor_goster():
    print("-----günlük satış raporu-----")
    toplam_kazanc=0
    for s in siparisler:
        print(f"{s['musteri']}  {s['urun']} {s['adet']}  {s['toplam_tutar']}TL")
        toplam_kazanc +=s["toplam_tutar"]  
        print("------toplam ciro : {toplam_kazanc} TL")

def ana_menu():
    verileri_yukle()
    while True:
        print("-----şirket sipariş yönetimi----")
        print("1--envantere ürün ekle")
        print("2--yeni sipariş oluştur")
        print("3--satış raporu görüntüle")
        print("4--çıkış")
        secim=input("seçiminiz (1-4) :")
        if secim=="1":
            urun_ekle()
        elif secim=="2":
            siparis_olustur()
        elif secim=="3":
            rapor_goster()
        elif secim=="4":
            print(" çıkış ")
            break
        else:
            print("geçersiz işlem seçimi!")
if __name__=="__main__": 
    ana_menu()
                     
                                                         
    