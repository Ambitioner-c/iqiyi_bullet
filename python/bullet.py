import zlib
import requests

tv_id_module = __import__('tv_id')


def get_bullet(tv_id):
    for page in range(1, 17):
        # https://cmts.iqiyi.com/bullet/tv_id[-4:-2]/tv_id[-2:]/tv_id_300_x.z
        url = 'https://cmts.iqiyi.com/bullet/'\
              + tv_id[-4:-2] + '/'\
              + tv_id[-2:] + '/'\
              + tv_id + '_300_'\
              + str(page) + '.z'
        print(url)

        # 请求弹幕压缩文件
        res = requests.get(url).content
        res_byte = bytearray(res)
        try:
            xml = zlib.decompress(res_byte).decode('utf-8')

            # 保存路径
            path = '../data/' + tv_id + '_300_' + str(page) + '.xml'
            with open(path, 'w', encoding='utf-8') as f:
                f.write(xml)
        except:
            return


if __name__ == '__main__':
    # aid
    my_aid = '212447801'
    # tv_id列表
    my_tv_id_list = tv_id_module.get_tv_id(my_aid)
    for i in my_tv_id_list:
        get_bullet(str(i))
