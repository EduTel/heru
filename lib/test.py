from translate import Translate
o_translate = Translate(orden="sxocqnmwpfyheljrdgui",foo_letters="udxsmpf")

assert o_translate.preposition("ddxsmp")==True
assert o_translate.preposition("1dxsmp")==False # tiene un signo que no es una letra
assert o_translate.preposition("udxsmp")==False # tiene una u

assert o_translate.verbs("ddxsmpi")==True
assert o_translate.verbs("ddxsmpp")==False # no termina en "bar letters"

assert o_translate.inflected_in_its_subjunctive("ddxsmpi")==False # no inicia con "bar letters"
assert o_translate.inflected_in_its_subjunctive("odxsmpi")==True

assert o_translate.parse_herucode_to_decimal("gxjrc")==605637