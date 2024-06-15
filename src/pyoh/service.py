from .recorder import Recorder
from .mock_bank import MockBank

class Service:
    recorder: Recorder

    def __init__(self, bank: MockBank):
        self.recorder = Recorder(bank)

    def run(self):
        while True:
            mock_trxs = [f"trx{i}" for i in range(20)]
            self.recorder.record_transactions(mock_trxs)
            self.recorder.tick()
