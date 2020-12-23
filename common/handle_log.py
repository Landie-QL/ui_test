import logging
from logging import handlers
import os
from datetime import datetime
from common.handle_path import log_path
from common.handle_config import conf


class HandleLog(logging.Logger):
    def __init__(self):
        # 创建日志收集器
        super().__init__(conf.get('log', 'name'))
        # 设置日志等级
        self.setLevel(conf.get('log', 'level'))
        # 设置日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s [第%(lineno)d行] %(message)s'
        formatter = logging.Formatter(fmt)
        # 设置日志输出渠道1控制台
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        # 设置日志输出渠道2文件
        now_time = datetime.now().strftime("%Y-%m-%d %H：%M：%S")
        logname = f"{conf.get('log', 'file')}_{now_time}.log"
        logpath = os.path.join(log_path, logname)
        handle2 = logging.FileHandler(logpath, encoding='utf-8')
        handle2.setFormatter(formatter)
        # 加入日志收集器
        self.addHandler(handle1)
        self.addHandler(handle2)


log = HandleLog()
# log.info('hellow')