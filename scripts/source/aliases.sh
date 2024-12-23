alias ls='ls --color=auto'
alias ll='ls -laS'
alias tt='tree -L 2'
alias grep='grep --color=auto'
alias qtile-logs='less +G ~/.local/share/qtile/qtile.log'
alias vim='nvim'
alias config='ranger /home/bryn/arch-config'

# Desktop crashes for some reason if I don't put this
# as the kernel parameters.
# GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet splash pci=assign-busses apicmaintimer idle=poll reboot=cold,hard"
alias grub_config="$EDITOR /etc/default/grub"

# For generating grub bootloader configuration
alias grub_genconfig="grub-mkconfig -o /boot/grub/grub.cfg"

alias rr=". ranger"
alias cp_last_obs='cp ~/obs_recordings/$(ls ~/obs_recordings -t | head -n 1)'
alias q='QHOME=~/q rlwrap -r ~/q/l64/q'

alias disk-usage='sudo ncdu / --exclude /mnt'
