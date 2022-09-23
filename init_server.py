from flask import Flask, request
from model.Automaton import Automaton
from controller.Automaton_operation import Operations
import json


app = Flask(__name__)


@app.route('/union', methods=['GET'])
def getUnio():
    quintuple_one = None
    quintuple_two = None

    try:
        quintuple_one = request.files.get('quintuple_one')
        quintuple_one = json.load(quintuple_one)

        quintuple_two = request.files.get('quintuple_two')
        quintuple_two = json.load(quintuple_two)
    except:
        return {"message": "Archivo(s) no válido(s)"}, 400

    a1 = Automaton()
    a2 = Automaton()

    try:
        a1.load_automaton_dict(quintuple_one)
        a2.load_automaton_dict(quintuple_two)
    except Exception as error:
        return {"message": str(error)}, 400

    union = Operations.automaton_union(a1, a2)
    unio_quintuple = union.get_quintuple()

    return {"message": "operación exitosa.", "automaton_union": unio_quintuple}, 400


@app.route('/address', methods=["POST"])
def address():
    body = request.json

    return {'message': "no se pudo registrar la dirección"}


@app.route('/union/<quintuples>', methods=['GET'])
def getCitiesDealership(quintuples):

    return {'ciudades': quintuples}


if __name__ == "__main__":
    app.run(debug=True)
