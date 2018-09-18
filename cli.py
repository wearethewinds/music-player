from indexer import indexer
from indexer.strategy import elasticsearch
from webapi import server

if __name__ == "__main__":
    indexer.index_source('/home/fabian/Music', ['*.flac', '*.mp3'])
    server.start()
