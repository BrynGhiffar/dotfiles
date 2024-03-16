from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile import bar
from colors import nord_fox
from libqtile.lazy import lazy
from typing import Literal

FIRA_CODE_NERD_FONT_MONO = "FiraCode Nerd Font Mono"

widget_defaults = dict(
    font=FIRA_CODE_NERD_FONT_MONO,
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

LEFT = "LEFT"
LEFT_TYPE = Literal["LEFT"]
RIGHT = "RIGHT"
RIGHT_TYPE = Literal["RIGHT"]

def pl_arrow(direction: LEFT_TYPE | RIGHT_TYPE):
    powerline_arrow_right = dict(
        decorations=[ PowerLineDecoration(path="arrow_right") ]
    )
    powerline_arrow_left = dict(
        decorations=[ PowerLineDecoration(path="arrow_left") ]
    )
    if direction == LEFT:
        return powerline_arrow_left
    return powerline_arrow_right

def shutdown_button(**config):
    def onclick(qtile):
        qtile.spawn('shutdown now', shell=True)

    return widget.TextBox(
        **config,
        fmt="󰤆", 
        fontsize=24, 
        padding=6,
        mouse_callbacks=dict(Button1=lazy.function(onclick))
    )

def logoff_button(**config):
    def onclick(qtile):
        qtile.cmd_spawn('reboot')

    return widget.TextBox(
        **config,
        fmt="󰩈", 
        fontsize=18, 
        padding=6,
        mouse_callbacks=dict(Button1=lazy.function(onclick))
    )

def get_cpu_icon(**config):
    return widget.TextBox(
        **config,
        fmt="󰘚", 
        fontsize=18, 
    )

def get_brain_icon(**config):
    return widget.TextBox(
        **config,
        fmt="", 
        fontsize=18, 
    )

def get_cpu_widget(**config):
    return [
        get_cpu_icon(**config),
        widget.CPU(
            format='CPU {load_percent}%  ',
            **config,
            **pl_arrow(RIGHT),
        ),
    ]

def get_memory_widget(**config):
    return [
        get_brain_icon(**config),
        widget.Memory(
            measure_mem='G',
            format='RAM {MemPercent:.2f}%  ',
            **config,
            **pl_arrow(RIGHT),
        ),
    ]

def get_volume_widget(**config):
    return [
        widget.TextBox(
            "", 
            fontsize=30,
            **config,
        ),
        widget.PulseVolume(
            **pl_arrow(RIGHT),
            **config,
        ),
    ]

def get_disk_storage_widget(**config):
    return [
        widget.DF(
            format="[{p}] {uf}{m}/{s}{m} {r:.0f}%",
            visible_on_warn=False,
            **config,
            **pl_arrow(RIGHT),
        ),
    ]

def get_network_widget(**config):
    return [
        widget.Net(
            format=' {down:.0f}{down_suffix} | {up:.0f}{up_suffix} ',
            **config,
            **pl_arrow(RIGHT),
        ),
    ]

def get_clock_widget(**config):
    return [
        widget.Systray(
            **pl_arrow(RIGHT),
            **config,
        ),
        widget.Clock(
            format="%a %d/%m/%Y %H:%M  ",
            **pl_arrow(RIGHT),
            **config,
        ),
    ]

def parse_text_task_list(s):
    return ""

BG = "#202022"
GRAY1 = "#313135"
GRAY2 = "#404044"
GRAY3 = "#525257"
GRAY4 = "#606066"
GRAY5 = "#727279"
GRAY6 = "#818188"
GRAY7 = "#919197"
GRAY8 = "#45454a"

volume_widget = get_volume_widget(
    background=GRAY1
)

disk_storage_widget = get_disk_storage_widget(
    background=GRAY2,
)

network_widget = get_network_widget(
    background=GRAY3,
)

cpu_widget = get_cpu_widget(
    background=GRAY4,
)

memory_widget = get_memory_widget(
    background=GRAY5,
)

clock_widget = get_clock_widget(
    background=GRAY6,
)

left_bar = bar.Bar(
    [
        widget.CurrentLayout(
            background=BG,
            **pl_arrow(LEFT)
        ),
        widget.GroupBox(
            active=nord_fox['magenta'],
            inactive="#ffffff",
            block_highlight_text_color="#ffffff",
            this_current_screen_border="#ffffff",
            highlight_color=BG,
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
            border=nord_fox['bg'],
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
        *volume_widget,
        *disk_storage_widget,
        *network_widget,
        *cpu_widget,
        *memory_widget,
        *clock_widget,
        widget.WidgetBox(
            close_button_location='right',
            padding=10,
            fontsize=12,
            text_closed="󰇙",
            text_open="󰇙",
            background=GRAY7,
            widgets=[
                logoff_button(
                    background=GRAY7
                ),
                shutdown_button(
                    background=GRAY7
                ),
            ]
        )
    ],
    24,
)

right_bar = bar.Bar(
    [
        widget.CurrentLayout(
            background=BG,
            **pl_arrow(LEFT)
        ),
        widget.GroupBox(
            active=nord_fox['magenta'],
            inactive="#ffffff",
            block_highlight_text_color="#ffffff",
            this_current_screen_border="#ffffff",
            highlight_color=BG,
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
            border=nord_fox['bg'],
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
    ],
    24,
)
