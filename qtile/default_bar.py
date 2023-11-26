from libqtile import widget, bar
from unicodes import left_arrow,right_arrow
from colors import nord_fox

bar = bar.Bar(
    [
        widget.CurrentLayout(
            background=nord_fox['bg']
        ),
        right_arrow(nord_fox['red'], nord_fox['bg']),
        widget.GroupBox(
            active=nord_fox['magenta'],
            inactive=nord_fox['black'],
            block_highlight_text_color=nord_fox['fg_gutter'],
            highlight_color=nord_fox['bg'],
            background=nord_fox['red'],
            borderwidth=0,
            highlight_method='line',
            padding=13
        ),
        right_arrow(nord_fox['fg_gutter'], nord_fox['red']),
        widget.Prompt(
            background=nord_fox['fg_gutter']
        ),
        # widget.WindowName(
        #     background=nord_fox['fg_gutter']
        # ),
        # widget.WindowTabs(
        #     background=nord_fox['fg_gutter'],
        #     selected=('<b>[',"]</b>")
        # ),
        widget.TaskList(
            border=nord_fox['bg'],
            borderwidth=0,
            highlight_method="block",
            background=nord_fox['fg_gutter'],
            urgent_border=nord_fox['cyan']
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        left_arrow(nord_fox['fg_gutter'], nord_fox['orange']),
        widget.TextBox("", background=nord_fox['orange'], fontsize=30),
        widget.PulseVolume(
            background=nord_fox['orange'],
        ),
        left_arrow(nord_fox['orange'], nord_fox['green']),
        widget.TextBox(text="", background=nord_fox['green'], fontsize=30),
        widget.Backlight(
            backlight_name="intel_backlight",
            brightness_file="brightness",
            max_brightness_file="max_brightness",
            background=nord_fox['green']
        ),
        left_arrow(nord_fox['green'], nord_fox['cyan']),
        widget.TextBox("Battery", background=nord_fox['cyan']),
        widget.Battery(
            background=nord_fox['cyan'],
            format='{char} {percent:2.0%} {hour:d}:{min:02d}'
        ),
        left_arrow(nord_fox['cyan'], nord_fox['pink']),
        widget.Systray(),
        widget.Clock(
            format="%Y-%m-%d %a %I:%M %p",
            background=nord_fox['pink']
        ),
        # widget.QuickExit(),
    ],
    28,
    # margin=8
    # margin=[2, 2, 0, 2],
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
)
