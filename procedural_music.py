import threading
import time
from queue import Queue

from CodeBase.Config.general_config import GeneralConfig
from CodeBase.Config.gui_config import GUIConfig
from CodeBase.FileIO.read_in_wav import read_in_wav
from CodeBase.Music.music_object import MusicObject
from CodeBase.UI.Type.FreqVisualize.plot_freq_data_thread import plot_freq_data_thread
from CodeBase.UI.create_ui import create_ui

if __name__ == "__main__":
    print("Procedural Music")
    print("Work in progress by Steven Naliwajka")
    time.sleep(.5)


    # Create config file
    general_config = GeneralConfig()
    gui_config = GUIConfig()
    # reads in file and populates sampling rate
    data = read_in_wav(general_config)

    # Creates GUI for plotting
    fft_queue = Queue()
    plotting_stop_event = threading.Event()
    plotting_thread = threading.Thread(target=plot_freq_data_thread, args=(fft_queue, plotting_stop_event), daemon=True)
    plotting_thread.start()


    # Creates the music object
    music_object = MusicObject(data, general_config, fft_queue)

    gui = create_ui(gui_config, music_object)

    gui.begin()

    # Stop plotting
    plotting_stop_event.set()
    plotting_thread.join()
    #music_object.play_sound()