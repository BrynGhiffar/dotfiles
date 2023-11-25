#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
# PS1='[\u@\h \W]\$ '
GREEN="\[$(tput setaf 2)\]"
RESET="\[$(tput sgr0)\]"
# PS1="\u:\w (\t)\n${GREEN}\$${RESET} "
PS1="\u:\w (\t)\n${GREEN}=>${RESET} "
