#!/bin/bash

echo ""
echo "config file"
echo "----------------"
if [ -f /usr/local/mindsensors/conf/msdev.cfg ]
then
    cat /usr/local/mindsensors/conf/msdev.cfg
    homefolder=`grep homefolder /usr/local/mindsensors/conf/msdev.cfg | cut -d"=" -f2`
else
    echo "config file is missing"
    homefolder=/home/pi/PiStorms
fi
echo "homefolder: $homefolder"


#python $homefolder/programs/utils/msg-to-screen.py "Loading Raspbian" "Please wait"
echo "Running PiStorms Diagnostics"
echo "--------------------------"
echo ""
echo "Date..."
echo "-------"
date

echo ""
echo "PiStorms info "
echo "--------------"

if [ -f $homefolder/programs/utils/psm-info.py ]
then
    python $homefolder/programs/utils/psm-info.py
else
    echo "psm-info.py is missing"
fi

echo ""
echo "i2cdetect output"
echo "----------------"
i2cdetect -y 1 0x03 0x74
i2cdetect -y 1 0x76 0x77

echo ""
echo "Voltage check..."
echo "----------------"

if [ -f $homefolder/programs/utils/print-battery-voltage.py ]
then
    echo "voltage check"
    python $homefolder/programs/utils/print-battery-voltage.py
else
    echo "print-battery-voltage.py is missing"
fi

#echo ""
#echo "Screen test....."
#echo "----------------"
#
#if [ -f /home/pi/PiStorms/programs/utils/screen-test.py ]
#then
#    python /home/pi/PiStorms/programs/utils/screen-test.py
#else
#    echo "screen-test.py is missing"
#fi

echo ""
echo "uname ...."
echo "----------"
uname -a

echo ""
echo "Network info ...."
echo "-----------------"
ifconfig -a

echo ""
echo "Ping test ...."
echo "-----------------"
ping -c 3 8.8.8.8

echo ""
echo "PiStorms Diagnostics test concluded...."
echo "---------------------------------------"

