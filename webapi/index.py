from indexer import indexer


def generate():
    file_list = indexer.reader.list_files_recursive('/home/fabian/Music', ['*.flac', '*.mp3'])

    return file_list, 200
