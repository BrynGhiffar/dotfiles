#!/usr/bin/python

from libqtile.command.client import InteractiveCommandClient
from libqtile import hook
import argparse

def get_screen(group):
    if group in "123":
        return 0
    if group in "asd":
        return 1

def onChoiceArg(choice):
    ss = choice.find("|")
    lss = choice.rfind("|")
    if ss == lss:
        return exit(0)
    if ss == -1:
        return exit(0)

    group, win_name, wid = choice[:ss].strip(), choice[ss+1:lss].strip(), int(choice[lss+1:].strip())
    # print(group, win_name)
    client = InteractiveCommandClient()
    # groups = client.get_groups()
    # group_ob = groups[group]
    screen = get_screen(group)

    client.to_screen(int(screen))
    client.group[group].toscreen(screen)
    if client.window[wid].info()["minimized"]:
        client.window[wid].toggle_minimize()
    client.window[wid].focus()
    # client.group[group].focus_by_index(wid)
    # print(screen)
    pass

def onWidArg(wid):
    wid = int(wid)
    client = InteractiveCommandClient()
    window_info = client.window[wid].info()
    group = window_info["group"]
    screen = get_screen(group)
    client.to_screen(int(screen))
    client.group[group].toscreen(screen)
    if window_info["minimized"]:
        client.window[wid].toggle_minimize()
    client.window[wid].focus()

def main():
    parser = argparse.ArgumentParser(
        prog="Set Window for Rofi",
    )
    parser.add_argument("choice", nargs="?")
    parser.add_argument("--wid", nargs="?")
    args = parser.parse_args()
    choice = args.choice
    wid = args.wid
    if choice is not None:
        onChoiceArg(choice)
        return
    if wid is not None:
        onWidArg(wid)
        return

main()
