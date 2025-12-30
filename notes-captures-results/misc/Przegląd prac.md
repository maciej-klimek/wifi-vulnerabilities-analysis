
1. Framing Frames: Bypassing {Wi-Fi} Encryption by Manipulating Transmit Queues   
   1. [Prace Matiego Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C)  (2.1.1 wyjaśnienie całego procesu ) (Przeczytałem do 3.3.2 i od 4 do 4.1.1 bo więcej to już dużo szczegółów)  
   2. [Git Framing Frames](https://github.com/domienschepers/wifi-framing)  
      1. Hardware:  
         1. Home WPA2 or WPA3,Public hotspots protected by [Passpoint](https://www.wi-fi.org/discover-wi-fi/passpoint) (formerly Hotspot 2.0), Enterprise networks where users may distrust each other,Public hotspots based on [WPA3 SAE-PK](https://www.wi-fi.org/beacon/thomas-derham-nehru-bhandaru/wi-fi-certified-wpa3-december-2020-update-brings-new-0)([Git Izolacja](https://github.com/vanhoefm/macstealer))  
         2. Linux, FreeBSD, iOS, and Android ([Prace Matiego Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C)**)**  
         3. Chyba musi obsługiwać 802.11w i nowsze (2.2 z [Prace Matiego Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C) )  
         4. Network card that supports frame injection ( [Prace Matiego Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C) **4** )   
         5. Consider a victim client which is connected to a **vulnerable** access point, where the stations have **agreed to enforce Wi-Fi MFP protection**. ( [Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C) **4.1.1)**  
      2. Software:  
         1. Client Isolation ( [Git Izolacja](https://github.com/vanhoefm/macstealer) )  
         2. Intercept (steal) traffic toward other clients at the MAC layer, even if clients are prevented from communicating with each other.  
         3. Leaking Frames from from FreeBSD Queue ( [Git](https://github.com/domienschepers/wifi-framing) , [Prace Matiego Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C) chyba to jest od **3.0 do 3.3.1** ):   
            1. We **transmit an encrypted echo request frame with the sleep-bit set** causing its echo reply frame to be buffered by the access point. We then **start an optimized reconnection** (that is, skipping authentication) and **after the association** (that is, prior to the 4-Way handshake) **we wake up the client with an arbitrary frame without setting the sleep-bit.** Since we did not yet derive a new pairwise encryption key using the 4-Way handshake, **the buffered data** (in this case an echo reply frame) **should not be transmitted**. However, since the FreeBSD AP leaks frames by falling back on the group encryption key, **we can now listen for such frames using the group key from our first session** and verify if the access point is vulnerable.  
            2.   
         4. Queueing SA query Request( Chyba też FreeBSD, [Git](https://github.com/domienschepers/wifi-framing), [Prace Matiego Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C) chyba to jest od **4.0**  )  
            1. In this [test case](https://github.com/domienschepers/wifi-framing/blob/main/framework/test-queue-saquery.py), **we transmit an association request with the sleep-bit set** causing frames to be buffered by the access point. Note that not all frames are bufferable (IEEE 802.11-2020; "11.2.2 Bufferable MMPDUs") and the association response will be transmitted. Since **our association request is rejected,** the access point will initiate the SA Query procedure. The SA Query request is a bufferable frame and therefore it will be buffered by the access point's kernel, consequently causing the procedure to time out. **Then, we transmit a second association request which will now be accepted by the access point** since the security association expired. When the connection establishment fails to proceed (since we are only transmitting an association request), the client will **be deauthenticated by the access point**. Finally, the test case **listens for the unprotected deauthentication frame** (that is, unprotected since the access point no longer posseses a pairwise key) which proves the SA Query procedure has timed out.  
                 
         5. ( [Prace Matiego Framing Frames](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:j3f4tGmQtD8C) )The attacker can **inject and intercept frames and manipulate the victim client’s security context,** e.g., injecting unprotected management frames such as authentication and association frames. Furthermore, the attacker can tamper with the powersave status of the victim client by **spoofing frames that use the power-save bit** (e.g., an unprotected null-data frame). **Typically,** the attacker does **not require knowledge of network credentials and therefore is an outside threat.** However, under certain conditions, leaked frames are protected with the network group key, in which case network credentials are required to obtain the respective key.  
              
2. A Security Analysis of WPA3-PK: Implementation and Precomputation Attacks \- Trzy różne Ataki(skupiłbym się na tym z 3 )  
   1. [Prace Matiego A Security Analysis of WPA3-PK](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:ns9cj8rnVeAC)  
   2. [Git A Security Analysis of WPA3-PK](https://github.com/vanhoefm/acns-wpa3-pk-sae)  
      1. Hardware:  
         1. Linux ( [Git A Security Analysis of WPA3-PK](https://github.com/vanhoefm/acns-wpa3-pk-sae) ) \-\> Kali, Ubuntu   
         2. WPA3's SAE-PK (rainbow tables [Git A Security Analysis of WPA3-PK](https://github.com/vanhoefm/acns-wpa3-pk-sae))  
         3. Home wifi( [Prace Matiego A Security Analysis of WPA3-PK](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:ns9cj8rnVeAC) **3.1**)  
         4. Store Value of Rainbows Tables **(4.3)**  
      2. Software:  
         1. The three tested implementations of PKHash can be found at: ( raczej git wszystkie ,  [Git A Security Analysis of WPA3-PK](https://github.com/vanhoefm/acns-wpa3-pk-sae), [Prace Matiego A Security Analysis of WPA3-PK](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:ns9cj8rnVeAC) **3.1**):  
            1. [Hostap’s sae-pk-gen](https://github.com/vanhoefm/acns-wpa3-pk-sae/blob/main/code-pkgen/hostap-v2.10/hostapd/sae_pk_gen.c)  
            2. [OpenSSL-based tool](https://github.com/vanhoefm/acns-wpa3-pk-sae/blob/main/code-pkgen/openssl-ddwrt/openssl_pkgen.c) **( Potrzeba MAC address AP)**  
            3. [Python3 implementation](https://github.com/vanhoefm/acns-wpa3-pk-sae/blob/main/code-pkgen/python-wpa3tools/python_pkgen.py)  (Scapy)   
         2. Rainbow Tables ( chyba linux daje rade,  [Git A Security Analysis of WPA3-PK](https://github.com/vanhoefm/acns-wpa3-pk-sae))  
         3. Collision ( Kali, Ubuntu ,  [Git A Security Analysis of WPA3-PK](https://github.com/vanhoefm/acns-wpa3-pk-sae))  
         4. **Capture the public key pk** that is sent in plaintext in the last AuthConfirm frame ( [Prace Matiego A Security Analysis of WPA3-PK](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:ns9cj8rnVeAC) **3.1 \- screen jest obok**). Once the adversary has obtained the public key, the initial value of the **modifier M** can **be guessed**, and the **PKHash algorithm can be executed** to find the WPA3-PK password of the network. It is therefore essential that a cryptographically strong random number generator is used to initialize the modifier M in the PKHash algorithm, since that will prevent an adversary from guessing the (initial) value of the modifier  
         5. **3.2 Network-based attacks (** [Prace Matiego A Security Analysis of WPA3-PK](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:ns9cj8rnVeAC)**) :**   
            1. In particular, an attacker can **connect as a client** and then use **ARP poisoning** to redirect and intercept the traffic of other users that are connected to the hotspot  
            2. **must know the IP address of victim (Can be done with nmap )**  
            3. abuse this key to **spoof broadcast and multicast traffic to all clients.** More worrisome, previous work has shown that against many devices, it is possible to **inject unicast traffic using the group key**  
         6. **4  Background on time-memory trade-off attacks** ([Prace Matiego A Security Analysis of WPA3-PK](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:ns9cj8rnVeAC))  
            1. Our goal is to **find a modifier M and public key pk** that results in a given password, i.e., to perform a preimage attack**(4.1)**  
            2.  We then define the function f(p) \= R(H(p))**(4.1)**  
            3. Both attacks have as input a public key pk for which we know the private key and a WPA3-PK password with parameters ℓ and θ, i.e., a fingerprint, and then find a modifier M such that PKHashθ,ℓ(pk, SSID, M) has as output the given fingerprint. The baseline time-memory trade-off attack works as follows**(4.3)**   
            4. Są podane funkcje do napisania ( Syzyf max xd), ale chyba doable , np funkcja skrótu albo szukania modyfikatora M ( ale chyba mathy ma je napisane na repo)  
                 
                 
         7. **5 Multi-Network Password Collisions** ([Prace Matiego A Security Analysis of WPA3-PK](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:ns9cj8rnVeAC))  
            1. We also create multi-network password collisions, where multiple SSIDs have the same WPA3-PK password. **These password collisions allow an attacker to create a single precomputed table that can be used to attack multiple networks**  
            2. To create WPA3-PK password collisions, we ensure that the input to the underlying hash function of PKHash, i.e., equation 1 in Algorithm 1, is identical for different SSIDs \[26\]. The core idea to achieve this is that an attacker can still change the length of the SSID after the password has already been generated \[26\]. This idea is illustrated in **Figure 5,**  
            3. To create a valid WPA3-PK password, we need to be able to freely modify certain bytes to ensure that the internal hash operation in PKHash starts with enough zeros.  
            4. However, as shown in Figure 5, the modifier M cannot be freely changed anymore because it now overlaps with the SSID or public key of the other network.\\  
            5. (Straszne rzeczy)

3. SSID Confusion: Making Wi-Fi Clients Connect to the Wrong Network  
   1. [Prace Matiego](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:fPk4N6BV_jEC)   
   2. [Git](https://github.com/vanhoefm/ssid-confusion-hostap)  
      1. Hardware:  
         1. Właściwe każde urządzenie   
      2. Software:  
         1. Multi-channel MitM: [github](https://github.com/vanhoefm/mc-mitm)  
         2. Wifi 802.11x i nowsze

4. FragAttacks: Forging Frames in Protected Wi-Fi Networks  
   1. [Prace Matiego](https://scholar.google.pl/citations?view_op=view_citation&hl=en&user=02_-sZ0AAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=02_-sZ0AAAAJ:4OULZ7Gr8RgC)  
   2. [Git](https://github.com/vanhoefm/fragattacks)  
      1. Hardware:  
         1.   
      2. Software:  
         1. Mc MitM  
         2. Forge \- A msdu or IP that looks like A \- msdu  
         3. DNS server.  
         4. spoof the MAC address of the targeted client

