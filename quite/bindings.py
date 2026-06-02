# quite/bindings.py
import pygame

def expose_to_lua(lua_runtime, engine_instance):
    # Graphics
    def draw_image(path, x, y):
        img = pygame.image.load(path)
        engine_instance.screen.blit(img, (x, y))

    # Audio
    def play_sound(path):
        sound = pygame.mixer.Sound(path)
        sound.play()

    # Input: Check if a specific key is held down (e.g., "K_SPACE")
    def is_key_pressed(key_name):
        keys = pygame.key.get_pressed()
        key_constant = getattr(pygame, key_name.upper(), None)
        if key_constant:
            return keys[key_constant]
        return False

    # Input: Get mouse position as (x, y)
    def get_mouse_pos():
        return pygame.mouse.get_pos()

    # Input: Check if mouse button is pressed (0: left, 1: middle, 2: right)
    def is_mouse_pressed(button_id):
        buttons = pygame.mouse.get_pressed()
        if 0 <= button_id < len(buttons):
            return buttons[button_id]
        return False

    # Mapping Python functions to Lua global functions
    lua_runtime.globals().draw_image = draw_image
    lua_runtime.globals().play_sound = play_sound
    lua_runtime.globals().is_key_pressed = is_key_pressed
    lua_runtime.globals().get_mouse_pos = get_mouse_pos
    lua_runtime.globals().is_mouse_pressed = is_mouse_pressed