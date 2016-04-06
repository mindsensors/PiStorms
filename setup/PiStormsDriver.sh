#!/bin/sh
### BEGIN INIT INFO
# Provides:          PiStormsDriver
# Required-Start:    hostname $local_fs
# Required-Stop:
# Should-Start:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop PiStormsDriver
# Description:       This script starts/stops PiStormsDriver.
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin
. /lib/init/vars.sh

do_start () {
	sudo python /usr/local/bin/PiStormsDriver.py >/var/tmp/psmd.out 2>&1 &
    chmod a+rw /dev/i2c* > /dev/null 2>&1
	sleep 2
}

do_status () {
	#if [ -e /dev/servoblaster ] ; then
	#	return 0
	#else
	#	return 4
	#fi
    return 0
}

case "$1" in
  start|"")
	do_start
	;;
  restart|reload|force-reload)
	sudo kill -9 `ps -ef | grep PiStormsDriver.py |grep -v grep| cut -c11-16`
    do_start
	exit 3
	;;
  stop)
    # do not stop the driver.
	;;
  status)
	do_status
	exit $?
	;;
  *)
	echo "Usage: PiStormsDriver [start|stop|status|restart]" >&2
	exit 3
	;;
esac

:
