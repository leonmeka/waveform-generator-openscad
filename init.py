from src.model_generator import ModelGenerator
from src.input_handler import InputHandler
import os

"""
AUDIO WAVEFORM MODEL GENERATOR

This script generates a 3D model of an audio waveform.
It takes an audio file as input and creates a 3D model in OpenSCAD format.

Configuration Parameters:
    - 'width': Width of the waveform model in OpenSCAD units.
    - 'scale': Scaling factor applied to the amplitude values for visual representation.
    - 'thickness': Thickness of each waveform element (cubes).
    - 'threshold': Minimum amplitude threshold for including a cube in the model.
    - 'resolution': Number of subdivisions per waveform element for smoother rendering.
    - 'input_path': Path to the input audio file (e.g., "./assets/audio.wav").
    - 'output_path': Path to save the generated OpenSCAD model file (e.g., "./result/output.scad").

Dependencies:
Run `pip install -r requirements.txt` to install the required dependencies.

Author: Leon Meka
"""

if __name__ == "__main__":
    print("\n────────────────────────────────────────")
    print("    AUDIO WAVEFORM MODEL GENERATOR  ")
    print("  Free and Open Technologies VU WS23  ")
    print("────────────────────────────────────────\n")
    
    input_handler = InputHandler(assets_folder="./assets")
    audio_files = input_handler.list_audio_files()
    
    if not audio_files:
        print("No audio files found in the 'assets' folder.")
    else:
        selection = input_handler.prompt_user_selection(audio_files)
        
        try:
            selection = int(selection)
            if 1 <= selection <= len(audio_files):
                selected_audio_file = os.path.join(input_handler.assets_folder, audio_files[selection - 1])
                print(f"Selected audio file: {selected_audio_file}")
                
                modelGenerator = ModelGenerator(
                    width=10,
                    scale=10,
                    thickness=0.01,
                    threshold=0.01,
                    resolution=10,
                    input_path=selected_audio_file,
                    output_path="./output/model.scad"
                )
                modelGenerator.run()
                modelGenerator.open()
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")