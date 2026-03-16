import hashlib
import mysql.connector

db = mysql.connector.connect(
    host = "localhost", #Szerver, amin van az SQL adatbázis
    user = "root", #MySQL Szerver felh. név
    password = "titok", #MySQL Szerver jelszó
    database = "Bolt" #MySQL Szerver adatbázis, amiben dolgozunk
)

def start():
    print("Welcome to 'Bolt' DB manager!")
    print("Please choose an action:")
    print("1) Login")
    action = input()
    if action == '1':
        login()


def login():
    print("Enter your login name: ")
    name = input()
    print("Enter your password: ")
    pwd = input()

hashed = hashlib.sha256("abc12345".encode('utf-8')).hexdigest()
print(hashed)