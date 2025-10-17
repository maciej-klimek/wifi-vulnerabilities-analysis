### 1. Wyjaśnienie celu pracy/projektu

### Experimental Analysis of Modern Attacks Against IEEE 802.11 Networks
*Analiza eksperymentalna współczesnych ataków na sieci IEEE 802.11*	

**Zakres pracy i oczekiwany rezultat:** Celem pracy jest analiza eksperymentalna współczesnych ataków na sieci IEEE 802.11. Należy dokonać przeglądu ataków na sieci Wi-Fi z ostatnich czterech lat a następnie odtworzyć wybrane ataki w odpowiednio skonfigurowanym środowisku laboratoryjnym. Należy ocenić trudność wykonania wybranych ataków i podatność współczesnych urządzeń na te ataki.

---
### 2. Zaprezentowanie dokładnego planu pracy i przewidywanego spisu jej treści:
[Wstepny-konspekt-pracy](../wstepny-konspekt-pracy.md)

---
### 3. Przedstawienie zebranej literatury, min. 4 pozycje, wyjaśnienie::
- **Prace Mathy:** [https://scholar.google.com/citations?user=02_-sZ0AAAAJ&hl=en](https://scholar.google.com/citations?user=02_-sZ0AAAAJ&hl=en)
    
    > Prace są cytowane, głowne źródło wiedzy na temat przeprowadzanych eksperymentów

- **Lumin:** 
    - SSID: `https://app.luminpdf.com/viewer/67541f150717db6d69070757`
    - Framing: `https://app.luminpdf.com/viewer/6753554e48d273cb7a4afaf4`

- **Notatki starsze:**
    - [../Przegląd prac.md](<../Przegląd prac.md>)
    - [../../ssid-integrity-vulnerability/SSID-tldr-DRAFT.md](../../ssid-integrity-vulnerability/SSID-tldr-DRAFT.md)
    - [../../ssid-integrity-vulnerability/Wstępne Przygotowania.md](<../../ssid-integrity-vulnerability/Wstępne Przygotowania.md>)

- **Notatki nowsze:**
    - [Let the numbers talk](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:IWHjjKOFINEC) - [notatka](https://docs.google.com/document/d/1VDVzoKpSgDJKLGcJjrB-dIcpqv0HnVsn5RXsTrQHJGU/edit?tab=t.0)
    
    - [Fragment and Forge](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:dhFuZR0502QC) - [notatka](https://docs.google.com/document/d/1MF_7N2eQLGSk97Id3Wvsa0lMu2DVwOMDaKxAkW8jJ98/edit?usp=sharing)
    
    - [WPA3-dragonfly](../WPA3-dragonfly-analysis.md)

---
### 4. Przedstawienie krótkiego *State-of-Art* dot. zagadnień badanych w pracy/projekcie:

- **Co w tej dziedzinie już zrobiono/wymyślono?** 
  - Prace Mathiego -> Kilku vendorów podjęło działania zapobiegające udowodnionym podatnościom

- **Jak na tym tle lokuje się moja praca?**
  -  Eskperymentalna analiza grup podatności z użyciem powszechnego sprzętu WiFi (zarówno APs jak i urządzenia klienckie), badania charakterystyki podtaności na tle prakycznym a nie tylko czysto naukowym, 
  -  Ocena trudności wykonania i złożoności testowanych scenariuszy
  -  Nasza ocena wpływu podatności na realne środowiska bezprzewodowe (Gdzie podatności mają prawo namieszać)
  -  Porównanie wpływu software'u oraz standardu na podatność na urządzenia

