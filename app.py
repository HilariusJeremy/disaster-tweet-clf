from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

classifier = pipeline('sentiment-analysis', model='HilariusJeremy/disaster_tweet_distilbert')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    tweet = data['tweet']

    prediction = classifier(tweet)

    top_prediction = prediction[0]
    label = top_prediction['label']
    score = top_prediction['score']

    return jsonify({'prediction': label, 'confidence': score})

if __name__ == '__main__':
    app.run(debug=True)

    
