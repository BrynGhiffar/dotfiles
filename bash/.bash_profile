#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ "$(tty)" = "/dev/tty1" ]]; then
  if [[ $(hostname) == *"laptop"* ]]; then
    pgrep qtile || startx /home/brynghiffar/.xinitrc
  else
    pgrep qtile || startx /home/bryn/.xinitrc
  fi
  xset s off
  xset -dpms
  # Hyprland
fi
