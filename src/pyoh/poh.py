from hashlib import sha256

class Poh:
    def __init__(self, initial_hash: str, hashes_per_tick: int):
        self.curr_hash = initial_hash
        self.hashes_per_tick = hashes_per_tick
        self.num_hashes = 0
        self.remaining_hashes = hashes_per_tick

    def hash_next(self, data: str):
        print("new hash")
        self.curr_hash = sha256((self.curr_hash + data).encode()).hexdigest()
        self.num_hashes += 1
        self.remaining_hashes -= 1

    def tick(self, mixin: str) -> str:
        while self.remaining_hashes:
            self.hash_next(mixin)
        final = self.curr_hash
        print("reset")
        self.reset()
        return final

    def reset(self):
        self.__init__(self.curr_hash, self.hashes_per_tick)
