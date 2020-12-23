import os
import yaml
from configparser import ConfigParser

from common.handle_path import config_path


class HandleConfig(ConfigParser):
    # 配置文件的读取
    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding='utf-8')


test_path = os.path.join(config_path, 'test.ini')
# 直接实例化对象为了方便调用
conf = HandleConfig(test_path)

