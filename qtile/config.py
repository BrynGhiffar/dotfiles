from libqtile import layout, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from bar_preset import left_bar, right_bar
import traverse
from backlight import backlight
from keys import keys as _keys

mod = "mod4"
# terminal = guess_terminal()
terminal = "kitty"

ROFI_GET_WINDOWS = "/home/bryn/arch-config/rofi/scripts/get_windows.py"
ROFI_SET_WINDOW = "/home/bryn/arch-config/rofi/scripts/set_window.py"

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
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "s", lazy.spawn("maim --select | xclip -selection clipboard -t image/png", shell=True)),
    Key([mod], "r", lazy.spawn(f"{ROFI_SET_WINDOW} \"$({ROFI_GET_WINDOWS} | rofi -dmenu -i -p \"\")\"", shell=True)),
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

groups = [
    Group(name="1", screen_affinity=0),
    Group(name="2", screen_affinity=0),
    Group(name="3", screen_affinity=0), 
    Group(name="a", screen_affinity=1),
    Group(name="s", screen_affinity=1),
    Group(name="d", screen_affinity=1),
]

@hook.subscribe.focus_change
def focus_changed():
    qtile.current_window.bring_to_front()
    # logger.warning(f"Focus change {name}")


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '123':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner

def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        if name in "123":
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner

def switch_group(qtile, groupName):
    screens = [screen for screen in qtile.screens]
    for screen in screens:
        if groupName == screen.group.name:
            qtile.focus_screen(screen.index)
            return
    for group in qtile.groups:
        if group.name == groupName:
            group.toscreen()
    return


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                # lazy.group[i.name].toscreen(),
                lazy.function(go_to_group(i.name)),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                # lazy.window.togroup(i.name, switch_group=False),
                lazy.function(go_to_group_and_move_window(i.name)),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus="#3489eb",
        # border_focus="#ffffff",
        border_on_single=True,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=0,
        margin=5
    ),
    layout.Max(
        border_focus="#3489eb",
        border_width=0,
        margin=5
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Spiral(
    #     margin=5,
    #     border_width=0,
    # )
    # layout.Bsp(
    #     border_width=0,
    #     margin=5,
    # ),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(
    #     columnwidth=800,
    #     border_width=0,
    #     margin=5
    # ),
]

widget_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=left_bar
    ),
    Screen(
        top=right_bar
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = True
floating_layout = layout.Floating(
    border_focus="#000000",
    border_normal="#000000",
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="zoom.real "),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
