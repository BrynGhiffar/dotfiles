# PS1='[\u@\h \W]\$ '
GREEN="\[$(tput setaf 2)\]"
RESET="\[$(tput sgr0)\]"
# PS1="\u:\w (\t)\n${GREEN}\$${RESET} "

# GIT_PS1_SHOWUNTRACKEDFILES=1
GIT_PS1_SHOWDIRTYSTATE=1

GREEN_ARROW="${GREEN}=>${RESET} "
PS1='󰛡 \u@\h:\w (\t)'
PS1+=' $(__git_ps1 "'
PS1+="${GREEN}[ %s]${RESET}"
PS1+='")'
PS1+="\n$GREEN_ARROW"
#PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '
