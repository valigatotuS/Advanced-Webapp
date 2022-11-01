from distutils.log import debug
from flask import Flask, request, render_template, redirect
from app import create_app
from config import config
from flask_socketio import SocketIO
import coapclient
import asyncio
# from app.extensions import SocketIO
import threading
import sys

app = create_app(config)
socketio = SocketIO(app, async_mode='eventlet', debug=True)


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(5)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})

@socketio.on('connect')
def socketioconnected():
    print("Socketio session connected.", request.sid)


@socketio.on('disconnect')
def socketiodisconnected():
    print("Socketio disconnected.")

@socketio.on('addToChat')
def chat(content):
    print("Chat message received: %s from %s" % (content, str(request.sid)))
    lamp_level ="level"
    lamp_level = get_lamps_level()#(asyncio.run(coapclient.coapgetlampstatus('coap://' + 'lamp1a' + '.irst.be/lamp/dimming'))).decode('utf-8')
    data = content + " from " + str(request.sid) + '\t' + str(lamp_level)
    socketio.emit('ReceiveFromChatServer', data)

def get_lamps_level():
    lamp_levels = {}

    for row in range(1,6):
        for col in ['a', 'b', 'c']:
            lamp_levels['lamp' + str(row) + col] = (int((asyncio.run(coapclient.coapgetlampstatus('coap://lamp' + str(row) + str(col) + '.irst.be/lamp/dimming'))).decode('utf-8')))
    return lamp_levels

#asyncio's async await werkt binnen flask maar werkt NIET met socketio  
@app.route('/api/await')
async def socketio_await():
    data = await say_after(1, 'Uitvoeren met async await ...')
    print(data)
    socketio.emit('ReceiveFromChatServer', data)
    return "Request uitgevoerd. Print naar terminal maar voert GEEN socketio emit uit. Bestande socketio sessies crashen zelfs..."

#asyncio.run() routine WERKT met flask en socketio
@app.route('/api/asyncio_run')
def socketio_asyncio_run():
    data = asyncio.run(say_after(1, 'Uitvoeren met asyncio.run() ...'))
    print(data)
    socketio.emit('ReceiveFromChatServer', data)
    return "Request uitgevoerd. Print naar terminal en voert ook socketio emit uit."


def achtergrondthread(delay):
    while True:
        socketio.sleep(delay)
        lamps_level = get_lamps_level()
        socketio.emit('ReceiveFromChatServer', lamps_level)

if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=config.DEBUG)
    with threading.Lock():
        socketio.start_background_task(achtergrondthread, 5)
        
    socketio.run(app, host='localhost', port=8080, debug=True, use_reloader=False)

    
    
    