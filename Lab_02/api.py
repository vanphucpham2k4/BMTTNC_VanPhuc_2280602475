from flask import Flask, jsonify, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    caesar = CaesarCipher() 
    encrypted_text = caesar.encrypt(plain_text, key)  
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    encrypted_text = data['encrypted_text']
    key = int(data['key'])
    caesar = CaesarCipher()  
    decrypted_text = caesar.decrypt(encrypted_text, key)  
    return jsonify({'decrypted_text': decrypted_text})

vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    if not key or not all(c.isalpha() for c in key):
        return jsonify({'error': 'Key phải chứa chữ cái và không rỗng'}), 400
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    if not key or not all(c.isalpha() for c in key):
        return jsonify({'error': 'Key phải chứa chữ cái và không rỗng'}), 400
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    num_rails = data.get('rails')

    if not plain_text or not isinstance(num_rails, int):
        return jsonify({'error': 'Invalid input'}), 400

    cipher_text = railfence_cipher.rail_fence_encrypt(plain_text, num_rails)
    return jsonify({'cipher_text': cipher_text})


@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    num_rails = data.get('rails')

    if not cipher_text or not isinstance(num_rails, int):
        return jsonify({'error': 'Invalid input'}), 400

    plain_text = railfence_cipher.rail_fence_decrypt(cipher_text, num_rails)
    return jsonify({'plain_text': plain_text})




@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    text = data.get('text')
    key = data.get('key')
    if not text or not key:
        return jsonify({'error': 'Missing text or key'}), 400

    cipher = PlayFairCipher(key)
    encrypted = cipher.encrypt(text)
    return jsonify({'cipher_text': encrypted})


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    text = data.get('text')
    key = data.get('key')
    if not text or not key:
        return jsonify({'error': 'Missing text or key'}), 400

    cipher = PlayFairCipher(key)
    decrypted = cipher.decrypt(text)
    return jsonify({'plain_text': decrypted})

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_create_matrix():
    data = request.get_json()
    key = data.get('key')

    if not key:
        return jsonify({'error': 'Missing key'}), 400

    cipher = PlayFairCipher(key)
    matrix = cipher.get_matrix()

    return jsonify({'matrix': matrix})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)