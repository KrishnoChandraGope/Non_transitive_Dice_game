from typing import List
from dice import Dice
import random
from fair_random_generator import FairRandomGenerator

class Game:
    def __init__(self, dice: List[Dice]):
        self.dice = dice
        self.fair_generator = FairRandomGenerator()

    def run(self):
        print("\nLet's determine who makes the first move.")
        hmac_value = self.fair_generator.generate(2)
        print(f"I selected a random value in the range 0..1 (HMAC={hmac_value}).")
        user_guess = self._get_user_guess()
        computer_value, key = self.fair_generator.reveal()
        print(f"My selection: {computer_value} (KEY={key.hex()}).")

        if user_guess == computer_value:
            print("You guessed correctly. You make the first move.")
            self.user_turn()
        else:
            print("I make the first move.")
            self.computer_turn()

    def user_turn(self):
        user_dice = self._select_dice("Choose your dice:")
        computer_dice = self._computer_choose_dice(user_dice)
        print(f"I choose the {computer_dice.faces} dice.")
        self._play_round(user_dice, computer_dice)

    def computer_turn(self):
        computer_dice = self._computer_choose_dice()
        print(f"I choose the {computer_dice.faces} dice.")
        user_dice = self._select_dice("Choose your dice:", exclude=computer_dice)
        self._play_round(user_dice, computer_dice)

    def _play_round(self, user_dice: Dice, computer_dice: Dice):
        print("\nIt's time for my throw.")
        computer_throw = self._fair_throw(len(computer_dice.faces))
        print(f"My throw: {computer_throw}.")

        print("\nIt's time for your throw.")
        user_throw = self._fair_throw(len(user_dice.faces))
        print(f"Your throw: {user_throw}.")

        if user_throw > computer_throw:
            print("You win!")
        elif user_throw < computer_throw:
            print("I win!")
        else:
            print("It's a tie!")

    def _fair_throw(self, range_max: int) -> int:
        hmac_value = self.fair_generator.generate(range_max)
        print(f"I selected a random value in the range 0..{range_max - 1} (HMAC={hmac_value}).")
        user_input = self._get_user_guess(range_max)
        computer_value, key = self.fair_generator.reveal()
        print(f"My number is {computer_value} (KEY={key.hex()}).")
        result = (user_input + computer_value) % range_max
        print(f"The result is {user_input} + {computer_value} = {result} (mod {range_max}).")
        return result

    def _get_user_guess(self, range_max: int = 2) -> int:
        while True:
            user_input = input(f"Choose a number between 0 and {range_max - 1}: ")
            if user_input.isdigit() and 0 <= int(user_input) < range_max:
                return int(user_input)
            print("Invalid input. Try again.")

    def _select_dice(self, prompt: str, exclude: Dice = None) -> Dice:
        while True:
            print(prompt)
            for i, d in enumerate(self.dice):
                if d != exclude:
                    print(f"{i} - {d.faces}")
            user_input = input("Your selection: ")
            if user_input.isdigit() and 0 <= int(user_input) < len(self.dice):
                selected = self.dice[int(user_input)]
                if selected != exclude:
                    return selected
            print("Invalid selection. Try again.")

    def _computer_choose_dice(self, exclude: Dice = None) -> Dice:
        available_dice = [d for d in self.dice if d != exclude]
        return random.choice(available_dice)
