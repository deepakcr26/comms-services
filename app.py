from flask import Flask, Response, request
from flask_cors import CORS
import os

from src.constants import JSON_HEADER
from src.token_mgt.token_mgr import get_token
# from src.utils.construct_response import construct_response

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    print('Sample Python App running on Flask')
    return 'Sample Python App running on Flask'


@app.route('/token', methods=['GET'])
def return_token():
    if 'room_name' in request.headers and 'identity' in request.headers:
        room_name = request.headers.get('room_name')
        identity = request.headers.get('identity')
        resp = Response(response=get_token(identity, room_name), mimetype=JSON_HEADER, status=200)
    else:
        resp = Response(response='headers: identity and room_name are missing', mimetype=JSON_HEADER, status=400)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


if __name__ == '__main__':
    app.run(host=os.environ['FLASK_RUN_HOST'], port=os.environ['FLASK_RUN_PORT'])
    # app.run(host='0.0.0.0', port=7001)
