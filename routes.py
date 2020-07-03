from flask import request, render_template, g
from app import app

import time, threading
from runero import controller as runeroController


########################################## RUTAS

@app.route("/stop")
def stop():
    raise RuntimeError('Not running with the Werkzeug Server')

@app.route("/alive")
def alive():
    alive = 5

########################################## RUTAS

#@app.before_request
#def before_request():
#    g.method = 'DELETE' if 'DELETE' in request.form else request.method

@app.route("/")
def inicio():  
    return render_template('inicio.html')
    

###################### RUNERO

@app.route("/runero")
def runero(): 
    #return 'runero'
    return runeroController.runero()

@app.route('/runero/edit', methods=['POST','DELETE'])
def runero_edit(): 
    return runeroController.runero_edit()

@app.route("/runero/apply", methods=['POST'])
def runero_apply():
    return runeroController.runero_apply()

###################### BATALLA
