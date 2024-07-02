from flask import Flask, request, jsonify, render_template
import boto3
from templates import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
