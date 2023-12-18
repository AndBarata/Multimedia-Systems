## Script to test classes .py

from ProcessingManager import ProcessingManager
from MusicSheetManager import MusicSheetManager

processingManager = ProcessingManager()
musicSheetManager = MusicSheetManager(processingManager)


for i in range(0, 10):

    noteNumber = processingManager.calculatePitch(100*(i+1)/2)
    musicNote = processingManager.createMusicNote(
        noteNumber,
        "",
        0,
        125,
        0,
        44100,
        1
    )
    musicSheetManager.addMusicNote(musicNote)
    print("DEBUG: freqs: ", 100*(i+1)/2)
print("\n")
for note in musicSheetManager.sheet.getNotes():
    name = musicSheetManager.pitchList[note.getPitch()]
    print(name)

