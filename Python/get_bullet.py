import zlib
import requests


def bullet(tv_id):

    for page in range(12, 17):
        # https://cmts.iqiyi.com/bullet/tv_id[-4:-2]/tv_id[-2:]/tv_id_300_x.z
        url = 'https://cmts.iqiyi.com/bullet/'\
              + tv_id[-4:-2] + '/'\
              + tv_id[-2:] + '/'\
              + tv_id + '_300_'\
              + str(page) + '.z'

        # 请求弹幕压缩文件
        res = requests.get(url).content
        res_byte = bytearray(res)
        try:
            xml = zlib.decompress(res_byte).decode('utf-8')

            # 保存路径
            path = '../Data/' + tv_id + '_300_' + str(page) + '.xml'
            with open(path, 'w', encoding='utf-8') as f:
                f.write(xml)
        finally:
            return


if __name__ == '__main__':
    my_tv_id = '11298454000'
    bullet(my_tv_id)
