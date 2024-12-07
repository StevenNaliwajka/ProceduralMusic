import numpy as np
import matplotlib.pyplot as plt


def plot_freq_data_thread(data_queue, stop_event):
    while not stop_event.is_set():
        if not data_queue.empty():
            fft_result, freqs = data_queue.get()

            # Used to demo peak index for troubleshooting maximum data
            peak_index = np.argmax(fft_result)
            print(f"Peak plot freq: {freqs[peak_index]} Hz, Peak Magnitude: {fft_result[peak_index]}")

            # print(f"Shape of freqs: {freqs.shape}")
            # print(f"Shape of fft_result: {fft_result.shape}")
            plt.plot(freqs, fft_result)
            plt.xlabel('Frequency (Hz)')
            plt.ylabel('Magnitude')
            plt.title('FFT of Current Chunk')
            plt.xlim(0, 2000)  # Adjust range
            plt.ylim(0, .2)
            plt.pause(0.01)
            plt.clf()