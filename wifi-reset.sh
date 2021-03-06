#!/bin/sh

#google dns
SERVER=8.8.8.8

# Send five pings, sending output to /dev/null
ping -c5 ${SERVER} > /dev/null

if [ $? -ne 0 ] 
then
    # Restart the wireless interface
    sudo ifdown --force wlan0
    sudo ifup wlan0
fi
