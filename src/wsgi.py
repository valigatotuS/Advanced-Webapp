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

app = create_app(config)                                                    # constructing app based on the configuration
app_with_socket = SocketIO(app, async_mode='eventlet', debug=config.DEBUG)  # app with socket support 


def background_lamp_status(delay)->None:
    """"""
    while True:
        app_with_socket.sleep(delay)        # sleeping before sending our next request
        lamps_level = get_lamps_level()     # asynchronous function getting the lamps brightness
        app_with_socket.emit('ReceiveFromChatServer', lamps_level) # sending the lamps brightness through the socket to our clients

if __name__ == "__main__":

    with threading.Lock():  # launching periodic background thread
        app_with_socket.start_background_task(background_lamp_status, 5) 

    app_with_socket.run(app, host='localhost', port=8080, debug=True, use_reloader=False) # running our app and making it accessible
    # app.run(host="0.0.0.0", debug=config.DEBUG) # app without socket

    
    
    