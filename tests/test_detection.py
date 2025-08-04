import unittest
from core.detection import Detector


class TestDetection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.detector = Detector('core/models/weights/best.pt')

    def test_detection_on_sample(self):
        # 测试样本检测
        pass


if __name__ == '__main__':
    unittest.main()
