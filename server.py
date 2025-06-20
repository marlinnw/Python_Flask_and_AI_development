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
    dominant = max(result, key=result.get)

    result_parts = [f"'{k}': {v * 100:.2f}%" for k, v in result.items()]
    result_sentence = ', '.join(result_parts[:-1]) + " and " + result_parts[-1]

    result_str = f"For the given statement, the system response is {result_sentence}. The dominant emotion is {dominant}."
    return result_str

# Start the flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)