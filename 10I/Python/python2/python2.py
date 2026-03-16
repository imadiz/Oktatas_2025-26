#--------------------------
''' 
    A szorzat  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak szorzatával.
    
    Üres lista esetén 1 a visszatérési érték.
'''
def szorzat(lista):
    ered = 1
    for i in lista:
        ered *= i
    return ered


#--------------------------
''' 
    Az osszeg  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak összegével.
    Üres lista esetén 0 a visszatérési érték.
    A feladat megoldása során nem használhatod a sum() függvényt!
'''
def osszeg(lista):
    osszeg = 0
    for szam in lista:
        osszeg += szam
    return osszeg


#--------------------------
''' 
    A legkisebb nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legkisebb számával.
    Üres lista esetén None a visszatérési érték.
    
    A feladat megoldása során nem használhatod a min() függvényt!
'''
def legkisebb(lista):
    if len(lista) == 0:
        return None
    minimum = lista[0]
    for i in lista:
        if i < minimum:
            minimum = i
    return minimum



#--------------------------
''' 
    Az utolso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér az adott string utolso karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def utolso_karakter(sztring):
    if sztring == "":
        return None
    return sztring[-1]


#--------------------------
'''
    A negativok_kivalogatasa nevű függvény,
    visszatér egy listával, 
      amely a paraméterként átadott számokat tartalmazó lista
      negatív számait tartalmazza.
'''
def negativok_kivalogatasa(lista):
    neg = []
    for i in lista:
        if i < 0:
            neg.append(i)
    return neg

#--------------------------
'''
    A benne_van_a_stringben nevű függvény.
    első paraméterként egy stringet kap,
    második paraméterként egy betüt.
    Visszatérési értéke True, ha  a betü benne van a stringben.
    A visszatérési érték False, ha  a betü nics benne a stringben.
'''



#--------------------------
''' 
    A lista_atlag nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak átlagával.
'''



#--------------------------
'''
    A faktorialis nevű függvény,
    visszatér a paraméterként megkapott szám faktoriálisával.
'''
def faktorialis(n):
    if n >= 0:
        eredmeny = 1
        for i in range(1, n+1):
            eredmeny *= i
        return eredmeny
    else:
        return None


#--------------------------
''' 
    A pozitivok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        pozitiv számait tartalmazza. 
'''
def pozitivok_kivalogatasa(lista):
    pozi = []
    for i in lista:
        if i > 0:
            pozi.append(i)
    return pozi



#--------------------------
'''
    A kereses_a_listaban nevű függvény.
    Első bemeneti paraméter egy lista,
    második bemeneti paraméter egy szám.
    A visszatérési érték a paraméterként megadott szám
        első előfordulási helye a listában.
    
    A visszatérési érték None, ha a szám nics benne a listában.
'''



#--------------------------
''' 
    A legnagyobb  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legnagyobb számával.
    Üres lista esetén None a visszatérési érték.

    A feladat megoldása során nem használhatod a max függvényt!
'''



#--------------------------
''' 
    A negativok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista negativ számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def negativok_szama(lista):
    if lista== []:
        return 0
    neg= 0
    for i in lista:
        if i < 0:
            neg+=1 
    return neg        

    


#--------------------------
'''
    A paratlanok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páratlan számait tartalmazza.
'''



#--------------------------
''' 
    A parosok_szama  nevű függvény,
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#--------------------------
'''
    A kereses_a_stringben nevű függvény,
    első paraméterként egy sztringet kap,
    második paraméterként egy betüt.
    Visszatérési érték a paraméterként megadott betü
        első előfordulási helye a stringben. 
    
    A visszatérési érték None, ha a betü nics benne a stringben.
'''



#--------------------------
'''
    A parosok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páros számait tartalmazza.
'''



#--------------------------
''' 
    A pozitivok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista pozitív számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#--------------------------
'''
    A benne_van_a_listaban nevű függvény,
    első paraméterként egy listát kap,
    második paraméterként egy számot.
    A visszatérési érték True, ha  a szám benne van a listában.
    A visszatérési érték False, ha  a szám nics benne a listában.
    
    Üres lista esetén a visszatérési érték False.
'''



#--------------------------
''' 
    A paratlanok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#--------------------------
''' 
    Az elso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér a string első karakterével.
    
    Üres string esetén None a visszatérési érték.
'''



#======================================================================================================================/home/tanarok/weszerle/Oktatas_2025-26/10I/Python/python2