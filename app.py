import textwrap
from borgesModel import BorgesModel

borges_model = BorgesModel()

def start_playng():
  user_input = ""
  print('''Hola, soy un bot entrenado para imitar a Jorge Luis Borges y estás por empezar a escribir un texto conmigo:\n
        Cuando quieras terminar de escribir sólo ingresa 'fin'\n''')
  if user_input == "":
    total_text = ""
    user_input = input("Ingresa tus primeras líneas:\n")
    
    while user_input.lower() != 'fin':
      total_text = total_text + user_input
      new_text = borges_model.generate(get_last_words(total_text, 200), count_words(user_input)*2)
      total_text = total_text + new_text
      print_new(new_text)
      user_input = input()
     
 
def get_last_words(text , number_of_words):
  words = text.split()
  return ' '.join(words[-number_of_words:])


def print_new(text):
  max_lenght = 70

  lines = textwrap.wrap(text, width=max_lenght)

  for line in lines:
      print(line)

def count_words(text):
    words = text.split()
    return len(words)

start_playng()