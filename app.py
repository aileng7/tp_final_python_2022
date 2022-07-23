from flask import Flask, request, jsonify

import db
from models import Operation

app = Flask(__name__)


@app.route('/operations', methods=['POST'])
def inform_operations():
    date = request.json['date']
    type_operation = request.json['type_operation']
    description = request.json['description']
    amount = request.json['amount']
    new_operation = Operation(date, type_operation, description, amount)
    db.session.add(new_operation)
    db.session.commit()
    return jsonify({'message': 'Operación registrada:'}, new_operation)


@app.route('/operations', methods=['GET'])
def consult_operations():
    operations_list = Operation.query.all()
    return jsonify(operations_list)


@app.route('/operations/<id>', methods=['GET'])
def consult_operations_id(id):
    operation = Operation.query.get(id)
    return jsonify(operation)


@app.route('/operations/<date>', methods=['GET'])
def consult_operations_date(date):
    operation = Operation.query.get(date)
    return jsonify(operation)


@app.route('/operations/<type_operation>', methods=['GET'])
def consult_operations_type(type_operation):
    operation = Operation.query.get(type_operation)
    return jsonify(operation)


@app.route('/operations/<id>', methods=['PUT'])
def update_task(id):
    operation = Operation.query.get(id)
    date = request.json['date']
    type_operation = request.json['type_operation']
    description = request.json['description']
    amount = request.json['amount']
    operation.date = date
    operation.type = type_operation
    operation.description = description
    operation.amount = amount
    db.session.add(operation)
    db.session.commit()
    return jsonify(operation)


if __name__ == "__main__":
    app.run()
