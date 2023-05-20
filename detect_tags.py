import json
import os

import streamlit as st
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# with open("secret.json") as f:
#     secret = json.load(f)
# KEY = secret["KEY"]
# ENDPOINT = secret["ENDPOINT"]
KEY = st.secrets.AzureApiKey.KEY
ENDPOINT = st.secrets.AzureApiKey.ENDPOINT
client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))


def get_tags(file_path: str) -> list[str]:
    tag_list = [str]
    local_image = open(file_path, "rb")
    image_analysis = client.analyze_image_in_stream(local_image, visual_features=[VisualFeatureTypes.tags])

    for tag in image_analysis.tags:
        tag_list.append(tag.name)
    tag_list.pop(0)
    return tag_list


def detect_objects(file_path: str) -> list:
    local_image = open(file_path, "rb")
    detected_objects_result = client.detect_objects_in_stream(local_image, visual_features=[VisualFeatureTypes.objects])
    objects = detected_objects_result.objects
    return objects


if __name__ == "__main__":
    local_image_path = "//Users/a81701/code/streamlit/detection/img/sample01.jpg"
    print(get_tags(local_image_path))

    # l = detect_objects(local_image_path)
    # for obj in l:
    #     print(obj.object_property)
