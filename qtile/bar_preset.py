from qtile_extras import widget
from libqtile.log_utils import logger
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile import bar
from unicodes import left_arrow,right_arrow
from colors import nord_fox
from libqtile.lazy import lazy

powerline_arrow_right = {
    "decorations": [
        PowerLineDecoration(path="arrow_right")
    ]
}

powerline_arrow_left = {
        "decorations": [
                PowerLineDecoration(path="arrow_left")
            ]
        }

def ShutdownButton(**config):
    def onclick(qtile):
        qtile.spawn('shutdown now', shell=True)

    return widget.TextBox(
        **config,
        fmt="󰤆", 
        fontsize=24, 
        padding=6,
          mouse_callbacks={ "Button1": lazy.function(onclick) }
    )

def LogOffButton(**config):
    def onclick(qtile):
        qtile.cmd_spawn('reboot')

    return widget.TextBox(
        **config,
        fmt="󰩈", 
        fontsize=18, 
        padding=6,
          mouse_callbacks={ "Button1": lazy.function(onclick) }
    )

left_bar = bar.Bar(
    [
        widget.CurrentLayout(
            background=nord_fox['bg'],
            **powerline_arrow_left
        ),
        widget.GroupBox(
            active=nord_fox['magenta'],
            inactive=nord_fox['black'],
            block_highlight_text_color=nord_fox['fg_gutter'],
            highlight_color=nord_fox['bg'],
            background=nord_fox['red'],
            borderwidth=0,
            highlight_method='line',
            padding=10,
            visible_groups=['1', '2', '3', '4', '5'],
            disable_drag=True,
            **powerline_arrow_left
        ),
        widget.Prompt(
            background=nord_fox['fg_gutter'],
            **powerline_arrow_left
        ),
        widget.TaskList(
            border=nord_fox['bg'],
            borderwidth=0,
            highlight_method="block",
            background=nord_fox['fg_gutter'],
            urgent_border=nord_fox['cyan'],
            max_title_width=100,
            **powerline_arrow_right,
        ),

        widget.TextBox(
            "", 
            background=nord_fox['orange'], 
            fontsize=30,
        ),
        widget.PulseVolume(
            background=nord_fox['orange'],
            **powerline_arrow_right,
        ),
        widget.WidgetBox(
            background=nord_fox['blue'],
            close_button_location='right',
            text_closed="",
            text_open="",
            **powerline_arrow_right,
            widgets=[
                widget.Net(
                    background=nord_fox['green'],
                    format=' {down:.0f}{down_suffix} | {up:.0f}{up_suffix} ',
                    **powerline_arrow_right,
                ),
                widget.TextBox(
                    fmt="󰘚", 
                    fontsize=18, 
                    background=nord_fox['cyan'],
                ),
                widget.CPU(
                    background=nord_fox['cyan'],
                    format='{load_percent}%  ',
                    **powerline_arrow_right,
                ),
                widget.TextBox(
                    fmt="", 
                    fontsize=18, 
                    background=nord_fox['blue'],
                ),
                widget.Memory(
                    background=nord_fox['blue'],
                    measure_mem='G',
                    format='{MemPercent:.2f}%  '
                ),
            ]
        ),
        widget.Systray(
            background=nord_fox['pink'],
            **powerline_arrow_right,
        ),
        widget.Clock(
            format="%a %d/%m/%Y %H:%M  ",
            background=nord_fox['pink'],
            **powerline_arrow_right,
        ),
        widget.WidgetBox(
            close_button_location='right',
            padding=10,
            fontsize=20,
            text_closed="",
            text_open="",
            background=nord_fox["red"],
            widgets=[
                LogOffButton(
                    background=nord_fox["red"]
                ),
                ShutdownButton(
                    background=nord_fox["red"]
                ),
            ]
        )
        # widget.QuickExit(),
    ],
    24,
)

right_bar = bar.Bar(
    [
        widget.CurrentLayout(
            background=nord_fox['bg'],
            **powerline_arrow_left
        ),
        widget.GroupBox(
            active=nord_fox['magenta'],
            inactive=nord_fox['black'],
            block_highlight_text_color=nord_fox['fg_gutter'],
            highlight_color=nord_fox['bg'],
            background=nord_fox['red'],
            borderwidth=0,
            highlight_method='line',
            padding=13,
            visible_groups=['a', 's', 'd'],
            disable_drag=True,
            **powerline_arrow_left
        ),
        widget.Prompt(
            background=nord_fox['fg_gutter'],
            **powerline_arrow_left
        ),
        widget.GlobalMenu(
            background=nord_fox['fg_gutter'],
        ),
        widget.TaskList(
            border=nord_fox['bg'],
            borderwidth=0,
            highlight_method="block",
            background=nord_fox['fg_gutter'],
            urgent_border=nord_fox['cyan'],
            **powerline_arrow_left
        ),
    ],
    24,
)
