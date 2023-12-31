import math
from MusicNote import MusicNote

class ProcessingManager:
    def __init__(self):
        self.microphone = None
        self.windowSize = 0.0007 # seconds
        self.minF0 = 110.0 # A2
        self.maxF0 = 880.0 # A5
        self.sampleFrequency = 44100.0 # Hz
        self.referenceFrequency = 440.0 # Hz
        self.referenceNoteNumber = 69 # A4

    def getMicrophone(self):
        return self.microphone

    def getWindowSize(self):
        return self.windowSize

    def getMinF0(self):
        return self.minF0

    def getMaxF0(self):
        return self.maxF0

    def getSampleFrequency(self):
        return self.sampleFrequency

    def setWindowSize(self, newWindowSize):
        self.windowSize = newWindowSize

    def setSampleFrequency(self, newSampleFrequency):
        self.sampleFrequency = newSampleFrequency
        
    def setMinF0(self, newMinF0):
        self.minF0 = newMinF0

    def setMaxF0(self, newMaxF0):
        self.maxF0 = newMaxF0

    def searchForMicrophone(self):
        # TODO: Implement this method
        pass

    def calculateF0(self, signal):
        # TODO: Implement this method
        pass

    def calculateZeroCrossingRate(self, signal):
        # TODO: Implement this method
        pass

    def calculateEnergy(self, signal):
        # TODO: Implement this method
        pass

    def filterNoise(self, zcr, energy):
        # TODO: Implement this method
        pass

    def calculateRythm(self, signal, zcr, energy):
        # TODO: Implement this method
        pass

    def calculatePitch(self, f0):
        # Calculate pitch from frequency
        return round(12 * math.log2(f0 / self.referenceFrequency) + self.referenceNoteNumber)
 

    def createMusicNote(self, pitch, rhythm, timestamp, frequency, zeroCrossingRate, sampleFrequency, duration):
        # Create a MusicNote object
        
        return MusicNote(
            pitch, # pitch number
            rhythm, # rhythm
            timestamp, # ts
            frequency, # freq
            zeroCrossingRate, # zcr
            sampleFrequency, # fs
            duration # duration
        )