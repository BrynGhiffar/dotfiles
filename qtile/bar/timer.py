from libqtile.widget import base

class Timer(base.InLoopPollText):

    def __init__(self, **config):
        update_interval = 1 # update interval is every 1 second
        config = { **config, "update_interval": update_interval }
        super().__init__(**config)
        self.counter = 0
        self.is_paused = True
        self.add_callbacks({
            "Button1": self.toggle_pause,
            "Button3": self.reset_counter
        })
    
    def poll(self):
        play_symbol = "@"
        pause_symbol = "#"
        val = self.counter
        hours = val // 3600
        minutes = (val - hours * 3600) // 60
        seconds = val - hours * 3600 - minutes * 60
        hours = str(hours).zfill(2)
        minutes = str(minutes).zfill(2)
        seconds = str(seconds).zfill(2)
        time_str = f"{hours}:{minutes}:{seconds}"
        if self.is_paused:
            return f"[{play_symbol} {time_str}]"
        self.counter += 1
        return f"[{pause_symbol} {time_str}]"
    
    def toggle_pause(self):
        self.is_paused = not self.is_paused
    
    def reset_counter(self):
        if not self.is_paused: return
        self.counter = 0