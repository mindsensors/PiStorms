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

## artwork

## .gitattributes
- Marks the www/html/assets folder as documentation so GitHub recognizes this as a primarily Python project, not HTML and Javascript

## .version
- The version number corresponding with each software release
- Used in the [About Me](https://github.com/mindsensors/PiStorms/blob/master/programs/00-About_Me.py) program to list "s/w version" and in the [web interface](https://github.com/mindsensors/PiStorms/blob/master/CONTRIBUTING.md#www) to display on the dashboard.

## README.md
- Instructions for an end-user to download and setup this project

## CONTRIBUTING.md
- An overview of this repository and explanation of the structure of this project
