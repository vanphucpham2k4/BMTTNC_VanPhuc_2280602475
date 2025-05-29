class PlayFairCipher:
    def __init__(self, key):
        self.matrix = self.generate_key_matrix(key)
    

    def generate_key_matrix(self, key):
        key = key.upper().replace('J', 'I')
        seen = set()
        matrix = []
        for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(self, char):
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val == char:
                    return i, j
        return None, None

    def prepare_text(self, text, for_encrypt=True):
        text = text.upper().replace('J', 'I')
        text = ''.join(filter(str.isalpha, text))
        result = ''
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else 'X'
            if a == b:
                result += a + 'X'
                i += 1
            else:
                result += a + b
                i += 2
        if len(result) % 2 != 0:
            result += 'X'
        return result

    def encrypt(self, plaintext):
        text = self.prepare_text(plaintext)
        cipher_text = ''
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            r1, c1 = self.find_position(a)
            r2, c2 = self.find_position(b)
            if r1 == r2:
                cipher_text += self.matrix[r1][(c1+1)%5] + self.matrix[r2][(c2+1)%5]
            elif c1 == c2:
                cipher_text += self.matrix[(r1+1)%5][c1] + self.matrix[(r2+1)%5][c2]
            else:
                cipher_text += self.matrix[r1][c2] + self.matrix[r2][c1]
        return cipher_text

    def decrypt(self, cipher_text):
        text = self.prepare_text(cipher_text, for_encrypt=False)
        plain_text = ''
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            r1, c1 = self.find_position(a)
            r2, c2 = self.find_position(b)
            if r1 == r2:
                plain_text += self.matrix[r1][(c1-1)%5] + self.matrix[r2][(c2-1)%5]
            elif c1 == c2:
                plain_text += self.matrix[(r1-1)%5][c1] + self.matrix[(r2-1)%5][c2]
            else:
                plain_text += self.matrix[r1][c2] + self.matrix[r2][c1]
        return plain_text

    def get_matrix(self):
        return self.matrix

