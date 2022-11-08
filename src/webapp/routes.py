"""
   :::     :::     :::     :::        ::::::::::: ::::::::      ::: ::::::::::: :::::::: ::::::::::: :::    :::  :::::::: 
  :+:     :+:   :+: :+:   :+:            :+:    :+:    :+:   :+: :+:   :+:    :+:    :+:    :+:     :+:    :+: :+:    :+: 
 +:+     +:+  +:+   +:+  +:+            +:+    +:+         +:+   +:+  +:+    +:+    +:+    +:+     +:+    +:+ +:+         
+#+     +:+ +#++:++#++: +#+            +#+    :#:        +#++:++#++: +#+    +#+    +:+    +#+     +#+    +:+ +#++:++#++   
+#+   +#+  +#+     +#+ +#+            +#+    +#+   +#+# +#+     +#+ +#+    +#+    +#+    +#+     +#+    +#+        +#+    
#+#+#+#   #+#     #+# #+#            #+#    #+#    #+# #+#     #+# #+#    #+#    #+#    #+#     #+#    #+# #+#    #+#     
 ###     ###     ### ########## ########### ########  ###     ### ###     ########     ###      ########   ########       
  

Description         : Webapp Routes
Author              : valigatotuS
Last date updated   : 07/11/2022
"""

from flask import current_app as app
from flask import render_template, request, redirect
import flask, bcrypt, sqlalchemy, coapclient, flask_login, asyncio, datetime as dt
from flask_login import current_user
from webapp.extensions import db, login_manager
from webapp.database.models import User, LampLog
from webapp.forms import LoginForm, RegisterForm

@app.route("/")
@flask_login.login_required
def home():
    """Landing page route."""
    return render_template('lamp_dashboard.html')

#---------------- API -----------------#

@app.route('/api/lamp/<lamp_id>/', methods=['GET', 'POST', 'PUT'])
async def lamp_status_request(lamp_id):
    # rewrite the whole function properly

    if request.method == 'GET':
        level = await coapclient.coapgetlampstatus('coap://' + lamp_id + '.irst.be/lamp/dimming')
        return {'brightness_value':str(int(level))}

    elif request.method == 'POST' or request.method == 'PUT':
        if ('dimming' in request.form):
            value = request.form['dimming']
            # log post
            lamp_log = LampLog(
                user_id = current_user.get_id(),
                timestamp = dt.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
                lamp_id = lamp_id,
                level = value
            )
            db.session.add(lamp_log)
            db.session.commit()
        else:
            return({'error':'missing dimming payload.'}, 400)

        await coapclient.setlampstatus(lamp_id, value)
        
        return {'result': 'ok'}
    else:
        #implement error afhandeling (error format or reponses)
        return({'error':'not supported'}, 405)


@app.route('/api/lamp/all', methods=['GET', 'POST', 'PUT'])
async def room_brightness():
    if request.method == 'GET': 
        lamp_levels = {}

        # getting the lamps brightness
        for row in range(1,6):
            for col in ['a', 'b', 'c']:
                lamp_levels['lamp' + str(row) + col] = (int((asyncio.run(coapclient.coapgetlampstatus('coap://lamp' + str(row) + str(col) + '.irst.be/lamp/dimming'))).decode('utf-8')))

        return lamp_levels

    elif request.method == 'POST' or request.method == 'PUT':
        if ('dimming' in request.form):
            value = request.form['dimming']
        # no payload handling
        else:
            return({'error':'missing dimming payload.'}, 400)

        # setting room brightness
        for row in range(1,6):
            for col in ['a', 'b', 'c']:
                await asyncio.sleep(0.2) # protects our server with overflooding
                await coapclient.setlampstatus('lamp' + str(row) + col, value)
        
        return ({'result':'room brightness updated with value %i' % value}, 200)
        
    else:
        return({'error':'not supported'}, 405)

@app.route('/history', methods=['GET', 'POST'])
@flask_login.login_required
def history():
    logs = LampLog.query.order_by(LampLog.timestamp.desc()).all()
    return render_template("history.html", logs=logs)

#------- login/register routes -------#

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if flask.request.method == 'POST':
        try:
            user = User.query.filter_by(email=form.email.data).first()
            password = form.password.data.encode('utf-8')
            hash = user.password.encode('utf-8')

            if user and user.password and bcrypt.checkpw(password, hash):
                flask_login.login_user(user)
                return flask.redirect('/')
            else:
                flask.flash("Invalid username or password, try again")
        except Exception as e:
            print(e)
            return e

    return flask.render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if flask.request.method == 'POST':
        try:
            newUser = User(
                email = form.email.data, 
                password = (bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
            )
            db.session.add(newUser)
            db.session.commit()
            flask.flash("Your account has been registered, try to log in")
            return redirect('\login')
        except sqlalchemy.exc.IntegrityError as err:
            flask.flash("A user is already registered with this email.")
            return redirect('\login') 
        except Exception as e:
            flask.flash(str(e))
            return redirect('\login') 
    else:
        return flask.render_template('register.html', form=form)

@app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flask.flash("Logged out.")
    return redirect('\login')
