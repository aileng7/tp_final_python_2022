from flask import Flask, request, jsonify

import db
from models import Operation

app = Flask(__name__)


@app.route('/operation', methods=['POST'])
def inform_operation():
    type_operation = request.json['type_operation']
    description = request.json['description']
    amount = request.json['amount']
    new_operation = Operation(type_operation, description, amount)
    db.session.add(new_operation)
    db.session.commit()
    return jsonify(new_operation)


if __name__ == "__main__":
    app.run()
