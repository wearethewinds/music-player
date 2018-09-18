from collections import deque
from player import Song, play


queue = deque()
current_song = None


def append(song: Song):
    queue.append(song)

    play.player_wrapper.enqueue([song.file])


def getCurrentSong() -> Song:
    return current_song


def receive_new() -> Song:
    return queue.popleft()


def clear():
    queue.clear()


def remove(idx: int):
    queue.remove(idx)
