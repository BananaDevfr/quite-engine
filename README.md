# Quite Engine

Quite is a lightweight, easy-to-use game engine that allows you to bundle your game assets and logic into a single Use the packer.py script to bundle your game folder:

## Features
* **Simple Packaging:** Bundles D, Lua, XML, JSON, YML, and media files (PNG/JPG/MP3/WAV) into a single archive.
* **Lua Scripting:** Write your game logic using Lua for flexibility and speed.
* **Built-in Bindings:** Includes easy-to-use functions for graphics, audio, and player input (keyboard/mouse).
* **Cross-Platform:** Built on Python and Pygame.

## How to use

1. **Pack your game:**
   Place your game files (`main.lua`, assets, etc.) in a folder, then run the `packer.py` script to bundle them into a `.qut` archive:
```bash
   python packer.py
   ```
2. **Run your game:**
Use `quite.py` to launch your packaged game file:

```bash
python quite.py my_game.qut
```
## Prerequisites
You will need Python 3 installed. Install the required dependencies via pip:

```bash
pip install pygame lupa