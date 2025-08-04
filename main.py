import argparse
from core.detection import Detector
from utils.logger import setup_logger


def main():
    # 初始化日志
    logger = setup_logger()
    logger.info("Starting Rice Pest Detection System")

    # 参数解析
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='data/samples/', help='input source')
    parser.add_argument('--weights', type=str, default='core/models/weights/best.pt', help='model weights path')
    args = parser.parse_args()

    # 初始化检测器
    detector = Detector(args.weights)

    # 运行检测
    results = detector.detect(args.source)

    # 处理结果
    # ...


if __name__ == '__main__':
    main()