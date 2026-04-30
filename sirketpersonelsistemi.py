# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:47:02 2026

@author: PC
"""

personeller={}
son_id=1000
def personel_ekle():
    global son_id
    print("------yeni personel kaydı------")
    ad=input("lütfen adı giriniz : ")
    departman=input("lütfen departmanı girinizzz : ")
    try:
        maas=float(input("başlangıç maaşı: "))
        son_id+=1
        personeller[son_id]={"ad":ad, "departman":departman,"maas":maas}
        print(f"kayıt başarılı personel id :{son_id}")
    except ValueError:
        print("HATA!!! Maaş sayısal bir değer olmalı")

def personelleri_listele():
    print("-----şirket personel listesi------")
    if not personeller:
        print("henüz kayıtlı personeel bulunmuyor ")
    else:
        for pers_id,bilgi in personeller.items():
            print(f"id:{pers_id}  isim:{bilgi["ad"]}   maaş:{bilgi["maas"]} TL")

def zamyap():
    print("-----Maaş güncellemesi-----")
    pers_id=int(input("zam yapılacak personel id : "))
    if pers_id in personeller:
        oran=float(input("zam oranı (%) : "))
        eski_maas=personeller[pers_id]["maas"]
        yeni_maas=eski_maas*(1+oran/100)
        personeller[pers_id]["maas"]=yeni_maas
        print(f"{personeller[pers_id]["ad"]}için yeni maaş: {yeni_maas}TL")
    else:
        print("personel bulunamadı!")
        
def menu():
    while True:
        print("-----şirket yönetim paneli-----")
        print("1--personel ekle")
        print("2--personelleri listele")
        print("3--maaş zammı yap")
        print("4--çıkış")
        
        secim=input("seçiminiz (1-4) :")
        if secim=="1":
            personel_ekle()
        elif secim=="2":
            personelleri_listele()
        elif secim=="3":
            zamyap()
        elif secim=="4":
            print("sistemden çıkılıyor ")
            break
        else:
            print("geçersiz seçim!")
if __name__=="__main__":
    menu()
        
        
        
        
