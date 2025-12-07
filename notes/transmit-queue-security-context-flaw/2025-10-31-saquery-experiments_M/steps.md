## Setup:


### pre-reqs:

```
apt-get update
apt-get install git make gcc python3-venv net-tools
apt-get install libdbus-1-dev libnl-3-dev libnl-genl-3-dev libnl-route-3-dev libssl-dev 
```

### framework:

```
cd ../dependenciesdependencies
./build.sh
cd ../setup
./pysetup.sh
```

> Plus libwifi w depsach potrzebne

## Usage:

- Best to: `sudo su` first

- `source setup/venv/bin/activate`
- `cd setup`
- `./setup-hwsim.sh 4`
- `./load-config.sh wpa3-personal-pmf`
- `cd ..`

#### AP/Client creation:
`hostap.py [-h] [--config CONFIG] [--binary BINARY] [--debug DEBUG] [--ap] iface`

For ex:
`./hostap.py wlan0 --ap`

#### Testcases:
`run.py [-h] [--config CONFIG] [--binary BINARY] [--debug DEBUG] iface name`

For ex:
`./run.py wlan1 queue-saquery-samsung`

---

### Troubleshooting

`nmcli radio wifi off`


`killall hostapd wpa_supplicant`

```
hostapd_cli -i wlan0 raw PING
wpa_cli -i wlan1 raw PING
```
