# LenovoL13YogaGen2AmdTabletMode
Hacky scripts to swap between tablet &amp; laptop modes on Lenovo L13 Yoga Gen 2 AMD (enable screen rotation, disable keyboard &amp; trackpad)

Scripts need(?) to run as root, hence the use of `sudo` in the `.desktop` files. I have all these scripts owned by root so they can't be modified without root permissions.

I'm using the following line in my sudoers to allow the scripts to be run as root without a password being provided:

    alex ALL = (root) NOPASSWD: /home/alex/laptop_mode.sh, /home/alex/tablet_mode.sh
