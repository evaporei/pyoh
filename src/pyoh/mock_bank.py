class MockBank:
    def __init__(self):
        self.tick_height = 0

    def register_tick(self, tick_hash: str):
        print("new height")
        self.tick_height += 1
        # do something with tick_hash
