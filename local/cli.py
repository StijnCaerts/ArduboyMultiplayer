import sys, signal
import serial, serial.tools.list_ports
import fire
from typing import Set
import logging

logging.basicConfig(level=logging.INFO)


class App:

    def devices(self):
        """
        List the connected serial devices.
        :return: serial ports
        """
        return serial.tools.list_ports.comports()

    def play(self, *devices):
        """
        Start the multi player communication for the given devices.
        :param devices: names of the devices
        """

        if len(devices) < 2:
            raise fire.core.FireError("You cannot have multi player with less than 2 players.")

        serial_connections: Set[serial.Serial] = {serial.Serial(name) for name in devices}
        logging.debug(serial_connections)

        print("Press Ctrl+C to stop the application.")

        def signal_handler(signal, frame):
            for con in serial_connections:
                con.close()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        while True:
            for con in serial_connections:
                while con.in_waiting > 0:
                    line = con.readline().replace(b'\r', b'')
                    logging.debug(line)
                    for ocon in serial_connections:
                        if con == ocon:
                            # don't echo message to sender
                            continue
                        ocon.write(line)


if __name__ == "__main__":
    fire.Fire(App)
