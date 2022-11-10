"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
  

Description         : Web Server Gateway Interface
Author              : valigatotuS
Last date updated   : 07/11/2022
"""

from webapp import create_app           # App constructor
from config import config               # App configurations
from coapclient import get_lamps_level  # Lamps level getter through CoAP
from flask_socketio import SocketIO     # Socket implementation 
import threading                        # Launching background-thread
from flask_login import current_user

app = create_app(config)                                             # constructing app based on the configuration
socketio = SocketIO(app, async_mode='eventlet', debug=config.DEBUG)  # app with socket support 

@socketio.on('connect')
def connect_handler():
    if current_user.is_authenticated:
        socketio.emit('my response',
             {'message': '{0} has joined'.format(current_user.name)},
             broadcast=True)
    else:
        return False  # not allowed here

def background_lamp_status(delay)->None:
    """"""
    while True:
        socketio.sleep(delay)               # sleeping before sending our next request
        lamps_level = get_lamps_level()     # asynchronous function getting the lamps brightness
        socketio.emit('ReceiveFromChatServer', lamps_level) # sending the lamps brightness through the socket to our clients

if __name__ == "__main__":

    with threading.Lock():  # launching periodic background thread
        socketio.start_background_task(background_lamp_status, 5) 

    socketio.run(app, host='localhost', port=8080, debug=True, use_reloader=False) # running our app and making it accessible
    # app.run(host="0.0.0.0", debug=config.DEBUG) # app without socket

    
    
    