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


python $homefolder/programs/tests/msg-to-screen.py "Loading Raspbian" "Please wait"
echo "PiStorms Diagnostics tests"
echo "--------------------------"
echo ""
echo "Date..."
echo "-------"
date

echo ""
echo "i2cdetect output"
echo "----------------"
i2cdetect -y 1

echo ""
echo "Voltage check..."
echo "----------------"

if [ -f $homefolder/programs/tests/print-battery-voltage.py ]
then
    python $homefolder/programs/tests/print-battery-voltage.py
else
    echo "print-battery-voltage.py is missing"
fi

#echo ""
#echo "Screen test....."
#echo "----------------"
#
#if [ -f /home/pi/PiStorms/programs/tests/screen-test.py ]
#then
#    python /home/pi/PiStorms/programs/tests/screen-test.py
#else
#    echo "screen-test.py is missing"
#fi

echo ""
echo "PiStorms info "
echo "--------------"

if [ -f $homefolder/programs/tests/psm-info.py ]
then
    python $homefolder/programs/tests/psm-info.py
else
    echo "psm-info.py is missing"
fi

python $homefolder/programs/tests/msg-to-screen.py "Loading PiStorms" "Please wait"

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

