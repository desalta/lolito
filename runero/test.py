import pyautogui
import time
import mapeo

TEST = ""
#TEST = 'acciones'
#TEST = 'ruta_prim'
#TEST = 'ruta_sec'
#TEST = 'runas'
#TEST = 'precision_prim'
#TEST = 'dominacion_prim'
#TEST = 'brujeria_prim'
#TEST = 'valor_prim'
#TEST = 'inspiracion_prim'
#TEST = 'precision_sec'
#TEST = 'brujeria_sec'
#TEST = 'valor_sec'
#TEST = 'dominacion_sec'
#TEST = 'fragmentos'

pyautogui.alert('Despues de clickear OK, ubicar mouse en el boton de seleccion de runas, y esperar 2 segundos')
time.sleep(2)
#pyautogui.displayMousePosition()
x,y = pyautogui.position()

if TEST == 'acciones':
    for key in mapeo.acciones:
        pos = mapeo.acciones[key]
        pyautogui.moveTo(x+pos[0], y+pos[1], duration=0.2)
        print(key)

if TEST == 'ruta_prim':
    for key in mapeo.ruta_prim:
        pos = mapeo.ruta_prim[key]
        pyautogui.moveTo(x+pos[0], y+pos[1], duration=0.2)
        print(key)

if TEST == 'ruta_sec':
    for key in mapeo.ruta_sec:
        pos = mapeo.ruta_sec[key]
        pyautogui.moveTo(x+pos[0], y+pos[1], duration=0.2)
        print(key)

else:
    mapeo = getattr(mapeo,TEST)
    for group in mapeo:
        map_group = mapeo[group]
        for key in map_group:
            pos = map_group[key]
            pyautogui.moveTo(x+pos[0], y+pos[1], duration=0.2)
            print(key)



