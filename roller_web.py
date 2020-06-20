#!/home/pi/roller/env/bin/python

import os
import json
from flask import Flask, render_template
from flask_socketio import SocketIO

# flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/virtual')
def virtual():
    return render_template('virtual.html')


@socketio.on('open')
def handle_open(data):
    os.system('python3 roller.py web_ui open %s'%(data))


@socketio.on('close')
def handle_close(data):
    os.system('python3 roller.py web_ui close %s'%(data))

@socketio.on('virtual')
def handle_virt(button):
    os.system('python3 virtual.py %s'%(button))
    print('sending button: %s'%(button))
    

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
