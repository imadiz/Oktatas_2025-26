# Cisco EtherChannel Összefoglaló

Az **EtherChannel** egy port-aggregációs technológia, amely lehetővé teszi több fizikai Ethernet link összevonását egyetlen logikai kapcsolattá. Célja a sávszélesség növelése és a redundancia biztosítása.

---

## 1. Alapfogalmak
* **Port-Channel:** A logikai interfész, amely az összefogott fizikai portokat képviseli.
* **Bundling:** A fizikai portok csoportosítása.
* **Sávszélesség:** Az EtherChannel sávszélessége a benne lévő aktív fizikai linkek összege (max. 8 aktív port).

## 2. Előnyök
* **Növelt sávszélesség:** Több link ereje adódik össze.
* **Redundancia:** Ha egy fizikai link kiesik, a forgalom automatikusan a megmaradt linkeken halad tovább (nincs STP újraszámolás).
* **Load Balancing:** A forgalom eloszlik a fizikai linkek között (forrás/cél MAC vagy IP cím alapján).
* **STP egyszerűsítés:** A Spanning Tree Protocol az egész csoportot egyetlen logikai linkként kezeli, így nem blokkolja a redundáns ágakat.



---

## 3. EtherChannel Protokollok

| Jellemző | LACP (IEEE 802.3ad) | PAgP (Cisco Propietary) | Statikus (On) |
| :--- | :--- | :--- | :--- |
| **Szabvány** | Nyílt szabvány | Cisco saját | Nincs protokoll |
| **Módok** | Active / Passive | Desirable / Auto | On |
| **Ajánlás** | Általánosan javasolt | Csak Cisco eszközöknél | Nem javasolt (hibafelismerés hiánya) |

### Módok párosítása (Mikor épül fel?)
* **LACP:** 
    * Active + Active = **Igen**
    * Active + Passive = **Igen**
    * Passive + Passive = **Nem**
* **PAgP:**
    * Desirable + Desirable = **Igen**
    * Desirable + Auto = **Igen**
    * Auto + Auto = **Nem**

---

## 4. Konfigurációs feltételek
Ahhoz, hogy az EtherChannel felálljon, a portoknak **egyezniük kell** a következőkben:
1.  **Sebesség (Speed)** és **Duplex** mód.
2.  **VLAN tagság** (Access port esetén ugyanaz a VLAN).
3.  **Trunk beállítások** (Trunk mód, Native VLAN, Allowed VLAN lista).

---

## 5. Ellenőrző parancsok (Verification)

| Parancs | Funkció |
| :--- | :--- |
| `show etherchannel summary` | A legfontosabb státusz-áttekintő parancs. |
| `show etherchannel port-channel` | Logikai interfész paramétereinek listázása. |
| `show interface port-channel 1` | Sávszélesség és fizikai státusz megtekintése. |
| `show etherchannel load-balance` | Aktuális elosztási algoritmus ellenőrzése. |
| `show lacp neighbor` | LACP szomszéd információk lekérése. |

## 6. Státuszkódok magyarázata (show etherchannel summary)

* **(S)** - Layer 2 (Switched): Kapcsolt hálózatban (VLAN alapú) működik.
* **(R)** - Layer 3 (Routed): Forgalomirányított (IP alapú) interfészként működik.
* **(U)** - In Use: A Port-Channel aktív, sávszélességet ad és forgalmat továbbít.
* **(P)** - In Port-Channel: A fizikai port sikeresen csatlakozott a logikai csatornához.
* **(I)** - Stand-alone: Hiba! A port nem tudott csatlakozni (gyakran paraméter-eltérés miatt).
* **(D)** - Down: A port le van állítva (shutdown) vagy nincs fizikai link.

## 7. Alapvető konfigurációs parancsok (Példa)

### LACP konfiguráció (Interfész szinten)
```ios
Switch# configure terminal
Switch(config)# interface range fastEthernet 0/1 - 2
Switch(config-if-range)# speed 100
Switch(config-if-range)# duplex full
Switch(config-if-range)# channel-group 1 mode active
Switch(config-if-range)# exit
```

## 8. Layer 3 (Router / L3 Switch) Konfiguráció

Abban az esetben, ha nem Layer 2-es kapcsolót, hanem IP-címmel ellátott interfészeket akarunk összefogni:
1. Belépés a fizikai interfészekhez és a switchport funkció kikapcsolása

```ios
Router(config)# interface range gigabitEthernet 0/0 - 1
Router(config-if-range)# no switchport
Router(config-if-range)# channel-group 1 mode active
Router(config-if-range)# exit
```

2. IP cím beállítása a logikai Port-Channel interfészen
```
Router(config)# interface port-channel 1
Router(config-if)# ip address 10.1.1.1 255.255.255.252
Router(config-if)# no shutdown
```