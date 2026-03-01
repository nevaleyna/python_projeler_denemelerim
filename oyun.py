import random
def oyun():
    die1=random.randrange(1,7)
    die2=random.randrange(1,7)
    workSum=die1+die2
    print("player %d+%d=%d"%(die1,die2,workSum))
    return workSum
sum =oyun()
if sum==7 or sum==11:
    durum="kazandı"
elif sum==2 or sum==3 or sum==12:
    durum="kaybetti"
else:
    durum="devam et"
    puan=sum
    print("puanım",puan)
while durum=="devam et":
    sum=oyun()
    if sum==puan:
        durum="kazandı"
    elif sum==7:
        durum="kaybetti"
if durum=="kazandı":
    print("oyuncu kazandı")
else:
     print("oyuncu kaybetti")  