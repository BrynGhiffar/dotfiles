from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy
from backlight import backlight
import traverse
from groups import groups
from utils import \
    go_to_group, \
    go_to_group_and_move_window, \
    rofi_window_switcher, \
    start_wgpu_wallpaper

mod = "mod4"
terminal = "kitty"
rofi_get_window_script = "/home/bryn/arch-config/rofi/scripts/get_windows.py"
rofi_set_window_script = "/home/bryn/arch-config/rofi/scripts/set_window.py"
rofi_win_switcher_cmd = f"{rofi_set_window_script} \"$({rofi_get_window_script} | rofi -dmenu -i -p \"\")\""
screenshot_cmd = "maim --select | xclip -selection clipboard -t image/png"
color_selection_cmd = "xcolor | xclip -selection clipboard"

MOD_CTRL = [ mod, "control" ]
MOD_SHIFT = [ mod, "shift" ]
MOD = [ mod ]
FN_KEY_BRIGHTNESS_UP = "XF86MonBrightnessUp"
FN_KEY_BRIGHTNESS_DOWN = "XF86MonBrightnessDown"
FN_KEY_MUTE_VOLUME = "XF86AudioMute"
FN_KEY_RAISE_VOLUME = "XF86AudioRaiseVolume"
FN_KEY_LOWER_VOLUME = "XF86AudioLowerVolume"
KEY_ENTER_RETURN = "Return"
KEY_TAB = "Tab"
MOUSE_LEFT_CLICK = "Button1"
MOUSE_RIGHT_CLICK = "Button2"
MOUSE_MIDDLE_CLICK = "Button3"

window_navigation_keys = [
    Key(
        MOD, "h", 
        lazy.function(traverse.left),
        desc="Move focus to left"
    ),
    Key(
        MOD, "l", 
        lazy.function(traverse.right), 
        desc="Move focus to right"
    ),
    Key(
        MOD, "j", 
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key(
        MOD, "k", 
        lazy.layout.up(), 
        desc="Move focus up"
    ),
]

window_shuffle_keys = [
    Key(
        MOD_SHIFT, "h", 
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key(
        MOD_SHIFT, "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
    ),
    Key(
        MOD_SHIFT, "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
    ),
    Key(
        MOD_SHIFT, "k", 
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
]

window_grow_keys = [
    Key(
        MOD_CTRL, "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),
    Key(
        MOD_CTRL, "l", 
        lazy.layout.grow_right(),
        desc="Grow window to the right"
    ),
    Key(
        MOD_CTRL, "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),
    Key(
        MOD_CTRL, "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    Key(
        MOD, "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),
]

function_keys = [
    Key(
        [], FN_KEY_BRIGHTNESS_UP, 
        lazy.function(backlight('inc'))
    ),
    Key(
        [], FN_KEY_BRIGHTNESS_DOWN,
        lazy.function(backlight('dec'))
    ),
    Key(
        [], FN_KEY_MUTE_VOLUME, 
        lazy.spawn('ponymix toggle')
    ),
    Key(
        [], FN_KEY_RAISE_VOLUME,
        lazy.spawn('ponymix increase 5')
    ),
    Key(
        [], FN_KEY_LOWER_VOLUME, 
        lazy.spawn('ponymix decrease 5')
    ),
]

rofi_keys = [
    Key(
        MOD, "space", 
        lazy.spawn("rofi -show run"),
        desc="spawn rofi"
    ),
    Key(
        MOD, "r", 
        lazy.function(rofi_window_switcher),
        desc="spawn rofi window switcher"
    ),
]

app_shortcut_keys = [
    Key(
        MOD, KEY_ENTER_RETURN, 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),
]

qtile_keys = [
    Key(
        MOD_CTRL, "r", 
        lazy.reload_config(),
        desc="Reload the config"
    ),
    Key(
        MOD_CTRL, "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),
]

window_layout_keys = [
    Key(
        MOD, "f",
        lazy.next_layout(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        MOD_SHIFT, "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        MOD, "t", 
        lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"
    ), Key(
        MOD, KEY_TAB, 
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
]

group_navigation_keys = list(map(lambda group: Key(
    MOD, group.name,
    # lazy.group[i.name].toscreen(),
    lazy.function(go_to_group(group.name)),
    desc="Switch to group {}".format(group.name),
), groups))

move_window_to_group_keys = list(map(lambda group: Key(
    MOD_SHIFT, group.name,
    # lazy.window.togroup(i.name, switch_group=False),
    lazy.function(go_to_group_and_move_window(group.name)),
    desc="Switch to & move focused window to group {}".format(group.name),
), groups))

keys = [
    *window_navigation_keys,
    *window_shuffle_keys,
    *window_grow_keys,
    *rofi_keys,
    *app_shortcut_keys,
    *function_keys,
    *qtile_keys,
    *window_layout_keys,
    *group_navigation_keys,
    *move_window_to_group_keys,
    Key(
        MOD_SHIFT, "c", 
        lazy.spawn(color_selection_cmd, shell=True)
    ),
    Key(
        MOD_CTRL, "s", 
        lazy.spawn(screenshot_cmd, shell=True),
        desc="Screenshot selection"
    ),
    Key(
        MOD, "w", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),
    # Key(
    #     MOD, "B",
    #     # lazy.function(start_wgpu_wallpaper),
    #     lazy.spawn("cpulimit -l 5 wgpu-wallpaper"),
    #     desc="Start wgpu wallpaper"
    # )
]

mouse = [
    Drag(
        MOD, MOUSE_LEFT_CLICK, 
        lazy.window.set_position_floating(), 
        start=lazy.window.get_position()
    ),
    Drag(
        MOD, MOUSE_MIDDLE_CLICK, 
        lazy.window.set_size_floating(), 
        start=lazy.window.get_size()
    ),
    Click(
        MOD, MOUSE_RIGHT_CLICK, 
        lazy.window.bring_to_front()
    ),
]