import magic
from mutagen.flac import FLAC
from metadata import Metadata
from filesystem import reader

def isValid(file: str):
    mime = magic.from_file(file, True)

    return mime == 'audio/x-flac'


def parse(file: str) -> Metadata:
    flac = FLAC(file)

    checksum = reader.md5(file)

    return Metadata(flac.get('artist')[0], flac.get('album')[0], file, flac.get('title')[0], flac.get('tracknumber')[0], flac.info.length, checksum)
