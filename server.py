''' Execution of Emotion Detection using emotion_detector method and 
    deployment using flask framework under localhost:5000
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def render_index():
    ''' Functiion to render index.html page '''
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion_detector_deployment():
    ''' Function handle /emotionDetector as it receives text to analyze input from
        the interface and the emotion_detector returns a dictionary of emotions
        with teir respective scores. This method deploys result according to the input status
    '''

    text_to_analyze = request.args.get("textToAnalyze")

    emotion = emotion_detector(text_to_analyze)

    if emotion["dominant_emotion"] is None :
        return "Invalid text! Please try again!"

    anger = "'anger':" + str(emotion['anger'])
    disgust = "'disgust':" + str(emotion['disgust'])
    fear = "'fear':" + str(emotion['fear'])
    joy = "'joy':" + str(emotion['joy'])
    sadness = "'sadness':" + str(emotion['sadness'])
    res1 = "For the given statement, the system response is "
    res2 = f"{anger}, {disgust}, {fear}, {joy} and {sadness}."
    res3 = f" The dominant emotion is {emotion['dominant_emotion']}."
    formatted_response = res1 + res2 + res3

    return formatted_response

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
