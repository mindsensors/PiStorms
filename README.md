# PiStorms

To install and run this repo on your Pi,<br>

1) Install latest Raspbian image on a SD Card (use SD Card with 8 GB or more).<br>
2) Insert this SD card in your Raspberry Pi, affix Raspberry Pi on PiStorms frame and attach PiStorms to Raspberry Pi <br>
   for details of assembly instructions, visit: http://www.mindsensors.com/content/72-getting-started-with-pistorms<br>
3) Start your Raspberry Pi and login to your Pi as user 'pi'.<br>
4) Run raspi-config and 'expand the file system'<br>
5) Configure your Pi to connect to Internet (using wired ethernet or wifi)<br>
   to learn how to do this, visit: http://www.mindsensors.com/blog/how-to/connecting-raspberry-pi-to-wifi<br>
6) Download and configure this repo on your Pi with following commands<br>
<br>
<pre>
   $ git clone https://github.com/mindsensors/PiStorms.git
   $ cd PiStorms/setup
   $ chmod +x setup.sh
   $ ./setup.sh
</pre>

setup.sh will take several minutes to download files, and configure<br>
When it configures VNC server, it would ask for password, please provide a password that you will remember (e.g. raspberry).<br>Later, you would use this password to login to your Pi from a VNC client.
<br>
<br>
As a next step, follow the examples from PiStorms/programs folder. 

To write your own programs, start with a tutorial here: http://www.mindsensors.com/blog/how-to/pistorms-python-programming-tutorial
and then refer to online API reference here: http://www.mindsensors.com/reference/PiStorms/html/
