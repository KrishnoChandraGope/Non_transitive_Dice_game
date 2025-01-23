from typing import List
import random

class Dice:
    def __init__(self, faces: List[int]):
        self.faces = faces

    def roll(self) -> int:
        return random.choice(self.faces)