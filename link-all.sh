#!/usr/bin/bash

conf_loc=~/arch-config

if [ -d ~/.config/rofi ]; then
  rm -r ~/.config/rofi 
fi
ln -s $conf_loc/rofi ~/.config

if [ -d ~/.config/wofi ]; then
  rm -r ~/.config/wofi
fi
ln -s $conf_loc/wofi ~/.config

if [ -d ~/.config/kitty ]; then
  rm -r ~/.config/kitty
fi
ln -s $conf_loc/kitty ~/.config

if [ -f ~/.config/picom.conf ]; then
  rm ~/.config/picom.conf
fi
ln -s $conf_loc/picom.conf  ~/.config

if [ -d ~/.config/nvim ]; then
  rm -r ~/.config/nvim
fi
ln -s $conf_loc/nvim ~/.config

if [ -d ~/.config/qtile ]; then
  rm -r ~/.config/qtile
fi
ln -s $conf_loc/qtile ~/.config

if [ -d ~/.config/ranger ]; then
  rm -r ~/.config/ranger
fi
ln -s $conf_loc/ranger ~/.config

if [ -d ~/.config/hypr ]; then
  rm -r ~/.config/hypr
fi
ln -s $conf_loc/hypr ~/.config
