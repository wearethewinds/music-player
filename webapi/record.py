from connexion import NoContent
from player import queue, Song


def read_all():
    return NoContent, 404


def play(record_id: str):
    # retrieve record information
    record = _get_record(record_id)

    queue.clear()
    _append_record(record)


def enqueue(record_id: str):
    record = _get_record(record_id)
    _append_record(record)


def _append_record(record):
    for title in record.tracklist:
        song = Song(title.file, title.metadata)

        queue.append(song)


def _get_record(record_id: str):
    return {"tracklist": []}
