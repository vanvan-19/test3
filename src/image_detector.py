import requests
import json

class ImageDetector():

    GOOGLE_VISION_API_URL = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCAWdPG_HuzbBTTHM4MsVOv82qIIzeAC34"

    '''
    #1 This function initialises the class with the parameter of image url
    '''
    def __init__(self, image_url):
        # Initialise Google Vision API
        self.image_url = image_url

    '''
    #2 This function will analyse and label the image

    Iteration 0:
    def get_image_labels(self, max_results = 10):
        pass

    '''
    def get_image_labels(self, max_results = 10):
        # Trigger the google vision api to generate labelling

        data = {
            "requests": [
                {
                    "image": {
                        "source": {
                            "imageUri":self.image_url
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
        result = [label["description"] for label in result]
        return result
    
    '''
    #3 Create a function that can detect object from an image. The function will return a list of detected object from the google vision API
       Note that first test must fail. Hint: def get_image_objects(self, ...): pass
    '''

    '''
    #4 Create a function that can detect face from an image. The function will return the list of faces detected within an image.
       Note that first test must fail. Hint: def get_image_faces(self, ...): pass
    '''
