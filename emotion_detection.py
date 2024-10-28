"""
This module will contain the functionality for calling the embedded watson NLP
emotion detection library
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    sends a post request to the watson NLP
    args: text inputted by the user and recieved as an arg
    returns: the response text (yet to be formatted)
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/"\
    "NlpService/EmotionPredict"
    print(url)
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url = url, json = myobj, headers = headers)
    return response.text
