#!/bin/bash

set -m

echo serio1 > /sys/bus/serio/drivers/psmouse/unbind
echo serio0 > /sys/bus/serio/drivers/atkbd/unbind

stdbuf -oL -eL libinput debug-events | stdbuf -oL -eL grep 'DEVICE_ADDED.*ETPS/2 Elantech' |
while read line
do
	echo "read $line"
	echo serio1 > /sys/bus/serio/drivers/psmouse/unbind
done &


stdbuf -oL -eL libinput debug-events | stdbuf -oL -eL grep 'DEVICE_ADDED.*AT Translated Set 2 keyboard' |
while read line
do
	echo "read $line"
	echo serio0 > /sys/bus/serio/drivers/atkbd/unbind
done &

python3 tablet_mode.py

fg 2
fg 1
