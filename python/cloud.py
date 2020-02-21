from wordcloud import WordCloud
import cv2
import jieba

rename_module = __import__('rename')
read_bullet_file_module = __import__('read_bullet_file')


def get_cloud(bullet_list, image, font):
    # 拼接list
    bullet_text = ''
    for j in bullet_list:
        bullet_text = bullet_text + j

    text = jieba.cut(bullet_text, cut_all=False)

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
    # 字体文件
    my_font = '../font/wqy-microhei.ttc'
    # 保存路径
    my_save = '../image/cloud.jpg'

    # 获取文件列表
    my_dir_name_list = rename_module.get_dir_name_list(my_path)

    # 读取弹幕文件
    my_bullet_list = read_bullet_file_module.read_bullet_file(my_path)

    my_word_cloud = get_cloud(my_bullet_list, my_image, my_font)
    my_word_cloud.to_file(my_save)
