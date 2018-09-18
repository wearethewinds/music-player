import metadata.parsers
from metadata import Metadata


def parse_file(path: str) -> Metadata:
    if metadata.parsers.flac_parser.isValid(path):
        return metadata.parsers.flac_parser.parse(path)
