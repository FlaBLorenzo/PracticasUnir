from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/calc/add/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    result = {"result": a + b}
    return jsonify(result=result), 200

@app.route('/calc/subtract/<int:a>/<int:b>', methods=['GET'])
def subtract(a, b):
    result = {"result": a - b}
    return jsonify(result=result), 200

@app.route('/calc/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a, b):
    result = {"result": a * b}
    return jsonify(result=result), 200

@app.route('/calc/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed", 406
    result = {"result": a / b}
    return jsonify(result=result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
