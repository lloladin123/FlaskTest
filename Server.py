from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')

    data = {'param1': param1, 'param2': param2, 'msg': 'Server svar'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)