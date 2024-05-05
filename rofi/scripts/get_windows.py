#!/usr/bin/python

from libqtile.command.client import InteractiveCommandClient
from libqtile import hook

def get_class(window):
    if len(window['wm_class']) == 1:
        return window['wm_class'][0]
    return window['wm_class'][1]

def main():
    client = InteractiveCommandClient()
    # groups = client.get_groups()
    # windows = []
    # for group, info in groups.items():
    #     for idx, window in enumerate(info["windows"]):
    #         windows.append((group, idx, window))
    windows = [(w["group"], get_class(w), w["id"], w["name"]) for w in client.windows()]    
    windows.sort(key=lambda t: t[0])
    for group, wm_class, wid, win_name in windows:
        print(f"{group} | {wm_class} | {win_name} | {wid}")
    pass

main()
