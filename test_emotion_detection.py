"""
The purpose of the module is to run unit tests
for the function emotion_detector
"""
# Import the required libraries
import unittest
from EmotionDetection.emotion_detection import emotion_detector

# Create the class for performing the unittesting
class TestEmotionDetector(unittest.TestCase):
    # Define the function for testing
    def test_emotion_detector(self):
        """
        The purpose of this function is to provide 5 tests:
            Statement: I am glad this happened
            Dominant Emotion: joy
            Statment: I am really mad about this
            Dominant Emotion: andger
            Statment: I fell disgusted just hearung about this
            Dominant Emotion: disgust
            Statement: I am so sad about this
            Dominant Emotion: sadness
            Statment: I am really afraid that this will happen
            Dominant Emotion: fear
        """
        # Test Case for joy statment
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], "joy")
        # Test Case for anger statement
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], "anger")
        # Test Case for disgust statment
        result_3 = emotion_detector("I fell disgusted just about hearing this")
        self.assertEqual(result_3['dominant_emotion'], "disgust")
        # Test Case for sadness statement
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], "sadness")
        # Test case for fear statement
        result_5 = emotion_detector("I am really afraid this will happen")
        self.assertEqual(result_5['dominant_emotion'], "fear")
unittest.main()