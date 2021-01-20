# Codis per testejar el prototipus

Aquest repositori està dividit en carpetes. Cadascuna d'elles té el codi per provar les funcionalitats del prototipus. Les carpetes són les següents:

* [Pin](#Pin)
* [Button](#Button)
* [Accelerometer](#Accelerometer)
* [SD](#SD)
* [GPS](#GPS)
* [Deep_sleep](#Deep sleep)
* [Connector_TCS34725](#Connector TCS34725)
* [GPS_SD](#GPS SD)
* [UART](#UART)


## Pin
Conté el codi per provar els Pins que actuen com a pins de sortida del Lopy.
Aquest codi activa el pin durant 1 segon i desactiva el pin durant un altre segon. Ho fa repetidament 3 cops.  
Cal canviar el valor de la variable "pin_name" en el codi pel Pin que estem provant (per exemple, 'P9').
A continuació es mostra el llistat de pins:

El prototipus conté els següents pins de sortida (mode=Pin.OUT):
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
* pin_name = 'P19': free
* pin_name = 'P20': free
* pin_name = 'P21': Pytrack SCL
* pin_name = 'P22': Pytrack SDA
* pin_name = 'P23': SD card clk


## Button
Conté el codi per encendre el led de color verd en el moment que es prem el botó del prototipus. Hi ha un temps d'espera de 10 segons per poder prémer el botó.
Controla els següents pins:
- P14: Button

## Accelerometer
Conté el codi mostrar per pantalla el pitch i el roll de l'acceleròmetre cada 100 ms durant 100 vegades.
Controla els següents pins:
- P3: PWR_EN
- P13: Accelerometer Interrupt
- P22: SDA
- P21: SCL

## SD
Conté el codi per crear un arxiu .txt a la SD i mostrar per pantalla el contingut d'aquest arxiu. És necessari introduïr una tarjeta SD en format FAT16 o FAT32. 
Controla els següents Pins:
- P4: SD_CMD
- P8: SD_DAT
- P23: SD_CLK

## GPS
Conté el codi per provar el GNSS Glonass GPS. El codi permet mostrar per pantalla la latitud, longitud i hora actual. Ho fa repetidament durant 100 vegades. Cada vegada triga 30 segons en intentar establir la connexió amb els satèl·lits. Per obtenir dades correctes el dispositiu ha d'estar a cel obert, sino mostrarà valors de latitud = 0, longitud = 0 i time = 0.
Controla els següents Pins:
- P3: PWR_EN
- P22: SDA
- P21: SCL

## GPS_SD
Igual que el codi de la carpeta GPD però guardant les dades a la SD, fet que permet deixar el dispositiu mesurant a cel obert.
Controla els següents Pins:
- P3: PWR_EN
- P22: SDA
- P21: SCL

## Deep_sleep
Conté el codi per entrar en deep sleep durant 60 segons i tornar a executar el mateix codi.
Controla els següents pins:
- P3: PWR_EN
- P22: SDA
- P21: SCL


## Connector_TCS34725
Conté el codi per mostrar per pantalla els valors d'un sensor de llum que es connecta per I2C.
Controla els següents pins (SDA a configurar pels pins disponibles):
- P22: SDA
- P21: SCL

## UART
Conté el codi per transmetre i escoltar missatge pel port RxTx. Necessita configurar-se a través del Port 0, en els Pins 1 i 0 (es desactiva el REPL)
Controla els següents pins:
- P1: Rx 
- P0: Tx