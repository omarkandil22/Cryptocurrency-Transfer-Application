from collections import OrderedDict

from flask import Flask, jsonify, request, render_template


class Transaction:

    def __init__(self, sender_name, recipient_name, value):
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.value = value

    def __getattr__(self, attr):
        return self.data[attr]

    def to_dict(self):
        return OrderedDict({'sender_name': self.sender_name,
                            'recipient_name': self.recipient_name,
                            'value': self.value})

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/view/transactions')
def view_transaction():
    return render_template('./view_transactions.html')

@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():
    sender_name = request.form['sender_name']
    recipient_name = request.form['recipient_name']
    value = request.form['amount']

    transaction = Transaction(sender_name, recipient_name, value)

    response = {'transaction': transaction.to_dict()}

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)
