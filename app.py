from flask import Flask, request, jsonify, render_template
import boto3
from templates import *


app = Flask(_name_)

# Initialize the Amazon Comprehend client
comprehend = boto3.client('comprehend', region_name='ca-central-1')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Call Amazon Comprehend to detect sentiment
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment_scores = response['SentimentScore']
    return jsonify(sentiment_scores)


if _name_ == '_main_':
    app.run(debug=True)
    
