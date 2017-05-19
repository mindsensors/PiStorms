# PiStorms

The [PiStorms](http://www.mindsensors.com/content/78-pistorms-lego-interface) is a robotics platform. It enables you to create robots using LEGO Mindstorms parts, and control it on a Raspberry Pi with Python. Besides its 4 motor ports, 4 sensor ports, and all the benefits of the Raspberry Pi, the PiStorms lets you do even more. It has a touchscreen for easy visual feedback and touch input. It has a convenient web interface to program and control the device, even accessible on mobile devices.

This document will introduce you to the repository's structure and how the PiStorms functions overall.


## Platform structure

### MSBrowser
- This is the program the end-user will use to launch Python programs on the PiStorms
- Each page displays four items (files and folders). Left and right arrows in the top corner allow for page navigation.
- Tapping a folder will open it, and the leftmost page will have an up arrow to close it and go back
- The hostname appears in cyan at the top, and a battery indicator is shown in the bottom-right

### Screenshots

### Log files and diagnostics


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
```

### sys

### programs
- This folder is what the user will see on the PiStorms screen (through the [browser program](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#MSBrowser))
- **00-About_Me**: A useful diagnostics program that displays useful information about the device. This includes the device name, firmware and software versions, hostname, battery level, and IP addresses for Ethernet and WiFi.
- **00-Scratch_PiStorms**: Used to connect with [Scratch](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#scratch) and execute instructions from it.
- **00-TestInternetConnection**: Pings Google's domain name server to determine if the device is connected to the internet.
- **00-WiFi_Setup**: Used to connect to the internet directly from the PiStorms. It displays a list of scanned WiFi networks and will let you enter a passphrase using an on-screen keyboard.
- **03-Swarm_Demo**: ?
- **09-refresh**: If anything changes in the programs folder, they will not be reflected in the browser until it is refreshed. Another way to achieve this is to enter and exit any folder. A program might have been created or renamed from the web interface (or an SSH session).
- **09-shutdown**: Let's you shutdown the PiStorms from the device itself. It will display a confirmation before shutting down. Note there is also a shutdown (and restart) button on the PiStorms Web Interface dashboard. Also note holding the GO button for five seconds will restart the PiStorms.

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
- Marks the www/html/assets folder as documentation so GitHub recognizes this as a primarily Python project, not HTML and Javascript

### .version
- The version number corresponding with each software release
- Used in the [About Me](https://github.com/mindsensors/PiStorms/blob/master/programs/00-About_Me.py) program to list "s/w version" and in the [web interface](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#www) to display on the dashboard.

### README.md
- Instructions for an end-user to download and setup this project

### CONTRIBUTING.md
- An overview of this repository and explanation of the structure of this project
