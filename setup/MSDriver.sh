#!/bin/sh
### BEGIN INIT INFO
# Provides:          MSDriver
# Required-Start:    hostname $local_fs
# Required-Stop:
# Should-Start:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop MSDriver
# Description:       This script starts/stops MSDriver.
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin
#. /lib/init/vars.sh

psm_shutdown() {
  if [ -f /usr/local/mindsensors/conf/msdev.cfg ]
  then
      homefolder=`grep homefolder /usr/local/mindsensors/conf/msdev.cfg | cut -d"=" -f2`
  else
    echo "config file is missing"
    homefolder=/home/pi/PiStorms
  fi
  python $homefolder/programs/utils/psm_shutdown.py

}

show_logo() {
  if [ -f /usr/local/mindsensors/conf/msdev.cfg ]
  then
      homefolder=`grep homefolder /usr/local/mindsensors/conf/msdev.cfg | cut -d"=" -f2`
  else
    echo "config file is missing"
    homefolder=/home/pi/PiStorms
  fi
  python $homefolder/programs/utils/img-to-screen.py 0 0 320 240 /usr/local/mindsensors/images/ms-logo-w320-h240.png

}

do_start () {
    #show_logo
	sleep 1
	sudo python /usr/local/bin/MSDriver.py >/var/tmp/psmd.out 2>&1 &
    chmod a+rw /dev/i2c* > /dev/null 2>&1
	sleep 1
}

do_status() {
    ps -ef | grep MSDriver.py | grep -v grep
    return $?
}

case "$1" in
  start|"")
	do_start
	;;
  restart|reload|force-reload)
	sudo kill -9 `ps -ef | grep MSDriver.py |grep -v grep| cut -c11-16`
    do_start
	exit 3
	;;
  stop_old)
    show_logo

    lckfile=/tmp/.psm_shutdown.lck
    line=`cat $lckfile|tr -d [:space:]`
    if [ x$line = xhalt ]
    then
      cp /dev/null $lckfile
      rm -f $lckfile
      psm_shutdown
    fi
	;;
  stop)
    show_logo
    SHUTDOWN=3
    REBOOT=3
    HALT=3
    POWEROFF=3
    systemctl list-jobs | egrep -q 'shutdown.target.*start' && SHUTDOWN=1 || SHUTDOWN=0
    systemctl list-jobs | egrep -q 'reboot.target.*start' && REBOOT=1 || REBOOT=0
    systemctl list-jobs | egrep -q 'halt.target.*start' && HALT=1 || HALT=0
    systemctl list-jobs | egrep -q 'poweroff.target.*start' && POWEROFF=1 || POWEROFF=0
    #Only power off PiStorms if Raspberry Pi is being shutdown (and not reboot)
	if [ $SHUTDOWN -eq 1 ]
	then
		if [ $REBOOT -eq 1 ]
		then
		    echo "in reboot mode...."
		else
		    echo "in poweroff or halt mode...."
		      echo "Shutting down SmartUPS"
              psm_shutdown
		fi
	else
		echo "in starting mode... "
	fi
	;;
  status)
    do_status
	;;
  *)
	echo "Usage: MSDriver [start|stop|status|restart]" >&2
	exit 3
	;;
esac

:
