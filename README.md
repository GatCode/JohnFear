<p align="center">
  <img width="400" src="assets/logo.png">
  <h3 align="center">_🦌_🚜💨_ Let John fear the deer</h3>
</p>
<br><br>

## General
JohnFear is an open source project with the goal to reverse engineer [John Deere][1] tractors. At first we will more or less only focus exploiting the [can bis][2]. [John Deere][1] follows the industry standards and uses the [J1939][9] protocol for the control unit intercommunication. Because the [can bus][2] traffic is not encrypted, we see here your best change for extracting and manipulating the tractor.

Please keep in mind that this project is a **work in progress** and the advancements are limited by our time and money.

## CAN basics
Sorry guess but we will not explain the [can bus][2] in detail here. The most important attitue is mainly also the reason why we have started this project. [Can bus][2] broadcasts all the messages, which means that we can sniff all the data and anlysis it offline.

We suggest to go throw some tutorials first before you continue reading. Basically you can just google for can bus and you will get a bunch of information to go throw.
* [Wikipedia][2]
* [Tractor Hacking][5]
* [CSS electronics][8]

The takeaway should be that [can bus][2] is used as physical layer for transporting [J1939][9] messages.

## J1939
Yey you have finished the [can bus][2] section, so we assume yuo are an expert now. However let's check out what [J1939][9] is use for. In a nutshell it defined the messages tracture and is published by [SAE][10] (Society of Automotive Entineers). The entire standard is published within multiple papers, at first we will only need J1939/71, which describs the PGN (Parameter Group Number) and SPNs (Suspect Parameter Number). We really recommend to go throw this [guide](https://www.csselectronics.com/screen/page/simple-intro-j1939-explained).
Quite a good explanation can be found [here][11] as well.

## Related work
There is already some progress out there, so we have not started entirly from scratch. Please checkout [Tractor Hacking][5] from the California Polytechnic State University which is also an open source project. You can find some sniffed data in there github repository as well. In addition, they have written already and client in python refered to [PolyCan][6]. In your opinion we do not see any need to use this tool, because we achieved the same with Wireshark.

We recommand also to have a look at [CSS electronics][8]. Unfortunatly they only offer commercial project, but you can find really fantastic explainations on there side.

## Goals
The final goal of this project is not really defined. We will try to keep moving on as far as possible.

###  First goal
At first we will focus on sniffing only. The goal is to sniff and decode the [J1939][9] messages in real time with wireshark. This is basically already available by [CSS electronics][8], but let's get it done open source.

Please checkout your tutorial how to [sniff can bus data](./docs/howToCapture.md)

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

[1]: (https://www.deere.com/en/index.html)
[2]: (https://en.wikipedia.org/wiki/CAN_bus)
[3]: (https://github.com/GatCode)
[4]: (https://github.com/whati001)
[5]: (https://tractorhacking.github.io/)
[6]: (https://github.com/TractorHacking/PolyCAN)
[7]: (https://www.wireshark.org/)
[8]: (https://www.csselectronics.com/screen/overview)
[9]: (https://en.wikipedia.org/wiki/SAE_J1939)
[10]: (https://www.sae.org/)
[11]: (https://obd2allinone.com/products/j1939-t2adap.asp)