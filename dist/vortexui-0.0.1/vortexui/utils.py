from PySide6.QtCore import QUrl
from pathlib import Path
def playSfx(sfx, sound_name: str):
    sfx.setSource(
        QUrl.fromLocalFile(Path(__file__).parent / f"sfx/{sound_name}.wav")
    )
    sfx.setVolume(0.3)
    sfx.play()
