import subprocess
from libqtile.log_utils import logger
from libqtile import layout

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


def get_class(window):
    if len(window['wm_class']) == 1:
        return window['wm_class'][0]
    return window['wm_class'][1]

def get_screen(group):
    if group in "123":
        return 0
    if group in "asd":
        return 1

ZERO_WIDTH_CHAR = "\u200c"

def index_number_from_choice(choice: str):
    number = choice.count(ZERO_WIDTH_CHAR)
    if number == 0:
        return None
    return number - 1

def find_window_with_wid(qtile, wid):
    windows = [w for g in qtile.groups for w in g.windows]
    for _win in windows:
        if _win.info()["id"] == wid:
            return _win
    return None

def focus_to_window(qtile, window):
    wid = window["wid"]
    group = window["group"]
    win = find_window_with_wid(qtile, wid)
    screen = get_screen(group)
    if win is None:
        raise Exception("Win is none")
    qtile.focus_screen(screen)
    win.group.toscreen(screen)
    is_focused = win.group.current_window.info()["id"] == wid
    if is_focused:
        return
    is_max = isinstance(win.group.layout, layout.Max)
    if is_max:
        win.group.setlayout("columns")
    win.focus(True)
    win.disable_floating()
    # if is_max:
    #     win.group.setlayout("max")

def rofi_window_switcher(qtile):
    window_order = { "1": 1, "2": 2, "3": 3, "a": 4, "s": 5, "d": 6 }
    windows = [dict(
        wid=w["id"],
        name=w["name"],
        group=w["group"],
        clss=get_class(w),
    ) for w in qtile.windows()]
    windows.sort(key=lambda w: window_order[w["group"]])
    def render(i, w):
        name_max_len = 5
        name = w["name"]
        if len(name) > name_max_len:
            name = name[:name_max_len] + "..."
        group = w["group"]
        clss = w["clss"]
        num = i + 1
        hidden = ZERO_WIDTH_CHAR * num
        return f":{group}: {clss} | {name}{hidden}"
    items = windows
    strs = "\n".join([render(i, w) for i, w in enumerate(items)])
    template = f"echo -e '{strs}'"

    res = subprocess.run(
        [ f"{template} | rofi -dmenu -i -p ''" ],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    choice = res.stdout.decode("utf-8").strip()
    index = index_number_from_choice(choice)
    if index is None:
        return
    window = windows[index]
    focus_to_window(qtile, window)