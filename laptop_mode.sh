#!/bin/bash

killall tablet_mode.sh

echo serio1 > /sys/bus/serio/drivers/psmouse/bind
echo serio0 > /sys/bus/serio/drivers/atkbd/bind

python3 tablet_mode.py 0
