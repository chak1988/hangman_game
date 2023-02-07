from game import Game
from game_status import GameStatus

game = Game(10)
word = game.generate_word()
len_word = len(word)
print(f"The word consist of {len_word} letters \n Try guess a word letter by letter")


while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Pick a letter : ')
    status = game.guess_letters(letter)
    print(status)
    print(f'Remaining tries : {game.remaining_tries}')
    print(f'Tried letters : {game.tried_letters}')

if game.game_status == GameStatus.LOST:
    print(f"Sorry you are Hanged.\nThe word was {game.word}")
else:
    print('You are WON ! Congratulation !')