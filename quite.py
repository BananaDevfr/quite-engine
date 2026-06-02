# quite.py (in the root folder)
import sys
from quite.core import QuiteEngine

if __name__ == "__main__":
    if len(sys.argv) > 1:
        engine = QuiteEngine(sys.argv[1])
        engine.run()
    else:
        print("Usage: python quite.py <game_file.qut>")