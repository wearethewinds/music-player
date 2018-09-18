import player.state
from player.strategy.cmus import Cmus

player_wrapper = Cmus()


def play_queue():
    player_state = player_wrapper.get_state()
    if (player_state == player.state.playing):
        return player_wrapper.next()
    elif (player_state == player.state.paused):
        player_wrapper.stop()

    return player_wrapper.play()

def play_next_track():
    return player_wrapper.next()

def play_previous_track():
    return player_wrapper.prev()

def pause_playback():
    return player_wrapper.pause()

def stop_playback():
    return player_wrapper.stop()
