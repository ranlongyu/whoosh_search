#coding=utf-8
import xml.dom.minidom
import re
def read_xml(path):
    with open(path) as file_object:
        contents = file_object.read()
        '''
        #这个匹配有问题,只能用下面的方法
        #获取文档id
        article_id_1 = re.findall(r'<article-id pub-id-type="pmc">(.*)</article-id>', contents)
        '''
        # 获取body中的内容
        content = re.findall('<body>(.*)</body>', contents)
        dr = re.compile('</?\w+[^>]*>', re.S)
        body = dr.sub(' ', str(content))
    #打开xml文档
    dom = xml.dom.minidom.parse(path)
    #获取文档id
    cc = dom.getElementsByTagName('article-id')
    try:
        article_id = cc[1].firstChild.data
    except:
        article_id = cc[0].firstChild.data
    return(article_id,body)

