from qtile_extras import widget
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import PowerLineDecoration
from typing import Literal

LEFT = "LEFT"
LEFT_TYPE = Literal["LEFT"]
RIGHT = "RIGHT"
RIGHT_TYPE = Literal["RIGHT"]

powerline_arrow_right = dict(
    decorations=[ PowerLineDecoration(path="arrow_right") ]
)

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
            **pl_arrow(RIGHT),
            **config,
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
            **config,
            **pl_arrow(RIGHT),
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
            **config,
            **pl_arrow(RIGHT),
        ),
        widget.Clock(
            format="%a %d/%m/%Y %H:%M  ",
            **config,
            **pl_arrow(RIGHT),
        ),
    ]

def get_power_widget(**config):
    return [
        widget.WidgetBox(
            close_button_location='right',
            padding=10,
            fontsize=12,
            text_closed="󰇙",
            text_open="󰇙",
            **config,
            widgets=[
                logoff_button(
                    **config
                ),
                shutdown_button(
                    **config
                ),
            ],
        )
    ]