from pycmus import remote
from typing import List
import player.state
import re


class Cmus:
    old_volume = None

    def __init__(self):
        self.cmus = remote.PyCmus()

    def get_playing_info(self):
        state = self.cmus.status().splitlines()
        parameters = {}

        for line in state:
            prog = re.compile('^(tag|set)\s([^\s]*)\s([^\s]*)$')
            result = prog.match(line)

            if result is not None:
                parameters[result.group(2)] = result.group(3)
            else:
                other_prog = re.compile('^(duration|position)\s(\d+)$')
                other_result = other_prog.match(line)

                if other_result is not None:
                    parameters[other_result.group(1)] = other_result.group(2)

        return player.state.PlayerState(parameters.artist, parameters.title, parameters.tracknumber,
                                        parameters.duration, parameters.positoin, parameters.repeat, parameters.shuffle,
                                        parameters.vol_left)

    def stop(self):
        return self.cmus.player_stop()

    def pause(self):
        return self.cmus.player_pause()

    def play(self):
        return self.cmus.player_play()

    def prev(self):
        return self.cmus.player_prev()

    def next(self):
        return self.cmus.player_next()

    def play_file(self, file: str):
        return self.cmus.player_play_file(file)

    def set_volume(self, val: int):
        self.old_volume = val
        self.cmus.set_volume(val)

    def mute(self):
        self.cmus.set_volume(0)

    def unmute(self):
        self.cmus.set_volume(self.old_volume)

    def jump_to(self, val: int):
        self.cmus.seek(val)

    def get_state(self):
        return player.state.playing

    def enqueue(self, files: List[str]):
        self.cmus.send_cmd('clear\n')

        for file in files:
            self.cmus.send_cmd('add ' + file + '\n')
