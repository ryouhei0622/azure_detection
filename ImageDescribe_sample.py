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
# get tags
tags_result_remote = computervision_client.tag_image(remote_image_url)
# get description
description_results = computervision_client.describe_image(remote_image_url)

# Print results with confidence score
print("Tags in the remote image: ")
if len(tags_result_remote.tags) == 0:
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()

# Print rdescription with confidence score
print("Description of remote image: ")
if len(description_results.captions) == 0:
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
"""
END - Tag an Image - remote
"""
print("\nEnd of Computer Vision quickstart.")
