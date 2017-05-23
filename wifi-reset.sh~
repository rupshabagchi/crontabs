#!/bin/sh

SERVER=8.8.8.8

ping -c5 ${SERVER} > /dev/null
if [ $? -ne 0 ]; then
    sudo ifdown --force wlan0
    sudo ifup wlan0
fi
