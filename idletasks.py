#!/usr/bin/python

# This script is more of an experiment than anything, but it does function.

# To use this:
# 1. Put scripts to run when the system becomes idle in ~/.idletasks/idle.d
#    Put scripts to run when the system becomes unidle in ~/.idletasks/unidle.d
# 2. Configure your desktop environment to run this script when you log in.

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gobject import MainLoop
import os
from os import popen
import glob

def idle_d_tasks():
	idle_path = os.path.expanduser('~/.idletasks/idle.d/')
	for task in glob.glob(idle_path + '*'):
		print "run",
		print task
		popen(task)

def unidle_d_tasks():
	unidle_path = os.path.expanduser('~/.idletasks/unidle.d/')
	for task in glob.glob(unidle_path + '*'):
		print "run",
		print task
		popen(task)

def start_tasks():
	idle_d_tasks()

def stop_tasks():
	unidle_d_tasks()

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
