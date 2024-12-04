import time

from CodeBase.Config.general_config import GeneralConfig
from CodeBase.Config.gui_config import GUIConfig
from CodeBase.FileIO.read_in_wav import read_in_wav
from CodeBase.Music.music_object import MusicObject
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

    # Creates the music object
    music_object = MusicObject(data, general_config)

    gui = create_ui(gui_config, music_object)

    gui.begin()
    #music_object.play_sound()