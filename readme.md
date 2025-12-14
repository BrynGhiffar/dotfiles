
<div align="center">
    <h1>
        ✨ Dotfiles
    </h1>
    <p></p>
</div>
<div align="center">
    <a href="https://github.com/hyprwm/Hyprland"><img src="https://img.shields.io/badge/WM-Hyprland-272E48?style=for-the-badge&logo=i3&logoColor=fff"></a>
    <a href="https://github.com/neovim/neovim"><img src="https://img.shields.io/badge/Editor-Nvim-272E48?style=for-the-badge&logo=neovim&logoColor=white"></a>
</div>

https://github.com/user-attachments/assets/feee7e33-d5e7-4954-9286-d4d1a32dbae7

![Desktop](/screenshots/desktop_image.png)

## 👨🏻‍💻 Stack

This repo hosts a lot of configuration that I have used in the past. Currently I am using:

### 💻 Window Manager: [Hyprland](https://github.com/hyprwm/Hyprland)
> Fast, responsive, cool transparency blur effects built-in and awesome configurable animations.

### 🚀 Status Bar: [Waybar](https://github.com/Alexays/Waybar)
> Works well with hyprland, customizable using a css-like config file.

### ⬛ Terminal Emulator: [Kitty](https://github.com/kovidgoyal/kitty)
> Can render images, supports ligatures, feels fast.

### 📝 Text Editor: [Nvim](https://github.com/neovim/neovim)
> Great plugin ecosystem.

### 🐚 Shell: [Nushell](https://github.com/nushell/nushell)
> Trying it out, because it seemed like an interesting idea.

### 🎨 Theming: [Matugen](https://github.com/InioX/matugen)
> Matugen for deriving color palettes, only used with waybar, works with AWW.

### ✨ Wallpaper: [AWWW](https://codeberg.org/LGFae/awww)
> Awesome animations when switching wallpapers.

## 📜 Scripts

### Fzf App Switcher

```bash
#!/usr/bin/bash

# Silence all stdout, disable this for debugging
exec > /dev/null 2>&1

export FZF_DEFAULT_OPTS="--reverse --prompt ' ' --color=prompt:#19cb00,marker:#19cb00,pointer:#19cb00 --pointer ''"
find /usr/share/applications ~/.local/share/applications -name '*.desktop' \
	| xargs -I {} basename {} .desktop \
	| fzf \
	| xargs -I {} setsid nohup gtk-launch {}
```
Works by querying desktop files in the `~/.local/share/applications` directory. I usually have it binded to `Super + Space`.

### Custom Theme/Wallpaper Switcher with Kitty & Fzf

```bash
#!/usr/bin/bash

image=$(find \
	~/dotfiles/wallpapers \
	/usr/share/backgrounds/archlinux \
	-type f \( \
		-iname "*.jpg" \
		-o -iname "*.jpeg" \
		-o -iname "*.png" \) \
	| fzf --preview='kitty icat --clear --transfer-mode=memory --stdin=no --place=${FZF_PREVIEW_COLUMNS}x${FZF_PREVIEW_LINES}@0x0 {}')

if [ -z "$image" ]; then
	exit 0;
fi

matugen image "$image"
sleep 1 # Doesn't work if I remove this for some reason

```

Enumerates all wallpapers in the specified directories and uses matugen to setup the color palette and change the wallpaper.

## 🚀 Installation & Setup

### Prerequisites

Make sure you have the following core dependencies installed:
* `Hyprland`
* `Kitty`
* `Neovim` (>= 0.9.0)
* `Waybar`
* `fzf`
* `nushell`
* `python 3`

### Install
> ⚠️ **WARNING: If you have an existing `~/.config` setup, please backup before following these instructions.** 

1. **Clone Repository:**
    ```bash
    git clone [https://github.com/BrynGhiffar/dotfiles.git](https://github.com/BrynGhiffar/dotfiles.git)
    cd ~/dotfiles
    ```
2. **Run Setup Script**
    ```bash
    ./setup_dotfiles # Creates a symlink between dotfiles in this repo and ~/.config
    ```
