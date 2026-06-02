# quite/core.py
from lupa import LuaRuntime
from .bindings import expose_to_lua
import pygame

class QuiteEngine:
    def __init__(self, title="Quite Game"):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        # Expose the functions
        expose_to_lua(self.lua, self)

    def run_script(self, script_path):
        # Read and run the Lua script
        with open(script_path, 'r') as f:
            self.lua.execute(f.read())
            
        # The main engine loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Here, your game would ideally call Lua functions 
            # for logic and rendering every frame.
            
            pygame.display.flip()
            self.clock.tick(60) # Lock to 60 FPS
            
        pygame.quit()