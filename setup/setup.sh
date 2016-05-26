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
cp -p /boot/config.txt /tmp/config.txt

ff=/tmp/config.txt

grep "^dtparam=i2c_arm=on" $ff > /dev/null
if [ $? == 0 ]
then
    echo "i2c_arm is already enabled"
else
    sudo sed -i -e '$i \dtparam=i2c_arm=on' $ff
fi

grep "^dtparam=i2c1=on" $ff > /dev/null
if [ $? == 0 ]
then
    echo "i2c1 is already enabled"
else
    sudo sed -i -e '$i \dtparam=i2c1=on' $ff
fi

grep "^dtparam=i2c_baudrate" $ff > /dev/null
if [ $? == 0 ]
then
    echo "i2c_baudrate is already configured, changing it to 50000"
    sed -i 's/^dtparam=i2c_baudrate.*$/dtparam=i2c_baudrate=50000/g' $ff
else
    sudo sed -i -e '$i \dtparam=i2c_baudrate=50000' $ff
fi

grep "^dtparam=spi=on" $ff > /dev/null
if [ $? == 0 ]
then
    echo "spi is already enabled"
else
    sudo sed -i -e '$i \dtparam=spi=on' $ff
fi

sudo cp -p /tmp/config.txt /boot/config.txt

#
#
echo "Updating installations files. This may take several minutes..."
sudo apt-get update -qq
echo "Installing packages..."
sudo apt-get install -qq tightvncserver mpg123 build-essential python-dev python-smbus python-pip python-imaging python-numpy git nmap
sudo apt-get install -qq python-opencv
sudo pip install -qq imutils
#
#

sudo sed -i 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/g' /etc/modprobe.d/raspi-blacklist.conf
grep i2c-bcm2708 /etc/modules > /dev/null
if [ $? == 0 ]
then
    echo "i2c-bcm2708 already installed"
else
    sudo sed -i -e '$i \i2c-bcm2708\n' /etc/modules
fi

grep i2c-dev /etc/modules > /dev/null
if [ $? == 0 ]
then
    echo "i2c-dev already installed"
else
    sudo sed -i -e '$i \i2c-dev\n' /etc/modules
fi

echo "installing required python packages ... "
sudo pip install -qq RPi.GPIO
sudo pip install -qq mindsensors_i2c
sudo pip install -qq wireless
sudo pip install -qq wifi
sudo pip install -qq ws4py
sudo pip install -qq cv2

# clean up renamed legacy files.
sudo rm -f /usr/local/bin/PiStormsDriver.py
sudo rm -f /usr/local/bin/PiStormsBrowser.py
sudo update-rc.d -f PiStormsDriver.sh remove
sudo update-rc.d -f PiStormsBrowser.sh remove
sudo rm -f /etc/init.d/PiStormsDriver.sh
sudo rm -f /etc/init.d/PiStormsBrowser.sh

# copy startup scripts.
sudo cp -p ../sys/MSDriver.py /usr/local/bin/
sudo cp -p ../sys/MSBrowser.py /usr/local/bin/
if [ -f /etc/init.d/SwarmServer.sh ]
then
    sudo /etc/init.d/SwarmServer.sh stop
else
	sudo kill -9 `ps -ef | grep swarmserver |grep -v grep| cut -c11-16`
fi
sleep 2
sudo cp -p ../sys/swarmserver /usr/local/bin/
sudo cp -p ../sys/pistorms-diag.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/swarmserver
sudo chmod +x /usr/local/bin/pistorms-diag.sh
sudo chmod +x ../programs/addresschange

echo "copying library files ... "
sudo cp -p ../sys/rmap.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/rmapcfg.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/scratch.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/PiStorms.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/PiStormsCom.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/TouchScreenInput.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/mindsensorsUI.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/mindsensors.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/swarmclient.py /usr/local/lib/python2.7/dist-packages/

echo "copying config file ... "
sudo mkdir -p /usr/local/mindsensors/conf
if [ -f /usr/local/mindsensors/conf/msdev.cfg ]
then
    echo "using previous configuration..."
    # add/update any configurations here if you need to.
else
    sudo cp -p ../sys/msdev.cfg /usr/local/mindsensors/conf/
fi

# copy system images.
echo "copying system images ... "
sudo rm -rf /usr/local/mindsensors_images
sudo mkdir -p /usr/local/mindsensors/images
sudo cp -p ../programs/btns_center.png /usr/local/mindsensors/images/
sudo cp -p ../programs/btns_left.png /usr/local/mindsensors/images/
sudo cp -p ../programs/btns_right.png /usr/local/mindsensors/images/
sudo cp -p ../programs/button.png /usr/local/mindsensors/images/
sudo cp -p ../programs/dialogbg.png /usr/local/mindsensors/images/
sudo cp -p ../programs/Exclamation-mark-icon.png /usr/local/mindsensors/images/
sudo cp -p ../programs/Pane1.png /usr/local/mindsensors/images/
sudo cp -p ../programs/ms-logo-w320-h240.png /usr/local/mindsensors/images/
sudo cp -p ../programs/python.png /usr/local/mindsensors/images/
sudo cp -p ../programs/folder.png /usr/local/mindsensors/images/
sudo cp -p ../programs/leftarrow.png /usr/local/mindsensors/images/
sudo cp -p ../programs/rightarrow.png /usr/local/mindsensors/images/
sudo cp -p ../programs/uparrow.png /usr/local/mindsensors/images/
sudo cp -p ../programs/missing.png /usr/local/mindsensors/images/
sudo chmod a+r /usr/local/mindsensors/images/*

echo "copying artworks ... "
sudo cp -p ../artwork/* /usr/share/raspberrypi-artwork

echo "copying scratch programs ... "
mkdir -p /home/pi/Documents/Scratch\ Projects/PiStorms
sudo cp -p ../scratch/* /home/pi/Documents/Scratch\ Projects/PiStorms

echo "Changing ownerships"
sudo chown -R pi:pi /home/pi/PiStorms
sudo chown -R pi:pi /home/pi/Documents/Scratch\ Projects

#copy the initialization scripts
sudo cp -p MSDriver.sh /etc/init.d
sudo cp -p MSBrowser.sh /etc/init.d
sudo cp -p SwarmServer.sh /etc/init.d
sudo chmod +x /etc/init.d/MSDriver.sh
sudo chmod +x /etc/init.d/MSBrowser.sh
sudo chmod +x /etc/init.d/SwarmServer.sh
mkdir -p /home/pi/.config/autostart
cp -p tightvnc.desktop /home/pi/.config/autostart

#
# insert into startup scripts for subsequent use
#
echo "Updating Startup scripts..."
sudo update-rc.d MSDriver.sh defaults 95 05
sudo update-rc.d MSBrowser.sh defaults 96 04
sudo update-rc.d SwarmServer.sh defaults 94 06

#setup messenger
echo "Setting up messenger...."
sudo cp -p ../sys/ps_messenger_check.py /usr/local/bin
sudo cp -p ../sys/ps_updater.py /usr/local/bin
sudo touch /var/tmp/ps_data.json
sudo chmod a+rw /var/tmp/ps_data.json
sudo touch /var/tmp/ps_versions.json
sudo chmod a+rw /var/tmp/ps_versions.json

# delete previous messenger entry
sudo crontab -u root -l | grep -v 'ps_messenger_check.py'  | sudo crontab -u root -

# setup crontab entry of messenger for root
sudo crontab -l -u root | grep ps_messenger_check > /dev/null
if [ $? != 0 ]
then
    (sudo crontab -l -u root 2>/dev/null; echo "* */1 * * * python /usr/local/bin/ps_messenger_check.py") | sudo crontab - -u root
fi
# run the messenger once
python /usr/local/bin/ps_messenger_check.py > /dev/null

# delete previous updater entry
sudo crontab -u root -l | grep -v 'ps_updater.py'  | sudo crontab -u root -

# setup crontab entry of updater for root
sudo crontab -l -u root | grep ps_updater > /dev/null
if [ $? != 0 ]
then
    (sudo crontab -l -u root 2>/dev/null; echo "2 */2 * * * python /usr/local/bin/ps_updater.py") | sudo crontab - -u root
fi
# run the updater once
python /usr/local/bin/ps_updater.py > /dev/null


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

