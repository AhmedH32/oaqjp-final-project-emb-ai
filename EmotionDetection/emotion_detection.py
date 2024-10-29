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
    if (response.status_code == 400):
        answer = {'anger' : None, 'disgust' : None, 'fear' : None, 'joy' : None, 'sadness' : None}
        answer['dominantEmotion'] = None
        return answer
    formatted = json.loads(response.text)
    anger = formatted['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted['emotionPredictions'][0]['emotion']['fear']
    joy = formatted['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted['emotionPredictions'][0]['emotion']['sadness']

    answer = {'anger' : anger, 'disgust' : disgust, 'fear' : fear, 'joy' : joy, 'sadness' : sadness}
# Find the variable with the maximum value
    max_variable = max(answer, key=answer.get)
    answer['dominantEmotion'] = f'{max_variable}'
    return answer
