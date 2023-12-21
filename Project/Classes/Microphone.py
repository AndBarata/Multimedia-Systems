class Microphone:
    def __init__(self, state, sampleFrequency, systemID, audioSize):
        self.state = state
        self.sampleFrequency = sampleFrequency
        self.systemID = systemID
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
        return recording
