class Translate():
    """translate according to the rules."""

    def __init__(self, orden: str = "", foo_letters: str = "", bar_letters: str = ""):
        """Inicialize de instance.

        @param orden: str of all alphabet
        @type orden: str

        @param foo_letters: str of only foo letters
        @type foo_letters: str

        @param bar_letters: str of only ber letters
        @type bar_letters: str
        """
        self.orden = orden
        self.foo_letters = foo_letters
        self.bar_letters = bar_letters
        if bar_letters == "":
            self.bar_letters = [letter for letter in self.orden if letter not in self.foo_letters]

    def alphabet(self, word: str = ""):
        """Detect if is a alphabet valid.

        @param word: a word to verify
        @type word: str

        @rtype: bool
        """
        for data in word:
            if data not in self.orden:
                return False
        return len(word) > 1

    def preposition(self, word: str = ""):
        """Detect if is a preposition.

        @param word: a word to verify
        @type word: str

        @rtype: bool
        """
        if self.alphabet(word) and len(word) == 6 and word[-1:] in self.foo_letters:
            u_letter = [letter for letter in word if letter in ["u"]]
            return len(u_letter) == 0
        return False

    def verbs(self, word: str = ""):
        """Detect if is a verbs.

        @param word: a word to verify
        @type word: str

        @rtype: bool
        """
        return self.alphabet(word) and len(word) >= 6 and word[-1:] in self.bar_letters

    def inflected_in_its_subjunctive(self, word: str):
        """Detect if is a subjunctive.

        @param word: a word to verify
        @type word: str

        @rtype: bool
        """
        return self.verbs(word) and word[:1] in self.bar_letters

    def parse_herucode_to_decimal(self, herucode: str):
        """Parse language to decimal.

        @param herucode: a word to parse
        @type herucode: str

        @rtype: bool or int
        """
        if self.alphabet(herucode):
            return sum(self.orden.find(item) * (20**contador) for contador, item in enumerate(herucode))
        return False

    def number_to_be_pretty(self, herucode: str):
        """Detect if is a pretty number.

        @rtype: integer or None
        """
        num = self.parse_herucode_to_decimal(herucode)
        return num and num >= 81827 and num % 3 == 0

    def herucodes_alphabetical_order(self, words: dict = []):
        """Order alphabetically.

        @param herucode: a word to parse
        @type herucode: str

        @rtype: list
        """
        return sorted(words, key=lambda word: [self.orden.index(c) if c in self.orden else ord(c) for c in word])
