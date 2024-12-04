from scipy.io.wavfile import read, write


def read_in_wav(general_config):
    # reads in wav file into a numpy array.
    sampling_rate, data = read(general_config.song_file_path)
    # Updates sample rate
    general_config.set_sample_rate(sampling_rate)

    general_config.set_channel_count_from_wav()

    return data
