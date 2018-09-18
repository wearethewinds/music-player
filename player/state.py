from collections import namedtuple

playing = 'playing'
paused = 'paused'
stopped = 'stopped'

PlayerState = namedtuple('State', ['artist', 'title', 'tracknumber', 'duration', 'position', 'repeat', 'shuffle', 'vol'])
