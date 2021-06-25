class Translate():

    def __init__(self, orden: str = "", foo_letters: str = "", bar_letters: str = ""):
        self.inf = {
            "orden": "sxocqnmwpfyheljrdgui",
            "foo letters": "udxsmpf",
            "bar letters": ""
        }
        if bar_letters=="":
            self.inf["bar letters"] = [ letter for letter in self.inf["orden"] if letter not in self.inf["foo letters"]]

    def alphabet(self, word: str=""):
        for data in word:
            if data not in self.inf["orden"]:
                return False
        if len(word)>1:
            return True
        else:
            return False

    def preposition(self, word: str = ""):
        if self.alphabet(word) and  len(word) == 6 and word[-1:] in self.inf["foo letters"]:
            u_letter = [ letter for letter in word if letter in ["u"] ]
            if len(u_letter)==0:
                return True
        return False

    def verbs(self, word: str = ""):
        if self.alphabet(word) and len(word) >= 6 and word[-1:] in self.inf["bar letters"]:
            return True
        return False

    def inflected_in_its_subjunctive(self, word):
        if self.verbs(word) and word[:1] in self.inf["bar letters"]:
            return True
        return False

    def parse_herucode_to_decimal(self, herucode):
        if self.alphabet(herucode):
            suma = 0
            contador = 0
            for num in herucode:
                suma = suma + self.inf["orden"].find(num)*(20**contador)
                contador = contador + 1
            return suma
        return False

    def number_to_be_pretty(self, herucode):
        num = self.parse_herucode_to_decimal(herucode)
        if num and num>=81827 and num%3==0:
            return num

    def herucodes_alphabetical_order(self, words=[]):
        return sorted(words,  key=lambda word: [self.inf["orden"].index(c) if c in self.inf["orden"] else ord(c) for c in word])