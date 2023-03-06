from process.cal import Blockchain
from flask import Flask, request, render_template


app = Flask(__name__)
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    a = int(request.json['a'])
    b = int(request.json['b'])
    operator = request.json['operator']
    result = blockchain.calculate(a, b, operator)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)