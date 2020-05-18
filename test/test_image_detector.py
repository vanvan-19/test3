import sys
sys.path.append('src/')

from image_detector import ImageDetector
import unittest

class TestImageDetector(unittest.TestCase):

    BIRTHDAY_IMAGE_URL = "https://cdn1.parksmedia.wdprapps.disney.com/resize/mwImage/1/960/330/90/media/dm/en-us/global/social-events/event-types/SocialEvents-TypesofEvents-Hero-5x2..jpg"

    '''
    #1 This method sets up the image detector object.
    '''
    @classmethod
    def setUpClass(self):
        self.image_detector = ImageDetector(image_url=self.BIRTHDAY_IMAGE_URL)

    '''
    #2 This method test the image labelling
    '''
    def test_get_image_labels(self):
        expected_labels = ['Event', 'Ceremony', 'Alcohol', 'Happy', 'Drink', 'Leisure', 'Party', 'Fashion accessory', 'Conversation', 'Taste']
        labels = self.image_detector.get_image_labels()
        labels = [label["description"] for label in labels]
        self.assertListEqual(expected_labels, labels)

if __name__ == "__main__":
    unittest.main()