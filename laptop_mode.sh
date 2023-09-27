#!/bin/bash

killall tablet_mode.sh

echo serio1 > /sys/bus/serio/drivers/psmouse/bind
echo serio0 > /sys/bus/serio/drivers/atkbd/bind

# temp disable accelerometer
echo '0020:1022:0001.0001' > /sys/bus/hid/drivers/hid-sensor-hub/unbind

# tablet mode off & reset orientation
python3 tablet_mode.py 0

# reenable accelerometer
echo '0020:1022:0001.0001' > /sys/bus/hid/drivers/hid-sensor-hub/bind
