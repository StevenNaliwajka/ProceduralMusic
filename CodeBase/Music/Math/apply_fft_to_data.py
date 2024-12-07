import numpy as np


def apply_fft_to_data(chunk_data, sampling_rate, real_data=True):
    if len(chunk_data) == 0:
        return np.array([]), np.array([])
    # avg to mono not sterio
    if chunk_data.ndim > 1:
        chunk_data = chunk_data.mean(axis=1)
    if real_data:
        fft_result = np.fft.rfft(chunk_data)
        freqs = np.fft.rfftfreq(len(chunk_data), d=1 / sampling_rate)
    else:
        fft_result = np.fft.fft(chunk_data)
        freqs = np.fft.fftfreq(len(chunk_data), d=1 / sampling_rate)

        # Used to demo peak index for troubleshooting maximum data
        peak_index = np.argmax(fft_result)
        print(f"Peak FFT Freq: {freqs[peak_index]} Hz, Peak Magnitude: {fft_result[peak_index]}")

    # Correct FFT magnitudes for amplitude scaling
    # fft_magnitudes = (2 * np.abs(fft_result)) / len(chunk_data)
    fft_magnitudes = np.abs(fft_result) / (len(chunk_data) / 2)

    # DC and Nyquist frequencies don't need to be doubled
    if real_data:
        fft_magnitudes[0] /= 2
        if len(chunk_data) % 2 == 0:  # Even-length signal
            fft_magnitudes[-1] /= 2

    return fft_magnitudes, freqs
