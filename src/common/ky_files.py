import os


# 不删除空文件夹,只删除文件
def remove_all_files(path):
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
            remove_all_files(tmp)
