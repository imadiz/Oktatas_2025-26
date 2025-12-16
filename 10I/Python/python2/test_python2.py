import os
import pytest
import math
import random
import json
from unittest.mock import patch

pwd = os.getcwd()
if not os.path.exists('python2.py'):
    with open('tasks.json', 'r', encoding='utf-8') as json_data:
        lista = json.load(json_data)
    
    random.shuffle(lista)
    text = "'''\n\n\n\n#--------------------------\n'''".join(lista)
    
    with open('python2.py', 'w',encoding='utf-8') as f:
        f.write("#--------------------------\n'''")
        f.writelines(text)
        f.write("'''\n\n\n\n#======================================================================================================================"+pwd)
        
from python2 import *


# Tesztelés az elso_karakter függvénnyel
def test_elso_karakter():
    assert elso_karakter("alma") == "a"
    assert elso_karakter("körte") == "k"
    assert elso_karakter("szilva") == "s"
    assert elso_karakter("") == None  # Ha üres stringet kap

# Tesztelés az utolso_karakter függvénnyel
def test_utolso_karakter():
    assert utolso_karakter("alma") == "a"
    assert utolso_karakter("körte") == "e"
    assert utolso_karakter("szilva") == "a"
    assert utolso_karakter("") == None  # Ha üres stringet kap

# Tesztelés a legkisebb függvénnyel
def test_legkisebb():
    with patch('python2.min', side_effect=Exception("min() is not allowed")) as mock_min:
        assert legkisebb([7, 4, 9, -4, -8, 3]) == -8
        assert legkisebb([1, 2, 3, 4, 5]) == 1
        assert legkisebb([-1, -2, -3, -4, -5]) == -5
        assert legkisebb([0, 0, 0, 0]) == 0
        assert legkisebb([5]) == 5  # Egy elemű lista
        assert legkisebb([]) == None  # Null elemű lista
        

# Tesztelés a legnagyobb függvénnyel
def test_legnagyobb():
    with patch('python2.max', side_effect=Exception("max() is not allowed")) as mock_max:
        assert legnagyobb([7, 4, 9, -4, -8, 3]) == 9
        assert legnagyobb([1, 2, 3, 4, 5]) == 5
        assert legnagyobb([-1, -2, -3, -4, -5]) == -1
        assert legnagyobb([0, 0, 0, 0]) == 0
        assert legnagyobb([5]) == 5  # Egy elemű lista
        assert legnagyobb([]) == None  # Null elemű lista

# Tesztelés az osszeg függvénnyel
def test_osszeg():
    with patch('python2.sum', side_effect=Exception("sum() is not allowed")) as mock_sum:
        assert osszeg([1, 2, 3, 4, 5, 6]) == 21
        assert osszeg([1, 2, 3]) == 6
        assert osszeg([-1, -2, -3]) == -6
        assert osszeg([0, 0, 0]) == 0
        assert osszeg([5]) == 5  # Egy elemű lista
        assert osszeg([]) == 0  # Üres lista

# Tesztelés a szorzat függvénnyel
def test_szorzat():
    assert szorzat([1, 2, 3, 4, 5]) == 120
    assert szorzat([1, 2, 3]) == 6
    assert szorzat([-1, -2, -3]) == -6
    assert szorzat([0, 1, 2, 3]) == 0
    assert szorzat([5]) == 5  # Egy elemű lista
    assert szorzat([]) == 1  # Üres lista, a szorzat definíció szerint 1

# Tesztelés a parosok_szama függvénnyel
def test_parosok_szama():
    assert parosok_szama([7, 4, 9, -4, -8, 3, 1]) == 3
    assert parosok_szama([2, 4, 6, 8, 10]) == 5
    assert parosok_szama([1, 3, 5, 7, 9]) == 0
    assert parosok_szama([0, 2, -4]) == 3
    assert parosok_szama([]) == 0  # Üres lista

# Tesztelés a paratlanok_szama függvénnyel
def test_paratlanok_szama():
    assert paratlanok_szama([7, 4, 9, -4, -8, 3, 1]) == 4
    assert paratlanok_szama([1, 3, 5, 7, 9]) == 5
    assert paratlanok_szama([2, 4, 6, 8, 10]) == 0
    assert paratlanok_szama([1, -3, 5]) == 3
    assert paratlanok_szama([]) == 0  # Üres lista

# Tesztelés a pozitivok_szama függvénnyel
def test_pozitivok_szama():
    assert pozitivok_szama([-7, -4, 9, -4, -8, 3, 1, 0]) == 3
    assert pozitivok_szama([1, 2, 3, 4, 5]) == 5
    assert pozitivok_szama([-1, -2, -3, -4, -5]) == 0
    assert pozitivok_szama([0, 0, 0]) == 0
    assert pozitivok_szama([1, -1, 0]) == 1
    assert pozitivok_szama([]) == 0  # Üres lista

# Tesztelés a negativok_szama függvénnyel
def test_negativok_szama():
    assert negativok_szama([-7, -4, 9, -4, -8, 3, 1, 0]) == 4
    assert negativok_szama([-1, -2, -3, -4, -5]) == 5
    assert negativok_szama([1, 2, 3, 4, 5]) == 0
    assert negativok_szama([0, 0, 0]) == 0
    assert negativok_szama([1, -1, 0]) == 1
    assert negativok_szama([]) == 0  # Üres lista

# Tesztelés a benne_van_a_listaban függvénnyel
def test_benne_van_a_listaban():
    assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 2) == False
    assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 9) == True
    assert benne_van_a_listaban([1, 2, 3, 4, 5], 3) == True
    assert benne_van_a_listaban([1, 2, 3, 4, 5], 6) == False
    assert benne_van_a_listaban([], 5) == False  # Üres lista

# Tesztelés a benne_van_a_stringben függvénnyel
def test_benne_van_a_stringben():
    assert benne_van_a_stringben("abrakadabra", "x") == False
    assert benne_van_a_stringben("abrakadabra", "d") == True
    assert benne_van_a_stringben("alma", "a") == True
    assert benne_van_a_stringben("alma", "b") == False
    assert benne_van_a_stringben("", "a") == False  # Üres string

# Tesztelés a kereses_a_listaban függvénnyel
def test_kereses_a_listaban():
    assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], -7) == 0
    assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 9) == 2
    assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 2) == None
    assert kereses_a_listaban([1, 2, 3, 2, 1], 2) == 1
    assert kereses_a_listaban([], 5) == None  # Üres lista

# Tesztelés a kereses_a_stringben függvénnyel
def test_kereses_a_stringben():
    assert kereses_a_stringben("abrakadabra", "a") == 0
    assert kereses_a_stringben("abrakadabra", "k") == 4
    assert kereses_a_stringben("abrakadabra", "s") == None
    assert kereses_a_stringben("alma", "l") == 1
    assert kereses_a_stringben("", "a") == None  # Üres string

# Tesztelés a parosok_kivalogatasa függvénnyel
def test_parosok_kivalogatasa():
    assert parosok_kivalogatasa([7, 4, 9, 4, 8, 3, 1, 12, 0]) == [4, 4, 8, 12, 0]
    assert parosok_kivalogatasa([1, 3, 5, 7, 9]) == []
    assert parosok_kivalogatasa([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert parosok_kivalogatasa([-2, 0, 2]) == [-2, 0, 2]
    assert parosok_kivalogatasa([]) == []  # Üres lista

# Tesztelés a paratlanok_kivalogatasa függvénnyel
def test_paratlanok_kivalogatasa():
    assert paratlanok_kivalogatasa([7, 4, 9, 4, 8, 3, 1, 12, 0]) == [7, 9, 3, 1]
    assert paratlanok_kivalogatasa([2, 4, 6, 8, 10]) == []
    assert paratlanok_kivalogatasa([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
    assert paratlanok_kivalogatasa([-1, 1, 3]) == [-1, 1, 3]
    assert paratlanok_kivalogatasa([]) == []  # Üres lista

# Tesztelés a pozitivok_kivalogatasa függvénnyel
def test_pozitivok_kivalogatasa():
    assert pozitivok_kivalogatasa([-7, -4, 9, -4, -8, 3, 1, 0]) == [9, 3, 1]
    assert pozitivok_kivalogatasa([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert pozitivok_kivalogatasa([-1, -2, -3, -4, -5]) == []
    assert pozitivok_kivalogatasa([0, 0, 0]) == []
    assert pozitivok_kivalogatasa([1, -1, 0]) == [1]
    assert pozitivok_kivalogatasa([]) == []  # Üres lista

# Tesztelés a negativok_kivalogatasa függvénnyel
def test_negativok_kivalogatasa():
    assert negativok_kivalogatasa([-7, -4, 9, -4, -8, 3, 1, 0]) == [-7, -4, -4, -8]
    assert negativok_kivalogatasa([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert negativok_kivalogatasa([1, 2, 3, 4, 5]) == []
    assert negativok_kivalogatasa([0, 0, 0]) == []
    assert negativok_kivalogatasa([1, -1, 0]) == [-1]
    assert negativok_kivalogatasa([]) == []  # Üres lista

# Tesztelés a lista_atlag függvénnyel
def test_lista_atlag():
    assert lista_atlag([1, 2, 3, 4, 5]) == 3.0
    assert lista_atlag([1, 2, 3]) == 2.0
    assert lista_atlag([-1, -2, -3]) == -2.0
    assert lista_atlag([0, 0, 0]) == 0.0
    assert lista_atlag([5]) == 5.0
    assert lista_atlag([]) == 0  # Üres lista

# Tesztelés a faktorialis függvénnyel
def test_faktorialis():
    assert faktorialis(0) == 1
    assert faktorialis(1) == 1
    assert faktorialis(5) == 120
    assert faktorialis(10) == 3628800
    assert faktorialis(-1) ==None # Negatív számot nem fogad el
