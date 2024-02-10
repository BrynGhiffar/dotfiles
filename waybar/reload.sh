#!/usr/bin/bash

killall waybar
nohup waybar >/dev/null 2>&1 &
