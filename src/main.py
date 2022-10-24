from common import ky_ymls, ky_files
import sys  # 获取命令行的参数
import os


def clear(config):
    profile_path = config['profile_path']
    remove_files = config['remove_files_path']
    for rf in remove_files:
        ky_files.remove_all_files(os.path.join(profile_path, rf))


if __name__ == '__main__':
    cmd_params = sys.argv
    # 获取配置文件的绝对路径
    config_path = os.path.abspath(os.path.dirname(cmd_params[0])) + '/config.yml'
    config = ky_ymls.read_yml_config(config_path)
    clear(config['google'])
    print('程序运行完毕')
