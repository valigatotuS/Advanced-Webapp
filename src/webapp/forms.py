"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
  

Description         : Client Forms (inputs)
Author              : valigatotuS
Last date updated   : 07/11/2022
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """Sign-in form"""
    email = StringField("email", [DataRequired(message="fill your email out")])
    password = PasswordField("password", [DataRequired(message="fill your password out")])
    # role = SelectField(u'Role', choices=["student", "docent", "admin"])
    submit = SubmitField("Log in")

class RegisterForm(FlaskForm):
    """Sign-up form"""
    fname = StringField("firstname", [DataRequired()])
    lname = StringField("lastname", [DataRequired()])
    email = StringField("email", [DataRequired()])
    password = PasswordField("password", [DataRequired()])
    submit = SubmitField("Create account")
    