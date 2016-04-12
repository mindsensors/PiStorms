#!/bin/bash
#
# Copyright (c) 2016 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# Apr 2016  Deepak      install from github created environment

#setup i2c and spi 
if [ -e /boot/config.txt ]
then
    echo "Updating config files..."
    sudo rm -f /boot/config.txt
    sudo cp config.txt /boot/config.txt
else
    echo "Copying config files..."
    sudo cp config.txt /boot/config.txt
fi
#
#
echo "Updating installations files. This may take several minutes..."
sudo apt-get update -qq
echo "Installing packages..."
sudo apt-get install -qq tightvncserver mpg123 build-essential python-dev python-smbus python-pip python-imaging python-numpy git nmap
#
#

sudo sed -i 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/g' /etc/modprobe.d/raspi-blacklist.conf
grep i2c-bcm2708 /etc/modules > /dev/null
if [ $? == 0 ]
then
    echo "i2c-bcm2708 already installed"
else
    sudo sed -i -e '$i \i2c-bcm2708\n' /etc/modules
    #sudo echo 'i2c-bcm2708' >> /etc/modules
fi

grep i2c-dev /etc/modules > /dev/null
if [ $? == 0 ]
then
    echo "i2c-dev already installed"
else
    sudo sed -i -e '$i \i2c-dev\n' /etc/modules
    #sudo echo 'i2c-dev' >> /etc/modules
fi

echo "installing required python packages ... "
sudo pip install -qq RPi.GPIO
sudo pip install -qq mindsensors_i2c
sudo pip install -qq wireless
sudo pip install -qq wifi
sudo pip install -qq ws4py

sudo cp ../sys/PiStormsDriver.py /usr/local/bin/
sudo cp ../sys/PiStormsBrowser.py /usr/local/bin/
sudo cp ../sys/swarmserver /usr/local/bin/
sudo cp ../sys/pistorms-diag.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/swarmserver
sudo chmod +x /usr/local/bin/pistorms-diag.sh

echo "copying library files ... "
sudo cp ../sys/rmap.py /usr/local/lib/python2.7/dist-packages/
sudo cp ../sys/rmapcfg.py /usr/local/lib/python2.7/dist-packages/
sudo cp ../sys/scratch.py /usr/local/lib/python2.7/dist-packages/
sudo cp ../sys/PiStorms.py /usr/local/lib/python2.7/dist-packages/
sudo cp ../sys/PiStormsCom.py /usr/local/lib/python2.7/dist-packages/
sudo cp ../sys/mindsensorsUI.py /usr/local/lib/python2.7/dist-packages/
sudo cp ../sys/mindsensors.py /usr/local/lib/python2.7/dist-packages/
sudo cp ../sys/swarmclient.py /usr/local/lib/python2.7/dist-packages/

# copy system images.
echo "copying system images ... "
sudo mkdir -p /usr/local/mindsensors_images
sudo cp ../programs/btns_center.png /usr/local/mindsensors_images/
sudo cp ../programs/btns_left.png /usr/local/mindsensors_images/
sudo cp ../programs/btns_right.png /usr/local/mindsensors_images/
sudo cp ../programs/button.png /usr/local/mindsensors_images/
sudo cp ../programs/dialogbg.png /usr/local/mindsensors_images/
sudo cp ../programs/Exclamation-mark-icon.png /usr/local/mindsensors_images/
sudo cp ../programs/Pane1.png /usr/local/mindsensors_images/
sudo cp ../programs/lock.png /usr/local/mindsensors_images/
sudo cp ../programs/ulock.png /usr/local/mindsensors_images/
sudo cp ../programs/load.png /usr/local/mindsensors_images/
sudo cp ../programs/x_red.png /usr/local/mindsensors_images/
sudo cp ../programs/wifi_green.png /usr/local/mindsensors_images/
sudo chmod a+r /usr/local/mindsensors_images/*


echo "copying scratch programs ... "
mkdir -p /home/pi/Documents/Scratch\ Projects/PiStorms
sudo cp ../scratch/* /home/pi/Documents/Scratch\ Projects/PiStorms

echo "Changing ownerships"
sudo chown -R pi:pi /home/pi/PiStorms
sudo chown -R pi:pi /home/pi/Documents/Scratch\ Projects

#copy the initialization scripts
sudo cp PiStormsDriver.sh /etc/init.d
sudo cp PiStormsBrowser.sh /etc/init.d
sudo cp SwarmServer.sh /etc/init.d
sudo chmod +x /etc/init.d/PiStormsDriver.sh
sudo chmod +x /etc/init.d/PiStormsBrowser.sh
sudo chmod +x /etc/init.d/SwarmServer.sh
mkdir -p /home/pi/.config/autostart
cp tightvnc.desktop /home/pi/.config/autostart

#
# insert into startup scripts for subsequent use
#
echo "Updating Startup scripts..."
sudo update-rc.d PiStormsDriver.sh defaults 95 05
sudo update-rc.d PiStormsBrowser.sh defaults 96 04
sudo update-rc.d SwarmServer.sh defaults 94 06

#setup messenger
echo "Setting up messenger...."
sudo cp ../sys/ps_messenger_check.py /usr/local/bin
sudo touch /var/tmp/ps_data.json
sudo chmod a+rw /var/tmp/ps_data.json
# setup crontab entry for root
sudo crontab -l -u root | grep ps_messenger_check > /dev/null
if [ $? != 0 ]
then
    (sudo crontab -l -u root 2>/dev/null; echo "*/5 * * * * python /usr/local/bin/ps_messenger_check.py") | sudo crontab - -u root
fi
# run the messenger once
python /usr/local/bin/ps_messenger_check.py > /dev/null


echo "Installing image libraries..."
cd ~
git clone -qq https://github.com/adafruit/Adafruit_Python_ILI9341.git
cd Adafruit_Python_ILI9341
sudo python setup.py -q install
cd  .. 
sudo rm -rf Adafruit_Python_ILI9341

echo "If prompted, enter a password to access vnc"
tightvncserver

echo "For VNC to start upon bootup,"
echo "use rapi-config to set your pi to"
echo "automatically log into the desktop environment."

echo "-----------------------------"
echo "Install completed.   "
echo "Please reboot your Raspberry Pi for changes to take effect."
echo "-----------------------------"

