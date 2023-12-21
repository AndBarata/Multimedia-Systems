import sounddevice as sd
import numpy as np

class Microphone:
    def __init__(self, sampleFrequency, audioSize):
        self.state = 'disconnect'
        self.sampleFrequency = sampleFrequency
        self.systemID = 0
        self.audioSize = audioSize

    def getSampleFrequency(self):
        return self.sampleFrequency

    def getSystemID(self):
        return self.systemID

    def setSampleFrequency(self, newFs):
        self.sampleFrequency = newFs

    def acquireAudio(self):
        recording = sd.rec(int(self.sampleFrequency * self.audioSize), samplerate=self.sampleFrequency, channels=1)
        sd.wait()  # Wait for the recording to finish
        if recording.ndim > 1: #Se houver mais que um canal
            recording = np.mean(recording, axis=1)
        return recording
