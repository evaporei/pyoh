from .recorder import Recorder

class Service:
    recorder: Recorder

    def __init__(self):
        self.recorder = Recorder()

    def run(self):
        while True:
            self.recorder.tick()
