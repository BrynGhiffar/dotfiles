#!/bin/sh

/usr/bin/pipewire &
/usr/bin/pipewire-pulse &
/usr/bin/pipewire-media-session &

# Starting discord minimized
# exec --no-startup-id discord --start-minimized
nitrogen --restore
picom &
# So that dunst can start without a display manager
systemctl --user import-environment DISPLAY
exec qtile start
