import sys
from dice_parser import DiceParser
from probability_calculator import ProbabilityCalculator
from help_menu import HelpMenu
from game import Game

if __name__ == "__main__":
    try:
        dice = DiceParser.parse_dice(sys.argv[1:])
        probabilities = ProbabilityCalculator.calculate_probabilities(dice)
        HelpMenu.display_probabilities(probabilities, dice)
        game = Game(dice)
        game.run()
    except ValueError as e:
        print(f"Error: {e}")
        print("Example: python main.py 2,2,4,4,9,9 6,8,1,1,8,6 7,5,3,7,5,3")