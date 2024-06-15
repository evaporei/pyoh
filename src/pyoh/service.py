from .recorder import Recorder

class Service:
    recorder: Recorder

    def __init__(self):
        self.recorder = Recorder()

    def run(self):
        while True:
            mock_trxs = [f"trx{i}" for i in range(20)]
            self.recorder.record_transactions(mock_trxs)
            self.recorder.tick()
