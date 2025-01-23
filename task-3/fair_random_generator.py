import secrets
import hmac
import hashlib
from typing import Tuple

class FairRandomGenerator:
    def __init__(self):
        self.key = None
        self.number = None

    def generate(self, range_max: int) -> str:
        self.key = secrets.token_bytes(32)
        self.number = secrets.randbelow(range_max)
        hmac_value = hmac.new(self.key, str(self.number).encode(), hashlib.sha3_256).hexdigest()
        return hmac_value

    def reveal(self) -> Tuple[int, bytes]:
        return self.number, self.key