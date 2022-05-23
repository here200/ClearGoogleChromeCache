import os
import json


# 不删除空文件夹,只删除文件
def removeAllFile(path):
    # 检查路径是否存在
    if not os.path.exists(path):
        print(path + ' 不存在')
        return
    # 如果该路径是一个文件，直接删除
    if os.path.isfile(path):
        os.remove(path)
        return
    # 该路径是一个文件夹的路径
    for i in os.listdir(path):
        tmp = os.path.join(path, i)
        if os.path.isfile(tmp):
            os.remove(tmp)
        else:
            removeAllFile(tmp)


def clear(profile_path):
    if not os.path.exists(profile_path):
        print('google_profile_path 不存在')
        return
    # 清除缓存的文件和图片
    res = os.path.join(profile_path, 'Cache/Cache_Data/')
    removeAllFile(res)
    # 清除历史记录
    res = os.path.join(profile_path, 'History')
    removeAllFile(res)
    res = os.path.join(profile_path, 'History-journal')
    removeAllFile(res)


# 导入config.json文件的数据
def importConfig():
    str = ''
    with open('./config.json', 'r', encoding='utf8') as f:
        str = f.read()
    json_data = json.loads(str)
    path = json_data['google_profile_path']
    return path


if __name__ == '__main__':
    clear(importConfig())
