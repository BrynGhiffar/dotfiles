#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
export EDITOR='nvim'
export VISUAL='nvim'
export FZF_DEFAULT_OPTS="--reverse --prompt ' ' --color=prompt:#19cb00,marker:#19cb00,pointer:#19cb00 --pointer ''"

if [[ $(hostname) == "home" ]]; then
  # Ask gpg from the terminal
  export GPG_TTY=$(tty)
  # export GPG_AGENT_INFO=""
  export QLIC=/home/bryn/q/kdb_plus

  # Created by `pipx` on 2024-05-22 04:54:36
  export PATH="$PATH:/home/bryn/.local/bin:/home/bryn/.cargo/bin"

  export CC="/usr/bin/clang"
  export CXX="/usr/bin/clang++"

  shopt -s histappend
  export PROMPT_COMMAND='history -a'

  # The next line updates PATH for the Google Cloud SDK.
  if [ -f '/home/bryn/Downloads/gcloud/google-cloud-sdk/path.bash.inc' ]; then . '/home/bryn/Downloads/gcloud/google-cloud-sdk/path.bash.inc'; fi

  # The next line enables shell command completion for gcloud.
  if [ -f '/home/bryn/Downloads/gcloud/google-cloud-sdk/completion.bash.inc' ]; then . '/home/bryn/Downloads/gcloud/google-cloud-sdk/completion.bash.inc'; fi
fi


if [[ $(hostname) == "archlaptop" ]]; then
  . "$HOME/.cargo/env"
  # The next line updates PATH for the Google Cloud SDK.
  if [ -f '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/path.bash.inc' ]; 
    then . '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/path.bash.inc';
  fi

  # The next line enables shell command completion for gcloud.
  if [ -f '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/completion.bash.inc' ];
    then . '/home/brynghiffar/projects/google-cloud-cli/google-cloud-sdk/completion.bash.inc';
  fi

fi

# nvm configuration
source /usr/share/nvm/init-nvm.sh

source ~/.local/scripts/source/ffmgif.sh
source ~/.local/scripts/source/path.sh
source ~/.local/scripts/source/git-prompt.sh
source ~/.local/scripts/source/bash-prompt.sh
source ~/.local/scripts/source/aliases.sh

# Bitwyre aliases
source ~/projects/work/bitwyre/env/activate.sh

# Use setcap for setting port access permission to files
# sudo setcap cap_net_bind_service=+ep `readlink -f \`which node\``
eval $(keychain --eval --quiet id_ed25519)

# Set repeat rate
# xset r rate 300 40

function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}
