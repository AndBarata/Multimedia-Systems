class MusicNote:
    def __init__(self, pitch, rhythm, timestamp, frequency, zeroCrossingRate, sampleFrequency, duration):
        self.pitch = pitch # Note number
        self.rhythm = rhythm
        self.timestamp = timestamp
        self.frequency = frequency
        self.zeroCrossingRate = zeroCrossingRate
        self.sampleFrequency = sampleFrequency
        self.duration = duration

    def getFrequency(self):
        return self.frequency

    def getZCR(self):
        return self.zeroCrossingRate

    def getSampleFrequency(self):
        return self.sampleFrequency

    def getDuration(self):
        return self.duration
    
    def getPitch(self):
        return self.pitch
