# Google Vision Test

Google vision test is a light python script for testing google vision pretrained machine learning api by Google. This is also one of the assignments for the CSIT314 at University of Wollongong.

## Quick Start
While there is no need to create a virtual environment, we provide a pipfile which for creating a virtual environment and installing requests library. This project requires python 3.6.8 to run.

```
# Running the test
python test/test_image_detector.py

# Running the test of the test
python test/test_test_image_detector.py

# Running the tool with a given url
python image_detector.py --image_url "https://images.pexels.com/photos/4019754/pexels-photo-4019754.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"

```