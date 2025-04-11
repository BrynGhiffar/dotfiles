from libqtile.config import Screen
from bar import left_bar, right_bar

screens = [
    Screen(
        top=left_bar
    ),
    Screen(
        top=right_bar
    ),
]
