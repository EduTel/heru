from translate import Translate
o_translate = Translate(orden="sxocqnmwpfyheljrdgui",foo_letters="udxsmpf")

assert o_translate.preposition("ddxsmp") is True
assert o_translate.preposition("1dxsmp") is False  # tiene un signo que no es una letra
assert o_translate.preposition("udxsmp") is False  # tiene una u

assert o_translate.verbs("ddxsmpi") is True
assert o_translate.verbs("ddxsmpp") is False  # no termina en "bar letters"

assert o_translate.inflected_in_its_subjunctive("ddxsmpi") is False  # no inicia con "bar letters"
assert o_translate.inflected_in_its_subjunctive("odxsmpi") is True

assert o_translate.parse_herucode_to_decimal("gxjrc") == 605637
