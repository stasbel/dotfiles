# brew
export HOMEBREW_BREW_GIT_REMOTE="$HOME/.brew-cache/brew"
export HOMEBREW_CORE_GIT_REMOTE="$HOME/.brew-cache/homebrew-core"
eval "$(/opt/homebrew/bin/brew shellenv)"

# zsh with oh-my-zsh
export ZSH="$HOME/.oh-my-zsh"
export ZSH_THEME="sorin"
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  zsh-completions
  zsh-vim-mode
  docker
  docker-compose
  autoenv
)
# zsh completitions from brew
# https://docs.brew.sh/Shell-Completion
FPATH="$(brew --prefix)/share/zsh/site-functions:${FPATH}"
autoload -U compinit && compinit
source $ZSH/oh-my-zsh.sh

# basics
export LANG=en_US.UTF-8
export EDITOR=vim
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
export TERM=xterm-256color
export HISTSIZE=100000
export HISTFILESIZE=1000000

# vi mode (mostly handled by zsh-vim-mode)
export KEYTIMEOUT=1
setopt PROMPT_SUBST
export RPS1='${MODE_INDICATOR_PROMPT}'${RPS1}

# iTerm2
test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

# nnn
nnn ()
{
    # Block nesting of nnn in subshells.
    if [ -n $NNNLVL ] && [ "${NNNLVL:-0}" -ge 1 ]; then
        echo "nnn is already running"
        return
    fi

    # Add `export` to cd-on-quit every time.
    NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"

    command nnn -e "$@"

    if [ -f "$NNN_TMPFILE" ]; then
        . "$NNN_TMPFILE"
        rm -f "$NNN_TMPFILE" > /dev/null
    fi
}

# lsd
alias ls='lsd'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree'

# fzf
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$($HOME'/.miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$HOME/.miniconda3/etc/profile.d/conda.sh" ]; then
        . "$HOME/.miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="$HOME/.miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
# Removing `conda` bin files so `brew` doesn't get us any warnings.
# brew () {
#     old_path=$PATH
#     export PATH=$(echo $PATH | sed -e "s;:$CONDA_PREFIX/bin;;" -e "s;$CONDA_PREFIX/bin:;;")
#     command brew "$@"
#     export PATH=$old_path
# }

# youtube-dl
alias ydl='youtube-dl'

# dotfiles
export DOTFILES=$HOME/.dotfiles
export PATH=$PATH:$DOTFILES/bin

# nltk
export NLTK_DATA="$HOME/.nltk"

# go
export GOPATH="$HOME/.go"

# gcloud
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.ssh/gcloud.json"
source "$(brew --prefix)/share/google-cloud-sdk/path.zsh.inc"
source "$(brew --prefix)/share/google-cloud-sdk/completion.zsh.inc"

# secrets (APIs, etc.)
. $HOME/.secretsrc

# autoenv
AUTOENV_ENABLE_LEAVE=True

