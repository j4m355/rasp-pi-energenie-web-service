from flask import Flask, request
from energenie import switch_on, switch_off

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
    s = "Swith " + plug + " has been pluged " + english
    print s
    return s

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)