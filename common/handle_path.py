import os

# 根目录
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件路径
config_path = os.path.join(file_path, 'config')
# 日志输出路径
log_path = os.path.join(file_path, 'outputs', 'logs')
# 报告目录
reports_path = os.path.join(file_path,  'outputs', 'reports')
# 历史报告目录
history_path = os.path.join(reports_path, 'history')
# 截图路径
screenshot_path = os.path.join(file_path, 'outputs', 'screenshots')

# 测试用例路径
testdatas_path = os.path.join(file_path, 'testdatas')
# 测试数据路径
testcases_path = os.path.join(file_path, 'testcases')
