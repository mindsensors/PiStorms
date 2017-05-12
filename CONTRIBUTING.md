# PiStorms

## setup

## sys
### Suggestions
- When developing, hard link the source files from `/home/pi/PiStorms/...` to their destinations from `setup.sh`
```bash
# note: section in progress
stat {/home/pi/sys,/usr/local/lib/python2.7/dist-packages}/PiStorms.py
find /usr/local/lib/python2.7/dist-packages -samefile /home/pi/PiStorms/sys/PiStorms.py
```

## programs

## www

## scratch
- Examples files of using Scratch to connect to the PiStorms
- You would use VNC to connect to the Raspberry Pi desktop, then run [00-Scratch_PiStorms](https://github.com/mindsensors/PiStorms/blob/master/programs/00-Scratch_PiStorms.py) on the PiStorms to let it connect with Scratch. The PiStorms will broadcast `READY`, there is no need to click the green flag.
- We have a [programming guide](http://www.mindsensors.com/index.php?controller=attachment&id_attachment=307) and a getting started [blog post](http://www.mindsensors.com/blog/how-to/program-pistorms-with-scratch-getting-started)

## artwork
- Contains the desktop background and mindsensors.com logo
- Also contains the PiStorms case image used when taking screenshots from the web interface

## html
- Documentation, available [online](http://www.mindsensors.com/reference/PiStorms/html/index.html) and updated each new software release

## .gitattributes
- Marks the www/html/assets folder as documentation so GitHub recognizes this as a primarily Python project, not HTML and Javascript

## .version
- The version number corresponding with each software release
- Used in the [About Me](https://github.com/mindsensors/PiStorms/blob/master/programs/00-About_Me.py) program to list "s/w version" and in the [web interface](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#www) to display on the dashboard.

## README.md
- Instructions for an end-user to download and setup this project

## CONTRIBUTING.md
- An overview of this repository and explanation of the structure of this project
