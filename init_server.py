from flask import Flask, request
from model.Automaton import Automaton
from controller.Automaton_operation import Operations


app = Flask(__name__)


@app.route('/union/', methods=['GET'])
def getUnio():
    quintuples = request.json
    quintuple1 = quintuples["quintuple1"]
    quintuple2 = quintuples["quintuple2"]

    a1 = Automaton()
    a1.load_automaton_dict(quintuple1)
    a2 = Automaton()
    a2.load_automaton_dict(quintuple2)

    union = Operations.automaton_union(a1, a2)
    unio_quintuple = union.get_quintuple()

    return {"automaton_union": unio_quintuple}


@app.route('/address', methods=["POST"])
def address():
    body = request.json

    return {'message': "no se pudo registrar la dirección"}


@app.route('/union/<quintuples>', methods=['GET'])
def getCitiesDealership(quintuples):

    return {'ciudades': quintuples}


if __name__ == "__main__":
    app.run(debug=True)
