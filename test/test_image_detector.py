import sys 
sys.path.append('src/')

from image_detector import ImageDetector
import unittest
import random

'''
Test Driven Development (TDD) says when developing a software/application, we develop a software with the expected test result. Therefore, the next part of the software would not continue before the test has passed.

'''

class TestImageDetector(unittest.TestCase):

    '''
    TEST CASES: Classroom picture, Birthday picture, and a city picture
    '''
    test_cases = [{
        "id":1,
        "description":"Classroom",
        "image_url":"https://images.pexels.com/photos/4019754/pexels-photo-4019754.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
        "labels":["classroom", "teacher", "student", "kids", "children", "study", "book"],
        "objects":["person", "chair"],
        "overall_emotion":"not_joy"
    }, 
    {
        "id":2,
        "description":"Birthday party",
        "image_url":"https://images.pexels.com/photos/1405528/pexels-photo-1405528.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
        "labels":["birthday", "party", "celebration", "candle", "crowd", "event", "dress", "family"],
        "objects":["person", "dress", "cake"],
        "overall_emotion":"not_joy"
    },
    {
        "id":3,
        "description":"Downtown scenery",
        "image_url":"https://images.pexels.com/photos/378570/pexels-photo-378570.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        "labels":["building", "town", "people", "traffic", "cityscape", "infrastructure", "city", "skycrapper", "downtown"],
        "objects":["person", "flag", "car"],
        "overall_emotion":"neutral"
    }]

    '''
    #1 This function sets up the image detector object. It runs every test is performed
    '''

    def setUp(self):
        self.image_detector = ImageDetector()

    '''
    #2 This function tests the image labelling

    TODO: Create other test cases for each of the function

    Iteration 0: FAIL, because the returned value of get_image_labels() contains nothing.

    '''
    def test_get_image_labels(self):
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
            # Count similarity score
            pass_count = 0
            for label in labels: 
                for ex_label in ex_labels: 
                    if label.lower() in ex_label.lower(): pass_count += 1
            score = pass_count / len(ex_labels)
            # Print results
            print("Test Description: Labelling Test")
            print("Description: ", test_case["description"])
            print("Similarity Score: ", score)
            # Test will pass if the similarity score > 0.5
            self.assertGreaterEqual(score, 0.5)

    '''
    #3 This function tests the object detection
    '''

    def test_get_image_objects(self):
        for test_case in self.test_cases:
            # Set image url
            self.image_detector.set_image_url(image_url=test_case["image_url"])
            # Expected objects
            ex_objects = test_case["objects"]
            # Get generated labels
            objects = self.image_detector.get_image_objects()
            # Count similarity score
            pass_count = 0
            for obj in objects: 
                for ex_object in ex_objects: 
                    if obj.lower() in ex_object.lower(): pass_count += 1
            score = pass_count / len(ex_objects)
            # Test will pass if the similarity score > 0.5
            self.assertGreaterEqual(score, 0.5)

    '''
    #4 This function tests the face detection 
    '''
    def test_get_image_faces(self):
        for test_case in self.test_cases:
            # Set image url
            self.image_detector.set_image_url(image_url=test_case["image_url"])
            # Expected emotion
            ex_emotion = test_case["overall_emotion"]
            # Emotion
            emotion = self.image_detector.get_image_faces()
            # Test will pass if the similarity score > 0.5
            self.assertEqual(ex_emotion, emotion)

    '''
    #5 This function run automated test case generation

    def test_get_image_labels_random(self, num_of_cases=10):
        pass

    '''
    def test_get_image_labels_random(self):
        # Get the randomized test cases
        test_cases = self.get_randomized_test_cases(num_of_cases=10)
        # Test image label for each case
        self.image_labels(test_cases)

    def get_randomized_test_cases(self, num_of_cases=10):
        test_cases = []
        # Generate randomized index and get the element from the test_cases
        for i in range(num_of_cases):
            index = random.randint(0,2)
            test_cases.append(self.test_cases[index])
        return test_cases

if __name__ == "__main__":
    unittest.main()
