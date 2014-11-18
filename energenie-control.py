from wsgiref.validate import validator
from flask import Flask, request

app = Flask(__name__)

@app.route('/switch/<switch>/status/<status>', methods=['GET'])
def pi_switch(switch,status):
    print "switch:"
    print switch
    print "status:"
    print status
    english = ""
    if status == 1:
        english = " on"
    if status == 0:
        english = " off"
    s = "Swith " + switch + " has been switched " + english
    return s

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)