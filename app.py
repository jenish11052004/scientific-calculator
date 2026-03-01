from flask import Flask, request, jsonify
from calculator import square_root, factorial, natural_log, power

app = Flask(__name__)


@app.route('/sqrt')
def sqrt():
    try:
        number = float(request.args.get('number'))
        result = square_root(number)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/factorial')
def fact():
    try:
        number = int(request.args.get('number'))
        result = factorial(number)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/ln')
def ln():
    try:
        number = float(request.args.get('number'))
        result = natural_log(number)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/power')
def pow():
    try:
        x = float(request.args.get('x'))
        b = float(request.args.get('b'))
        result = power(x, b)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)