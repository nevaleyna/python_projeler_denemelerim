# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:40:06 2026

@author: PC
"""

urunler={"elma":{"fiyat":10,"stok":50},"armut":{"fiyat":15,"stok":30}}
ciro=0
def urunekle():
    isim=input("lütfen ürün ismini giriniz :").lower()
    try:
        fiyat=float(input("birim fiyatı : "))
        stok=int(input("stok miktarı : "))
        urunler[isim]={"fiyat":fiyat,"stok":stok}
        print(f"{isim.capitalize()}başarıyla güncellendi")
    except ValueError:
        print("HATA: stok ve fiyat için sayısal değer girin")
def urunleri_listele():
    if not urunler:
        print("sistemde ürün bulunmamaktadır ")
    else:
        for isim,bilgi in urunler.items():
            print(f"ürün:{isim.capitalize()}  fiyat:{bilgi["fiyat"]} TL  stok:{bilgi["stok"]}")
print("--------------------")
def satis_yap():
    global ciro 
    isim=input("ismini giriniz : ").lower()
    if isim in urunler:
        try:
            adet=int(input("kaç adet satılacak :"))
            if adet <= urunler[isim]["stok"]:
                urunler[isim]["stok"]-=adet
                tutar=adet*urunler[isim]["fiyat"]
                ciro+=tutar
                print(f"satış başarılı!!! tutar: {tutar} TL")
            else:
                print(f"yetersiz stok!!! mevcut durum : {urunler[isim]["stok"]}")
        except ValueError:
            print("geçersiz adet girişi yapıldı!")
    else:
        print("ürün bulunamadı")
def ciro_göster():
    print(f"toplam ciro: {ciro}TL")
    
def menu():
    while True:
        print("-------MİNİ STOK VE SATIŞ SİSTEMİ-----")
        print("1--ürün ekle")
        print("2--ürünleri listele")
        print("3--satış yap")
        print("4--ciro göster")
        print("5--çıkış")
        secim=input("seçiminiz(1-5):")
        if secim=="1":
            urunekle()
        elif secim=="2":
            urunleri_listele()
        elif secim=="3":
            satis_yap()
        elif secim=="4":
            ciro_göster()
        elif secim=="5":
            print("programdan çıkılıyor")
            break
        else:
            print("geçersiz seçim, lütfen tekrar deneyin")
    
if __name__=="__main__":
    menu()
                
                
                
                
                
                
                
                
                
                
                
                