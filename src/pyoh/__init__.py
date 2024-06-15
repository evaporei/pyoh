from .service import Service
from .mock_bank import MockBank

def main() -> int:
    bank = MockBank()
    s = Service(bank)
    print("start")
    s.run()
    return 0
