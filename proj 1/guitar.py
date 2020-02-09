class Guitar:
    DEFAULT_STRING_COUNT : int = 6
    DEFAULT_STRING_GAUGE : int = 3221 
    DEFAULT_TUNING : str = "E A D G B E"
    ACCEPTABLE_NOTES : list = ['Ab','A','A#','Bb','B','C','C#','Db','D','D#','Eb','E','F','F#','Gb','G','G#']
    DEFAULT_VOLUME : float = 0.0

    def __init__(self, tuning : str = DEFAULT_TUNING, stringCount : int = DEFAULT_STRING_COUNT, stringGauge : int = DEFAULT_STRING_GAUGE, volume : float = DEFAULT_VOLUME):
      self._stringCount = stringCount
      self._stringGauge = stringGauge
      self._tuning = tuning
      self._volume = volume

    @property
    def stringCount(self):
        return self._stringCount

    @stringCount.setter
    def stringCount(self, numStrings : int):
        if numStrings < 0:
            numStrings = 0
        self._stringCount = numStrings

    @property
    def stringGauge(self):
        return self._stringGauge
    
    @stringGauge.setter
    def stringGauge(self, strGauge : int):
        self._stringGauge = strGauge

    @property
    def tuning(self):
        return self._tuning

    @tuning.setter
    def tuning(self, vals : str):
        newVals = list(vals.split(" "))
        if len(newVals) != self._stringCount:
            vals = self.DEFAULT_TUNING
        for note in newVals:
            if note not in self.ACCEPTABLE_NOTES:
                vals = self.DEFAULT_TUNING
        self._tuning = vals


    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, vol : float):
        if (vol < 0):
            vol = 0
        elif (vol > 10):
            vol = 10
        self._volume = vol