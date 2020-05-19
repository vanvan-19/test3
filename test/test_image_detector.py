import sys
sys.path.append('src/')

from image_detector import ImageDetector
import unittest

'''
Test Driven Development (TDD) says when developing a software/application, we develop a software with the expected test result. Therefore, the next part of the software would not continue before the test has passed.

'''

class TestImageDetector(unittest.TestCase):

    # This is the test cases.

    BIRTHDAY_IMAGE_URL = "https://cdn1.parksmedia.wdprapps.disney.com/resize/mwImage/1/960/330/90/media/dm/en-us/global/social-events/event-types/SocialEvents-TypesofEvents-Hero-5x2..jpg"

    '''
    #1 This function sets up the image detector object.
    '''
    @classmethod
    def setUpClass(self):
        self.image_detector = ImageDetector(image_url=self.BIRTHDAY_IMAGE_URL)

    '''
    #2 This function tests the image labelling

    TODO: Create other test cases for each of the function

    Iteration 0: FAIL, because the returned value of get_image_labels() contains nothing.

    '''
    def test_get_image_labels(self):
        expected_labels = ['Event', 'Ceremony', 'Alcohol', 'Happy', 'Drink', 'Leisure', 'Party', 'Fashion accessory', 'Conversation', 'Taste']
        labels = self.image_detector.get_image_labels()
        self.assertListEqual(expected_labels, labels)

    '''
    #3 Create a test function that can detect object from an image. Look at the test above.
    '''

    '''
    #3 Create a test function that can detect object from an image. Look at the test above.
    '''

if __name__ == "__main__":
    unittest.main()