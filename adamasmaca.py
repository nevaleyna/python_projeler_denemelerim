# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 21:22:54 2025

@author: PC
"""

import random
liste=["kırmızı","turuncu","yeşil","mavi"]
kelime=random.choice(liste)
man=['''
   
     +----+
     o     |
   / | \   |
   /  \    |
         ----''','''
      +----+
      o     |
    / | \   |
    /       |
          ----''','''
      +----+
      o     |
    / | \   |
            |
          ----''','''
       +----+
       o     |
     / |     |
             |
           ----''','''
       +----+
       o     |
     /       |
             |
           ----''','''
       +----+
       o     |
             |
             |
           ----''','''
         +----+
               |
               |
               |
             ----''']
dogruharf=[]
yanlisharf=[]
hak=len(man)

while hak>0:
    out=""
    for i in kelime :
        if i in dogruharf:
            out+=i 
            
        else:
            out+="_"
    if out==kelime:
        break
    print("kelime ",out)
    print(man[hak-1]) 
    yeniharf=input("harf gir :")
    if yeniharf in dogruharf or yeniharf in yanlisharf:
        print(yeniharf,"zaten girildi")
    elif yeniharf in kelime:
        print("doğru harf")
        dogruharf.append(yeniharf)
    else:
        print("yanlış bir harf girdin")
        hak-=1
        
