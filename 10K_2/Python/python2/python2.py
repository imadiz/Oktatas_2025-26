#--------------------------
''' 
    Az elso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér a string első karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def elso_karakter(sz):
    if sz == "":
        return None
    return sz[0]
    


#--------------------------
''' 
    A legnagyobb  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legnagyobb számával.
    Üres lista esetén None a visszatérési érték.

    A feladat megoldása során nem használhatod a max függvényt!
'''
def legnagyobb(a):
    if len(a) == 0:
        return None
    
    max = a[0]
    for i in a:
        if (i > max):
            max = i

    return max


#--------------------------
''' 
    A parosok_szama  nevű függvény,
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def parosok_szama(gayron):
    if len(gayron) == 0:
        return 0
    
    nimmie = 0
    for i in gayron:
        if i % 2 == 0:
            nimmie += 1

    return nimmie



#--------------------------
''' 
    Az utolso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér az adott string utolso karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def utolso_karakter(trapista):
    if trapista == "":
        return None
    
    return trapista[-1]


#--------------------------
''' 
    A paratlanok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def paratlanok_szama(gayron):
    if len(gayron) == 0:
        return 0
    
    nimmie = 0
    for i in gayron:
        if i % 2 != 0:
            nimmie += 1

    return nimmie




#--------------------------
'''
    A paratlanok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páratlan számait tartalmazza.
'''
def paratlanok_kivalogatasa(camambert):
    
    
    nimmie = []
    for i in camambert:
        if i % 2 != 0:
            nimmie.append(i)

    return nimmie 




#--------------------------
'''
    A kereses_a_listaban nevű függvény.
    Első bemeneti paraméter egy lista,
    második bemeneti paraméter egy szám.
    A visszatérési érték a paraméterként megadott szám
        első előfordulási helye a listában.
    
    A visszatérési érték None, ha a szám nics benne a listában.
'''
def kereses_a_listaban(hat,het):
    index = 0
    for i in hat:
        if i == het:
            return index
        index += 1
    
    return None


#--------------------------
''' 
    Az osszeg  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak összegével.
    Üres lista esetén 0 a visszatérési érték.
    A feladat megoldása során nem használhatod a sum() függvényt!
'''
def osszeg(x):
    if len(x)== 0:
        return 0
    osszeg = 0
    for i in x:
        osszeg += i
    
    return osszeg



#--------------------------
'''
    A faktorialis nevű függvény,
    visszatér a paraméterként megkapott szám faktoriálisával.
'''
def faktorialis(mozzarella):
    if mozzarella < 0:
        return None
    
    if mozzarella == 0:
        return 1
    
    szam = 1
    osszeg = 1
    while(szam <= mozzarella):
        osszeg *= szam
        szam += 1

    return osszeg

#--------------------------
'''
    A parosok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páros számait tartalmazza.
'''
def parosok_kivalogatasa(parmezan):
    lista = []
    for i in parmezan:
        if i % 2 == 0:
            lista.append(i)
    
    return lista


#--------------------------
''' 
    A lista_atlag nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak átlagával.
'''

def lista_atlag(x):
    if len(x) == 0:
        return 0
    osszeg = 0
    for i in x:
        osszeg += i

    return osszeg / len(x)

#--------------------------
''' 
    A szorzat  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak szorzatával.
    
    Üres lista esetén 1 a visszatérési érték.
'''
#67
def szorzat(x):
    osszeg = 1
    for i in x:
        osszeg *= i

    return osszeg 
#67
#--------------------------
''' 
    A pozitivok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        pozitiv számait tartalmazza. 
'''
#67
def pozitivok_kivalogatasa(x):
    lista = []
    for i in x:
        if i > 0:
            lista.append(i)
    
    return lista
    





#--------------------------
'''
    A benne_van_a_stringben nevű függvény.
    első paraméterként egy stringet kap,
    második paraméterként egy betüt.
    Visszatérési értéke True, ha  a betü benne van a stringben.
    A visszatérési érték False, ha  a betü nics benne a stringben.
'''

def benne_van_a_stringben(x, y):
    for i in x:
        if i == y:
            return True
    
    return False






#--------------------------
''' 
    A legkisebb nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legkisebb számával.
    Üres lista esetén None a visszatérési érték.
    
    A feladat megoldása során nem használhatod a min() függvényt!
'''
def legkisebb(x):
    if len(x) == 0:
        return None
    
    min = x[0]
    for i in x:
        if i < min:
            min = i

    return min




#--------------------------
'''
    A kereses_a_stringben nevű függvény,
    első paraméterként egy sztringet kap,
    második paraméterként egy betüt.
    Visszatérési érték a paraméterként megadott betü
        első előfordulási helye a stringben. 
    
    A visszatérési érték None, ha a betü nics benne a stringben.
'''
def kereses_a_stringben(x,y):
    index = 0
    for i in x:
        if i == y:
            return index
        index += 1

    return None


#--------------------------
''' 
    A negativok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista negativ számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def negativok_szama(a):
    if len(a) == 0:
        return 0
    
    neg = 0
    for i in a:
        if i < 0:
            neg += 1

    return neg

#--------------------------
'''
    A benne_van_a_listaban nevű függvény,
    első paraméterként egy listát kap,
    második paraméterként egy számot.
    A visszatérési érték True, ha  a szám benne van a listában.
    A visszatérési érték False, ha  a szám nics benne a listában.
    
    Üres lista esetén a visszatérési érték False.
'''

def benne_van_a_listaban(x, y):
    for i in x:
        if i == y:
            return True
    
    return False

#--------------------------
''' 
    A pozitivok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista pozitív számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
#67 == 13
#67 == 41

def pozitivok_szama(neckhurts):
    if len(neckhurts) == 0:
        return 0
    
    neg = 0
    for i in neckhurts:
        if i > 0:
            neg += 1

    return neg
    

    






#--------------------------
'''
    A negativok_kivalogatasa nevű függvény,
    visszatér egy listával, 
      amely a paraméterként átadott számokat tartalmazó lista
      negatív számait tartalmazza.
'''
def negativok_kivalogatasa(djiboutigae):
    lista = []
    for i in djiboutigae:
        if i < 0:
            lista.append(i)
    
    return lista



#======================================================================================================================/home/tanarok/weszerle/Oktatas_2025-26/10K_2/Python/python2