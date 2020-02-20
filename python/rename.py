import os

tv_id_module = __import__('tv_id')


def get_tv_id_dict(tv_id_list):
    """
    将tv_id与对应的集数相匹配
    """
    tv_id_dict = {}
    for j in range(len(tv_id_list)):
        tv_id_dict[str(tv_id_list[j])] = str(j + 1)

    return tv_id_dict


def get_dir_name_list(pathname):
    dir_name_list = os.listdir(pathname)

    return dir_name_list


def rename(pathname, old_dir_name_list, tv_id_dict):
    # 新列表
    new_dir_name_list = []

    for j in old_dir_name_list:
        new_dir_name_list.append(tv_id_dict[str(j)[0:11]] + '_' + str(j))

    for j in range(len(old_dir_name_list)):
        old_name = pathname + old_dir_name_list[j]
        new_name = pathname + new_dir_name_list[j]
        os.rename(old_name, new_name)


if __name__ == '__main__':
    # 节目id
    my_aid = '212447801'
    # 路径
    my_pathname = '../data/'

    # 获取tv_id列表
    my_tv_id_list = tv_id_module.get_tv_id(my_aid)
    # 获取tv_id字典
    my_tv_id_dict = get_tv_id_dict(my_tv_id_list)

    # 获取文件列表
    my_dir_name_list = get_dir_name_list(my_pathname)

    # 重命名
    rename(my_pathname, my_dir_name_list, my_tv_id_dict)

