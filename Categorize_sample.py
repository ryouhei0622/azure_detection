import json
import os
import sys
import time
from array import array

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import (
    OperationStatusCodes,
    VisualFeatureTypes,
)
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image

with open("secret.json") as f:
    secret = json.load(f)
"""
Authenticate
Authenticates your credentials and creates a client.
"""
KEY = secret["KEY"]
ENDPOINT = secret["ENDPOINT"]

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
"""
END - Authenticate
"""

"""
Quickstart variables
These variables are shared by several examples
"""
# Images used for the examples: Describe an image, Categorize an image, Tag an image,
# Detect faces, Detect adult or racy content, Detect the color scheme,
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
"""
END - Quickstart variables
"""


"""
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
"""
print("===== Tag an image - remote =====")
# Call API with remote image
# get category
remote_image_features = ["categories"]
categorize_result_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)


# Print results with confidence score
print("Categorize from the remote image: ")
if len(categorize_result_remote.categories) == 0:
    print("No categories detected.")
else:
    for category in categorize_result_remote.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))
print()

"""
END - Tag an Image - remote
"""
print("End of Computer Vision quickstart.")
