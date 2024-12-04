import threading

import numpy as np
import sounddevice as sd

from CodeBase.UI.GeneralOperations.wait_for_x_before_set_flag import wait_for_x_before_set_flag
from CodeBase.UI.Type.CMD.UserInput.user_input_stop_flag_check import user_input_stop_flag_check


class MusicObject:
    def __init__(self, data, general_config):
        self.general_config = general_config
        # Sets converts data to a NumPy data array.
        if data.dtype != np.float32:
            # Normalize to 0-1
            data = data / np.max(np.abs(data), axis=0)
        # Converts to float32 numpy
        self.data = np.asarray(data, dtype=np.float32)

        # changes volume % setting
        self.data = self.data * general_config.volume

    def _play_audio(self, stop_flag, start_time=0, end_time=None):
        """
        Play audio data dynamically based on start and end times.

        :param stop_flag: Thread-safe flag to stop playback.
        :param start_time: Start time in seconds for playback.
        :param end_time: End time in seconds for playback. If None, play until the end.
        """
        # Calculate start and end indices based on start_time and end_time
        start_index = int(start_time * self.general_config.sampling_rate * self.general_config.channel_count)
        end_index = int(
            end_time * self.general_config.sampling_rate * self.general_config.channel_count) if end_time else len(
            self.data)

        # Ensure indices are within bounds
        start_index = max(0, start_index)
        end_index = min(len(self.data), end_index)

        stream = sd.OutputStream(samplerate=self.general_config.sampling_rate,
                                 channels=self.general_config.channel_count, dtype='float32')
        stream.start()

        # Adjust the starting index
        index = start_index
        while not stop_flag.is_set() and index < end_index:
            # Write chunks of audio data to the stream
            chunk_end_index = min(index + self.general_config.window_size, end_index)
            stream.write(self.data[index:chunk_end_index])
            index = chunk_end_index

        stream.stop()

    def play_sound_till_input(self):
        # Stop flag to stop audio playback
        stop_flag = threading.Event()

        # Plays audio
        audio_thread = threading.Thread(target=self._play_audio, args=(stop_flag,))
        audio_thread.start()

        # Checks for user input to stop
        input_thread = threading.Thread(target=user_input_stop_flag_check, args=(stop_flag,))
        input_thread.start()

        # waits till completed
        audio_thread.join()
        input_thread.join()

    def play_song_from_x_to_y(self, time_start, time_end):
        # plays sound from X to Y (Seconds)
        # Stop flag to stop audio playback
        stop_flag = threading.Event()

        # Plays audio
        audio_thread = threading.Thread(target=self._play_audio, args=(stop_flag, time_start, time_end))
        audio_thread.start()

        # Checks for user input to stop
        input_thread = threading.Thread(target=user_input_stop_flag_check, args=(stop_flag,))
        input_thread.start()

        duration = time_end-time_start
        time_thread = threading.Thread(target=wait_for_x_before_set_flag, args=(duration, stop_flag))
        time_thread.start()

        # waits till completed
        audio_thread.join()
        input_thread.join()
        time_thread.join()
