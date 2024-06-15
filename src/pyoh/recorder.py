from hashlib import sha256
import time

from .poh import Poh
from .mock_bank import MockBank

HASHES_PER_TICK = 5

class Recorder:
    def __init__(self, bank: MockBank):
        self.transactions = []
        self.poh = Poh("initial hash", HASHES_PER_TICK)
        self.bank = bank

    def tick(self):
        print("tick")
        mixin = sha256(str(self.transactions).encode()).hexdigest()
        tick_hash = self.poh.tick(mixin)
        self.bank.register_tick(tick_hash)
        self.transactions.clear()
        time.sleep(2)
        
    # would come externally
    def record_transactions(self, transactions: list[str]):
        for trx in transactions:
            self.transactions.append(trx)
