from abc import abstractmethod


class UIParent:
    def __init__(self, ui_type, music_object):
        self.ui_type = ui_type
        self.run_state = True
        self.music_object = music_object
        self.run_switcher = {
            0: self.exit_program,
            1: self.play_song,
            2: self.play_song_from_x_to_y
        }

    def begin(self):
        while self.run_state:
            user_input = self.get_user_input()
            self.search_run_switcher(user_input)

    def search_run_switcher(self, user_input):
        for item, method in self.run_switcher.items():
            if item == user_input:
                method()
                return

    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def exit_program(self):
        pass

    @abstractmethod
    def play_song(self):
        pass

    @abstractmethod
    def play_song_from_x_to_y(self):
        pass
