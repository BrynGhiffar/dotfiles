#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ "$(tty)" = "/dev/tty1" ]]; then
	pgrep qtile || startx /home/bryn/.xinitrc
  xset s off
  xset -dpms
  # Hyprland
fi
