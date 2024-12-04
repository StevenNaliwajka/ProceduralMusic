import os
import wave

class GeneralConfig:
    def __init__(self):
        self.volume = 0.2

        # gets music samples directory
        music_samples_directory = self.build_music_samples_directory()

        self.song_file_directory = music_samples_directory
        self.song_file_name = "Chikoi_The_Maid_song.wav"
        self.song_file_path = os.path.join(self.song_file_directory, self.song_file_name)

        # (HZ) Standard for audio, the number of samples that is taken per second
        # Sets maximum 'frequency range' to analyzer
        self.sampling_rate = 44100

        # The Number of FastFormatTransform operations that are calculated, determines resolution of freq spectrum
        # Should be kept as a power of 2^#
        # Changes the 'frequency resolution'
        self.fft_size = 4096

        # Analyze every 0.1 seconds # (seconds)
        # Duration of each analyzed frame. Lower = More depth
        self.time_interval = 0.1

        # The size of the sampled window (samples)
        self.window_size = int(self.sampling_rate * self.time_interval)

        # The % of overlap size.
        # The % of overlap from the last used sample to minimize information loss
        # Reduces abrupt changes
        self.window_overlap = 0.5  # 50% overlap ?

        # Human hearing range, Range of freq to analyze (HZ)
        self.frequency_range = (20, 20000)

        # Minimum amplitude threshold, Eliminates noise. (HZ)
        self.magnitude_threshold = 0.001

        self.channel_count = None

    def set_sample_rate(self, sample_rate):
        if sample_rate is None:
            self.sampling_rate = 44100
        else:
            self.sampling_rate = sample_rate

    def set_channel_count_from_wav(self):
        with wave.open(self.song_file_path, 'rb') as wav_file:
            channels = wav_file.getnchannels()  # Get the number of channels
        self.channel_count = channels

    def build_music_samples_directory(self):
        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file_path)
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        parent2_directory = os.path.abspath(os.path.join(parent_directory, os.pardir))
        music_samples_directory = os.path.join(parent2_directory, "MusicSamples")
        return music_samples_directory