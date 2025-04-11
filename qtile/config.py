
# ██████╗░░██████╗░██╗░░██╗██╗███████╗███████╗░█████╗░██████╗░  ░██████╗░████████╗██╗██╗░░░░░███████╗
# ██╔══██╗██╔════╝░██║░░██║██║██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔═══██╗╚══██╔══╝██║██║░░░░░██╔════╝
# ██████╦╝██║░░██╗░███████║██║█████╗░░█████╗░░███████║██████╔╝  ██║██╗██║░░░██║░░░██║██║░░░░░█████╗░░
# ██╔══██╗██║░░╚██╗██╔══██║██║██╔══╝░░██╔══╝░░██╔══██║██╔══██╗  ╚██████╔╝░░░██║░░░██║██║░░░░░██╔══╝░░
# ██████╦╝╚██████╔╝██║░░██║██║██║░░░░░██║░░░░░██║░░██║██║░░██║  ░╚═██╔═╝░░░░██║░░░██║███████╗███████╗
# ╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░░░░╚═╝░░░╚═╝╚══════╝╚══════╝

# Welcome to my Qtile configuration :D

from libqtile import hook, qtile
from libqtile.log_utils import logger
from screen import screens as _screens
from bar import \
    widget_defaults as _widget_defaults, \
    extension_defaults as _extension_defaults
from keys import keys as _keys, mouse as _mouse
from groups import groups as _groups
from layouts import \
    layouts as _layouts, \
    floating_layout as _floating_layout
import os

import subprocess

# █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ █░░
# █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ █▄▄

screens = _screens
keys = _keys
mouse = _mouse
groups = _groups
layouts = _layouts
floating_layout = _floating_layout
widget_defaults = _widget_defaults
extension_defaults = _extension_defaults

# █▀▄▀█ █ █▀ █▀▀
# █░▀░█ █ ▄█ █▄▄                                                                                                   

dgroups_key_binder = None
dgroups_app_rules = [] 
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

# █░█ █▀█ █▀█ █▄▀ █▀
# █▀█ █▄█ █▄█ █░█ ▄█

@hook.subscribe.focus_change
def focus_changed():
    # qtile.current_window.bring_to_front()
    pass

def get_wm_class(window):
    wm_classes = window.info()["wm_class"]
    return wm_classes[0]

@hook.subscribe.client_new
def new_client(window):
    static_wm_class = "app-wallpaper"
    wm_class = get_wm_class(window)
    if wm_class != static_wm_class:
        return
    window.static(screen=0, x=-1, y=-1, width=1921, height=1081)
    window.keep_below(True)

@hook.subscribe.startup_once
def start():
    # subprocess.run([ "start-wgpu", "&" ])
    # subprocess.Popen("cpulimit -l 5 wgpu-wallpaper")
    # subprocess.Popen("fluid-simul-bin")
    pass
