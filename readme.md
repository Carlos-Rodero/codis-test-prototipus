# Codis per testejar el prototipus

Aquest repositori està dividit en carpetes. Cadascuna d'elles té el codi per provar les funcionalitats del prototipus. Les carpetes són les següents:

* [LED](#LED)
* [WLAN](#WLAN)
* [Bluetooth](#Bluetooth)
* [RTC](#RTC)
* [Deep Sleep](#Deep_Sleep)
* [Battery voltage](#Battery_voltage)
* [SD](#SD)
* [GPS](#GPS)

## LED

## WLAN

## Bluetooth

## RTC

## Deep_Sleep

## Battery_voltage

## SD
La carpeta SD conté el codi per obrir i tancar un arxiu dins de la SD. Necessita introduïr una tarjeta SD en format FAT16 o FAT32. 
Controla els següents Pins:
- P4: SD_CMD
- P8: SD_DAT
- P23: SD_CLK

## GPS
La carpeta GPS conté el codi per mostrar per pantalla la latitud, longitud i hora actual. Ho fa repetidament durant 100 vegades. Per cada vegada triga 30 segons en intentar establir la connexió amb els satèl·lits. Per obtenir dades correctes el dispositiu ha d'estar a cel obert, sino mostrarà valors de latitud = 0, longitud = 0 i time = 0.
Controla els següents Pins:
- P22: SDA
- P21: SCL