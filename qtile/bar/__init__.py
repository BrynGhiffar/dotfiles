from qtile_extras import widget
from libqtile import bar
from colors import nord_fox
import colorsys
from socket import gethostname
from bar.widgets import \
    get_backlight_widget, \
    get_battery_widget, \
    get_volume_widget, \
    get_disk_storage_widget, \
    get_network_widget, \
    get_cpu_widget, \
    get_memory_widget, \
    get_systray_widget, \
    get_clock_widget, \
    get_power_widget, \
    pl_arrow, \
    LEFT, \
    RIGHT

from bar.timer import Timer

# Idea: Dynamically set the color of the bar according to your wallpaper

FIRA_CODE_NERD_FONT_MONO = "FiraCode Nerd Font Mono"

widget_defaults = dict(
    font=FIRA_CODE_NERD_FONT_MONO,
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def parse_text_task_list(s):
    return ""

def hex_to_tup(hex: str):
    hex = hex.lstrip("#")
    r, g, b = (round(int(hex[i:i+2], 16) / 255, 3) for i in (0, 2, 4))
    return (r, g, b)

def tup_to_hex(tup: tuple[int, int, int]):
    nums = "".join((hex(round(i * 255)).replace("0x", "").rjust(2, "0") for i in tup))
    return f"#{nums}"

def lighten(hex_color: str, inc: int):
    hinc = 0.0 * inc
    vinc = 0.03 * inc
    r, g, b = hex_to_tup(hex_color)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h = (h + hinc) % 1
    v = min(v + vinc, 1.0)
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return tup_to_hex((r, g, b))

BG = "#1d1e32"

GRAY1 = lighten(BG, 2)
GRAY2 = lighten(BG, 6)
GRAY3 = lighten(BG, 10)
GRAY4 = lighten(BG, 14)
GRAY5 = lighten(BG, 18)
GRAY6 = lighten(BG, 22)
GRAY7 = lighten(BG, 26)
GRAY8 = "#45454a"

network_widget = get_network_widget(
    background=GRAY1,
)

volume_widget = get_volume_widget(
    background=GRAY1,
)

backlight_widget = get_backlight_widget(
    background=GRAY2
)

battery_widget = get_battery_widget(
    background=GRAY2
)

disk_storage_widget = get_disk_storage_widget(
    background=GRAY3,
)

cpu_widget = get_cpu_widget(
    background=GRAY4,
)

memory_widget = get_memory_widget(
    background=GRAY5,
)

systray_widget = get_systray_widget(
    background=GRAY6,
)

clock_widget = get_clock_widget(
    background=GRAY6,
)

power_widget = get_power_widget(
    background=GRAY7
)

def get_bar_height():
    hostname = gethostname()
    if "laptop" in hostname:
        return 28
    return 24

BAR_HEIGHT = get_bar_height()

left_bar = bar.Bar(
    [
        widget.CurrentLayout(
            background=BG,
            **pl_arrow(LEFT)
        ),
        widget.GroupBox(
            active="#00ff00",
            inactive="#ffffff",
            block_highlight_text_color="#ffffff",
            this_current_screen_border="#ffffff",
            highlight_color=GRAY1,
            foreground="#ffffff",
            this_screen_border="#ffffff",
            background=BG,
            borderwidth=2,
            highlight_method='line',
            padding=5,
            visible_groups=['1', '2', '3', '4', '5'],
            disable_drag=True,
            **pl_arrow(LEFT)
        ),
        widget.TaskList(
            border=GRAY5,
            borderwidth=0,
            highlight_method="block",
            background=BG,
            urgent_border=nord_fox['cyan'],
            theme_mode = "preferred",
            theme_path = "/usr/share/icons/Papirus-Dark",
            # max_title_width=100,
            parse_text=parse_text_task_list,
            **pl_arrow(LEFT),
        ),
        widget.Spacer(
            background=BG, 
            **pl_arrow(RIGHT),
        ),
        *network_widget,
        *backlight_widget,
        *battery_widget,
        *volume_widget,
        *disk_storage_widget,
        *cpu_widget,
        *memory_widget,
        *systray_widget,
        Timer(background=GRAY6, **pl_arrow(RIGHT)),
        *clock_widget,
        *power_widget
    ],
    BAR_HEIGHT,
)

right_bar = bar.Bar(
    [
        widget.CurrentLayout(
            background=BG,
            **pl_arrow(LEFT)
        ),
        widget.GroupBox(
            active="#00ff00",
            inactive="#ffffff",
            block_highlight_text_color="#ffffff",
            this_current_screen_border="#ffffff",
            highlight_color=GRAY1,
            foreground="#ffffff",
            this_screen_border="#ffffff",
            background=BG,
            borderwidth=2,
            highlight_method='line',
            padding=5,
            visible_groups=['a', 's', 'd'],
            disable_drag=True,
            **pl_arrow(LEFT)
        ),
        widget.TaskList(
            # border=nord_fox['bg'],
            borderwidth=0,
            theme_mode = "preferred",
            theme_path = "/usr/share/icons/Papirus-Dark",
            highlight_method="block",
            background=BG,
            urgent_border=nord_fox['cyan'],
            parse_text=parse_text_task_list,
        ),
        widget.Spacer(
            background=BG, 
            **pl_arrow(RIGHT),
        ),
        *network_widget,
        *volume_widget,
        *disk_storage_widget,
        *cpu_widget,
        *memory_widget,
        *clock_widget,
        *power_widget
    ],
    BAR_HEIGHT,
)
