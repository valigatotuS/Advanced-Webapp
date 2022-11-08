"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
  

Description         : User handlers
Author              : valigatotuS
Last date updated   : 07/11/2022
"""

from webapp.database.models import User
from webapp.extensions import login_manager
import flask

#flask-login user_loader functie controleert bij elk pagina verzoek de geldigheid van de sessie
@login_manager.user_loader
def load_user(user_id):
    print("flask-login: user_loader functie opgeroepen om geldigheid user sessie %s te controleren." % user_id)
    return User.query.get(int(user_id))


#flask-login custom unauthorized handler. Wordt uitgevoerd indien niet ingelogd of ongeldig...
@login_manager.unauthorized_handler
def unauthorized():
    flask.flash("unauthorized access, log in first")
    return flask.redirect('/login')
