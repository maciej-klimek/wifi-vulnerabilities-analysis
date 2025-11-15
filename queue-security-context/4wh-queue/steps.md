### venv
python3 -m venv venv
source venv/bin/activate

pip install scapy

sudo modprobe mac80211_hwsim radios=2

sudo ifconfig wlan1 down

sudo iw dev wlan1 interface add monwlan1 type monitor

sudo ifconfig wlan1 up
sudo ifconfig monwlan1 up

sudo iw dev monwlan1 set channel 1



sudo hostapd -dd hostapd-wpa3.conf


sudo venv/bin/python3 run.py


=======
Just injection:

sudo hostapd hostapd-wpa3.conf -dd

sudo wpa_supplicant -i wlan1 -c wpa-supplicant.conf -D nl80211 -B

sudo wpa_cli -i wlan1 reconnect & 
***useless