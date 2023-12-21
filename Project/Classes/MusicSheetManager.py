from MusicNote import MusicNote
from MusicSheet import MusicSheet

class MusicSheetManager:
    def __init__(self, processingManager):
        self.sheet = MusicSheet()
        self._updateFrequency = processingManager.getAudioSize() # seconds
        self.pitchList = { # Associates a number to a note
            45: "lá2",
            46: "lá#2",
            47: "si2",
            48: "dó3",
            49: "dó#3",
            50: "ré3",
            51: "ré#3",
            52: "mi3",
            53: "fá3",
            54: "fá#3",
            55: "sol3",
            56: "sol#3",
            57: "lá3",
            58: "lá#3",
            59: "si3",
            60: "dó4",
            61: "dó#4",
            62: "ré4",
            63: "ré#4",
            64: "mi4",
            65: "fá4",
            66: "fá#4",
            67: "sol4",
            68: "sol#4",
            69: "lá4",
            70: "lá#4",
            71: "si4",
            72: "dó5",
            73: "dó#5",
            74: "ré5",
            75: "ré#5",
            76: "mi5",
            77: "fá5",
            78: "fá#5",
            79: "sol5",
            80: "sol#5",
            81: "lá5"
        }
        self._rhythmList = {
            "semibreve": "sb",
            "mínima": "m",
            "semínima": "sm",
            "colcheia": "c",
            "semicolcheia": "sc",
        }

    def setUpdateFrequency(self, newUpdateFrequency):
        self._updateFrequency = newUpdateFrequency

    def addMusicNote(self, newNote):
        #print("DEBUG: newnote pitch: ", newNote.getPitch())
        self.sheet.allNotes.append(newNote)             # Add note to list of all notes
        if len(self.sheet.getNotes()) < self.sheet.maxDisplayLength:    # If sheet is not full
            self.sheet.notesOnDisplay.append(newNote)

        else:                                           # If sheet is full
            self.sheet.shiftDisplay()
            self.sheet.notesOnDisplay.append(newNote)
            
        

    def _updateLength(self):
        # TODO : Update length of musicSheet
        pass

    def getUpdateFrequency(self):
        return self._updateFrequency