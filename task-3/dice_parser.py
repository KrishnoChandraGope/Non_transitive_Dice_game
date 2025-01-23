from typing import List
from dice import Dice

class DiceParser:
    @staticmethod
    def parse_dice(args: List[str]) -> List[Dice]:
        dice_list = []
        for arg in args:
            try:
                faces = list(map(int, arg.split(',')))
                if len(faces) < 1:
                    raise ValueError("Dice must have at least one face.")
                dice_list.append(Dice(faces))
            except ValueError:
                raise ValueError(f"Invalid dice configuration: '{arg}'. Expected a comma-separated list of integers.")
        if len(dice_list) < 3:
            raise ValueError("You must provide at least 3 dice configurations.")
        return dice_list