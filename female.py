from human import Human


class Woman(Human):
    def __init__(self, name, dob, address):
        super().__init__(name, dob, address)
        self.__estrogen = True
        self._can_get_pregnant = True
        self.prefix = "Ms"
        self.height = "1.40"

    def __getsPregnant(self):
        return "wow I am looking forward to having a kid"

    def __givesBirth(self):
        return "this hurts"

    def play_female_sport(self):
        return "this is so fun! "


# creates object
# h3 = Woman("Sam","311000","33")
#
# # tries to call the attribute
# try:
#     print(h3.__estrogen)
# except AttributeError:
#     print("That information is private.")
#


# print(h3.play_female_sport())
# print(h3.eat())
# print(h3.name)