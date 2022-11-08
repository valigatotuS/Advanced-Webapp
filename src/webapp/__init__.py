"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
  

Description         : Webapp Creator
Author              : valigatotuS
Last date updated   : 07/11/2022
"""

from flask import Flask                             
from webapp.extensions import db, bcrypt, login_manager     # Accessing app extensions
from webapp import handlers                                 # Configuring the user-loader & unauthorized handler

def create_app(config)-> Flask:
    """Return configured and initiated app"""
    webapp = Flask(__name__, template_folder="templates", static_folder="static")   # Creating app
    webapp.config.from_object(config)                                               # Configuring app
    
    with webapp.app_context():
        login_manager.init_app(webapp)          # Initiating the login manager
        db.init_app(webapp)                     # Initiating the webapp           
        db.create_all()                         # Creating the missing tables
        bcrypt.init_app(webapp)                 # Initiating the hashing utilities
        
        from webapp import routes               # Importing the the routes our webapp is pointing to (urls)

    return webapp