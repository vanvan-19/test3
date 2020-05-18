import requests
import json

class ImageDetector():

    GOOGLE_VISION_API_URL = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCAWdPG_HuzbBTTHM4MsVOv82qIIzeAC34"

    '''
    #1 This method initialise the class with the parameter of image url
    '''
    def __init__(self, image_url):
        # Initialise Google Vision API
        self.image_url = image_url

    '''
    #2 This method will analyse and label the image
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
        return json.loads(result.text)["responses"][0]["labelAnnotations"]
        