# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:57:33 2026

@author: PC
"""
gorev_listesi=[]
gorev_sayaci=1

def gorev_ekle():
    global gorev_sayaci
    baslik=input("görevin başlığını giriniz :")
    yeni_gorev={"id":gorev_sayaci,"baslik":baslik,"tamamlandi_mi":False}
    gorev_listesi.append(yeni_gorev)
    gorev_sayaci+=1
    print(f"görev başarılı bir şekilde eklendi(id:{yeni_gorev['id']})")

def gorevleri_listele():
    print("---------GÖREV LİSTESİ-------")
    if not gorev_listesi:
        print("henüz hiç görev eklenmemiş")
    else:
        for g in gorev_listesi:
            durum_isareti="+" if g["tamamlandi_mi"] else "-" 
            print(f"{g['id']}-[{durum_isareti}] {g['baslik']}")
    print("-----------------------------")
    
def gorev_tamamla():
    gorevleri_listele()
    try:
        secilen_id=int(input("tamamlanan görevin id'sini girin : "))
        bulundu=False
        for g in gorev_listesi:
            if g["id"]==secilen_id:
                g["tamamlandi_mi"]=True
                print(f"'{g['baslik']}' görevi tamamlandı olarak işareetlendi!")
                bulundu=True
                break
        if not bulundu:
            print("bu id'ye sahip bir görev bulunamadı.")
    except ValueError:
        print("lütfen geçerli bir sayı girin")


def ana_menu():
    while True:
        print("1--görev ekle| 2--listele | 3--tamamla | 4--çıkış")
        secim=input("seciminiz :")
        if secim=="1":
            gorev_ekle()
        elif secim=="2":
            gorevleri_listele()
        elif secim=="3":
            gorev_tamamla()
        elif secim=="4":
            print("bitti")
            break
        else:
            print("geçersiz işlem")
if __name__=="__main__":
    ana_menu()

    