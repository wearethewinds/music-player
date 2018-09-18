from indexer.strategy import elasticsearch
from connexion import NoContent
import player
import player.play


# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return elasticsearch.get_titles()


def play(title_id: str):
    title_obj = elasticsearch.get_title(title_id)
    song = player.Song(title_obj.file, title_obj)

    player.queue.clear()
    player.queue.append(song)

    return player.play.play_queue()


def enqueue(title_id: str):
    title_obj = elasticsearch.get_title(title_id)
    song = player.Song(title_obj.file, title_obj)

    player.queue.append(song)

    return NoContent, 204
