from flask import Flask, request
from flask_cors import CORS

from model.Automaton import Automaton
from controller.Automaton_operation import Operations
import json


app = Flask(__name__)
CORS(app)


@app.route('/load', methods=['POST'])
def post():
    quintuple = None
    try:
        quintuple = request.files.get('quintuple')
        quintuple = json.load(quintuple)
    except:
        return {"message": "Archivo(s) no válido(s)"}, 400

    a1 = Automaton()

    try:
        a1.load_automaton_dict(quintuple)
    except Exception as error:
        return {"message": str(error)}, 400


    return {"message": "carga exitosa", "automaton": a1.get_quintuple()}, 200


@app.route('/union', methods=['POST'])
def union():
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

    return {"message": "operación exitosa.", "automaton_union": unio_quintuple}, 200


@app.route('/complement', methods=['POST'])
def complement():
    quintuple = None

    try:
        if request.files.get('quintuple_one'):
            quintuple = request.files.get('quintuple_one')
        elif request.files.get('quintuple_two'):
            quintuple = request.files.get('quintuple_two')
        quintuple = json.load(quintuple)

    except:
        return {"message": "Archivo(s) no válido(s)"}, 400

    a1 = Automaton()

    try:
        a1.load_automaton_dict(quintuple)
    except Exception as error:
        return {"message": str(error)}, 400

    complement = Operations.automaton_complement(a1)
    complement_quintuple = complement.get_quintuple()
    print(complement_quintuple)

    return {"message": "operación exitosa.", "automaton_complement": complement_quintuple}, 200


@app.route('/reverse', methods=['POST'])
def reverse():
    quintuple = None

    try:
        if request.files.get('quintuple_one'):
            quintuple = request.files.get('quintuple_one')
        elif request.files.get('quintuple_two'):
            quintuple = request.files.get('quintuple_two')
        quintuple = json.load(quintuple)

    except:
        return {"message": "Archivo(s) no válido(s)"}, 400

    a1 = Automaton()

    try:
        a1.load_automaton_dict(quintuple)
    except Exception as error:
        return {"message": str(error)}, 400

    reverse = Operations.automaton_reverse(a1)
    reverse_quintuple = reverse.get_quintuple()

    return {"message": "operación exitosa.", "automaton_reverse": reverse_quintuple}, 200



@app.route('/address', methods=["POST"])
def address():
    body = request.json

    return {'message': "no se pudo registrar la dirección"}


@app.route('/union/<quintuples>', methods=['GET'])
def getCitiesDealership(quintuples):

    return {'ciudades': quintuples}


if __name__ == "__main__":
    app.run(debug=True)
