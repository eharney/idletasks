#!/usr/bin/python

# This script is more of an experiment than anything, but it does function.

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
	# Lock CPUs to lowest possible speed
	popen('sudo sh -c "echo powersave > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')
	popen('sudo sh -c "echo powersave > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"')

def cpu_speedup():
	# Set CPUs for ondemand scheduler
	popen('sudo sh -c "echo ondemand > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')
	popen('sudo sh -c "echo 20 > /sys/devices/system/cpu/cpu0/cpufreq/ondemand/up_threshold"')
	popen('sudo sh -c "echo ondemand > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"')
	popen('sudo sh -c "echo 20 > /sys/devices/system/cpu/cpu1/cpufreq/ondemand/up_threshold"')

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
