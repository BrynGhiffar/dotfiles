autoload -U colors
colors

autoload -Uz vcs_info
# Add the info to the right prompt to avoid complex PS1
# You can also use $PROMPT_SUBST to enable variable substitution inside PROMPT/RPROMPT
setopt prompt_subst

# Define how the Git info should look
zstyle ':vcs_info:*' formats ' %F{green}%B[ %b]%f' # %B for bold, %b to end bold
zstyle ':vcs_info:*' actionformats ' %F{yellow}%B[ %b|%a]%f'
zstyle ':vcs_info:*' check-for-changes true

# Function to pull in the git info before the prompt
precmd() {
  vcs_info
}

# The main prompt (PS1)
GREEN="%{$(tput setaf 2)%}"
RESET="%{$(tput sgr0)%}"
GREEN_ARROW="${GREEN}${RESET} "

# %n=username, %m=hostname, %~=current directory, %*=time
# ${vcs_info_msg_0_} is the variable where vcs_info places the formatted git string
NEWLINE=$'\n'
PROMPT='bryn@work:%~ (%*) ${vcs_info_msg_0_}'
PROMPT+="$NEWLINE$GREEN_ARROW"
