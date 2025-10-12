

1. **Build hostapd**
   Skrypt pobiera hostapd, modyfikuje plik konfiguracyjny i kompiluje program.

   ```bash
   python build_hostapd.py
   ```

2. **Przygotowanie interfejsu**
   Skrypt ustawia interfejs w tryb AP, nadaje statyczny adres IP i uruchamia dnsmasq.

   ```bash
   python hostapd_prereq.py prepare
   ```

3. **Uruchomienie hostapd**
   Hostapd uruchamiamy ręcznie z przygotowanym plikiem konfiguracyjnym.

   ```bash
   sudo ./hostapd/hostapd ./hostapd.conf -dd
   ```

4. **Podłączenie klienta**
   Podłącz telefon lub komputer do sieci Wi-Fi utworzonej przez hostapd.

5. **Przywrócenie interfejsu**
   Przywraca interfejs do normalnego stanu po zakończeniu testów.

   ```bash
   python hostapd_prereq.py restore
   ```

6. **Usunięcie zasobów hostapd**
   Skrypt czyści pliki tymczasowe i konfiguracje dnsmasq utworzone w trakcie procesu.

   ```bash
   python hostapd_remove.py
   ```
