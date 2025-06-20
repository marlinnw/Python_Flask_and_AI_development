"""Add commentMore actions
The purpose of this module is to create the flask
server that will run the Emotion Detector web app
"""
#import the required libraries
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create the flask app
app = Flask("Emotion Detector")

# Create the root endpoint
@app.route("/")
def render_index_page():
    """
    The purpose of this function is to render
    the index page
    """
    return render_template("index.html")

# Create the endpoint for 'emotion_detector
@app.route("/emotionDetector")
def RunSentimentAnalysis():
    """
    The purpose of this function is to retrieve
    the analyzedemotional response of the 
    supplied text.
    """
     # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Retrieve the reusult from AI in the form of a dictionary
    result = emotion_detector(text_to_analyze)

    # Return error message for blank text
    if result == {"none": "none"}:
        return "Invalid text! Please try again!"
    
    else:
        # Extract the dominant emotion from the dictionary
        dominant_emotion = result['dominant_emotion']
    
        # Format dictionary and build the sentance
        emotion_parts = [f"'{k}': {v}" for k, v in result.items()]
        emotion_sentence = ', '.join(emotion_parts[:-2]) + " and " + emotion_parts[-2]
        result = f"For the given statement, the system response is {emotion_sentence}. The dominant emotion is {dominant_emotion}."

    # Return the sentance.
        return result
# Start the flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
    