from human import Human


class Male(Human):
    def __init__(self, name, dob, address):
        super().__init__(name, dob, address)
        self.__testosterone = True
        self._can_get_pregnant = False
        self.prefix = "Mr"
        self.height = "1.80"

    def getsWomanPregnant(self):
        return "wow I am looking forward to having a kid"

    def paternityLeave(self):
        return "cant wait to look after my kid"

    def playMaleSport(self):
        return "this is so much fun! "


# h2 = Male("Sam", "311000", "33")
# print(h2.dob)
# print(h2.paternityLeave())