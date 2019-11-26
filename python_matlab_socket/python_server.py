"""
A python server example using Flask
"""

from flask import Flask, request, jsonify
app = Flask(__name__)


# test connection
@app.route('/hello')
def hello():
    return 'Hello, World'


# test get a POST request containing JSON
@app.route('/post-json', methods=['POST'])
def post_json_test():
    input_json = request.get_json()
    print('Get data: {}, datatype: {}'.format(input_json, type(input_json)))

    # NOTE: cannot use tuple as key
    return jsonify({'message': 'request success', 'data': input_json})
