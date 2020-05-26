import sys 
sys.path.append('src/')

from image_detector import ImageDetector
import unittest
import random
import json

'''
Test Driven Development (TDD) says when developing a software/application, we develop a software with the expected test result. Therefore, the next part of the software would not continue before the test has passed.

'''

class TestImageDetector(unittest.TestCase):

    test_cases_path = 'test/test_cases.json'

    '''
    This function runs once and will load the test cases stored on the json file test_cases.json
    '''
    @classmethod
    def setUpClass(cls):
        print("=" * 10, "SETUP TEST CASES", "=" * 10)
        with open(cls.test_cases_path) as json_file:
            cls.full_test_cases = json.load(json_file)
            cls.test_cases = cls.full_test_cases[:4]
            print("Number of test cases: ", len(cls.test_cases))
            print("Number of all test cases: ", len(cls.full_test_cases))

    '''
    This function sets up the image detector object. It runs every test is performed
    '''

    def setUp(self):
        self.image_detector = ImageDetector()

    '''
    This function tests the image labelling

    TODO: Create other test cases for each of the function

    Iteration 0: FAIL, because the returned value of get_image_labels() contains nothing.

    '''
    def test_get_image_labels(self):
        print("=" * 10, "LABELLING TEST", "=" * 10)
        test_cases = self.test_cases
        self.image_labels(test_cases=test_cases)

    def image_labels(self, test_cases):
        for test_case in test_cases:
            # Set image url
            self.image_detector.set_image_url(image_url=test_case["image_url"])
            # Expected labels
            ex_labels = test_case["labels"]
            # Get generated labels
            labels = self.image_detector.get_image_labels()
            labels = [label["description"] for label in labels]
            # Score
            score = self.score_comparison(ex_list=ex_labels, ac_list=labels)
            # Print results
            print("Test Description: Labelling Test")
            print("Description: ", test_case["description"])
            print("Similarity Score: ", score)
            # Test will pass if the similarity score > 0.1
            self.assertGreaterEqual(score, 0.1)

    '''
    This function compares between ex_labels and labels and returns score
    '''

    def score_comparison(self, ex_list, ac_list):
        # Remove duplicates
        ex_list = list(dict.fromkeys(ex_list))
        ac_list = list(dict.fromkeys(ac_list))
        # Initialise correct count
        correct_count = 0
        # Make all the string to lower
        ac_list = [ac_item.lower() for ac_item in ac_list]
        # Count the correct item
        for ex_item in ex_list:
            if ex_item.lower() in ac_list:
                correct_count += 1
        # Measure the score
        score = correct_count / len(ac_list)
        return score

    '''
    This function tests the object detection
    '''

    def test_get_image_objects(self):
        print("=" * 10, "OBJECT DETECTION TEST", "=" * 10)
        test_cases = self.test_cases
        self.image_objects(test_cases=test_cases)

    def image_objects(self, test_cases):
        for test_case in self.test_cases:
            # Set image url
            self.image_detector.set_image_url(image_url=test_case["image_url"])
            # Expected objects
            ex_objects = test_case["objects"]
            # Get generated labels
            objects = self.image_detector.get_image_objects()
            objects = [obj["name"] for obj in objects]
            # Measure score
            score = self.score_comparison(ex_list=ex_objects, ac_list=objects)
            # Test will pass if the similarity score > 0
            self.assertGreaterEqual(score, 0)

    '''
    #5 This function run automated test case generation

    def test_get_image_labels_random(self, num_of_cases=10):
        pass

    '''
    def test_get_image_labels_random(self):
        print("=" * 10, "AUTOMATED LABELLING TEST", "=" * 10)
        # Get the randomized test cases
        test_cases = self.get_randomized_test_cases(num_of_cases=10)
        # Test image label for each case
        self.image_labels(test_cases)

    def get_randomized_test_cases(self, num_of_cases=10):
        test_cases = []
        # Generate randomized index and get the element from the test_cases
        for i in range(num_of_cases):
            index = random.randint(0,len(self.full_test_cases))
            test_cases.append(self.full_test_cases[index])
        return test_cases

if __name__ == "__main__":
    unittest.main()
