from game_status import GameStatus
import random

from invalid_operation_exception import InvalidOperationError


class Game:

    def __init__(self, allowed_misses: int = 6):
        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__open_indexes = []
        self.__tried_letters = []
        self.__word = ""
        self.__game_status = GameStatus.NOT_STARTED

    def generate_word(self):
        words = []
        with open("hangman_words_rus.txt", encoding="utf8", mode='r') as file:
            for word in file:
                word = word.strip()
                words.append(word)
        self.__word = random.choice(words)
        self.__open_indexes = [False for _ in self.__word]
        self.__game_status = GameStatus.IN_PROGRESS
        return self.__word

    def guess_letters(self, letter: str):
        if self.tries_counter > self.allowed_misses:
            raise InvalidOperationError(f"Exceeded the max misses limit. Allowed {self.__allowed_misses} attempts")
        if self.__game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f"Inappropriate game status: {self.__game_status}")

        open_any = False
        result = []
        for i, char in enumerate(self.word):
            if char == letter:
                self.__open_indexes[i] = True
                open_any = True
            if self.__open_indexes[i]:
                result.append(char)
            else:
                result.append("-")
        if not open_any:
            self.__tries_counter += 1
        self.__tried_letters.append(letter)
        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.__allowed_misses == self.__tries_counter:
            self.__game_status = GameStatus.LOST
        return "".join(result)

    def __is_winning(self):
        for x in self.__open_indexes:
            if not x:
                return False
        return True

    @property
    def word(self) -> str:
        return self.__word

    @property
    def tried_letters(self) -> list[str]:
        return ''.join(sorted(list(set(self.__tried_letters))))

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def allowed_misses(self) -> int:
        return self.__allowed_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def remaining_tries(self) -> int:
        return self.allowed_misses - self.__tries_counter
