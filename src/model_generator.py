import os
from src.amplitude_extractor import AmplitudeExtractor
from src.waveform_generator import WaveformGenerator

class ModelGenerator:
    def __init__(self, input_path, output_path, threshold=0.01, scale=100, width=100, thickness=1.0, resolution=10):
        self._input_path = input_path
        self._output_path = output_path
        self._threshold = threshold
        self._scale = scale
        self._width = width
        self._thickness = thickness
        self._resolution = resolution
        self._shouldO = open

    def _ensure_directory_exists(self):
        output_dir = os.path.dirname(self._output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"📁 [INFO] Created directory: {output_dir}")

    def save(self, model):
        self._ensure_directory_exists()
        model.write(self._output_path)
        print(f"💾 [INFO] Waveform saved to: {self._output_path}")

    def open(self):
        os.system("osascript -e 'tell application \"OpenSCAD\" to quit'")
        os.system("sleep 0.1")
        os.system(f"open {self._output_path}")

    def run(self):
        amplitude_extractor = AmplitudeExtractor(self._input_path, self._threshold)
        amplitudes = amplitude_extractor.extract_amplitudes()
        waveform_generator = WaveformGenerator(amplitudes, self._width, self._thickness, self._scale, self._resolution)
        waveform = waveform_generator.create_waveform()
        self.save(waveform)