#--------------------------
'''
A paros nevű függvény,
egy számot kap bemenetként, 
majd True-val tér vissza, ha a szám páros és 
False-al ha a szám páratlan.
'''
def paros(x):
    if x%2 == 0:
        return True
    else:
        return False




#--------------------------
'''
A harommal_oszthato nevű függvény,
egy számot kap bemenetként és 
True-val tér vissza, ha a szám hárommal osztható és 
False-al ha nem.
'''
def harommal_oszthato(x):
    return x%3 == 0


#--------------------------
'''
A szamtani_kozep nevű függvény, 
két számot kap és 
visszatér a számtani középpel.
'''
def szamtani_kozep(x,y):
    return (x+y)/2



#--------------------------
'''
Az abszolut nevű függvény, 
a bemenő paraméterként kapott szám 
abszolút értékével tér vissza.
'''
def abszolut(x):
    if x < 0:
        return x*-1
    return x


#--------------------------
'''
A negyzet_terulet nevű függvény,
egy négyzet oldalhosszát kapja bemenetként és 
visszatér a négyzet területével.
'''
def negyzet_terulet(x):
    return x*x


#--------------------------
'''
A teglatest_terfogat nevű függvény, 
bemenetként megkapja a téglatest oldalainak hosszúságát és 
a téglatest térfogatával tér vissza.
'''
def teglatest_terfogat(x,y,z):
    return x*y*z


#--------------------------
'''
A maradek nevű függvény,
két számot kap bemenetként és 
visszatér a két szám hányadosának maradékával.
'''
def maradek(x,y):
    return x%y


#--------------------------
'''
A derekszogu_haromszog_terulet nevű függvény, 
bemenetként megkapja a befogók hosszát és 
a háromszög területével tér vissza.
'''
def derekszogu_haromszog_terulet(x,y):
    return (x*y)/2


#--------------------------
'''
A teglalap_atloja nevű függvény, 
bemenetként megkapja az oldalak hosszát és 
az átló hosszával tér vissza.
'''
def teglalap_atloja(x,y):
    return (x**2+y**2)**0.5



#--------------------------
'''
A kisebb nevű függvény,
két számot kap és 
visszatér a kisebbik számmal.

Nem használhatod a min nevű függvényt

'''
def kisebb(x,y):
    if x < y:
        return x
    else:
        return y



#--------------------------
'''
A negyzet_kerulet nevű függvény, 
egy négyzet oldalhosszát kapja bemenetként és 
visszatér a négyzet kerületével.
'''
def negyzet_kerulet(x):
    return 4*x 


#--------------------------
'''
A kocka_terfogat nevű függvény,
bemenetként megkapja a kocka oldal hosszúságát és 
a kocka térfogatával tér vissza.
'''
def kocka_terfogat(x):
    return x*x*x


#--------------------------
'''
A kor_kerulete nevű függvény 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör kerületével.
'''
import math
def kor_kerulete(x):
    return x*2*math.pi




#--------------------------
'''
A kettovel_oszthato nevű függvény, 
egy számot kap bemenetként és 
visszatér True-val, ha a szám kettővel osztható és 
visszatér False-al ha a szám kettővel nem ossztható.
'''
def kettovel_oszthato(x):
    return x%2 == 0


#--------------------------
'''
A negyzet_atloja nevű függvény, 
bemenetként megkapja a négyzet oldalának hosszát és 
az átló hosszával tér vissza.
'''
def negyzet_atloja(x):
    return (x**2+x**2)**0.5


#--------------------------
'''
A teglalap_terulet nevű függvény,
egy téglalap oldalhosszait kapja bemenetként és 
visszatér a téglalap területével.
'''
def teglalap_terulet(x,y):
    return x*y 


#--------------------------
'''
A nagyobb nevű függvény,
két számot kap és 
visszatér a nagyobb számmal.

Nem használhatod a max nevű függvényt.
'''
def nagyobb(x,y):
    if x > y:
        return x
    else:
        return y


#--------------------------
'''
A teglalap_kerulet nevű függvény, 
egy téglalap oldalhosszait kapja bemenetként és 
visszatér a téglalap kerületével.
'''
def teglalap_kerulet(x,y):
    return (x+y)*2


#--------------------------
'''
A hettel_oszthato nevű függvény, 
egy számot kap bemenetként és 
True-val tér vissza, ha a szám héttel osztható és 
False-al ha nem.
'''
def hettel_oszthato(x):
    return x%7 == 0


#--------------------------
'''
Az osszead nevű nevű függvény,
két számot kap és 
visszatér a két szám összegével.

Nem használhatod a sum nevű függvényt!
    
'''
def osszead(x,y):
    return x + y


#--------------------------
'''
A kulonbseg nevű függvény,
két számot kap bemenetként és 
visszatér a két szám különbségével.
'''
def kulonbseg(x,y):
    return x - y


#--------------------------
'''
A derekszogu_haromszog_atfogo nevű függvény, 
bemenetként megkapja a befogók hosszát és 
az átfogó hosszával tér vissza.
'''
def derekszogu_haromszog_atfogo(x , y):
    return (x**2 + y**2)**0.5


#--------------------------
'''
A kor_terulete nevű függvény, 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör területével.
'''
def kor_terulete(x):
    import math
    return x**2 * math.pi 


#======================================================================================================================/home/tanarok/weszerle/Oktatas_2025-26/10K_2/Python/python1