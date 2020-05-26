import requests
import json
import argparse

class ImageDetector():

    GOOGLE_VISION_API_URL = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCAWdPG_HuzbBTTHM4MsVOv82qIIzeAC34"

    '''
    #1 These functions initialises the class with the parameter of image url
    '''
    def __init__(self, image_url=""):
        self.image_url = image_url

    '''
    #2 This function will analyse and label the image

    Iteration 0:
    def get_image_labels(self, max_results = 10):
        pass

    '''

    def get_image_labels(self, max_results=10):
        # Trigger the google vision api to generate labelling

        try:
            data = {
                "requests": [
                    {
                        "image": {
                            "source": {
                                "imageUri": self.image_url
                            }
                        },
                        "features": [
                            {
                                "maxResults": max_results,
                                "type": "LABEL_DETECTION"
                            }
                        ]
                    }
                ]
            }

            result = requests.post(url=self.GOOGLE_VISION_API_URL, json=data)

            result = json.loads(result.text)["responses"][0]["labelAnnotations"]
            return result
        except:
            print("Error")
            return []

    '''
    #3 Create a function that can detect object from an image. The function will return a list of detected object from the google vision API
       Note that first test must fail. Hint: def get_image_objects(self, ...): pass
    '''


    def get_image_objects(self, max_results=10):
        # Trigger the google vision api to generate labelling
        try:
            data = {
                "requests": [
                    {
                        "image": {
                            "source": {
                                "imageUri": self.image_url
                            }
                        },
                        "features": [
                            {
                                "maxResults": max_results,
                                "type": "OBJECT_LOCALIZATION"
                            }
                        ]
                    }
                ]
            }

            result = requests.post(url=self.GOOGLE_VISION_API_URL, json=data)
            result = json.loads(result.text)["responses"][0]["localizedObjectAnnotations"]
            return result
        except:
            print("Error")
            return []

    def set_image_url(self, image_url):
        self.image_url = image_url

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_url', type=str, required=False)
    args = parser.parse_args()

    image_url = "https://images.pexels.com/photos/4019754/pexels-photo-4019754.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
    if args.image_url:
        image_url = args.image_url

    image_detector = ImageDetector(image_url=image_url)
    labels = image_detector.get_image_labels()
    objects = image_detector.get_image_objects()
    objects = [obj["name"] for obj in objects]
    labels = [label["description"] for label in labels]
    labels = list(dict.fromkeys(labels))
    objects = list(dict.fromkeys(objects))
    print("=" * 100)
    print("Google Vision API Image Detector")
    print("=" * 100)
    print("Detected Labels: ", ", ".join(labels))
    print("Detected Objects: ", ", ".join(objects))
    print("=" * 100)