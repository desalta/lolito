from flask import render_template, request
from . import livegame, helper

servers = [{'code':'br' , 'name' : 'Brasil'},{'code':'euw' , 'name' : 'Europa O'},{'code':'eune' , 'name' : 'Europa N&E'},{'code':'lan' , 'name' : 'Latinoamerica Norte'},{'code':'las' , 'name' : 'Latinoamerica Sur'},{'code':'jp' , 'name' : 'Japon'},{'code':'kr' , 'name' : 'Korea'},{'code':'na' , 'name' : 'America del Norte'},{'code':'oce' , 'name' : 'Oceania'},{'code':'ru' , 'name' : 'Rusia'},{'code':'tr' , 'name' : 'Turquia'}]

def getespia(server):
    #Retornar servers
    if server is None:
        return render_template('espia.html',servers=servers)

    #Obtener datos locales
    localdata = livegame.getLocalData()
    if localdata is None:
        return render_template('espia.html',servers=servers,error="No se pudo obtener datos del juego")

    #Obtener datos de cada campeon
    livegame.getLiveData(server,localdata)

    #Corrije mapa para enviar
    print("fix request ...")
    lang = request.args.get('lang')
    helper.fixData(localdata,lang)

    #Devolver pagina completa
    return render_template('espia.html', servers=servers, data=localdata)