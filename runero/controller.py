from flask import request, g, render_template, redirect, url_for
import pyautogui, time

from . import models,mapeo

def runero():
    runas = models.Runas.get_all()
    return render_template('runero.html',runas=runas)
    

def runero_edit():
    #form = forms.RunasForm(request.args)
    json = request.get_json()

    if request.method == 'POST':
        obj = models.Runas.get(json['name'])
        if obj is None:
            obj = models.Runas()
            obj.name = json['name']
            obj.sett(json['prim_runa'],json['prim_clave'],json['prim_ran1'],json['prim_ran2'],json['prim_ran3'],
                    json['sec_runa'],json['sec_ran1'],json['sec_ran2'],json['frag1'],json['frag2'],json['frag3']
            )
            obj.insert()
        else:
            obj.sett(json['prim_runa'],json['prim_clave'],json['prim_ran1'],json['prim_ran2'],json['prim_ran3'],
                    json['sec_runa'],json['sec_ran1'],json['sec_ran2'],json['frag1'],json['frag2'],json['frag3']
            )
            obj.update()
    
    if request.method == 'DELETE':
        models.Runas.delete(json['name'])
    
    return 'ok'


def runero_apply():
    json = request.get_json()
    setRunas(json['name'])
    return 'ok'






def moveClick(x,y,pos):
    pyautogui.moveTo(x+pos[0], y+pos[1], duration=0.1)
    pyautogui.click()

def setRunas(campeon):
    obj = models.Runas.get(campeon)
    actual = [obj.prim_runa,obj.prim_clave,obj.prim_ran1,obj.prim_ran2,obj.prim_ran3,obj.sec_runa,obj.sec_ran1,obj.sec_ran2,obj.frag1,obj.frag2,obj.frag3]
    
    pyautogui.alert('Despues de clickear Aceptar, ubicar mouse en el boton de seleccion de runas, y esperar 2 segundos')
    time.sleep(2.5)

    #Referencia de la posicion
    x,y = pyautogui.position()

    #Click Abrir Opcion
    pyautogui.click()
    time.sleep(1)


    ########################################### HACK RESTABLECER
    moveClick(x,y,mapeo.acciones['PRIM_RUNA'])
    moveClick(x,y,mapeo.ruta_prim['PRE'])
    moveClick(x,y,mapeo.ruta_prim['DOM'])
    moveClick(x,y,mapeo.ruta_prim['BRU'])

    ########################################### RUTA PRINCIPAL
    #Seleccion de ruta principal
    RUTA1 = actual[0]
    moveClick(x,y,mapeo.acciones['PRIM_RUNA'])
    moveClick(x,y,mapeo.ruta_prim[RUTA1])

    #Seleccionar ruta principal - runa clave
    RUNAC = actual[1]
    moveClick(x,y,mapeo.runa_prim[RUTA1]['clave'][RUNAC])

    #Seleccionar ruta principal - runa ranura 1
    RUNA1 = actual[2]
    moveClick(x,y,mapeo.runa_prim[RUTA1]['ranura1'][RUNA1])

    #Seleccionar ruta principal - runa ranura 2
    RUNA2 = actual[3]
    moveClick(x,y,mapeo.runa_prim[RUTA1]['ranura2'][RUNA2])

    #Seleccionar ruta principal - runa ranura 3
    RUNA3 = actual[4]
    moveClick(x,y,mapeo.runa_prim[RUTA1]['ranura3'][RUNA3])

    ########################################### HACK RESTABLECER
    moveClick(x,y,mapeo.ruta_sec['RUN0'])
    moveClick(x,y,mapeo.acciones['SEC_RUNA'])
    moveClick(x,y,mapeo.ruta_sec['RUN0'])
    moveClick(x,y,mapeo.ruta_sec['RUN1'])
    moveClick(x,y,mapeo.ruta_sec['RUN2'])

    ########################################### RUTA SECUNDARIA
    #Seleccion de ruta secundaria
    RUTA2 = actual[5]
    moveClick(x,y,mapeo.acciones['SEC_RUNA'])
    moveClick(x,y,mapeo.get_ruta_sec(RUTA1,RUTA2))

    #Seleccionar ruta secundaria - runa ranura 1
    RUNA1 = actual[6]
    moveClick(x,y,mapeo.runa_sec[RUTA2][RUNA1])

    #Seleccionar ruta secundaria - runa ranura 2
    RUNA2 = actual[7]
    moveClick(x,y,mapeo.runa_sec[RUTA2][RUNA2])

    ########################################### FRAGMENTOS
    #Seleccionar fragmentos - ranura 1
    FRA1 = actual[8]
    moveClick(x,y,mapeo.acciones['FRAG1'])
    moveClick(x,y,mapeo.frag['ranura1'][FRA1])

    #Seleccionar fragmentos - ranura 2
    FRA2 = actual[9]
    moveClick(x,y,mapeo.acciones['FRAG2'])
    moveClick(x,y,mapeo.frag['ranura2'][FRA2])

    #Seleccionar fragmentos - ranura 3
    FRA3 = actual[10]
    moveClick(x,y,mapeo.acciones['FRAG3'])
    moveClick(x,y,mapeo.frag['ranura3'][FRA3])

    ########################################### NOMBRE Y GUARDAR
    
    moveClick(x,y,mapeo.acciones['EDITAR'])
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(campeon.lower())
    pyautogui.press('enter')
    
    moveClick(x,y,mapeo.acciones['GUARDAR'])
    pyautogui.click()

    return 'ok'