rasp-pi-energenie-web-service
=============================

flask web service for controlling energenie plug sockets via raspberry pi

    sudo python energenie-server-run-me.py

To control switches:

    HTTP POST to 'http://localhost:5000/'
    JSON Body:
              {
                 "PlugNumber" : "0",
                 "PlugState" : "1"
               }
 
 
 PlugNumber: 0 turns all on - 1 and 2 etc control socket 1 and 2 etc

 PlugState: 1 or 0 - 1 turns socket on, 0 turns socket off
