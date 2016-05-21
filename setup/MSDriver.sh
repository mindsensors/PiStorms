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

show_logo() {
  if [ -f /usr/local/mindsensors/conf/msdev.cfg ]
  then
      homefolder=`grep homefolder /usr/local/mindsensors/conf/msdev.cfg | cut -d"=" -f2`
  else
    echo "config file is missing"
    homefolder=/home/pi/PiStorms
  fi
  python $homefolder/programs/tests/img-to-screen.py 0 0 320 240 /usr/local/mindsensors/images/ms-logo-w320-h240.png

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
  stop)
    show_logo
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
