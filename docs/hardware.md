# Hardware
This page, will shortly introduce all your used tools.

## PC
As PC we used an Dell Latitude 7480 with Linux Arch x64 operating system.
Kernel verison 5.5.10-arch1-1

## CAN connector
We decided to go with the same toolset as [Tractor Hacking][1] did. Therefore we started with the CANable Pro from [canable][2]. Why the PRO? the reason for it was security. The normal one should also work fine. 

Important is to know that the CAN connector supports a baud rate up the 500k, so we are good to go with CANable. 

### CANable PRO
If you use the CANable PRO, you have the option to use either the stock firmware 'slcan' or 'candlelight'. We flashed 'candlelight'. The reason was because we wanted to use it in combination with [Wireshark][3]. It is important to mention, that we have used linux (Arch x64). If you use the 'slcan', you need to create an serial interface with [can-utils][4]. It is not difficult to get it up and running, just clone the repository and build it from source. But by flashing 'candlelight', you can bypass all this and the interface pops up as a native can device (like your wifi card or so).

#### Flashing candlelight
We used the online updater with really worked pretty straight forward. Just connect it to your PC, open your browser (please ensure that the browser has permission to read your devices, may sudo is needed) and update the firmware. For CANable PRO, you need to hold the 'Boot' button for bringing up the bootloader.

After successful flashing, your devices should be visible via `ls /dev/can*` and in [wireshark][3] as well.

#### Setting jumper
CANable PRO also includes a jumper, which enables or disables the terminator resistor. [Can bus][5] needs to be terminated, but this is already done somewhere in the tractor. So please disable it.

## J1939 cable
Please feel free to use any type of j1939 cable. 

### Cable type 
The only thing to consider is to buy the correct version. Currently there is type1 and type2 available. Normally type1 us colored black and type2 green. But in your case (John Deere 6125R), the female connector was black but type2 type. So please have a deeper look before you buy something. Both look nearly the same, but one pin is a little bit thicker in type1. Therefore a type1 male can not connect to a type2 female but vise versa. So you are good to go with buying a type2.

An good explanation can be fond [here][6]. Just match the socket from your tactor with those in the web page and you will retrieve with version you need to buy. The version number also defines the baud rate (usually). type1 uses 250k and type2 500k. Normally all heavy duty trucks build in 2016 should have type2.

### Baudrate
(usually)
* type1 -> 250k
* type2 -> 500k

 If this baudrate is missmatched, you will get a bus violation error message in rapid paste! We faced this many times and without any sideeffects. After disconnecting the board, we were able to start the tractor normally. So we have not destryed anything by choosing a wrong baudrate.

### Pinout
Please again reference to this page [here][6].
There is no need to connect the GND pin, please just leaf it open. Necessary is just `CANH` and `CANL`. If you connect them wrongly, nothing should happen or at least you will not sniff any usefull data.

<img width="400" src="assets/j1939.jpg">  

(image above copied from: [https://guatemaladigital.com/](https://guatemaladigital.com/Automotriz+-+sistema+el%E9ctrico/Producto.aspx?CodigoP=B07DC6C72B))

Usually we only need to connect the CAN-L and CAN-H (C and D) to sniff the bus - a ground connection is not needed. 

[1]: (https://tractorhacking.github.io/)
[2]: (https://canable.io/)
[3]: (https://www.wireshark.org/)
[4]: (https://github.com/linux-can/can-utils)
[5]: (https://en.wikipedia.org/wiki/CAN_bus)
[6]: (https://obd2allinone.com/products/j1939-t2adap.asp)