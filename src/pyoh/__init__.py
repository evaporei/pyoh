from .service import Service

def main() -> int:
    s = Service()
    print("start")
    s.run()
    return 0
