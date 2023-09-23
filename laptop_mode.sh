#!/bin/bash

killall tablet_mode.sh

python3 laptop_mode.py

echo serio1 > /sys/bus/serio/drivers/psmouse/bind
echo serio0 > /sys/bus/serio/drivers/atkbd/bind
