#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export SEM_WORKSTATION=100.125.155.125
export EDITOR='nvim'
export VISUAL='nvim'

if [[ $(hostname) == "archdesktop" ]]; then
  # Ask gpg from the terminal
  export GPG_TTY=$(tty)
  # export GPG_AGENT_INFO=""
  export QLIC=/home/bryn/q/kc.lic

  # Created by `pipx` on 2024-05-22 04:54:36
  export PATH="$PATH:/home/bryn/.local/bin"

  export CC="/usr/bin/clang"
  export CXX="/usr/bin/clang++"
fi

# nvm configuration
source /usr/share/nvm/init-nvm.sh
source ~/.local/scripts/source/ffmgif.sh
source ~/.local/scripts/source/path.sh
source ~/.local/scripts/source/git-prompt.sh
source ~/.local/scripts/source/bash-prompt.sh
source ~/.local/scripts/source/aliases.sh

# Use setcap for setting port access permission to files
# sudo setcap cap_net_bind_service=+ep `readlink -f \`which node\``
eval $(keychain --eval --quiet id_ed25519)
