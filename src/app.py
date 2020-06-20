from flask import Flask, jsonify, request, Response
import base64
import jwt

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

with open(".secrets") as f:
    SECRETS = f.read().rstrip()


@app.route('/')
def index():
    return jsonify({
        "message": "Hi!! this is my first API. project is available at : https://github.com/dogodogodoggo/doggo_api.git"
    })


@app.route('/api/v1/hello/<string:name>', methods=['GET'])
def create_user_v1(name):
    if name == "admin":
        return jsonify({
            "message": "Bad Request, woof...."
        }), 400
    encoded = base64.b64encode(name.encode('utf-8'))
    return jsonify({
        "token": encoded.decode('utf-8')
    })


@app.route('/api/v1/doggo', methods=['POST'])
def doggo_v1():
    payload = request.json
    token = payload.get('token').encode('utf-8')
    name = base64.b64decode(token).decode('utf-8') 
    if name == "admin":
        resp = {
            "flag" : "m1z0r3{xxxxxxxxx}"
        }
    else:
        resp = {
            "doggo" : f"bowwow, {name}"
        }
    return jsonify(resp)


@app.route('/api/v2/hello/<string:name>', methods=['GET'])
def create_user_v2(name):
    if name == "admin":
        return jsonify({
            "message": "Bad Request, woof...."
        }), 400
    encoded = jwt.encode({'name': name}, SECRETS, algorithm='HS256')
    return jsonify({
        "token": encoded.decode('utf-8')
    })


@app.route('/api/v2/doggo', methods=['POST'])
def doggo_v2():
    token = request.json.get('token')
    decoded = jwt.decode(token, SECRETS, algorithms='HS256')
    name = decoded["name"]

    if name == "admin":
        resp = {
            "flag" : "m1z0r3{xxxxxxxxx}"
        }
    else:
        resp = {
            "doggo" : f"bowwow, {name}"
        }
    return jsonify(resp)


if __name__ == '__main__':
    app.run()
