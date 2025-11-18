### OGÓLNE:
- [X] dodac moduly i pliki ktorych uzywamy przy testach (ssid repo, wifi framework/framing)
  - [X] dodac dobre mc-mitm do ssid
- [X] opisac i zrobic wlasne instrukcje do funkcjonalnosci ktore uzywamy
- [X] Rename i lepsza struktura plikow
- [ ] Przerzucic logi i frame cap z dysku (2025-10-24)


### HOSTAPD:
- [ ] poprawic komentarze
- [X] test internet sharingu - komp labowy dziala
- [X] walidacji czy ma prawo dzialac na lab kompie - MA PRAWO !! (inny conf i problem z apd-update)
  - (opcja na wylaczenie apt-update)
- [X] test end-end dostepu
- [X] ssid test
  - [X] warto sprobowac zrobic modyfikacje do samego kodu ataku i pyknac jeszcze raz
  - [X] ztestowac z "dobrym" mc-mitm

### SIV:
- [X] zrobic python enva pod atak
- [X] przegladnac helpery czy instaluja wszystko fakycznie (opcja na wylaczenie apt-update)
- [X] Poprawić skrypt sprawdzający czy dane urządzenie jest podatne na atak
- [ ]* Test wirtualnych interfacow ale na dwoch kompach (PC1 = S + MITM  |   PC2 = AP)
- [ ] TESTY PODATNOSCI CLIENTOW
  - [ ] REFACTOR OUTPUT FILES + SAVE USEFUL FILTERS !!!! 
  - [X] Samsung - base case:
    - [X] dhcp needed - yes, (internet access? - no)
    - [X] custom scripts for testbed (wifi setup, dhcp...)
    - [X] Virtual interface for capture setup + steps (steps.md)
    - [X] Outputs(done) + frames(not done - VIF):
      - [X] open network
      - [X] wpa2
      - [X] wpa3 personal
      - [ ] wpa3 enterprise*
    - Comparasion - Android Motorola phone
  - [X] Windows
  - [X] Motorola
  - [ ] Linux
  - [ ] IOS - should be similar case to samsung

### QSC:
- [X] saquery testy na roznych apekach -> logi, capture, ssy:
  - [X] hostpad
  - [X] samsung hotspot
    - dorobic: wpa3 no pmf, wpa2, dodac ssy z telefonu
  - [X] ios hotspot - wpa2/3 no pmf
  - [X] wpa2 cheap ap
  - [X] wpa3 highend ap
    - Wstepne testy na orange home M - dodac ss z konsoli AP (jakie settingi testowane) ?pmf?
  - [X] im wiecej tym lepiej
  - [X] !!! jednoczesnie mozna porobic ssid vulnerabilty na clientach - look SIV

- [X] Test case 4wh przerobić i opisać własnymi słowami
  - [X] pskcache problem?
  - [ ] Wlasna implementacja injection w scapy
    - [X] full flow - nie da sie zrobic bez pelnego crypto
    - [X] just injection - timing issue - AP ignoruje null framesy jak juz zacznie procedure z realnym klientem   
      - [ ] Zcapturowac ramki jak to wyglada (ss w dirze jest)
    - [ ] Udokumentoac czemu frameworkiem sie tego nie da zrobic (inna warstwa)
    
### OVERLEAF
- [ ] Przepisać wstępny koncpekt i spis treści do overleava
- [X] Ogarnac czy jest jakis version control - idea pisania pracy troche jak sie robi pull requesty -> Jest:
  - [ ] Przetestowac to rozwiązanie

## POTRZEBNE DO PRACY:
### SIV:
- **TP-LINK:**
  - logi/screeny - mc-mitm, router, client
  - frame capture: mc-mitm rouge ap: probe req/res, 4whs...
  - schemat/frame flow
- **HOSTAPD:**
  - logi - AP, WPASuplicant (deamon, ping -> AP), mc-mitm,
  - frame capture: mc-mitm rouge ap: probe req/res, 4whs...
  - schemat/frame flow
- **ASUS:**
  - logi/screeny - mc-mitm, router, client
  - frame capture: mc-mitm rouge ap: probe req/res, 4whs...
  - schemat/frame flow
- **Cliend vuln testing** - all testcases -> outputs and capture for some


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

### PLANY NA PIĄTEK 24.10.2025r:
- [X] SIV ze zrytkiem:
  - [X]* jak cos nie bedzie stykac - potestowac drugie mc-mitm
  - [X]* Client: Telefon(Android/IoS) ALBO* wpa_suplicant
  - [X] Wszystkie logi (zrytek, mc-mitm)
  - [ ] Filmik z perpektywy mc-mitm
  - [X] Caly przeplyw ramek (filtr z ostatnieg commita)
  - [ ] Spisac dokladna konfiguracje zryta (moze byc ss)
  - [X] HDMI ! ! !
 
