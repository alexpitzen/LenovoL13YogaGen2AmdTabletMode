#!/bin/bash

stdbuf -oL -eL libinput debug-events 2>/dev/null | stdbuf -oL -eL grep 'DEVICE_ADDED.*ETPS/2 Elantech' |
while read line
do
  echo $0 disabling mouse
  (echo serio1 > /sys/bus/serio/drivers/psmouse/unbind) 2>/dev/null
done &


stdbuf -oL -eL libinput debug-events 2>/dev/null | stdbuf -oL -eL grep 'DEVICE_ADDED.*AT Translated Set 2 keyboard' |
while read line
do
  echo $0 disabling keyboard
  (echo serio0 > /sys/bus/serio/drivers/atkbd/unbind) 2>/dev/null
done &

python3 tablet_mode.py 1
