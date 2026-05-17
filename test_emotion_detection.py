import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test Case 1: Check for Joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test Case 2: Check for Anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test Case 3: Check for Sadness
        result_3 = emotion_detector('I am so sad about this')
        self.assertEqual(result_3['dominant_emotion'], 'sadness')
        
        # Test Case 4: Check for Fear
        result_4 = emotion_detector('I am really scared of this')
        self.assertEqual(result_4['dominant_emotion'], 'fear')
        
        # Test Case 5: Check for Disgust
        result_5 = emotion_detector('I am so disgusted by this')
        self.assertEqual(result_5['dominant_emotion'], 'disgust')

if __name__ == '__main__':
    unittest.main()