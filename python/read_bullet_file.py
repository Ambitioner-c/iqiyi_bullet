from bs4 import BeautifulSoup
from xml.dom.minidom import parse
import xml.dom.minidom

rename_module = __import__('rename')


def read_bullet_file(path):
    # 文件路径
    filename = '1_11298454000_300_1.xml'
    pathname = path + filename

    # DOM树
    DOMTree = xml.dom.minidom.parse(pathname)
    collection = DOMTree.documentElement

    # 评论文本xml
    content_xml_list = collection.getElementsByTagName("content")

    content_list = []
    for j in content_xml_list:
        content_list.append(j.childNodes[0].data)

    return content_list


if __name__ == '__main__':
    # 文件路径
    my_path = '../data/'

    # 获取文件列表
    my_dir_name_list = rename_module.get_dir_name_list(my_path)

    #
    read_bullet_file(my_path)

