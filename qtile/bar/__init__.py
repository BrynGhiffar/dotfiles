from qtile_extras import widget
from libqtile import bar
from colors import nord_fox
from bar.widgets import \
    get_volume_widget, \
    get_disk_storage_widget, \
    get_network_widget, \
    get_cpu_widget, \
    get_memory_widget, \
    get_clock_widget, \
    get_power_widget, \
    pl_arrow, \
    LEFT, \
    RIGHT

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
    background=GRAY1,
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

power_widget = get_power_widget(
    background=GRAY7
)

BAR_HEIGHT = 24

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
            active=nord_fox['magenta'],
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
        ),
    ],
    BAR_HEIGHT,
)