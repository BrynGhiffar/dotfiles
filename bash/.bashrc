#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export SEM_WORKSTATION=100.125.155.125
export EDITOR='nvim'
export VISUAL='nvim'

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
# neofetch
. "$HOME/.cargo/env"

if [[ $(hostname) == "archlaptop" ]]; then

  # The next line updates PATH for the Google Cloud SDK.
  if [ -f '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/path.bash.inc' ]; 
    then . '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/path.bash.inc';
  fi

  # The next line enables shell command completion for gcloud.
  if [ -f '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/completion.bash.inc' ];
    then . '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/completion.bash.inc';
  fi

fi
