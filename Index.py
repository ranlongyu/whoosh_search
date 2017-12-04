#coding=utf-8
import os
from read_nxml import read_xml
from whoosh.index import create_in,open_dir
from whoosh import fields

WHOOSH_ADD = 'whoosh_index'
WHOOSH_SCHEMA = fields.Schema(id=fields.TEXT(stored=True),
    content=fields.TEXT(stored=True),
    )
if not os.path.exists(WHOOSH_ADD):
    os.mkdir(WHOOSH_ADD)
    ix = create_in(WHOOSH_ADD,schema=WHOOSH_SCHEMA,indexname='comment')
ix = open_dir(WHOOSH_ADD,indexname='comment')
writer = ix.writer()

filename = '00'
pathDir = os.listdir(filename)
for allDir in pathDir:
    path = os.path.join('%s' % allDir)
    path = filename + '/' +path
    article_id, body = read_xml(path)
    writer.add_document(id=article_id, content=body)
writer.commit()
