from flask import Flask, request
from energenie import switch_on, switch_off
import json
from collections import namedtuple

app = Flask(__name__)

@app.route('/plug/<plug>/status/<status>', methods=['GET'])
def pi_plug(plug,status):
    english = ""
    if status == "1":
        english = "on"
        switch_on(int(plug))
    if status == "0":
        english = "off"
        switch_off(int(plug))
    y = "Everything"
    x = "Plug " + plug
    s = ""
    z = " has been switched " + english
    if plug == "0" :
        s = y + z
    else:
        s = x + z
    print s
    return s

@app.route('/', methods=['POST'])
def json_post():
    data = request.data
    body = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print body.PlugState
    print body.PlugNumber
    if body.PlugState == "true":
        print "inside true"
        switch_on(int(body.PlugNumber))
    else:
        print "inside false"        
        switch_off(int(body.PlugNumber))
    return 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)