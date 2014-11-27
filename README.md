A Raspberry Pi Web Service to control Energenie plug sockets
===========================================================

Flask web service for controlling energenie plug sockets via raspberry pi

##Dependencies:

	sudo apt-get install python-pip
	sudo pip install Flask

##To Run:

    sudo python energenie-server-run-me.py

###To control switches:

A sample HTTP POST to turn all (0) sockets on (1)

    HTTP POST to 'http://localhost:5000/'
    JSON Body:
              {
                 "PlugNumber" : "0",
                 "PlugState" : "1"
               }
 
 
 PlugNumber: 0 controls all sockets - 1 and 2 etc control socket 1 and 2 etc

 PlugState: 1 or 0 - 1 turns socket on, 0 turns socket off

 
##To start on boot:
 	sudo apt-get install upstart
 	sudo nano /etc/init/energenie.conf

###Insert:

 	start on runlevel [2345]
	stop on runlevel [016]

	respawn
	exec python /home/pi/apps/energenie-switch/energenie-server-run-me.py


