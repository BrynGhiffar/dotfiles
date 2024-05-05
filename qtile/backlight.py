import subprocess

def backlight(action):
    def f(qtile):
        index = 5
        brightness = int(subprocess.run(['xbacklight', '-get'],
                                        stdout=subprocess.PIPE).stdout)
        if action == "inc":
            res = subprocess.run(['sudo', 'xbacklight', '-inc', f"{index}"], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE
            )
        else:
            if brightness - index <= 0:
                return
            res = subprocess.run(['sudo', 'xbacklight', '-dec', f"{index}"], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE
            )
    return f
