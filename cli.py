import os
from borges_game import BorgesGame

borges_game = None
TOKEN = os.environ.get('BORGES_TELEGRAM_BOT_TOKEN')

def start():
    global borges_game
    borges_game = BorgesGame()
    print(borges_game.get_initial_message())

def play():
    response1 = borges_game.generate_random()
    print(response1+'\n')

    response1 = borges_game.generate_random()
    print(response1+'\n')

    response1 = borges_game.generate_random()
    print(response1+'\n')
    user_input = input()
    while user_input.lower() != borges_game.get_final_word():
        response = borges_game.predict(user_input)
        print(response[1:])
        user_input = input()
    print("Nuestro texto quedó así: \n")
    print(borges_game.get_total_text())

def main() -> None:
    start()
    play()

if __name__ == "__main__":
    main()
