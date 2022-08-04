from female import Woman


class Girl(Woman):
    def __init__(self, name, dob, address, school_name):
        super().__init__(name, dob, address)
        self.height = "0.8"
        self.school = school_name
        self.language = "undeveloped"

    def sleep(self):
        return "zzz"

    def playBulldog(self):
        return "yum"

    def read_horror(self):
        return "ah so scary! "


h5 = Girl("Sam","311000","33","Scargill")
print(h5.height)

# print(h5.prefix)
# print(h5.playBulldog())
