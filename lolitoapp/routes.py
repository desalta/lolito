from flask import render_template
from app import app

from runero import controller as runeroController
from wiki import controller as wikiController
from espia import controller as espiaController


########################################## RUTAS

@app.route("/")
def inicio():
    return render_template('inicio.html')
    #return render_template('reload.html') #Actualiza la interfaz


###################### RUNERO

@app.route("/runero")
def runero():
    return runeroController.runero()


@app.route('/runero/edit', methods=['POST', 'DELETE'])
def runero_edit():
    return runeroController.runero_edit()


@app.route("/runero/apply", methods=['POST'])
def runero_apply():
    return runeroController.runero_apply()


###################### WIKI

@app.route("/wiki")
def wiki():
    return wikiController.getwiki()


@app.route("/wiki/<champ>/<pos>")
def wiki_cahmp(champ, pos):
    return wikiController.getchamp(champ, pos)

###################### ESPIA

@app.route("/espia/", defaults={'server': None})
@app.route("/espia/<server>")
def espia(server):
    return espiaController.getwiki(server)