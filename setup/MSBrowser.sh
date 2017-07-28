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
    if [ -f /var/lock/msbrowser ]
    then
        echo "MSBrowser already running."
        exit 4
    fi

    if [ -f /usr/local/mindsensors/conf/msdev.cfg ]
    then
        homefolder=`grep homefolder /usr/local/mindsensors/conf/msdev.cfg | cut -d"=" -f2`
    else
        homefolder=/home/pi/PiStorms
    fi
    python $homefolder/programs/utils/msg-to-screen.py "Loading PiStorms" "Please wait"

    #
    # query the hardware for its version
    chmod a+rw /dev/i2c* > /dev/null 2>&1
    sudo python $homefolder/programs/utils/print-hw-version.py >/var/tmp/.hw_version

    # do not delete the json, as it may have user's choice about updates.
    #sudo rm -f /var/tmp/ps_versions.json
    #
    # start the browser
    sudo python /usr/local/bin/MSBrowser.py $homefolder/programs >/var/tmp/psmb.out 2>&1 &
    sleep 1
    sudo python /usr/local/bin/ps_messenger_check.py >> /var/tmp/ps_m 2>&1
    sleep 1
    sudo python /usr/local/bin/ps_updater.py >> /var/tmp/ps_u 2>&1
    sleep 1
    #
    # run diagnostics
    sudo /usr/local/bin/pistorms-diag.sh > /var/tmp/psm-diag.txt 2>&1
    cp /var/tmp/psm-diag.txt /boot
    sleep 1
}

do_status () {
    return 0
}

case "$1" in
  start|"")
    do_start
    ;;
  restart|reload|force-reload)
    sudo kill -9 `ps -ef | grep MSBrowser.py |grep -v grep| cut -c11-16`
    rm -f /var/lock/msbrowser
    rm -f /var/lock/ili9341
    do_start
    exit 3
    ;;
  stop)
    sudo kill -9 `ps -ef | grep MSBrowser.py |grep -v grep| cut -c11-16`
    rm -f /var/lock/msbrowser
    rm -f /var/lock/ili9341
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
