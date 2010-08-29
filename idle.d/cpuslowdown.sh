#!/bin/sh

# Requires proper sudo configuration

sudo sh -c "echo powersave > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

sudo sh -c "echo powersave > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"
