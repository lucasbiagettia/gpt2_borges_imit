from borgesModel import BorgesModel


class BorgesGame:
    total_text = ''
    FINAL_WORD = 'fin'
    INITIAL_MESSAGE = 'Hola, soy un bot entrenado para emular el estilo de escritura de Jorge Luis Borges y estás por empezar a escribir un texto conmigo:'
    def __init__(self):
        self.borges_model = BorgesModel()

    def get_total_text(self):
        return self.total_text
    
    def generate_random(self):
        return self.borges_model.generate_random()

    def predict(self, user_input):
        response = ''
        if user_input.lower() == self.FINAL_WORD:
            response = "Nuestro texto quedó así:\n"
            response = response + self.get_total_text()
        else:
            self.total_text = self.total_text + user_input
            cutted_text = self.get_last_words(self.total_text, 200)
            new_text = self.borges_model.generate(cutted_text, self.count_words(user_input))
            new_text = new_text[len(cutted_text):]
            self.total_text = self.total_text + new_text
            response = new_text
        return response
        
    @staticmethod
    def get_last_words(text, number_of_words):
        words = text.split()
        return ' '.join(words[-number_of_words:])

    @staticmethod
    def count_words(text):
        words = text.split()
        return len(words)
    
    def get_initial_message(self):
        return self.INITIAL_MESSAGE
    
    def get_final_word(self):
        return self.FINAL_WORD
    
    def clean(self):
        self.total_text = ""
    
