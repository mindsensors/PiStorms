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
# Jan 2017  Seth        Add files to upgrade firmware if below V3.00
# Jun 2017  Seth        Remove new touchscreen approach, organize


echo "Beginning setup"
# change the current working directory of the subshell to that of this script file
cd "$(dirname "$0")"


echo "Configuring I2C and SPI..."
# copy the boot config file to a temporary file, edit it, then (sudo) copy it back
ff=/tmp/config.txt
cp /boot/config.txt $ff

grep "^dtparam=i2c_arm=on" $ff > /dev/null
if [ $? != 0 ]
then
    sudo sed -i -e '$i \dtparam=i2c_arm=on' $ff
fi

grep "^dtparam=i2c1=on" $ff > /dev/null
if [ $? != 0 ]
then
    sudo sed -i -e '$i \dtparam=i2c1=on' $ff
fi

grep "^dtparam=i2c_baudrate" $ff > /dev/null
if [ $? == 0 ]
then
    # baudrate higher than 40000 does not work on PIXEL.
    sed -i 's/^dtparam=i2c_baudrate.*$/dtparam=i2c_baudrate=40000/g' $ff
else
    sudo sed -i -e '$i \dtparam=i2c_baudrate=40000' $ff
fi

grep "^dtparam=spi=on" $ff > /dev/null
if [ $? != 0 ]
then
    sudo sed -i -e '$i \dtparam=spi=on' $ff
fi

sudo cp /tmp/config.txt /boot/config.txt


echo "Depending on your internet connection, the following few steps may take several minutes."
echo "Updating package lists..."
sudo apt-get -qq -y update
echo "Downloading and installing 15 required packages..."
sudo apt-get  -y install build-essential git nmap mpg123 apache2 php7.3 libapache2-mod-php7.3 libapache2-mod-php\
                            python-numpy python-matplotlib python-scipy python-opencv \
                            python-dev python-smbus python-pip  
echo "Updating pip..."
sudo pip  install --upgrade pip
echo "Downloading and installing 7 required Python packages..."
sudo pip  install --upgrade mindsensors-i2c
sudo pip  install RPi.GPIO wireless wifi ws4py flask imutils 
sudo pip install pillow


echo "Copying files..."
# clean up renamed legacy files.
sudo rm -f /usr/local/bin/PiStormsDriver.py
sudo rm -f /usr/local/bin/PiStormsBrowser.py
sudo update-rc.d -f PiStormsDriver.sh remove
sudo update-rc.d -f PiStormsBrowser.sh remove
sudo rm -f /etc/init.d/PiStormsDriver.sh
sudo rm -f /etc/init.d/PiStormsBrowser.sh

# copy startup scripts
sudo cp -p ../sys/MSDriver.py /usr/local/bin/
sudo cp -p ../sys/MSBrowser.py /usr/local/bin/
sudo cp -p ../sys/psm_shutdown /usr/local/bin/
sudo cp -p ../sys/pistorms-diag.sh /usr/local/bin/
# stop swarmserver (if it's already running) before copying it
if [ -f /etc/init.d/SwarmServer.sh ]
then
    sudo /etc/init.d/SwarmServer.sh stop
else
    sudo kill -SIGKILL $(ps -aux | awk '/swarmserver/ && !/awk/ {print $2}' | tail -1) 2> /dev/null
fi
sleep 2
sudo cp -p ../sys/swarmserver /usr/local/bin/

# copy Python library files
sudo cp -p ../sys/rmap.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/rmapcfg.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/scratch.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/PiStorms.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/PiStorms_GRX.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/PiStormsCom.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/PiStormsCom_GRX.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/TouchScreenInput.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/mindsensorsUI.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/MS_ILI9341.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/mindsensors.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/MsDevices.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/LegoDevices.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/GroveDevices.py /usr/local/lib/python2.7/dist-packages/
sudo cp -p ../sys/swarmclient.py /usr/local/lib/python2.7/dist-packages/

# copy web interface files
sudo mkdir -p /var/www
sudo cp -r ../www/html /var/www/
# remove Apache2 Debian default page so index.php will be accessed instead
sudo rm -f /var/www/html/index.html
sudo cp -r ../www/web_api /var/www/web_api
# create directory for the web interface to save screenshots
sudo mkdir -p /var/tmp/ps_images

# copy config file
sudo mkdir -p /usr/local/mindsensors/conf
if [ ! -f /usr/local/mindsensors/conf/msdev.cfg ]
then
    sudo cp -p ../sys/msdev.cfg /usr/local/mindsensors/conf/
fi

# copy icons for MSBrowser
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
sudo cp -p ../programs/refresharrow.png /usr/local/mindsensors/images/
sudo cp -p ../programs/returnarrow.png /usr/local/mindsensors/images/
sudo cp -p ../programs/missing.png /usr/local/mindsensors/images/
sudo cp -p ../artwork/* /usr/local/mindsensors/images/

# copy desktop background
sudo cp -p ../artwork/* /usr/share/raspberrypi-artwork

# copy Scratch programs
mkdir -p /home/pi/Documents/Scratch\ Projects/PiStorms
sudo cp -p ../scratch/* /home/pi/Documents/Scratch\ Projects/PiStorms


echo "Setting up services..."
# copy service scripts
sudo cp -p MSDriver.sh /etc/init.d
sudo cp -p MSBrowser.sh /etc/init.d
sudo cp -p MSWeb.sh /etc/init.d
sudo cp -p SwarmServer.sh /etc/init.d
mkdir -p /home/pi/.config/autostart
# set these scripts to run at startup
sudo update-rc.d MSDriver.sh defaults 95 05
sudo update-rc.d MSBrowser.sh defaults 96 04
sudo update-rc.d MSWeb.sh defaults 96 04
sudo update-rc.d SwarmServer.sh defaults 94 06

# setup messenger and updaters, a system to check for updates and notices
sudo cp -p ../sys/ps_messenger_check.py /usr/local/bin
sudo cp -p ../sys/ps_updater.py /usr/local/bin
sudo touch /var/tmp/ps_data.json
sudo chmod a+rw /var/tmp/ps_data.json
sudo touch /var/tmp/ps_versions.json
sudo chmod a+rw /var/tmp/ps_versions.json
# initialize an empty crontab for root if one does not exist
sudo crontab -l -u root 2>/dev/null | sudo crontab -u root -
# delete any previous messenger or updater entries
sudo crontab -u root -l | grep -v 'ps_messenger_check.py' | sudo crontab -u root -
sudo crontab -u root -l | grep -v 'ps_updater.py' | sudo crontab -u root -
# setup crontab entry of messenger and updater for root
sudo crontab -l -u root | grep ps_messenger_check > /dev/null
if [ $? != 0 ]
then
    (sudo crontab -l -u root 2>/dev/null; echo "* */1 * * * python /usr/local/bin/ps_messenger_check.py") | sudo crontab - -u root
fi
sudo crontab -l -u root | grep ps_updater > /dev/null
if [ $? != 0 ]
then
    (sudo crontab -l -u root 2>/dev/null; echo "2 */2 * * * python /usr/local/bin/ps_updater.py") | sudo crontab - -u root
fi
# run messenger and updater once
python /usr/local/bin/ps_messenger_check.py > /dev/null
python /usr/local/bin/ps_updater.py > /dev/null


echo "Installing display libraries..."
# setup Adafruit GFX library requirement
cd ~
git clone -qq https://github.com/adafruit/Adafruit_Python_ILI9341.git
cd Adafruit_Python_ILI9341
sudo python setup.py install &> /dev/null
cd ..
sudo rm -rf Adafruit_Python_ILI9341


echo "Performing a few last configurations..."
# enable kernel modules
sudo sed -i 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/g' /etc/modprobe.d/raspi-blacklist.conf
grep i2c-bcm2708 /etc/modules > /dev/null
if [ $? != 0 ]
then
    sudo sed -i -e '$i \i2c-bcm2708\n' /etc/modules
fi

grep i2c-dev /etc/modules > /dev/null
if [ $? != 0 ]
then
    sudo sed -i -e '$i \i2c-dev\n' /etc/modules
fi

# configure wifi for pistormsclassroom
ff=/etc/wpa_supplicant/wpa_supplicant.conf
if [ -f $ff ]
then
    sudo grep "ssid=\"pistormsclassroom\"" $ff > /dev/null
    if [ $? != 0 ]
    then
        sudo sed -i -e '$a \network={\nssid="pistormsclassroom"\npsk="pistormsclassroom"\n}' $ff
    fi
else
    sudo mkdir -p /etc/wpa_supplicant
    echo \
'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
  ssid="pistormsclassroom"
  psk="pistormsclassroom"
}' \
    > /tmp/wpa
    sudo mv /tmp/wpa $ff
fi

# enable VNC
if [ -f /etc/init.d/vncserver-x11-serviced ]
then
    sudo /usr/sbin/update-rc.d vncserver-x11-serviced defaults
    sudo /usr/sbin/update-rc.d vncserver-x11-serviced enable
fi

if [ -f /lib/systemd/system/apache2.service ]
then
    sudo sed -i 's/PrivateTmp=true/PrivateTmp=false/' /lib/systemd/system/apache2.service
    sudo sed -i 's/PrivateTmp=true/PrivateTmp=false/' /lib/systemd/system/apache2@.service
fi

echo "
Install completed!
Please reboot your Raspberry Pi for changes to take effect."
