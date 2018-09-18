from elasticsearch_dsl import Document, Text, HalfFloat, Integer
from metadata import Metadata
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])

class Title(Document):
    artist = Text()
    title = Text()
    record = Text()
    tracknumber = Integer()
    length = HalfFloat()
    file = Text()

    class Index:
        name = 'title'

    def save(self, ** kwargs):
        return super(Title, self).save(**kwargs)

def save_title(metadata: Metadata):
    print(metadata)
    Title.init()

    title = Title(meta={'id': metadata.checksum}, tracknumber=metadata.tracknumber, title=metadata.title, artist=metadata.artist, record=metadata.album, length=metadata.length, file=metadata.file)
    title.save()


def get_title(id: str):
    return Title.get(id)


def get_titles():
    for h in Title.search().execute():
        print(h.record)

    return list(map(lambda x: {"artist": x.artist, "title": x.title}, Title.search().execute()))