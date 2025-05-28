from flask import Flask, jsonify, request
from cipher.caesar import CaesarCipher
app = Flask(__name__)

ceasar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.json()
    plaint_text = data.get('plaint_text')
    key = int(data['key'])
    encrypted_text = ceasar_cipher.encrypt(plaint_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.json()
    encrypted_text = data.get('encrypted_text')
    key = int(data['key'])
    decrypted_text = ceasar_cipher.decrypt(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0', port=5000)
    