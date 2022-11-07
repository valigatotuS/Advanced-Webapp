"""Route declaration."""
from curses import flash
from flask import current_app as app
from flask import render_template, request, redirect
import flask, sys, datetime as dt
import coapclient
from aiocoap import *
import flask_login
from flask_login import current_user
from app.extensions import db
from app.database.models import User, LampLog
import bcrypt
import sqlalchemy #.exc.IntegrityError
from flask_socketio import SocketIO


@app.route("/")
@flask_login.login_required
def home():
    """Landing page route."""
    return render_template('lamp_dashboard.html')

@app.route('/api/<lamp>')
async def getlampstatusrequest(lamp):
    level = await coapclient.coapgetlampstatus('coap://' + lamp + '.irst.be/lamp/dimming')
    result = 'Coap status ' + str(lamp) + " is aan " + str(level)
    return {'result':result}


@app.route('/api/<lamp>/<brightness>')
async def setlampstatusrequest(lamp, brightness):

    await coapclient.setlampstatus(lamp, brightness)
    result = 'Coap brightness status van ' + str(lamp) + " is gewijzigd aan " + str(brightness)

    return {'result':result}

@app.route('/api/get/room/')
async def get_room_brightness_request():
    values = []
    for row in range(1,6):
        for col in ['a', 'b', 'c']:
            values.append(await coapclient.coapgetlampstatus('coap://lamp' + str(row) + str(col) + '.irst.be/lamp/dimming'))

    return str(values)

@app.route('/api/set/room/<brightness>', methods=['GET', 'POST', 'PUT'])
async def roombrightness(brightness):
    # pas op voor overflooding attack, implementeet een timer !!!
    # check http response !!!!
    # implement put/post instead (for setting brightness)
    # check get or post (and handle it !)

    for row in range(1,6):
        for col in ['a', 'b', 'c']:
            await coapclient.setlampstatus('lamp' + str(row) + col, brightness)

    result = 'room brightness gewijzigd aan ' + brightness

    return {'result':result}

@app.route('/api/lamp/<lamp_id>/', methods=['GET', 'POST', 'PUT'])
async def lamp_status_request(lamp_id):
    # rewrite the whole function properly

    if request.method == 'GET':
        level = await coapclient.coapgetlampstatus('coap://' + lamp_id + '.irst.be/lamp/dimming')
        return {'result':str(int(level))}

    elif request.method == 'POST' or request.method == 'PUT':
    #implementeer key-value pairs
        if ('dimming' in request.form):
            # lamp_id = request.form['lamp_id']
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
        pass

    elif request.method == 'POST' or request.method == 'PUT':
        if ('dimming' in request.form):
            value = request.form['dimming']
        else:
            return({'error':'missing dimming payload.'}, 400)

        # setting room brightness
        for row in range(1,6):
            for col in ['a', 'b', 'c']:
                await coapclient.setlampstatus('lamp' + str(row) + col, value)
        
        return redirect('/')
        
    else:
        return({'error':'not supported'}, 405)

@app.route('/history', methods=['GET', 'POST'])
@flask_login.login_required
def history():
    logs = LampLog.query.order_by(LampLog.timestamp.desc()).all()
    return render_template("history.html", logs=logs)


#------- login/register routes -------#

from app.views.forms import LoginForm, RegisterForm
from app.extensions import login_manager


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

@app.route('/api/user/', methods=['GET', 'POST', 'PUT'])
def add_user_request():
    try: 
        pwd = 'test'
        newUser = User(
            email = "test5@gmail.com", 
            password = (bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
        )
        db.session.add(newUser)
        db.session.commit()
        return {'result': "user has been added"}
    except Exception as e:
        print(e)
        return e
    
    return "user added"

# logs

# @app.route('/post_log/<lamp_id>/<level>', methods=['GET', 'POST', 'PUT'])
# def post_lamp_log(lamp_id, level):
#     lamp_log = LampLog(
#         user_id = current_user.get_id(),
#         timestamp = dt.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
#         lamp_id = lamp_id,
#         level = level
#     )
#     db.session.add(lamp_log)
#     db.session.commit()

#     return 'log posted'
    

# websocket #

# from flask import Flask, render_template, session, request, \
#     copy_current_request_context
# from flask_socketio import SocketIO, emit, join_room, leave_room, \
#     close_room, rooms, disconnect 

