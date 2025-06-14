from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("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")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    
    answer = response['choices'][0]['message']['content'].strip()
    return jsonify({'answer': answer})
