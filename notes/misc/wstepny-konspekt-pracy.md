### Spis treści:
1. Wstęp do pracy
2. Wifi security - omówienie aktualnych teorii i standardów
3. State of the art tematu pracy
4. SSID Integrity Vulnerabilities - Podszywanie się pod punkty dostępowe Wi-Fi
5. Transmit queue security context flaw - Wykorzystanie podatności kolejkowania ramek
6. Wnioski ogólne, nasza interpretacja
7. Bibliografia


---
### Konspekt

1. **Wstęp do pracy:**

   1. [Motywacja] Charakterystyka obszaru tematycznego: *standard IEEE 802.11, 802.11i -  WPA(WPA3)*   
      Cel Pracy: Experimental Analysis of Modern Attacks Against IEEE 802.11 Networks   
   2. Cel pracy / pytania badawcze (np. czy łatwo wykonać atak? czy urządzenia są podatne?)  
   3. Metodologia - czyli jak odpowiemy na te pytania - na drodze eksperymentalnej  
   4. Indywidualny wkład “dyplomanta” (intencje i oczekiwania):   
      1. Weryfikacja wpływu podatności na realne środowiska i urządzenia komercyjne - ewaluacja implementacji softwaru urządzeń (COTS) zarówno po stronie access pointów jak i urządzeń klienckich  
      2. Tabela z podziałem zadań  
   5. Opis układu treści prezentowanych w pracy (struktura pracy):  
      1. *Zabawa na sam koniec :)*

2. **Wifi security - omówienie aktualnych teorii i standardów**      

3. **State of the art tematu pracy:**

   <!-- 1. obecne informacje o standardzie i omawianych podatnościach, kluczowe aspekty potrzebne do zobrazowania intencji pracy   -->
   1. powołanie się na podobne eksperymenty - nasza motywacja i inspiracja [odwołania do prac M. VanHoef oraz Inne]  
   2. obecne działania vendorów mające na celu zapobieganie omawianym zagrożeniom

4. **Podszywanie się pod punkty dostępowe Wi-Fi - SSID Integrity Vulnerabilities**  
   1. **Część teoretyczna** - wprowadzenie i dokładne omówienie podatności  
      1. opis teoretyczny - abstract mechanizmów bezpieczeństwa w sieciach Wi-Fi,  omówienie metod uwierzytelniania  
      2. threat model  
      3. schemat przebiegu ataku (frame exchange scheme)

   2. **Opis środowiska i sprzętu badawczego**  
      1. hardware, software (dokładne informacje, karty sieciowe, wersje softwaru itp.) - tabelka o strukturze :  
         1. Client  
         2. Rouge AP/Listener  
         3. Real AP  
      2. schemat sieci i komunikacji między urządzeniami - [link do pracy ze schematem](https://docs.google.com/document/d/1HgNRN2SXmuY6QG2xrLxQCXtfMp_a5B7XauGd_jrNtQY/edit?usp=sharing)

   3. (*)Client vulnerabilty testing - praktyczne przedstawienie badania podatnosci

   4. **Część praktyczna**  
      1. przebieg poszczególnych eksperymentów  
         1. Trzy stage ():
            1. Cheap COTS (TP-Link)
            2. Hostapd WPA3 conf
            3. High-end AP/Router
      2. opis zachodzących zjawisk i ich wyjaśnienie  
      3. pokazanie na przykładach, schematach

   5. **Zestawienie wyników,** wnioski i omówienie potencjalnego wpływu podatności - tabelka?

5. **Transmit queue security context flaw**  
   (Podatnosci na rozne rodzaje ramek (sposób w jaki software je interpertuje/na co im pozwala))
   4. **Część teoretyczna** - wprowadzenie i dokładne omówienie podatności
      1. opis teoretyczny - wytłumaczenie struktry queues która w kontekście standardu 802.11 nosi nazwę security associa-tion
      2. threat model  
      3. schemat przebiegu ataku (frame exchange scheme)
      
   5. **Opis środowiska i sprzętu badawczego**  
         1. hardware, software (dokładne informacje, karty sieciowe, wersje softwaru itp.) - tabelka o strukturze :  
            1. Client  
            2. Attacker  
            3. Real AP  
         2. schemat sieci i komunikacji między urządzeniami 

   6. **Część praktyczna**
      1. przebieg poszczególnych eksperymentów
         1. Queueing Frames:
            1. SA Query
            2. 4-Way Handshake Messages
         2. Overriding clients security context
         3. (*) FreeBSD frame leak
      2. opis zachodzących zjawisk i ich wyjaśnienie  
      3. pokazanie na przykładach, schematach    

   7. **Zestawienie wyników,** wnioski i omówienie potencjalnego wpływu podatności - tabelka?
      

   > schemat podobny jak dla SIV - threat modele dla tesowanych scenariuszy
6. **Wnioski ogólne, nasza interpretacja**
7. **Bibliografia**






