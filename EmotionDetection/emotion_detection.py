''' Execution of emotion_detector method using Watson AI's
    Emotion Predict module API
    The detected emotions are send in a dictionary format
'''
import json
import requests

def emotion_detector(text_to_analyse):
    ''' Function to execute emotion detection with the help of WatsonAI API for Emotion Prediction
        if the input is valid it returns response status code 200 conditional block result and 
        if the input is invalid the result is sent from response status code 400 conditional block
    '''

    domain = 'https://sn-watson-emotion.labs.skills.network/v1/'
    path = 'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    url = domain + path

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = input_text, headers = headers, timeout = 20)
    emotions = json.loads(response.text)["emotionPredictions"][0]["emotion"]

    if response.status_code == 200:
        dominant_emotion = max(emotions.values())
        for emotion,score in emotions.items():
            if score == dominant_emotion:
                emotions["dominant_emotion"] = emotion
                break

    if response.status_code == 400:
        for emotion in emotions.keys():
            emotions[emotion] = None

    return emotions

if __name__ == "__main__":
    text = input("Enter the text input : ")
    print(emotion_detector(text))
