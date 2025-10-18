### OGÓLNE:
- [X] dodac moduly i pliki ktorych uzywamy przy testach (ssid repo, wifi framework/framing)
  - [ ] dodac "dobre mc-mitm do ssid
- [ ] opisac i zrobic wlasne instrukcje do funkcjonalnosci ktore uzywamy
- [ ] Spróbować postawić sieć FreeBSD przy pomocy hostapd
- [ ] Rename i lepsza struktura plikow


### HOSTAPD:
- [ ] poprawic komentarze
- [X] test internet sharingu - komp labowy dziala
- [X] walidacji czy ma prawo dzialac na lab kompie - MA PRAWO !! (inny conf i problem z apd-update)
  - (opcja na wylaczenie apt-update)
- [X] test end-end dostepu
- [ ] ssid test
  - [ ] warto sprobowac zrobic modyfikacje do samego kodu ataku i pyknac jeszcze raz
  - [ ] ztestowac z "dobrym" mc-mitm

### SIV:
- [X] zrobic python enva pod atak
- [X] przegladnac helpery czy instaluja wszystko fakycznie (opcja na wylaczenie apt-update)
- [ ] Poprawić skrypt sprawdzający czy dane urządzenie jest podatne na atak

### QSC:
- [ ] Test case 4wh przerobić i opisać własnymi słowami

### OVERLEAF
- [ ] Przepisać wstępny koncpekt i spis treści do overleava
- [ ] Ogarnac czy jest jakis version control - idea pisania pracy troche jak sie robi pull requesty -> Jest:
  - [ ] Przetestowac to rozwiązanie

## POTRZEBNE DO PRACY:
### SIV:
- **TP-LINK:**
  - [ ] logi/screeny - mc-mitm, router, client
  - [ ] frame capture: mc-mitm rouge ap: probe req/res, 4whs...
  - [ ] schemat/frame flow
- **HOSTAPD:**
  - [ ] logi - AP, WPASuplicant (deamon, ping -> AP), mc-mitm,
  - [ ] frame capture: mc-mitm rouge ap: probe req/res, 4whs...
  - [ ] schemat/frame flow
- **ASUS:**
  - [ ] logi/screeny - mc-mitm, router, client
  - [ ] frame capture: mc-mitm rouge ap: probe req/res, 4whs...
  - [ ] schemat/frame flow

### QSC:
- **SA QUERY:**
  - [ ] logi/screeny - AP, Client
  - [ ] frame capture: Ramka z sleep bitem, SA Query
  - [ ] schemat/frame flow
- **4 WAY HANDSHAKE:**
  - [ ] TBD


---
---
---
### PLANY NA PIĄTEK 17.10.2025r:
- [X] Prep:
  - [X] HDMI NA PIĄTEK DO LABA !!!!!!!!!!!!!!
  - [X] Przeczytać dokładnie SA query i 4way handshake query w Framing Frames
- [X] Przerobić jeszcze raz scenaiursz SQ query 
  - [X] zrobić w miare dokładne notatki przebiegu eksperymentu
- [X] Porozmawiać z Profesorem Szottem o tym co zrobiliśmy do teraz, zapytać o wkład własny
  - [X] Zaproponować napisanie samemu ataku Queueing of 4-Way Handshake Messages
 
