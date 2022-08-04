from male import Male


class Boy(Male):
    def __init__(self, name, dob, address, school):
        super().__init__(name, dob, address)
        self.height = "0.8"
        self.school = school
        self.language = "undeveloped"

    def goSchool(self):
        return "i love learning"

    def playTag(self):
        return "so fun wow!!! "

    def read_action(self):
        return "wow this book is so cool. "


# h4 = Boy("Sam","311000","33","Scargill")