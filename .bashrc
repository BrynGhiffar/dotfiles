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
PATH=$PATH:~/.local/scripts
alias cp_last_obs='cp ~/obs_recordings/$(ls ~/obs_recordings -t | head -n 1)'

ffmgif() {
  local input output
  
  while [[ ${1} ]]; do
    case "${1}" in
      -i)
        input=${2}
        shift
        ;;
      -o)
        output=${2}
        shift
        ;;
      *)
        echo "Error: Unknown parameter: ${1}" >&2
        return 1
    esac

    if ! shift; then
      echo "Missing parameter argument." >&2
      return 1
    fi
  done
  
  if [[ -z "$input" ]]; then
    echo "Error: input file is not specified" >&2
    return 1
  fi

  if [[ -z "$output" ]]; then
    echo "Error: output file is not specified" >&2
    return 1
  fi

  ffmpeg -i "$input" -r 15 -vf "split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" "$output"
}
# Use setcap for setting port access permission to files
# sudo setcap cap_net_bind_service=+ep `readlink -f \`which node\``
neofetch
