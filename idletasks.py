#!/usr/bin/python

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gobject import MainLoop
from os import popen

def start_boinc():
#	popen("nice -n 19 /home/emh/BOINC/boinc -daemon -redirectio -dir /home/emh/BOINC/")
    pass
def stop_boinc():
#	popen("killall -SIGHUP boinc")
    pass

def idle_pidgin():
	# purple-remote mojo
	pass

def cpu_slowdown():
	popen('sudo sh -c "echo powersave > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')

def cpu_speedup():
	popen('sudo sh -c "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')

def start_tasks():
#	start_boinc()
	idle_pidgin()
	cpu_slowdown()

def stop_tasks():
#	stop_boinc()
	cpu_speedup()


def idlechange_handler(sender=None):
	if sender:
		print "just went idle, starting tasks"
		start_tasks()
	else:
		print "just went unidle, stopping tasks"
		stop_tasks()


dbus_loop = DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus(mainloop=dbus_loop)

bus.add_signal_receiver(idlechange_handler, "ActiveChanged", "org.gnome.ScreenSaver")

mainloop = MainLoop()
mainloop.run()
