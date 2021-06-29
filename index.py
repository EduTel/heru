from pprint import pprint
from flask import Flask, request
from lib.translate import Translate
from flask import json

app = Flask(__name__)
o_translate = Translate(orden="sxocqnmwpfyheljrdgui", foo_letters="udxsmpf")


@app.route("/parse", methods=['POST'])
def hello_world():
    """
    functionality.

    @rtype: dict
    """
    data_return = {
        "prepositions": "",
        "verbs": "",
        "subjunctive_verbs": "",
        "pretty_numbers": "",
        "vocabulary_list": ""
    }
    array_text = request.json.get('text')
    if type(array_text) is str:
        array_text = array_text.split()
        if len(array_text) > 0:
            lst_preposition = [text for text in array_text if o_translate.preposition(text)]
            lst_verbs = [text for text in array_text if o_translate.verbs(text)]
            lst_inflected_in_its_subjunctive = [text for text in array_text if o_translate.inflected_in_its_subjunctive(text)]
            lst_number_to_be_pretty = [num for num in array_text if o_translate.number_to_be_pretty(num)]
            lst_herucodes_alphabetical_order = o_translate.herucodes_alphabetical_order(array_text)
            data_return["prepositions"] = len(lst_preposition)
            data_return["verbs"] = len(lst_verbs)
            data_return["subjunctive_verbs"] = len(lst_inflected_in_its_subjunctive)
            data_return["pretty_numbers"] = len(lst_number_to_be_pretty)
            data_return["vocabulary_list"] = lst_herucodes_alphabetical_order
    response = app.response_class(
        response=json.dumps(data_return),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
