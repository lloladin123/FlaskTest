from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>My API</h1>'''

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'msg': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)