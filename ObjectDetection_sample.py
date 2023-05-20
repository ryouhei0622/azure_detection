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
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"
"""
END - Quickstart variables
"""


"""
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
"""
print("===== Tag an image - remote =====")
# Call API with remote image
# detect objecs
objects_result_remote = computervision_client.detect_objects(remote_image_url)


# Print results with confidence score
print("Objects in the remote image: ")
if len(objects_result_remote.objects) == 0:
    print("No object detected.")
else:
    for object in objects_result_remote.objects:
        # print("obejct: ", object.object)
        print(
            "object atlocation: {}, {}, {}, {}".format(
                object.rectangle.x,
                object.rectangle.x + object.rectangle.w,
                object.rectangle.y,
                object.rectangle.y + object.rectangle.h,
            )
        )
print()

print("===== Tag an image - local =====")

local_image_path = "/Users/a81701/code/streamlit/detection/02_物体検出アプリ/sample01.jpg"
local_image = open(local_image_path, "rb")

objects_result_remote = computervision_client.detect_objects_in_stream(local_image)


# Print results with confidence score
print("Objects in the remote image: ")
if len(objects_result_remote.objects) == 0:
    print("No object detected.")
else:
    for object in objects_result_remote.objects:
        # print("obejct: ", object.object)
        print(
            "object atlocation: {}, {}, {}, {}".format(
                object.rectangle.x,
                object.rectangle.x + object.rectangle.w,
                object.rectangle.y,
                object.rectangle.y + object.rectangle.h,
            )
        )
print()

"""
END - Tag an Image - remote
"""
print("\nEnd of Computer Vision quickstart.")
