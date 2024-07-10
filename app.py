from flask import Flask, request, jsonify
from joblib import load
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
from train_model import train_model, preprocess_text
from celery_app import celery

# Initialize Flask app
app = Flask(__name__)

# Attempt to load the trained model from disk
model_path = 'sentiment_model.joblib'
training_file='social_media_comments.csv'
def load_model():
    if os.path.exists(model_path):
        try:
            model = load(model_path)
        except FileNotFoundError as e:
            model = None
            print(f"Error: {e}")
    else:
        model = None
        print(f"Model file '{model_path}' not found.")
    return model

@app.route('/predict', methods=['POST'])
def predict():
    model = load_model()
    if model is None:
        return jsonify({'error': 'Model not loaded. Please check the server logs for more details.'}), 500
    data = request.get_json()
    text = data['text']
    print("the text" + text)
    processed_text = preprocess_text(text)
    print("processed_text" + processed_text)
    prediction = model.predict([processed_text])[0]
    print(prediction)
    predictionResult = 'positive'
    if(prediction == 0):
        predictionResult = 'negative'
    return jsonify({'prediction': predictionResult})

@app.route('/train-model', methods=['POST'])
def train():
    try:
        data = request.get_json()
        modelPath = data.get('modelPath', model_path)
        trainingFile = data.get('trainingFile', training_file)
        train_model.delay(modelPath, trainingFile)        
        return jsonify({'message': 'Training has been started'}), 200
    except Exception as e:
        print(f"Error during training: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
