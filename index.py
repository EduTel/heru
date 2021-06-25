from pprint import pprint
from flask import Flask, request
from lib.translate import Translate

app = Flask(__name__)
o_translate = Translate(orden="sxocqnmwpfyheljrdgui",foo_letters="udxsmpf")

@app.route("/parse", methods=['POST'])
def hello_world():
    array_text =  request.form.get('text').split()
    lst_preposition = [text for text in array_text if o_translate.preposition(text)]
    lst_verbs = [text for text in array_text if o_translate.verbs(text)]
    lst_inflected_in_its_subjunctive = [text for text in array_text if o_translate.inflected_in_its_subjunctive(text)]
    lst_number_to_be_pretty = [num for num in array_text if o_translate.number_to_be_pretty(num)]
    lst_herucodes_alphabetical_order = o_translate.herucodes_alphabetical_order(array_text)
    return {
        "prepositions": len(lst_preposition),
        "verbs": len(lst_verbs),
        "subjunctive_verbs": len(lst_inflected_in_its_subjunctive),
        "pretty_numbers": len(lst_number_to_be_pretty),
        "vocabulary_list": lst_herucodes_alphabetical_order
    }

if __name__ == "__main__":
    app.run(debug=True)