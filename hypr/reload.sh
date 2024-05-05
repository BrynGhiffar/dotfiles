#!/bin/bash

killall waybar
waybar &
hyperctl reload
killall hyprpaper
hyprpaper
