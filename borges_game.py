from borgesModel import BorgesModel

class BorgesGame:
    total_text = ""
    def __init__(self):
        self.borges_model = BorgesModel()

    def get_total_text(self):
        return self.total_text

    def predict(self, user_input):
        self.total_text = self.total_text + user_input
        cutted_text = self.get_last_words(self.total_text, 200)
        new_text = self.borges_model.generate(cutted_text, self.count_words(user_input))
        new_text = new_text[len(cutted_text):]

        self.total_text = self.total_text + new_text
        return new_text
        
    @staticmethod
    def get_last_words(text, number_of_words):
        words = text.split()
        return ' '.join(words[-number_of_words:])

    @staticmethod
    def count_words(text):
        words = text.split()
        return len(words)
    
