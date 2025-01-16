from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get("textToAnalyze")

    emotion = emotion_detector(text_to_analyze)

    if emotion["dominant_emotion"] is None :
        return "Invalid text! Please try again!"
    else:
        anger = "'anger':" + str(emotion['anger'])
        disgust = "'disgust':" + str(emotion['disgust'])
        fear = "'fear':" + str(emotion['fear'])
        joy = "'joy':" + str(emotion['joy'])
        sadness = "'sadness':" + str(emotion['sadness'])
        formatted_response = f"For the given statement, the system response is {anger}, {disgust}, {fear}, {joy} and {sadness}. The dominant emotion is {emotion['dominant_emotion']}."
        
        return formatted_response

if __name__ == "__main__":
    app.run(debug = True, port = 5000)