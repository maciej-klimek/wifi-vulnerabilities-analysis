## 1. SIV - SSID Integrity Vulnerability

### 1.1 Teoria
- Threat model — ogólny schemat ataku, flow ramek.

### 1.2 Testowanie klientów
- Test podatności najpopularniejszych systemów klienckich (Android, iOS, Windows, Linux) przy użyciu zmodyfikowanego skryptu hostapd.
- Analiza zachowania różnych wersji systemów i aplikacji (np. wpa_supplicant), porównując reakcje na atak w różnych środowiskach.

### 1.3 Testbed i eksperymenty

#### 1.3.1 Scenariusz na wirtualnych interfejsach
- Architektura sieci + flow ramek.
- Konfiguracje: hostapd, wpa_supplicant, wersje hostapd.
- Opis, wyjaśnienie, fragmenty używanego kodu.
- Przebieg ataku — logi, ramki, zestawienie z teorią.
- Podsumowanie: różne zachowania w zależności od wersji hostapd i środowiska (kernel, OS — wpływ na wyniki).

#### 1.3.2 Scenariusz z cheap COTS AP (TP-Link)
- Architektura sieci + flow ramek (realne kanały transmisyjne).
- Konfiguracja routera, różnice w działaniu mc-mitm vs hostapd-sim.
- Wyniki eksperymentów -  niedeterministyczność, wpływ kanału i warunków na powodzenie .

#### 1.3.3 Test high-tier AP (ASUS WPA3)
- Tak samo jak wyżej, opsi testbedu, omówienie kluczowych ramek (w jakis sposob software sie broni - constant deauth).

### 1.4 Podsumowanie
- Dużo przeprowadzonych eksperymentów.
- Bardzo różne wyniki — niemedeterministyczność.
- Symulacje wrażliwe na czynniki niezależne (kanał, OS, software).
- Ocena złożoności / trudności ataku — wąski timing, specyficzne środowisko - lab.

---

## 2. Macspoofing — wprowadzenie do security context

- Wprowadzenie do koncepcji security context AP.
- Prosty przykład ataku macstealer na wirtualnych interfejsach.
- Przykład na realnym sprzęcie.
- Test w kilku konfiguracjach — główna idea jako wprowadzenie do tematu.

---

## 3. QSC (Queue Security Context)

### 3.1 Teoria
- Definicja queue security context — dlaczego jest potrzebny, jak się kształtował na przestrzeni ewolucji standardu, jakie aspekty zostały zaniedbane.

### 3.2 SA Query threat model
- Opis, Schemat ataku, flow.
- Wyjaśnienie mechanizmu.
- Przedstawienie sytuacji na wirtualnych interfejsach — dokładna wizualizacja idealnego przebiegu ataku.
- Omówienie kluczowych pakietów (np. CSA — dane na kanale 11).
- Logi, ramki, przebieg krok po kroku.


#### 3.2.1 Testy podatności na różnych AP
- TP-Link
- Android hotspot (Samsung, Motorola)
- iPhone hotspot
- Orange Home Router
- ...

### 3.3 4-way-handshake-queue threat model
- Schemat ataku, flow.
- Ocena złożoności — bardzo wąski timing (trzeba się wstrzelić w Associate przy końcu handshake).
- Eksperymenty na wirtualnych interfejsach.
- Omówienie eksperymentów w środowisku wirtualnym.
- Próby na sprzęcie fizycznym — raczej mało prawdopodobne, że się uda.

---
