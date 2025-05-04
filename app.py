from flask import Flask, request, jsonify
from config import CLOVA_API_URL, CLOVA_KEY
from ocr.clova_ocr import call_clova_ocr

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    data = request.json
    image_base64 = data.get('image_base64')

    if not image_base64:
        return jsonify({"error": "No image_base64 provided"}), 400

    status_code, extracted_items = call_clova_ocr(CLOVA_API_URL, CLOVA_KEY, image_base64)

    if status_code == 200 and extracted_items:
        return jsonify(extracted_items)
    else:
        return jsonify({
            "error": "OCR failed",
            "status_code": status_code
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
