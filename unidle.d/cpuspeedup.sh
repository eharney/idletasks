#!/bin/sh

# Requires proper sudo configuration

sudo sh -c "echo ondemand > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

sudo sh -c "echo 20 > /sys/devices/system/cpu/cpu0/cpufreq/ondemand/up_threshold"

sudo sh -c "echo ondemand > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"

sudo sh -c "echo 20 > /sys/devices/system/cpu/cpu1/cpufreq/ondemand/up_threshold"

