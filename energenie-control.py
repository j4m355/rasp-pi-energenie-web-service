from wsgiref.validate import validator
from wsgiref.simple_server import make_server

# Our callable object which is intentionally not compliant to the
# standard, so the validator is going to break
def simple_app(environ, start_response):
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain')] # HTTP Headers
    start_response(status, headers)

    # This is going to break because we need to return a list, and
    # the validator is going to inform us
    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    return ret

# This is the application wrapped in a validator

httpd = make_server('0.0.0.0', 8000, simple_app)
print "Listening on port 8000...."
httpd.serve_forever()