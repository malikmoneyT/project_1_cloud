from flask import Flask, render_template, request, jsonify
from comprehend_service import ComprehendService

app = Flask(__name__)

AWS_REGION = 'ca-central-1'
comprehend_service = ComprehendService(AWS_REGION)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = comprehend_service.analyze_sentiment(text)
    sentiment = result['Sentiment']
    return jsonify(sentiment)

if __name__ == '__main__':
    app.run(debug=True)
