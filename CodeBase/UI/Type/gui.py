from CodeBase.UI.Type.ui_parent import UIParent


class GUI(UIParent):
    def __init__(self, music_object):
        super().__init__("gui", music_object)
