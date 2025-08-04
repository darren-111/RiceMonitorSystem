import logging
import os
from datetime import datetime


def setup_logger(log_dir='logs'):
    """配置日志系统"""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 创建以日期命名的日志文件
    log_file = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log'
    log_path = os.path.join(log_dir, log_file)

    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger('RicePestDetection')