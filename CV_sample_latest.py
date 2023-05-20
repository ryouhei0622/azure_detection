"""
cf: https://learn.microsoft.com/ja-jp/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python#analyze-an-image
"""

import json
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

with open("secret.json") as f:
    secret = json.load(f)
KEY = secret["KEY"]
ENDPOINT = secret["ENDPOINT"]

client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
# analysis
print("===== Analyze an image =====")
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
local_image_path = "/Users/a81701/code/streamlit/detection/02_物体検出アプリ/sample01.jpg"
local_image = open(local_image_path, "rb")

image_analysis = client.analyze_image_in_stream(local_image, visual_features=[VisualFeatureTypes.tags])

for tag in image_analysis.tags:
    print(tag.name)

print("===== List models =====")
models = client.list_models()
for x in models.models_property:
    print(x)
