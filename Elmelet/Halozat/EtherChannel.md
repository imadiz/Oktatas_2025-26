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
* **LACP:** Active + Active = **Igen**
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

## 5. Alapvető konfigurációs parancsok (Példa)

### LACP konfiguráció (Interfész szinten)
```ios
Switch# configure terminal
Switch(config)# interface range fastEthernet 0/1 - 2
Switch(config-if-range)# speed 100
Switch(config-if-range)# duplex full
Switch(config-if-range)# channel-group 1 mode active
Switch(config-if-range)# exit