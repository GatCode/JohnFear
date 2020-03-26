# How to capture
Now finally we will introduce you how to sniff and capture can bus data.
For this we used a [CANable PRO][1] board with candlelight firmware in compination with [wireshark][2].

## Connector
Please see your Hardware [page](./hardware.md) and prepare everything properly. 

## Interface
If your connector is prepared please connect it to your pc. Now we need to bring the native (with candlelight) can device up. Within this step we define the baudrate. 

```
  # command generic
  ip link set <devicename> up type can bitrate <baudrate>;
  ip link set down <devicename>
  
  # set interface down if up
  ip link set down can0

  # j1939 type1
  ip link set can0 up type can bitrate 250000;

  # j1939 type2
  ip link set can0 up type can bitrate 500000;

  # check links - should appear here now
  ip link show
```

If no error occured, `can0` device is not ready for sniffing.
Now you can connect to board to your tractor, we recommend to do this with a stopped engine.

## Wireshark
Start [wireshark][2] and start a new capture for the can device, in your case `can0`.

## Start Engine
Fire up the tractor. It is enought to start board computer without engine first, you should already receive can message yet. If only bus valuation messages pop up, you may have used the wrong baudrate.

## Trace data
After starting the tractor, wireshark should capture raw [CAN bus][3] data. Please see an example screenprint below. ![](../assets/wsharkCaptureCan.png)

[1]: (https://canable.io/)
[2]: (https://www.wireshark.org/)
[3]: (https://en.wikipedia.org/wiki/CAN_bus)