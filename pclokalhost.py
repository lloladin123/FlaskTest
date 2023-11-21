from flask import Flask, request, jsonify

app = Flask(__name__) # name must have __ before and after

# # define endpoint (url, method) 
@app.route('/get_data', methods=['GET'])
def get_data():
    # get the params from the request
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    # return a json
    data = {'param1': param1, 'param2': param2, 'msg': 'server svar'}
    return jsonify(data) # return json

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) 