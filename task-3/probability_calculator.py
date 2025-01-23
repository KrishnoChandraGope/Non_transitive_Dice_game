from typing import List
from dice import Dice

class ProbabilityCalculator:
    @staticmethod
    def calculate_probabilities(dice: List[Dice]) -> List[List[float]]:
        probabilities = []
        for i, dice1 in enumerate(dice):
            row = []
            for j, dice2 in enumerate(dice):
                if i == j:
                    row.append(0.5)  # Same dice, equal probability
                else:
                    row.append(ProbabilityCalculator._calculate_win_probability(dice1, dice2))
            probabilities.append(row)
        return probabilities

    @staticmethod
    def _calculate_win_probability(dice1: Dice, dice2: Dice) -> float:
        wins = 0
        total = 0
        for face1 in dice1.faces:
            for face2 in dice2.faces:
                total += 1
                if face1 > face2:
                    wins += 1
        return wins / total