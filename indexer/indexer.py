from filesystem import reader
from metadata import parser
from typing import List
import indexer.strategy


def index_source(source: str, extensions: List[str]):
    file_list = reader.list_files_recursive(source, extensions)

    for file in file_list:
        metadata = parser.parse_file(file)
        indexer.strategy.elasticsearch.save_title(metadata)

    return file_list
