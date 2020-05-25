import unittest
import statistics
from test_image_detector import TestImageDetector

class TestTestImageDetector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_image_detector = TestImageDetector()
        pass

    def test_test_get_image_labels_random(self):
        # Make sure that the distribution of the random good
        test_cases = self.test_image_detector.get_randomized_test_cases(num_of_cases=10)
        # Data preparation for variance calculation
        random_indexes = []
        for test_case in test_cases:
            random_indexes.append(test_case["id"])
        # Calculate variance
        var = statistics.variance(random_indexes)
        print("Variance: ", var)
        self.assertGreaterEqual(var, 0.5)

if __name__ == "__main__":
    unittest.main()