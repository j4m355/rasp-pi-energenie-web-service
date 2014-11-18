from flask import Flask, request
from energenie import switch_on, switch_off

app = Flask(__name__)

@app.route('/switch/<switch>/status/<status>', methods=['GET'])
def pi_switch(switch,status):
    english = ""
    if status == "1":
        english = "on"
        switch_on(1)
    if status == "0":
        english = "off"
        switch_off(1)
    s = "Swith " + switch + " has been switched " + english
    print s
    return s

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)