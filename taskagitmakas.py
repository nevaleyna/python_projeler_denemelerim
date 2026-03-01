# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 20:43:55 2025

@author: PC
"""

import random
Liste=["taş","kağıt","makas"]
pc=random.choice(Liste)
oyuncu=input("[taş ,kağıt, makas]").capitalize()
print("bilgisayar",pc,"seçti")
print("oynayan",oyuncu,"seçti")
if pc==oyuncu:
    print("eşit")
elif pc=="kağıt" and oyuncu=="taş":
    print("oyuncu kaybetti")
elif pc=="taş" and oyuncu=="makas":
    print("oyuncu kaybetti")
elif pc=="makas" and oyuncu=="kağıt":
    print("oyuncu kaybetti")
elif pc=="kağıt" and oyuncu=="makas":
    print("pc kaybetti")
elif pc=="taş" and oyuncu=="kağıt":
    print("pc kaybetti")
else:
    print("pc kaybetti")

    

    
    