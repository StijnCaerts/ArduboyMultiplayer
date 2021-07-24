# ArduboyMultiplayer
Arduboy communication platform for multiplayer games.

## How it works
This communication platform enables multiplayer games by forwarding messages on the serial port to the other connected devices.
So this platform could be used by Arduboys, Arduinos and other serial devices.

### Local multiplayer
Run the `local/cli.py` script to set-up local multiplayer communication, with multiple devices connected to the same computer.

Install the dependencies:
```
$ pip install -r local/requirements.txt
```

The `devices` command will list the connected devices:
```
$ python local/cli.py devices
COM3 - Arduino Leonardo bootloader (COM3)
COM5 - Arduino Leonardo bootloader (COM5)
```

Use the device names listed by the `devices` command to start the communication:
```
$ python local/cli.py play COM3 COM5
```