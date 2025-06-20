"""
The purpose of this module is to query the IBM AI module.
It sends a text string and the AI runs and analys and
returns a label for the emotion of the text as well
as a score for the response.
"""
# Import the required libraries
import json
import requests

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):
    """
    This function takes an text string as an input
    Returns:
    Text file showing emotion analysis of the input text.
    """
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network' \
    '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    #Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    result = {}

    if response.status_code == 200:
        # Find the emotion scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # Find the strongest emotions
        dominant_emotion = max(emotions, key=emotions.get)
        # Create the output dictionary
        result = emotions.copy()
        result['dominant_emotion'] = dominant_emotion
    
    elif response.status_code == 400:
        result = {"none": "none" }
        
    # Return the dictionary
    return result
