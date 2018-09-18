from connexion import NoContent

# Data to serve with our API
ARTIST = [
    {
        "id": 1,
        "name": "Anathema"
    },
    {
        "id": 2,
        "name": "King Gizzard & The Wizard Lizard"
    },
    {
        "id": 3,
        "name": "Tool"
    }
]


def read(artist_id: int):
    for artist in ARTIST:
        if artist['id'] == artist_id:
            return artist

    return NoContent, 404


# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return ARTIST
