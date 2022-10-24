import yaml


def read_yml_config(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        file_data = f.read()
    return yaml.load(file_data, Loader=yaml.BaseLoader)
