class stringClass():
    def get_string(self, some_string):
        self.some_string = some_string

    def print_string(self):
        print(self.some_string.upper())



wordtoup = stringClass()
x = input()

wordtoup.get_string(x)

wordtoup.print_string()



