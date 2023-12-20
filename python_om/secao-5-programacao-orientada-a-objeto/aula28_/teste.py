class AbstractFoo:
    def __init__(self, name):
        self.name = name
        self._name = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name