#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ "$(tty)" = "/dev/tty1" ]]; then
  if [[ $(hostname) == *"laptop"* ]]; then
    pgrep qtile || startx /home/brynghiffar/.xinitrc
    . "$HOME/.cargo/env"
  # else
    # pgrep qtile || startx /home/bryn/.xinitrc
  fi
  xset s off
  xset -dpms
  # Hyprland
fi

if [[ $(hostname) == "archdesktop" ]]; then
  # Created by `pipx` on 2024-05-22 04:54:36
  export PATH="$PATH:/home/bryn/.local/bin"
fi
