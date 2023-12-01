import soundfile as sf

class AmplitudeExtractor:
    def __init__(self, input_path, threshold=0.01):
        self._input_path = input_path
        self._threshold = threshold

    def extract_amplitudes(self):
        data, _ = sf.read(self._input_path)
        amplitudes = [abs(x) for x in data if abs(x) >= self._threshold]
        print(f"📊 [INFO] Extracted: {len(amplitudes)} Amplitudes | Threshold [{self._threshold}]")
        return amplitudes