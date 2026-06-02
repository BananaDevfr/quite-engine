import zipfile
import os

def pack_game(folder_path, output_name):
    """Packages a directory into a .qut file including media assets."""
    # Added image and audio extensions
    allowed_exts = {
        '.d', '.lua', '.xml', '.json', '.yml', '.yaml', 
        '.png', '.jpg', '.jpeg', '.mp3', '.wav'
    }
    
    output_filename = f"{output_name}.qut"
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as qut_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Check if the file extension is in our allowed list
                if any(file.lower().endswith(ext) for ext in allowed_exts):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    qut_file.write(file_path, arcname)
                    print(f"Added: {arcname}")
    
    print(f"\nSuccessfully created {output_filename}")

# Usage:
# pack_game('my_game_folder', 'my_game')