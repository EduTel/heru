from flask import Flask, request
app = Flask(__name__)

from pprint import pprint
inf = {
    "orden": "sxocqnmwpfyheljrdgui",
    "foo letters": "udxsmpf",
    "bar letters": ""
}
inf["bar letters"] = [ letter for letter in inf["orden"] if letter not in inf["foo letters"]]
#print(inf["bar letters"])
#print(len(inf["orden"]))

def alfabeto(word: str=""):
    for data in word:
        if data not in inf["orden"]:
            return False
    if len(word)>1:
        return True
    else:
        return False

def preposition(word: str = ""):
    if alfabeto(word) and  len(word) == 6 and word[-1:] in inf["foo letters"]:
        u_letter = [ letter for letter in word if letter in ["u"] ]
        #print("u_letter", u_letter)
        if len(u_letter)==0:
            return True
    return False

assert preposition("ddxsmp")==True
assert preposition("1dxsmp")==False # tiene un signo que no es una letra
assert preposition("udxsmp")==False # tiene una u

def verbs(word: str = ""):
    if alfabeto(word) and len(word) >= 6 and word[-1:] in inf["bar letters"]:
        return True
    return False

assert verbs("ddxsmpi")==True
assert verbs("ddxsmpp")==False # no termina en "bar letters"

def inflected_in_its_subjunctive(word):
    if verbs(word) and word[:1] in inf["bar letters"]:
        return True
    return False

assert inflected_in_its_subjunctive("ddxsmpi")==False # no inicia con "bar letters"
assert inflected_in_its_subjunctive("odxsmpi")==True

def parse_herucode_to_decimal(herucode):
    if alfabeto(herucode):
        suma = 0
        contador = 0
        for num in herucode:
            suma = suma + inf["orden"].find(num)*(20**contador)
            contador = contador + 1
        return suma
    return False

assert parse_herucode_to_decimal("gxjrc")==605637

def number_to_be_pretty(herucode):
    num = parse_herucode_to_decimal(herucode)
    if num and num>=81827 and num%3==0:
        return num

def herucodes_alphabetical_order(words=[]):
    return sorted(words,  key=lambda word: [inf["orden"].index(c) if c in inf["orden"] else ord(c) for c in word])

@app.route("/parse", methods=['POST'])
def hello_world():
    array_text =  request.form.get('text').split()
    #pprint(array_text)
    lst_preposition = [text for text in array_text if preposition(text)]
    #pprint(lst_preposition)
    lst_verbs = [text for text in array_text if verbs(text)]
    #pprint(lst_verbs)
    lst_inflected_in_its_subjunctive = [text for text in array_text if inflected_in_its_subjunctive(text)]
    #pprint(lst_verbs)
    lst_number_to_be_pretty = [num for num in array_text if number_to_be_pretty(num)]
    #pprint(lst_verbs)
    lst_herucodes_alphabetical_order = herucodes_alphabetical_order(array_text)
    return {
        "prepositions": len(lst_preposition),
        "verbs": len(lst_verbs),
        "subjunctive_verbs": len(lst_inflected_in_its_subjunctive),
        "pretty_numbers": len(lst_number_to_be_pretty),
        "vocabulary_list": lst_herucodes_alphabetical_order
    }

if __name__ == "__main__":
    app.run(debug=True)