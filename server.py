"""
the main server moduel
"""
from flask import Flask, render_template, make_response, url_for,request
from EmotionDetection.emotion_detection import *

app = Flask(__name__)

@app.route('/')
def index():
    """
    render homepage
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotiondetection():
    """
    calls the emotiondetection function
    """
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    return f"For the given statement, the system response is 'anger': {response['anger']}, "\
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and "\
    f"'sadness': {response['sadness']}. The dominant emotion is {response['dominantEmotion']}."

if __name__ == '__main__':
    app.run(debug = True)
