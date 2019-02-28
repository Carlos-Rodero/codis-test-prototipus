# Codis per testejar el prototipus

Aquest repositori està dividit en carpetes. Cadascuna d'elles té el codi per provar les funcionalitats del prototipus. Les carpetes són les següents:

* [Pin](#Pin)
* [Button](#Button)
* [Accelerometer](#Accelerometer)
* [SD](#SD)
* [GPS](#GPS)


## Pin
Conté el codi per provar els Pins que actuen com a pins de sortida. 
Aquest codi activa el pin durant 1 segon i desactiva el pin durant un altre segon. Ho fa repetidament 3 cops.  
Cal canviar el valor de la variable "pin_name" en el codi pel Pin que estem provant (per exemple, 'P9').
A continuació es mostra el llistat de pins:

El prototipus conté els següents pins:
* pin_name = 'P0': Programming Rx
* pin_name = 'P1': Programming Tx
* pin_name = 'P2': On-board LED
* pin_name = 'P3': PWR_EN, when pulled LOW, the pytrack will disconnect the lopy's power
* pin_name = 'P4': SD card CMD
* pin_name = 'P5': cellular modem
* pin_name = 'P6': cellular modem
* pin_name = 'P7': cellular modem
* pin_name = 'P8': SD card DAT0
* pin_name = 'P9': free
* pin_name = 'P10': free
* pin_name = 'P11': free
* pin_name = 'P12': external/on-board wifi/bt antenna switch
* pin_name = 'P13': input only, interrupt pin from Pytrack. Accelerometer
* pin_name = 'P14': input only, Pytrack on-board button
* pin_name = 'P15': input only
* pin_name = 'P16': input only
* pin_name = 'P17': input only
* pin_name = 'P18': input only
* pin_name = 'P19': free
* pin_name = 'P20': free
* pin_name = 'P21': Pytrack SCL
* pin_name = 'P22': Pytrack SDA
* pin_name = 'P23': SD card clk


## Button


## Accelerometer


## SD
Conté el codi per crear un arxiu .txt a la SD i mostrar per pantalla el contingut d'aquest arxiu. És necessari introduïr una tarjeta SD en format FAT16 o FAT32. 
Controla els següents Pins:
- P4: SD_CMD
- P8: SD_DAT
- P23: SD_CLK

## GPS
Conté el codi per mostrar per pantalla la latitud, longitud i hora actual. Ho fa repetidament durant 100 vegades. Cada vegada triga 30 segons en intentar establir la connexió amb els satèl·lits. Per obtenir dades correctes el dispositiu ha d'estar a cel obert, sino mostrarà valors de latitud = 0, longitud = 0 i time = 0.
Controla els següents Pins:
- P22: SDA
- P21: SCL