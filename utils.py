from PySide6.QtCore import QUrl
from pathlib import Path
from getpass import getuser


def playSfx(sfx, sound_name: str):
    source = f"/home/{getuser()}/tars/sfx/{sound_name}.wav"
    sfx.setSource(QUrl.fromLocalFile(source))
    sfx.setVolume(0.3)
    sfx.play()
