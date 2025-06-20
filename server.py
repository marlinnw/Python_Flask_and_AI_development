"""
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

    # Retrieve the reusult from AI
    result = emotion_detector(text_to_analyze)
    
    # Retrieve the dominant result
    dominant = result['dominant_emotion']

    return "for the given statement, the system response is {}. The dominant emotion is {}" .format(result, dominant)

# Start the flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)