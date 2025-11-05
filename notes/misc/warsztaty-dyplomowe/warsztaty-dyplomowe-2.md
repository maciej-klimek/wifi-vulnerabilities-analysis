# Warsztaty dyplomowe — część 2

## 1. SIV

- Dużo przeprowadzonych eksperymentów.
- Bardzo różne wyniki — ten sam testbed daje różne efekty (niemedeterministyczne).
- Symulacje są bardzo wrażliwe na czynniki niezależne od nas (sytuacja w kanale, system operacyjny, oprogramowanie urządzenia klienckiego).

Co planujemy w pracy:

- Testowanie podatności klientów (sprawdzamy podatności systemów klienckich).
- Przedstawienie sytuacji na wirtualnych interfejsach — dokładna wizualizacja idealnego przebiegu ataku.
- Omówienie kluczowych ramek (np. CSA — dane na kanale 11).
- Eksperyment na sprzęcie fizycznym:

  - Cheap AP (COTS) — TP-Link (WPA2) — częsty punkt MITM.
  - High-end AP — ASUS (WPA3) — nie udało się (problemy z oprogramowaniem).
  - Pokaz i dokładne omówienie kluczowych ramek (co nie działa).

- Ocena złożoności / trudności ataku — wąski timing, bardzo specyficzne środowisko.

## 2. QSC

- Wprowadzenie do koncepcji security context AP (macstealer).
  - Test w kilku konfiguracjach — główna idea to wprowadzenie do tematu.

Queueing vulnerabilities:

- SAQuery:

  - Przedstawienie sytuacji na wirtualnych interfejsach — dokładna wizualizacja idealnego przebiegu ataku.
  - Omówienie kluczowych pakietów (np. CSA — dane na kanale 11).
  - Testy podatności na różnych AP:
    - TP-Link
    - Android hotspot (Samsung, Motorola)
    - iPhone hotspot
    - Orange Home Router
    - ... (na przyszłość)

- 4-way-handshake-queue (testcase pisany od zera):
  - Ocena złożoności / trudności ataku — bardzo wąski timing (trzeba się wstrzelić w Associate wtedy, gdy klient kończy handshake).
  - Eksperymenty na wirtualnych interfejsach.
  - Omówienie eksperymentów w środowisku wirtualnym.
  - Próby na sprzęcie fizycznym — raczej mało prawdopodobne, że się uda.

Można pokazać filmik, kluczową ramkę i udowodnić, że mamy dużo logów.
