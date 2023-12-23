#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias ll='ls -laS'
alias tt='tree -L 2'
alias grep='grep --color=auto'
# PS1='[\u@\h \W]\$ '
GREEN="\[$(tput setaf 2)\]"
RESET="\[$(tput sgr0)\]"
# PS1="\u:\w (\t)\n${GREEN}\$${RESET} "
PS1="\u:\w (\t)\n${GREEN}=>${RESET} "
export SEM_WORKSTATION=100.125.155.125
alias qtile-logs='less +G ~/.local/share/qtile/qtile.log'
alias vim='nvim'
alias config='ranger /home/bryn/arch-config'
export EDITOR='nvim'
export VISUAL='nvim'

# Desktop crashes for some reason if I don't put this
# as the kernel parameters.
# GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet splash pci=assign-busses apicmaintimer idle=poll reboot=cold,hard"
alias grub_config="$EDITOR /etc/default/grub"

# For generating grub bootloader configuration
alias grub_genconfig="grub-mkconfig -o /boot/grub/grub.cfg"

# nvm configuration
source /usr/share/nvm/init-nvm.sh

# pyenv configurations
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

alias rr=". ranger"
# Use setcap for setting port access permission to files
# sudo setcap cap_net_bind_service=+ep `readlink -f \`which node\``
neofetch
