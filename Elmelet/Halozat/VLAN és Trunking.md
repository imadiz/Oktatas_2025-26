# VLAN, Trunking és Subinterface-ek Összefoglaló

Ez a dokumentum a hálózati szegmentálás és az inter-VLAN routing alapjait foglalja össze.

---

## 1. VLAN (Virtual Local Area Network)
A VLAN-ok lehetővé teszik, hogy egyetlen fizikai switchen több elkülönített logikai hálózatot hozzunk létre.

* **Broadcast domain csökkentése:** A forgalom nem árasztja el az egész fizikai hálózatot, csak az adott VLAN-t.
* **Biztonság:** A különböző VLAN-ban lévő eszközök alapértelmezés szerint nem látják egymást.
* **Logikai csoportosítás:** Nem a fizikai elhelyezkedés, hanem a feladatkör (pl. HR, IT, Vendég) alapján csoportosíthatunk.

## 2. Trunking (802.1Q)
Amikor a VLAN-ok forgalmát két switch vagy egy switch és egy router között kell továbbítani, **Trunk portot** használunk.

* **Tagging (Címkézés):** A switch egy 4 bájtos azonosítót (VLAN ID) szúr be az Ethernet keretbe.
* **802.1Q:** Ez a legelterjedtebb szabvány a trunkölésre.
* **Native VLAN:** Az a VLAN, amelynek a forgalma címke nélkül (untagged) halad át a trunkön.

---

## 3. Router-on-a-Stick és Subinterface-ek
Ha a VLAN-ok között kommunikációt (routingot) szeretnénk, routerre van szükség. A "Router-on-a-Stick" módszerrel egyetlen fizikai interfészen több VLAN-t is kiszolgálhatunk.

### Mi az a Subinterface?
A router fizikai portját virtuális részekre bontjuk. Minden egyes "al-interfész" egy-egy VLAN-hoz tartozik, és saját IP címmel rendelkezik, ami az adott VLAN **Default Gateway**-e lesz.

---

## 4. Konfigurációs Példa (Cisco CLI)

### Switch beállítások
Létrehozzuk a VLAN-okat és beállítjuk a Trunk portot a router felé.

```ios
! VLAN-ok létrehozása
vlan 10
 name Sales
vlan 20
 name Marketing

! Trunk port beállítása a Router felé (pl. Gi0/1)
interface GigabitEthernet0/1
 switchport mode trunk
 description Trunk-to-Router
```
### Router beállítások

```ios
! A fizikai interfészt csak bekapcsoljuk, nem adunk neki IP-t
interface GigabitEthernet0/0
 no shutdown

! Subinterface a VLAN 10-nek
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 description Gateway-for-Sales

! Subinterface a VLAN 20-nak
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 description Gateway-for-Marketing
```