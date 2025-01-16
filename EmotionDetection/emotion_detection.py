import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json = Input, headers = Headers)
    
    if response.status_code == 200:
        emotions = json.loads(response.text)["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions.values())
        for emotion,score in emotions.items():
            if score == dominant_emotion:
                emotions["dominant_emotion"] = emotion
                break

        return emotions
    
    if response.status_code == 400:

        return {"anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
                }

if __name__ == "__main__":
    text = input("Enter the text input : ")
    print(emotion_detector(text))