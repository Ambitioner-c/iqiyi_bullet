from wordcloud import WordCloud
import cv2
import jieba

rename_module = __import__('rename')
read_bullet_file_module = __import__('read_bullet_file')


def get_stopwords(stopwords_path):
    with open(stopwords_path, 'r') as f:
        stopwords_list = f.readlines()

    # 停用词
    stopwords = []
    for j in stopwords_list:
        stopwords.append(j.replace('\n', ''))

    return stopwords


def get_cloud(bullet_list, image, font, stopwords):
    # 拼接list
    bullet_text = ''
    for j in bullet_list:
        bullet_text = bullet_text + j

    # 分词
    text_iterable = jieba.cut(bullet_text, cut_all=False)

    # 去除停用词
    text = []
    stopwords_set = set(stopwords)
    for j in text_iterable:
        if j not in stopwords_set:
            text.append(j)

    text = ' '.join(text)
    mask = cv2.imread(image)
    word_cloud = WordCloud(mask=mask, background_color='white',
                           font_path=font,
                           width=620, height=464,
                           margin=2).generate(text)

    return word_cloud


if __name__ == '__main__':
    # 文件路径
    my_path = '../data/'

    # 图片路径
    my_image = '../image/pikaqiu.jpg'
    # 字体路径
    my_font = '../font/wqy-microhei.ttc'
    # 保存路径
    my_save = '../image/cloud.jpg'

    # 停用词路径
    my_stopwords_path = '../font/stopwords.txt'

    # 获取文件列表
    my_dir_name_list = rename_module.get_dir_name_list(my_path)

    # 读取弹幕文件
    my_bullet_list = read_bullet_file_module.read_bullet_file(my_path)

    # 获取停用词
    my_stopwords = get_stopwords(my_stopwords_path)

    # 生成词云
    my_word_cloud = get_cloud(my_bullet_list, my_image, my_font, my_stopwords)

    # 保存图片
    my_word_cloud.to_file(my_save)
