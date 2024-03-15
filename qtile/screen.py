from libqtile.config import Screen
from bar_preset import left_bar, right_bar

screens = [
    Screen(
        top=left_bar
    ),
    Screen(
        top=right_bar
    ),
]