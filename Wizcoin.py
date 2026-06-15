class wWizCoin:
    def __init__(self,galleons,sickles,knuts):
        """Create a new Wizcoin Object with galleons, sickeles and knuts."""
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts
    def value(self):
        """ The value (in knuts) of all the coins in this WizCoi object. """
        return (self.galleons*17*29)+(self.sickles*29)+(self.knuts)
    def weightInGrams(self):
        """Returns the weight of the coins in grams. """
        return (self.galleons*31.103)+(self.sickles*11.34)+(self.knuts*5.0)
    