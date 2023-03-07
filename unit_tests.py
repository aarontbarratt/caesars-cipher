import unittest
import main

cc = main.CaesarsCipher()


class TestCaesarsCiper(unittest.TestCase):
    def setUp(self):
        self.text = "Aaron"

    def test_input_exists(self):
        self.assertIsNotNone(self.text)

    def test_input_type(self):
        self.assertIsInstance(self.text, str)

    def test_output_type(self):
        self.assertIsInstance(cc.encrypt(self.text), str)

    def test_length(self):
        self.assertEqual(len(self.text), len(cc.encrypt(self.text)))

    def test_different_IO(self):
        self.assertNotIn(self.text, cc.encrypt(self.text))

    def test_caesars_cipher(self):
        self.assertEqual("Bbspo", cc.encrypt(self.text))


if __name__ == "__main__":
    unittest.main()
