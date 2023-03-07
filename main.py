class CaesarsCipher:
    def __init__(self):
        import string

        self.alphabet = string.ascii_letters + string.punctuation + string.digits + " "

    def encrypt(self, message: str):
        answer = ""

        for character in message:
            for i, letter in enumerate(self.alphabet):
                if character == letter and i + 1 == len(self.alphabet):
                    answer = answer + self.alphabet[0]
                elif character == letter:
                    answer = answer + self.alphabet[i + 1]
        return answer

    def decrypt(self, message: str):
        answer = ""
        for character in message:
            for i, letter in enumerate(self.alphabet):
                if character == letter and i == 0:
                    answer = answer + self.alphabet[len(self.alphabet) - 1]
                elif character == letter:
                    answer = answer + self.alphabet[i - 1]
        return answer


if __name__ == "__main__":
    cc = CaesarsCipher()

    text = "Hello my name is Aaron. I really like to eat dogs :)"
    text_encrypted = cc.encrypt(text)
    print(text_encrypted)

    text_decrypted = cc.decrypt(text_encrypted)
    print(text_decrypted)
