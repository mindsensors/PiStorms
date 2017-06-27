# PiStorms

The [PiStorms](http://www.mindsensors.com/content/78-pistorms-lego-interface) is a robotics platform. It enables you to create robots using LEGO Mindstorms parts, and control it on a Raspberry Pi with Python. Besides its 4 motor ports, 4 sensor ports, and all the benefits of the Raspberry Pi, the PiStorms lets you do even more. It has a touchscreen for easy visual feedback and touch input. It has a convenient web interface to program and control the device, even accessible on mobile devices.

This document will introduce you to the repository's structure and how the PiStorms functions overall.


## Platform structure and systems

### The Browser
- MSBrowser is the program the end-user will use to launch Python programs on the PiStorms
- Each page displays four items (files and folders). Left and right arrows in the top corner allow for page navigation.
- Tapping a folder will open it, and the leftmost page will have an up arrow to close it and go back
- The hostname appears in cyan at the top, and a battery indicator is shown in the bottom-right
- An red exclamation mark icon will appear in the top-right if there is a new message or update available

### The Web Interface
- Accessing the PiStorms's hostname via a web browser will yield the [PiStorms Web Interface](http://www.mindsensors.com/blog/how-to/how-to-access-pistorms-web-interface)
- The dashboard provides basic information including the software and firmware versions, Ethernet and WiFI IP addresses, and current battery voltage. Additionally there are buttons to shutdown or restart the Raspberry Pi, stop or start the browser, and begin touchscreen calibration.
- There is a tab to write and edit programs from your web browser. You can write Python or use the [Blockly](http://www.mindsensors.com/blog/pistorms/visual-programming-for-pistorms-robots) visual programming interface here.
- Screenshots can be taken at any time. This page lets you start and stop recording screenshots, as well as download individual screenshots or clear them all.
- A remote control is available, which is particularly useful on a mobile device. There is a joystick to move your robot (using motors B and C). There are also sliders to set the LED colors.
- Log files are also accessible from the web interface


## Coordinate systems

| ​ | ​ | ​ |
| --- | :---: | --- |
| x=320 <br> y=0 |  | x=0 <br> y=0 |
| | TS <br> (readings from touchscreen X/Y registers) | |
| x=320 <br> y=240 |  | x=0 <br> y=240 |

| ​ | ​ | ​ |
| --- | :---: | --- |
| x=0 <br> y=320 |  | x=0 <br> y=0 |
| | Screen <br> (drawing to TFT) | |
| x=240 <br> y=320 |  | x=240 <br> y=0 |

| ​ | ​ | ​ |
| --- | :---: | --- |
| x=0 <br> y=0 |  | x=320 <br> y=0 |
| | Rotation 3 <br> (right-side-up) | |
| x=0 <br> y=240 |  | x=320 <br> y=240 |

| ​ | ​ | ​ |
| --- | :---: | --- |
| x=320 <br> y=240 |  | x=0 <br> y=240 |
| | Rotation 1 <br> (up-side-down) | |
| x=320 <br> y=0 |  | x=0 <br> y=0 |

| ​ | ​ | ​ |
| --- | :---: | --- |
| x=0 <br> y=320 |  | x=0 <br> y=0 |
| | Rotation 0 <br> (Bank A up) | |
| x=240 <br> y=320 |  | x=240 <br> y=0 |

| ​ | ​ | ​ |
| --- | :---: | --- |
| x=240 <br> y=0 |  | x=240 <br> y=320 |
| | Rotation 2 <br> (Bank B up) | |
| x=0 <br> y=0 |  | x=0 <br> y=320 |


## Repository files

### setup
#### Suggestions
- When developing, hard link the source files from `/home/pi/PiStorms/...` to their destinations from `setup.sh` ([script](https://gist.github.com/seth10/e41a091ef56d0044474e82f3541755e4))
```bash
b=`grep homefolder /usr/local/mindsensors/conf/msdev.cfg | cut -d"=" -f2 | cut -c 2-`
for f in 'MSDriver.py' 'MSBrowser.py' 'psm_shutdown' 'swarmserver' 'pistorms-diag.sh'; do sudo ln -f $b/sys/$f /usr/local/bin/$f; done
chmod +x $b/sys/swarmserver $b/sys/pistorms-diag.sh $b/programs/addresschange
for f in 'rmap.py'  'rmapcfg.py' 'scratch.py' 'PiStorms.py' 'PiStormsCom.py' 'TouchScreenInput.py' 'mindsensorsUI.py' 'MS_ILI9341.py' 'mindsensors.py' 'MsDevices.py' 'LegoDevices.py' 'swarmclient.py'; do sudo ln -f $b/sys/$f /usr/local/lib/python2.7/dist-packages/$f; done
sudo rm -rf /var/www
sudo ln -s $b/www /var/www
sudo ln -f $b/sys/msdev.cfg /usr/local/mindsensors/conf/msdev.cfg
# skipping images, art, scratch, changing ownerships... programs are still only in /home/pi/PiStorms
for f in 'MSDriver.sh' 'MSBrowser.sh' 'MSWeb.sh' 'SwarmServer.sh'; do sudo ln -f $b/setup/$f /etc/init.d/$f; done
for f in 'MSDriver.sh' 'MSBrowser.sh' 'MSWeb.sh' 'SwarmServer.sh'; do chmod +x $b/setup/$f; done
for f in 'ps_messenger_check.py' 'ps_updater.py'; do sudo ln -f $b/sys/$f /usr/local/bin/$f; done
sudo chmod +x /usr/local/bin/psm_shutdown
```

### sys
- **LegoDevices.py**: Basic NXT and EV3 sensors
- **MSBrowser.py**: The [browser program](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#the-browser)
- **MSDriver.py**: Shuts down the Raspberry Pi after GO is held for 5 seconds
- **MS_ILI9341.py**: Inherits from `Adafruit_ILI9341` and adds screenshot support
- **MsDevices.py**: Implementations of mindsensors sensors
- **PiStorms.py**: The wrapper class users instantiate and use. It mainly aligns one-to-one with PiStormsCom functions.
- **PiStormsCom.py**: Handles primary I2C communications
- **TouchScreenInput.py**: A convenience module to get text input using a touchscreen keyboard
- **mindsensors.py**: Implementations of more mindsensors sensors
- **mindsensorsUI.py**: Represents the screen, providing useful graphics functions
- **msdev.cfg**: Configurations including the device type, default screen rotation, home folder, and from what URLs messages and updates are found
- **pistorms-diag.sh**: Diagnostics are written to psm-diag.txt on the boot partition
- **ps_messenger_check.py**: Checks the [message server](http://pistorms.mindsensors.com/messenger.php) and keeps `/var/tmp/ps_data.json` up-to-date
- **ps_updater.py**: Checks the [update server](http://pistorms.mindsensors.com/versions.php) (while sending analytics) to keep `/var/tmp/ps_versions.json` up-to-date
- **psm_shutdown**: Wraps the OS shutdown command, but also writes to `/tmp/.psm_shutdown.lck`
- **rmap.py**: Used for [Scratch](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#scratch) integration
- **rmapcfg.py**: IP and port to use for Scratch integration
- **scratch.py**: Methods for sending messages with Scratch
- **swarmclient.py**: Examples of communicating between multiple PiStorms
- **swarmserver**: Binary used for inter-PiStorms communication

### programs
- This folder is what the user will see on the PiStorms screen (through the [browser program](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#the-browser))
- **00-About_Me.py**: A useful diagnostics program that displays useful information about the device. This includes the device name, firmware and software versions, hostname, battery level, and IP addresses for Ethernet and WiFi.
- **00-Scratch_PiStorms.py**: Used to connect with [Scratch](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#scratch) and execute instructions from it.
- **00-TestInternetConnection.py**: Pings Google's domain name server to determine if the device is connected to the internet.
- **00-WiFi_Setup.py**: Used to connect to the internet directly from the PiStorms. It displays a list of scanned WiFi networks and will let you enter a passphrase using an on-screen keyboard.
- **03-Swarm_Demo.py**: ?
- **09-refresh.py**: If anything changes in the programs folder, they will not be reflected in the browser until it is refreshed. Another way to achieve this is to enter and exit any folder. A program might have been created or renamed from the web interface (or an SSH session).
- **09-shutdown.py**: Let's you shutdown the PiStorms from the device itself. It will display a confirmation before shutting down. Note there is also a shutdown (and restart) button on the PiStorms Web Interface dashboard. Also note holding the GO button for five seconds will restart the PiStorms.
- **10-ico**: These are files from the image recognition robot [blog post](http://www.mindsensors.com/blog/pistorms/image-recognition-robot-with-pistorms-and-pi-camera)
- **20-BlocklyDemos**: Examples using the [Blockly](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#the-web-interface) visual programming interface. These files should be modified through the web interface. However, it might be enlightening to view the code and learn how the blocks align with real Python code.
- **30-DataVisualization**: Examples of using matplotlib to display graphs on the PiStorms's screen. Introduce in this [blog post](http://www.mindsensors.com/blog/how-to/pistorms-data-logging) and projects include a pendulum and car impact.
- **45-Utils**: Various utility programs, including those to revert WiFi settings, calibrate an AbsoluteIMU, check battery voltage, change the PiStorms's I2C address, and the Explorer program to debug I2C devices
- **50-CameraDemos**: Examples using the Raspberry Pi camera
- **50-MotorDemos**: Examples of controlling the motor ports in various ways, and of the NXTServo
- **50-SensorDemos**: Example programs for most all supported sensors
- **60-Games**: Demo games and graphics tests act as examples of using the touchscreen
- **60-Robots**: Programs for some robots features in blog posts, including [My Loyal PyDog Companion](http://www.mindsensors.com/blog/how-to/my-loyal-pydog-companion) and [Sam the Emotional Robot](http://www.mindsensors.com/blog/how-to/sam-the-emotional-robot).
- **utils**: Various system utility programs. This folder is not visible in the browser as it is not preceded by two digits.
- **addresschange**: A binary used by `45-Utils/09-Change_i2c_addr.py` to change the PiStorms's I2C address
- **touch_sensor_tutorial.py**: The program written in the [PiStorms Python Programming Tutorial](http://www.mindsensors.com/blog/how-to/pistorms-python-programming-tutorial)
- **\*.png, \*.jpg, \*.mp3**: This folder also contains many resources used for the system, browser, and examples programs

### www
- These files power the [PiStorms Web Interface](http://www.mindsensors.com/blog/how-to/how-to-access-pistorms-web-interface)
- **html**: Contains the actual pages you access by web browser
- **web_api**: Handles request when you click buttons to actually *do* things (perform actions) on the PiStorms

### scratch
- Examples files of using Scratch to connect to the PiStorms
- You would use VNC to connect to the Raspberry Pi desktop, then run [00-Scratch_PiStorms](https://github.com/mindsensors/PiStorms/blob/master/programs/00-Scratch_PiStorms.py) on the PiStorms to let it connect with Scratch. The PiStorms will broadcast `READY`, there is no need to click the green flag.
- We have a [programming guide](http://www.mindsensors.com/index.php?controller=attachment&id_attachment=307) and a getting started [blog post](http://www.mindsensors.com/blog/how-to/program-pistorms-with-scratch-getting-started)

### artwork
- Contains the desktop background and mindsensors.com logo
- Also contains the PiStorms case image used when taking screenshots from the web interface

### html
- Documentation, available [online](http://www.mindsensors.com/reference/PiStorms/html/index.html) and updated each new software release

### .gitattributes
- Marks the html and www/html/assets folders as documentation so GitHub recognizes this as a primarily Python project, not HTML and Javascript

### .version
- The version number corresponding with each software release
- Used in the [About Me](https://github.com/mindsensors/PiStorms/blob/master/programs/00-About_Me.py) program to list "s/w version" and in the [web interface](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#www) to display on the dashboard.

### README.md
- Instructions for an end-user to download and setup this project

### CONTRIBUTING.md
- An overview of this repository and explanation of the structure of this project

## Details
Lets walk through what setup.sh does from start to finish, and what happens at boot time. We will also cover every relevant directory on the system.

`MSDriver.sh`, `MSBrowser.sh`, and `MSWeb.sh` will run at boot time. MSDriver handles shutting down the system when GO is held.

The PiStorms has firmware which controls the motor and sensor ports, and which gets input from the touch part of the touchscreen. The Raspberry Pi sends commands over I2C to the PiStorms to tell it what to do. The screen itself communicates via SPI. This means that the screen might work, but you won't be able to tap anything because you can't get touchscreen values from the PiStorms if I2C is broken. The opposite is, therefore, true, too. The screen will not work if SPI is broken, but you could still move motors, etc. if I2C is still functioning.

## Design improvement suggestions
- There are a number of things I would like to better organize or clean up, but most would be difficult due to the requirement of supporting previous systems. Backwards compatibility is the issue.
- For example, the images MSBrowser relies on should not be cluttering up the general programs folder.
- `rmap.py` should be renamed to make its purpose (Scratch) more clear.
- `MsDevices.py` and `mindsensors.py` should be merged.
- The log files should have more meaningful names and be put in `/var/log`, not `/tmp`. Further, `.psm_shutdown.lck` should be in `/var/lock`, not `/tmp`. Note `/var/lock` *is* on a temporary file system, so a reboot will remove any stale locks.

## Original version of repository structure notes
This was found in a file last modified April 5th, 2016, the day before the first commit to this repository. Copied verbatim:

> Folder structure for PiStorms development repo
> <br>
> <br>
> <br>
> <br>
>
> | ​ | ​ |
> | --- | --- |
> | PiStorms | top level folder for everything. |
> | PiStorms/setup | setup/install/config scripts. (some of these scripts will be run at the time of install, and move other scripts to correct folders – such as /etc/init.d, etc) \n pip:setup.py will go here. \n PiStormsBrowser.sh will go here. |
> | PiStorms/sys | library files, etc. (which would get relocated to dist-packages) \n PiStormsBrowser.py/PiStormsDriver.py will go here. |
> | PiStorms/programs | main programs folder. |
> | PiStorms/programs/utils | factory provided utllity programs |
> | PiStorms/programs/examples | factory provided samples & demos. |
> | PiStorms/scratch | the sb files will be here (relocate these to their standard location on Pi). |
> | ​ | ​ |
