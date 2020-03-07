<p align="center">
  <img width="400" src="assets/logo.png">
  <h3 align="center">_🦌_🚜💨_ Let John fear the deer</h3>
</p>
<br><br>

## About
This project is an attempt to **reverse engineer** the CAN bus system of a **John Deere 6125R** (later on all newer John Deere models) and to inject messages to gain control of the whole Traktor.

Please keep in mind that this project is a **work in progress** and the advancements are limited by our time and money.

## CAN basics:
To fully understand our work, we first will provide you a small introduction on the CAN system itself.

In general there are two different kinds of SAE J1939 connectors inside a John Deere. There are the old ones (black) and the newer ones (green with one pin smaller). No matter what bus sniffing device you use, these connectors should not limit you in any way!

<img width="400" src="assets/j1939.jpg">  

(image above copied from: [https://guatemaladigital.com/](https://guatemaladigital.com/Automotriz+-+sistema+el%E9ctrico/Producto.aspx?CodigoP=B07DC6C72B))


Since you never can be sure if the colors of the cables are right, just use a Multimeter to meassure which colors are connected to the CAN-L and CAN-H pins.

(this image contains the pinout in the direction of the image of the plug in the top - from behind!!!)  

<img width="400" src="assets/canPinout.jpg">  

(image above copied from: [https://tractorhacking.github.io/usage/](https://tractorhacking.github.io/usage/))

Usually we only need to connect the CAN-L and CAN-H (C and D) to sniff the bus - a ground connection is not needed.

Also keep in mind that the old connector means that the traktor usually uses a baudrate of 250k but in the case of an already installed GPS, the baudrate could also be 500k. If this baudrate is missmatched, you will get a bus violation error message in rapid paste!

## Hardware
We decided to use the [CANable](https://canable.io) device as our sniffing tool since it is open-souce and you can decide which firmware you are using.

Regarding the firmware, we opted for the [candleLight](https://github.com/normaldotcom/candleLight_fw) firmware which is also recommended from the manufacturer.

This in combination with a Linux Laptop yielded to our bus sniffs!

## Reports:

* [13 Feb 2020 - First CAN sniffs](reports/13Feb2020/13Feb2020.md)

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/whati001"><img src="https://avatars3.githubusercontent.com/u/16085873?s=460&v=4" width="100px;" alt=""/><br /><sub><b>whati001</b></sub></a><br /><a href="#question" title="Answering Questions">💬 </a><a href="#infrastructure" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance" title="Maintenance">🚧</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## Useful Links:
* [John Deere Service Pinout](https://obdii365.blogspot.com/2017/03/john-deere-service-edl-7215r-9-pin-cable-pinout.html)
* [J1939 Type 2 (Green) Pinout](https://obd2allinone.com/products/j1939-t2adap.asp)
* [CAN DBC File](https://www.csselectronics.com/screen/page/dbc-database-can-bus-conversion-wireshark-j1939-example/language/en)
