class Guitar:
    DEFAULT_STRING_COUNT : int = 6
    DEFAULT_STRING_GAUGE : int = 3221 
    DEFAULT_PICKUPS : str = 'Single Coil'
    DEFAULT_TUNING : str = 'EADGBE'

    def __init__(self, make : str, model : str, stringCount : int = DEFAULT_STRING_COUNT, stringGauge : int = DEFAULT_STRING_GAUGE, pickups : str = DEFAULT_PICKUPS, tuning : str = DEFAULT_TUNING):
      self._make = make
      self._model = model
      self._stringCount = stringCount
      self._stringGauge = stringGauge
      self._pickups = pickups
      self._tuning = tuning

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def stringCount(self):
        return self._stringCount

    @property
    def stringGauge(self):
        return self._stringGauge

    @property
    def pickups(self):
        return self._pickups

    @property
    def tuning(self):
        return self._tuning
