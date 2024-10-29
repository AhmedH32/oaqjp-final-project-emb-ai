"""
the main server moduel
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

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
    if response['dominantEmotion'] is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is 'anger': {response['anger']}, "\
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and "\
    f"'sadness': {response['sadness']}. The dominant emotion is {response['dominantEmotion']}."

if __name__ == '__main__':
    app.run(debug = True)
