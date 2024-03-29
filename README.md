# dotfiles

## Table

| What For | Tool | Config |
| -------- | ---- | ------ |
| Hardware | Macbook Pro 2020 w/ Arm M1 16Gb | [neofetch](neofetch) |
| OS | macOS [12.6] | [neofetch](neofetch) |
| Window Manager | [Magnet](https://magnet.crowdcafe.com) ||
| Terminal | [iTerm2](https://iterm2.com) | [iterm](iterm) |
| Shell | zsh w/ [oh-my-zsh](https://ohmyz.sh) (plugins) | [zshrc](zshrc) |
| Packages | [brew](https://brew.sh) | [Brewfile](Brewfile) |
| File Manager | [nnn](https://github.com/jarun/nnn), [lsd](https://github.com/Peltoche/lsd), [bat](https://github.com/sharkdp/bat) | [*rc lines](zshrc) |
| Search | [fzf](https://github.com/junegunn/fzf), [ripgrep](https://github.com/BurntSushi/ripgrep) ||
| VCS | git, [difftastic](https://github.com/Wilfred/difftastic), [lazygit](https://github.com/jesseduffield/lazygit) | [gitconfig](gitconfig) |
| Session Manager | tmux | [.tmux by @gpakosz](https://github.com/gpakosz/.tmux) |
| SSH | autossh, [rclone](https://rclone.org) | [sshconfig](sshconfig) |
| Monitoring | [neofetch](https://github.com/dylanaraps/neofetch), [htop](https://github.com/htop-dev/htop), [glances](https://github.com/nicolargo/glances), [ncdu](https://dev.yorhel.nl/ncdu), [speedtest](https://github.com/sivel/speedtest-cli), [duf](https://github.com/muesli/duf) ||
| Editor | [vim](https://www.vim.org) | [vimrc by @amix](https://github.com/amix/vimrc) |
| IDE | [JetBrains](https://www.jetbrains.com), [VSCODE](https://code.visualstudio.com) | [vscode](vscode) |
| Python | [miniconda](https://docs.conda.io/en/latest/miniconda.html) ||
| Markdown | [MacDown](https://github.com/MacDownApp/macdown) ||
| Docs | [tldr](https://github.com/tldr-pages/tldr), [Dash](https://kapeli.com/dash) ||
| Font | [Source Code Pro](https://github.com/sb2nov/mac-setup/issues/218), [Hard Nerd Font](https://github.com/ryanoasis/nerd-fonts) ||
| Video | [mpv](https://github.com/mpv-player/mpv), [youtube-dl](https://github.com/ytdl-org/youtube-dl) ||
| VPN | [Outline](https://getoutline.org) ||
| Network Blocker | `/etc/hosts 0.0.0.0 trick`, [AdGuard](https://adguard.com), `SafeSearchs` ||

## Settings

<details>
<summary>MacOS</summary>

* Swap `<C-Space>` and `<Cmd-Space>` for Sportlight/Language keyboard shortcuts.
* Switch on `<Fn>` for emoji choosing. 
* Switch off text autocomplete and capitalizing.
* Maximize keyboard repeat speed and minimize delay.
* "App Expose" 3 fingers for TrackPad
* "Do Not Disturb" auto setting
* Mission Control apps grouping and switch off separate spaces for displays.

</details>

<details>
<summary>Safari</summary>

* Switch off automatic files opening after download.

</details>

<details>
<summary>JetBrains</summary>

* "Keymap" profile is per-device base.
* "Code Style" and "Inspections" is per-project base.
* Other stuff, including "Theme", is synced through account.
* Enable Python inspections: all major and docstrings.

</details>

## Dev

```bash
pre-commit install
pre-commit run --all-files
```

## Licence

[MIT](LICENSE)

