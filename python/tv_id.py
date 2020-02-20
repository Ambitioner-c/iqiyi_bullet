import requests
import json


def get_tv_id(aid):
    # tv_id列表
    tv_id_list = []

    for page in range(1, 3):
        url = 'https://pcw-api.iqiyi.com/albums/album/avlistinfo?aid=' \
              + aid + '&page='\
              + str(page) + '&size=30'

        # 请求网页内容
        res = requests.get(url).text

        res_json = json.loads(res)

        # 视频列表
        move_list = res_json['data']['epsodelist']
        for j in move_list:
            tv_id_list.append(j['tvId'])

    return tv_id_list


if __name__ == '__main__':
    # 节目id
    my_aid = '212447801'
    my_tv_id_list = get_tv_id(my_aid)

