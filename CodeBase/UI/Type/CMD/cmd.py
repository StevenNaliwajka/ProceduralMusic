import os
import time

from CodeBase.UI.Type.CMD.UserInput.get_user_input_int import get_number_int_float
from CodeBase.UI.Type.ui_parent import UIParent


class CMD(UIParent):
    def __init__(self, music_object):
        super().__init__("cmd", music_object)

    def get_user_input(self):
        run = True
        user_int = None
        while run:
            self.clear_console()
            print("Choose an option:")
            print("0: Exit")
            print("1: Play song ")
            print("2: Play song from X to Y seconds")
            user_input = input("Input: ")
            try:
                user_int = int(user_input)
            except ValueError:
                print("Incorrect Output, Try again.")
                time.sleep(.5)
                continue

            if user_int not in {0, 1, 2}:
                print("Incorrect Output, Try again.")
                time.sleep(.5)
                continue
            time.sleep(.5)
            return user_int

    def clear_console(self):
        if os.getenv('PYCHARM_HOSTED'):  # Detect PyCharm
            print("\n" * 50)  # Print 100 blank lines to simulate clearing
        else:  # For cmd/terminal
            os.system('cls' if os.name == 'nt' else 'clear')

    def exit_program(self):
        print("Quitting")
        time.sleep(.5)
        self.run_state = False

    def play_song(self):
        print("Playing current song")
        self.music_object.play_sound_till_input()

    def play_song_from_x_to_y(self):
        print("Starting point? Seconds: ")
        start = get_number_int_float()
        print("Ending point? Seconds: ")
        end = get_number_int_float()
        self.music_object.play_song_from_x_to_y(start, end)
