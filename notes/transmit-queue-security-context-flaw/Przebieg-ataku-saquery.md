# **1. Repozytroria**
* [wifi-framework](https://github.com/domienschepers/wifi-framework)
* [wifi-framing](https://github.com/domienschepers/wifi-framing?tab=readme-ov-file#queueing-sa-query-requests)


# **2. Przygowanie śrdodowiska**
[intrukcja wifi-framework setup](https://github.com/domienschepers/wifi-framework/tree/master/setup)
 > Wszystko robimy z sudo

 > Z hardware to wydaję mi się, że obie karty muszą obsługiwać monitor mode

* pod linkiem jest prosta instrukcja która prosi o pobranie kilku package, wykonanie dwóch buildów oraz uaktualnienie libwifi -> trzeba to zrobić tylko raz po tym jak pullujesz repozytorium
* aby można było po prostu kopiować wstawiony tam kod należy być w wifi-framework/(jakis folder)

# **3. Jak korzystać**
[instrukcja wifi-framework how to](https://github.com/domienschepers/wifi-framework/blob/master/docs/USAGE.md)

## Co trzeba realnie zrobić ?
* Za każdym razem odpalić venv komendą source setup/venv/bin/activate w rootdirectory /wifi-framework 
* Pobrać testcase do rootdirectory: w naszym przypadku jest on w [wifi-framing](https://github.com/domienschepers/wifi-framing?tab=readme-ov-file#queueing-sa-query-requests) w directory framework i nazywa się: test-queue-saquery.py
* Wgrać konfiguracje bezpieczeństwa w setup: `cd setup; ./load-config.sh wpa3-personal-pmf`
* Odpalić komendą sudo ./run.py {interfejs} nazwa ataku bez test -> queue-saquery (run patrzy sobie na pliki które są w katalogu i je odpala)