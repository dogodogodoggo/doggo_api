from flask import Flask, jsonify, request, Response
import base64

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return jsonify({
    "message": "Hi!! this is my first API. project is available at : https://github.com/dogodogodoggo/doggo_api.git"
  })


@app.route('/api/v1/hello/<string:name>', methods=['GET'])
def create_user(name):
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


if __name__ == '__main__':
  app.run()
