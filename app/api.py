from flask import Flask, jsonify
from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}

@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"

@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        result = CALCULATOR.add(num_1, num_2)
        return jsonify({"result": result}), 200, HEADERS
    except TypeError as e:
        return str(e), 400, HEADERS

@api_application.route("/calc/subtract/<op_1>/<op_2>", methods=["GET"])
def subtract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        result = CALCULATOR.substract(num_1, num_2)
        return jsonify({"result": result}), 200, HEADERS
    except TypeError as e:
        return str(e), 400, HEADERS

@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        result = CALCULATOR.multiply(num_1, num_2)
        return jsonify({"result": result}), 200, HEADERS
    except TypeError as e:
        return str(e), 400, HEADERS

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        if num_2 == 0:
            return "Division by zero is not allowed.", 406, HEADERS
        result = CALCULATOR.divide(num_1, num_2)
        return jsonify({"result": result}), 200, HEADERS
    except TypeError as e:
        return str(e), 400, HEADERS

@api_application.errorhandler(404)
def not_found(error):
    return "Resource not found", 404



