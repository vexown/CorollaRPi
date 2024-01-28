#!/bin/sh

(
    pactl load-module module-udev-detect
    pactl set-default-sink alsa_output.usb-0d8c_USB_Sound_Device-00.analog-stereo
    pactl set-default-source bluez_source.F8_71_0C_F3_FE_6A.a2dp_source
    pactl set-card-profile 0 output:analog-surround-51+input:analog-stereo
) &