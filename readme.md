# Codis per testejar el prototipus

Aquest repositori està dividit en carpetes. Cadascuna d'elles té el codi per provar les funcionalitats del prototipus. Les carpetes són les següents:

* [LED](##LED)
* WLAN
* Bluetooth
* RTC
* Deep Sleep
* Battery voltage
* SD
* GPS

## LED
La carpeta SD conté el codi per obrir i tancar un arxiu dins de la SD. Necessita introduïr una tarjeta SD en format FAT16 o FAT32. Controla els següents Pins:
- P4: SD_CMD
- P8: SD_DAT
- P23: SD_CLK