from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)
SECRET_TOKEN = "sk-280304041506tn!"

@app.route('/convert', methods=['POST'])
def convert():
    token = request.headers.get('Authorization')
    if token != f"Bearer {SECRET_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    image_url = data.get('url')

    if not image_url:
        return jsonify({"error": "Missing 'url' in JSON body"}), 400

    try:
        response = requests.get(image_url)
        response.raise_for_status()
        base64_image = base64.b64encode(response.content).decode('utf-8')
        return jsonify({"base64Image": base64_image})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)