from libqtile.config import Group, ScratchPad, DropDown
from socket import gethostname

btop_width = 0.5
btop_height = 0.7

launcher_width = 0.25
launcher_height = 0.25

apps = [
    "google-chrome-stable",
    "code",
    "nitrogen"
]

def get_groups():
    hostname = gethostname()
    if "laptop" in hostname:
        return [
            Group(name="1", screen_affinity=0),
            Group(name="2", screen_affinity=0),
            Group(name="3", screen_affinity=0),
            Group(name="4", screen_affinity=0),
            Group(name="5", screen_affinity=0),
        ]
    return [
        ScratchPad(
            "scratchpad",
            [
                DropDown(
                    "btop", 
                    "kitty -o background_opacity=1.0 btop", 
                    x=0.5 - btop_width / 2, 
                    y=0.5 - btop_height / 2, 
                    width=btop_width, 
                    height=btop_height, 
                    on_focus_lost_hide=False,
                    opacity=1.0
                ),
                DropDown(
                    "launcher", 
                    "kitty -o background_opacity=1.0 bash -c 'fzfapp'", 
                    x=0.5 - launcher_width / 2, 
                    y=0.5 - launcher_height / 2, 
                    width=launcher_width, 
                    height=launcher_height, 
                    on_focus_lost_hide=False,
                    opacity=1.0
                ),
                DropDown(
                    "window_switcher", 
                    "kitty -o background_opacity=1.0 --title fzfwindow bash -c 'fzfwindow'", 
                    x=0.5 - launcher_width / 2, 
                    y=0.5 - launcher_height / 2, 
                    width=launcher_width, 
                    height=launcher_height, 
                    on_focus_lost_hide=False,
                    opacity=1.0
                ),
                DropDown(
                    "wallpaper", 
                    "kitty -o background_opacity=1.0 bash -c 'fzfwallpaper'", 
                    x=0.5 - btop_width / 2, 
                    y=0.5 - btop_height / 2, 
                    width=btop_width, 
                    height=btop_height, 
                    on_focus_lost_hide=False,
                    opacity=1.0
                ),
                DropDown(
                    "yazi", 
                    "kitty -o background_opacity=1.0 bash -c 'yazi'", 
                    x=0.5 - btop_width / 2, 
                    y=0.5 - btop_height / 2, 
                    width=btop_width, 
                    height=btop_height, 
                    on_focus_lost_hide=False,
                    opacity=1.0
                )
            ]
        ),
        Group(name="1", screen_affinity=0),
        Group(name="2", screen_affinity=0),
        Group(name="3", screen_affinity=0), 
        Group(name="a", screen_affinity=1),
        Group(name="s", screen_affinity=1),
        Group(name="d", screen_affinity=1),
    ]


groups = get_groups()
