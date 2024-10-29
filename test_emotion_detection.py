import unittest
from EmotionDetection.emotion_detection import *

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector("I am glad this happened")['dominantEmotion'], 'joy')
        self.assertEqual(emotion_detector("I am really mad about this")['dominantEmotion'], 'anger')
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominantEmotion'], 'disgust')
        self.assertEqual(emotion_detector("I am so sad about this")['dominantEmotion'], 'sadness')
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominantEmotion'], 'fear')

if __name__ == '__main__':
    unittest.main()