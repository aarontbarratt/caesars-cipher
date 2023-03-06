class CaesarsCipher:
    def __init__(self):
        self.alphabet = list(map(chr, range(97, 123)))

    def encrypt(self, text: str):
        text = text.lower()
        answer = ""

        for character in text:
            if character not in self.alphabet:
                answer = answer + character
            elif character == "z":
                answer = answer + "a"
            else:
                for x, letter in enumerate(self.alphabet):
                    if character == letter:
                        answer = answer + self.alphabet[x + 1]
        return answer

    def decrypt(self, text: str):
        text = text.lower()
        answer = ""

        for character in text:
            if character not in self.alphabet:
                answer = answer + character
            elif character == "a":
                answer = answer + "z"
            else:
                for x, letter in enumerate(self.alphabet):
                    if character == letter:
                        answer = answer + self.alphabet[x - 1]
        return answer


if __name__ == "__main__":
    cc = CaesarsCipher()

    name = "Hello. My name is Josephine O'Leary. I love big fat cocks up my bum :)"
    name_encrypted = cc.encrypt(name)
    print(name_encrypted)

    print(cc.decrypt(name_encrypted))
