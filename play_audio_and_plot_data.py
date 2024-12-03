import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sounddevice as sd
from scipy.io import wavfile

# Load the .wav file
sample_rate, data = wavfile.read('Chikoi_The_Maid_song.wav')

# Convert stereo to mono if necessary
if len(data.shape) > 1:
    data = np.mean(data, axis=1)

# Normalize the data to float32 for playback
data = data / np.max(np.abs(data), axis=0)  # Normalize to [-1.0, 1.0]
volume = 0.2  # Adjust this value to set the playback volume
data = data * volume

# Define playback and FFT parameters
chunk_size = 1024  # Number of samples per chunk
frequencies = np.fft.rfftfreq(chunk_size, 1 / sample_rate)  # Positive frequencies

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 6))
magnitude = np.zeros(len(frequencies))
line, = ax.plot(frequencies, magnitude)
ax.set_xlim(0, 2000)  # Limit x-axis to a reasonable range (e.g., 0-2000 Hz)
ax.set_ylim(0, 1)  # Initial y-axis range; will auto-adjust dynamically
ax.set_title("Live Frequency Spectrum")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")

# Shared buffer for audio chunks
audio_chunk = np.zeros(chunk_size)

# Audio callback function
def audio_callback(outdata, frames, time, status):
    global audio_chunk
    if status:
        print(f"Audio status: {status}")
    start_index = audio_callback.counter * chunk_size
    end_index = start_index + chunk_size
    if end_index > len(data):
        outdata[:len(data) - start_index] = data[start_index:end_index].reshape(-1, 1)
        outdata[len(data) - start_index:] = 0
    else:
        outdata[:] = data[start_index:end_index].reshape(-1, 1)
    audio_chunk = data[start_index:end_index]  # Update shared chunk for FFT
    audio_callback.counter += 1

audio_callback.counter = 0  # Initialize playback frame counter

# Update function for the plot
def update(frame):
    global audio_chunk
    # Apply a Hamming window to the chunk
    windowed_data = audio_chunk * np.hamming(len(audio_chunk))
    # Compute FFT
    fft_data = np.fft.rfft(windowed_data)
    magnitude = np.abs(fft_data)
    # Normalize magnitude for visualization
    magnitude = magnitude / np.max(magnitude) if np.max(magnitude) > 0 else magnitude
    # Update the line plot
    line.set_ydata(magnitude)
    return line,

# Set up the audio stream
with sd.OutputStream(callback=audio_callback, samplerate=sample_rate, channels=1, blocksize=chunk_size):
    ani = FuncAnimation(fig, update, interval=chunk_size / sample_rate * 1000, blit=True)
    plt.show()
