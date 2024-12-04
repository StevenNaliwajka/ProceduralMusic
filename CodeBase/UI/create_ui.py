from CodeBase.UI.Type.CMD.cmd import CMD
from CodeBase.UI.Type.gui import GUI


def create_ui(gui_config, music_object):
    if gui_config.gui_state:
        return GUI(music_object)
    else:
        return CMD(music_object)
