from libqtile.config import Group 
from socket import gethostname

def get_groups():
    hostname = gethostname()
    if "laptop" in hostname:
        return [
            Group(name="1", screen_affinity=0),
            Group(name="2", screen_affinity=0),
            Group(name="3", screen_affinity=0),
            Group(name="4", screen_affinity=0),
            Group(name="5", screen_affinity=0),
        ]
    return [
        Group(name="1", screen_affinity=0),
        Group(name="2", screen_affinity=0),
        Group(name="3", screen_affinity=0), 
        Group(name="a", screen_affinity=1),
        Group(name="s", screen_affinity=1),
        Group(name="d", screen_affinity=1),
    ]


groups = get_groups()