# Cisco Switch – Alapkonfiguráció magyarázatokkal, példákkal

## 1. Alapbeállítások


```
enable                                         Privilegizált módba lépés
configure terminal                             Globális konfigurációs mód
hostname SW1                                   Switch neve
no ip domain-lookup                            Hibás parancs ne indítson DNS-keresést
enable secret Cisco123                         Titkosított privileged exec jelszó
service password-encryption                    Összes jelszó titkosítása
banner motd  Engedély nélküli belépés TILOS!   Figyelmeztető üzenet belépéskor
```


---

## 2. VLAN-ok létrehozása


```
vlan 10           VLAN 10 létrehozása  
name SALES        VLAN 10 elnevezése  
vlan 20           VLAN 20 létrehozása  
name HR           VLAN 20 elnevezése  
vlan 99           Management VLAN létrehozása  
name MANAGEMENT   VLAN 99 elnevezése  
exit              Kilépés VLAN konfigurációból
```

---

## 3. Management VLAN IP cím

```
interface vlan 99                       SVI létrehozása a menedzsmenthez
ip address 192.168.99.2 255.255.255.0   IP-cím beállítása
no shutdown                             Interface engedélyezése

ip default-gateway 192.168.99.1         Menedzsment elérést biztosító gateway
(Alapértelmezett átjáró)
```

---

## 4. Access portok konfigurálása

```
interface range f0/1 - 12    Portok kijelölése
switchport mode access       Access mód (host eszközöknek)
switchport access vlan 10    Hozzárendelés VLAN 10-hez

interface range f0/13 - 20   Következő porttartomány
switchport mode access       Access mód
switchport access vlan 20    Hozzárendelés VLAN 20-hoz
```

---

## 5. Trunk port beállítása

```
interface g0/1                           Uplink vagy switch–switch port
switchport trunk encapsulation dot1q     802.1Q trunk protokoll
switchport mode trunk                    Trunk mód
switchport trunk allowed vlan 10,20,99   Engedélyezett VLAN-ok listája
```

---

## 6. Telnet konfigurálása (csak az iskolában, nem biztonságos!)

```
line vty 0 4             Távoli hozzáférési vonalak
password cisco           Telnet jelszó
login                    Jelszavas hitelesítés engedélyezése
transport input telnet   Csak Telnet elfogadása
```

---

## 7. SSH konfigurálása

```
ip domain-name lab.local             Domain név az RSA kulcshoz
username admin privilege 15 secret   Admin123   Admin felhasználó
crypto key generate rsa              RSA kulcspár generálása

SSH engedélyezése a VTY vonalakon

line vty 0 4          SSH a távoli hozzáféréshez
transport input ssh   Csak SSH engedélyezett
login local           Helyi felhasználóval való belépés
```

---

## 8. Konfiguráció mentése

```
end                                  Kilépés konfigurációs módból
copy running-config startup-config   Konfiguráció mentése újraindításra
```
