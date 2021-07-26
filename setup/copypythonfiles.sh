#!/bin/bash

PY3_PATH="/usr/local/lib/python3.5"

## dependancies for python3 OpenCV
#sudo apt install libatlas3-base libsz2 libharfbuzz0b libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0
#sudo apt install libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
#sudo pip3 install opencv-python opencv-contrib-python

## others used in the demo programs
#sudo apt install python3-matplotlib python3-scipy
#sudo pip3 install imutils

## used in the dist packages below
#sudo pip3 install configparser
#sudo pip3 install pillow

# copy Python library files
sudo cp -p ../sys/rmap.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/rmapcfg.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/scratch.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/PiStorms.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/PiStorms_GRX.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/PiStormsCom.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/PiStormsCom_GRX.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/TouchScreenInput.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/mindsensorsUI.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/MS_ILI9341.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/mindsensors.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/MsDevices.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/LegoDevices.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/GroveDevices.py $PY3_PATH/dist-packages/
sudo cp -p ../sys/swarmclient.py $PY3_PATH/dist-packages/


sudo cp -p ../sys/mindsensors_i2c.py $PY3_PATH/dist-packages/
