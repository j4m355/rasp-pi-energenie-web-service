from flask import Flask, request
from energenie import switch_on, switch_off
import json
from collections import namedtuple

app = Flask(__name__)

@app.route('/', methods=['POST'])
def json_post():
    data = request.data
    body = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print body.PlugState
    print body.PlugNumber
    plugNum = int(body.PlugNumber)
    plugState = int(body.PlugState)
    if plugState == 1:
        print "inside true"
        switch_on(plugNum)
    else:
        print "inside false"        
        switch_off(plugNum)
    return "200"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)