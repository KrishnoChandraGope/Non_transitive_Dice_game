from typing import List
from prettytable import PrettyTable  # type: ignore
from dice import Dice

class HelpMenu:
    @staticmethod
    def display_probabilities(probabilities: List[List[float]], dice: List[Dice]):
        table = PrettyTable()
        header = ["User Dice"] + [", ".join(map(str, d.faces)) for d in dice]
        table.field_names = header

        for i, row in enumerate(probabilities):
            formatted_row = [f"{p:.4f}" if i != j else f"- ({p:.4f})" for j, p in enumerate(row)]
            table.add_row([", ".join(map(str, dice[i].faces))] + formatted_row)

        print("\nProbability of the win for the user:")
        print(table)