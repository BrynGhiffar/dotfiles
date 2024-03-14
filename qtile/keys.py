from libqtile.config import Key
from libqtile.lazy import lazy
from backlight import backlight
import traverse

mod = "mod4"
terminal = "kitty"
rofi_get_window_script = "/home/bryn/arch-config/rofi/scripts/get_windows.py"
rofi_set_window_script = "/home/bryn/arch-config/rofi/scripts/set_window.py"
rofi_win_switcher_cmd = f"{rofi_get_window_script} \"$({rofi_set_window_script} | rofi -dmenu -i -p \"\")\""
screenshot_cmd = "maim --select | xclip -selection clipboard -t image/png"

keys = [
    Key([mod], "h", lazy.function(traverse.left), desc="Move focus to left"),
    Key([mod], "l", lazy.function(traverse.right), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "space", lazy.spawn("rofi -show run"), desc="spawn rofi"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "c", lazy.spawn("xcolor | xclip -selection clipboard", shell=True)),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key(
        [mod, "control"], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),
    Key(
        [mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    Key(
        [mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),
    Key(
        [mod, "control"], "s", 
        lazy.spawn(screenshot_cmd, shell=True),
        desc="Screenshot selection"
    ),
    Key(
        [mod], "r", 
        lazy.spawn(rofi_win_switcher_cmd, shell=True),
        desc="spawn rofi window switcher"
    ),
    # Key([mod], "r", lazy.spawn(f"wmctrl -i -a \"$({ROFI_GET_WINDOWS} | rofi -dmenu -i -p \"\" | cut -d '|' -f 4)\"", shell=True)),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([], 'XF86MonBrightnessUp',   lazy.function(backlight('inc'))),
    Key([], 'XF86MonBrightnessDown', lazy.function(backlight('dec'))),

    Key([], 'XF86AudioMute', lazy.spawn('ponymix toggle')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('ponymix increase 5')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('ponymix decrease 5')),
    Key(
        [mod],
        "m",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.next_layout(),
        # lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]