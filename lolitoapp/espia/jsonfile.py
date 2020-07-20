import os
import datetime
import json

def saveJson(path,nameFile,maxFiles,data):
    #Elimino los archivos que superan la cuota
    files = os.listdir(path)
    removes = len(files)-maxFiles+1
    for i in range(removes):
        os.remove("{}/{}".format(path,files[i]))
    
    fecha = datetime.datetime.now().strftime("%d-%m-%Y %H'%M'%S")
    with open('{}/{} {}.json'.format(path,nameFile,fecha), 'w') as fp:
        json.dump(data, fp)

def readJson(fileJson):
    return json.load(open(fileJson, 'r', encoding='utf-8')) 