#coding=utf-8
from whoosh import index,scoring
from whoosh.qparser import QueryParser
ix = index.open_dir('whoosh_index', indexname='comment')
hits = []
query = input("请输入查询内容：\n")
#用content字段构建分析器
parser = QueryParser("content", schema=ix.schema)
try:
    #解析一个查询字段
    word = parser.parse(query)
except:
    word = None
if word is not None:
    #创建搜索对器
    s = ix.searcher(weighting=scoring.BM25F)
    hits = s.search(word)
    #with  ix.searcher() as s:  注意此处，如果使用with 方法的话，文件会自动closed（）方法，下边将无法使用hits结果
    #    hits = s.search(word)
print(len(hits))
#打印排第一的结果
print(hits[0]['id'])
#打印文档评分
print(hits[0].score)
#打印文档排序序号
print(hits[0].rank)