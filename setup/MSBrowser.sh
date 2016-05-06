#!/bin/sh
### BEGIN INIT INFO
# Provides:          MSBrowser
# Required-Start:    hostname $local_fs
# Required-Stop:
# Should-Start:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop MSBrowser
# Description:       This script starts/stops MSBrowser.
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin
. /lib/init/vars.sh

do_start () {
    sudo /usr/local/bin/pistorms-diag.sh > /var/tmp/psm-diag.txt
    cp /var/tmp/psm-diag.txt /boot
	sudo python /home/pi/PiStorms/programs/tests/print-hw-version.py >/var/tmp/.hw_version
    sudo python /usr/local/bin/ps_updater.py
    sudo python /usr/local/bin/MSBrowser.py /home/pi/PiStorms/programs >/var/tmp/psmb.out 2>&1 &
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
	sudo kill -9 `ps -ef | grep MSBrowser.py |grep -v grep| cut -c11-16`
    do_start
	exit 3
	;;
  stop)
	sudo kill -9 `ps -ef | grep MSBrowser.py |grep -v grep| cut -c11-16`
	;;
  status)
	do_status
	exit $?
	;;
  *)
	echo "Usage: MSBrowser [start|stop|status|restart]" >&2
	exit 3
	;;
esac

:
