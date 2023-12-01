A proof of concept for transforming Audio Waveforms into printable 3D models using openscad

# Description
This script generates a 3D model of an audio waveform.
It takes an audio file as input and creates a 3D model in OpenSCAD format.

## Dependencies:
Run `pip install -r requirements.txt` to install the required dependencies.

## Configuration Parameters:
- 'width': Width of the waveform model in OpenSCAD units.
- 'scale': Scaling factor applied to the amplitude values for visual representation.
- 'thickness': Thickness of each waveform element (cubes).
- 'threshold': Minimum amplitude threshold for including a cube in the model.
- 'resolution': Number of subdivisions per waveform element for smoother rendering.
- 'input_path': Path to the input audio file (e.g., "./assets/audio.wav").
- 'output_path': Path to save the generated OpenSCAD model file (e.g., "./result/output.scad").

## Usage
Drop some audio file(s) in the ./assets folder, configure the generator settings in init.py and run `python init.py` to start the script.
