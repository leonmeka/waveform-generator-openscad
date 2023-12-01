import openpyscad as ops

class WaveformGenerator:
    def __init__(self, amplitudes, width=100, thickness=1, scale=100, resolution=10):
        self._amplitudes = amplitudes
        self._width = width
        self._thickness = thickness
        self._scale = scale
        self._resolution = resolution

    def create_waveform(self):
        target_width = self._width
        num_cubes = int(target_width / (2 * self._thickness))

        interpolated_amplitudes = self.interpolate_amplitudes()

        result = None
        for i in range(num_cubes):
            amplitude = interpolated_amplitudes[i]
            normalized_amplitude = amplitude / max(interpolated_amplitudes)

            cube_side = 2 * self._thickness
            x_position = i * cube_side

            cube = ops.Cube(size=[cube_side, cube_side, normalized_amplitude * self._scale], center=True).translate([x_position, 0, 0])

            result = result + cube if result else cube

            self._print_progress(i)

        print("\n✅ [INFO] Audio waveform creation complete!")
        return result

    def interpolate_amplitudes(self):
        interpolated_amplitudes = []

        for i in range(len(self._amplitudes) - 1):
            start_amplitude = self._amplitudes[i]
            end_amplitude = self._amplitudes[i + 1]
            for j in range(self._resolution):
                alpha = j / self._resolution
                interpolated_value = start_amplitude * (1 - alpha) + end_amplitude * alpha
                interpolated_amplitudes.append(interpolated_value)

        return interpolated_amplitudes

    def _print_progress(self, i):
        progress = round(i / (self._width / (2 * self._thickness)) * 100, 2)
        progress_bar = ("█" * int(progress // 2) + "-" * (50 - int(progress // 2)))
        print(f"[{progress_bar}] {progress}%", end="\r")
