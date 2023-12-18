class Microphone:
    def __init__(self, state, sampleFrequency, systemID):
        self.state = state
        self.sampleFrequency = sampleFrequency
        self.systemID = systemID

    def getSampleFrequency(self):
        return self.sampleFrequency

    def getSystemID(self):
        return self.systemID

    def setSampleFrequency(self, newFs):
        self.sampleFrequency = newFs
