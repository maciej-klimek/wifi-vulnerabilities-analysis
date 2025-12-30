1. **Build hostapd**
   ```bash
   python build_hostapd.py
   ```

2. **Prepare the interface**
   ```bash
   python hostapd_prereq.py prepare
   ```

3. **Run hostapd**
   ```bash
   sudo ./hostapd/hostapd ./hostapd.conf -dd
   ```

4. **Connect a client**
5. 
6. **Restore the interface**

   ```bash
   python hostapd_prereq.py restore
   ```

7. **Remove hostapd resources**
   ```bash
   python hostapd_remove.py
   ```