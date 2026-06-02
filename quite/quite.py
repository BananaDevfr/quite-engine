import sys
import os
import zipfile
import tempfile
import pygame
from lupa import LuaRuntime

# Import your bindings if you created that file
# from quite.bindings import expose_to_lua 

class QuiteEngine:
    def __init__(self, qut_file):
        self.qut_file = qut_file
        self.temp_dir = tempfile.mkdtemp()
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.lua = LuaRuntime(unpack_returned_tuples=True)

    def run(self):
        # Extract the game
        with zipfile.ZipFile(self.qut_file, 'r') as zip_ref:
            zip_ref.extractall(self.temp_dir)
        
        # Switch to game directory so assets load correctly
        os.chdir(self.temp_dir)
        
        # Run main.lua
        with open('main.lua', 'r') as f:
            self.lua.execute(f.read())
        
        pygame.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        engine = QuiteEngine(sys.argv[1])
        engine.run()
    else:
        print("Usage: python quite.py <game_file.qut>")