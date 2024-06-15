from hashlib import sha256
import time

from .poh import Poh

HASHES_PER_TICK = 5

class Recorder:
    def __init__(self):
        self.transactions = []
        self.poh = Poh("initial hash", HASHES_PER_TICK)

    def tick(self):
        print("tick")
        mixin = sha256(str(self.transactions).encode()).hexdigest()
        self.poh.tick(mixin)
        self.transactions.clear()
        time.sleep(2)
        
    # would come externally
    def record_transactions(self, transactions: list[str]):
        for trx in transactions:
            self.transactions.append(trx)
