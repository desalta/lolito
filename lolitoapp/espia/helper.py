import json

def getChampId(champName,lang):
    lang = "esAR" if lang is None else lang
    fileJson = './espia/champs/champion_{}.json'.format(lang)
    dataJson = json.load(open(fileJson, 'r', encoding='utf-8'))

    for key in dataJson['data']:
        if dataJson['data'][key]['name'] == champName:
            return key

def fixData(data,lang):
    lang = "esAR" if lang is None else lang

    for team in data:
        for champ in data[team]:

            ##### Corrijo Nombre de las posiciones
            champ['pos'] = "Top" if champ['pos'] == "TOP" else champ['pos']
            champ['pos'] = "Jg" if champ['pos'] == "JUNGLE" else champ['pos']
            champ['pos'] = "Mid" if champ['pos'] == "MIDDLE" else champ['pos']
            champ['pos'] = "Adc" if champ['pos'] == "BOTTOM" else champ['pos']
            champ['pos'] = "Supp" if champ['pos'] == "UTILITY" else champ['pos']

            ##### Traigo ChampID
            champID = getChampId(champ['champ'],lang)

            ##### Traigo Url Sking
            skinID = champ['skin']
            champ['champ_img'] = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{}_{}.jpg'.format(champID,skinID)

            #### Agrego % perdidas
            for keyAvg in champ['data']['avg']:
                avg = champ['data']['avg'][keyAvg]
                avg['loss'] = "{:.1f}%".format(100-float(avg['wins'][0:-1]))

            #### Pongo champ usado en primero lugar
            buscado = champ['champ']
            for league in champ['data']['champs']:
                lista = champ['data']['champs'][league]
                noesta = True
                for i in range(len(lista)):
                    if lista[i]['champ_name']==buscado:
                        lista.insert(0, lista.pop(i))
                        noesta = False
                if noesta:
                    lista.insert(0,{
                            "champ_name": buscado,
                            "champ_level": "",
                            "champ_level_img": "",
                            "kda": {
                                "kills": "0",
                                "deaths": "0",
                                "assists": "0"
                            },
                            "plays": "0",
                            "wins": "0"
                        })
            
            ##### Corregir porcentajes y traer Imgen de champs frecuentes
            for league in champ['data']['champs']:
                for champPlayed in champ['data']['champs'][league]:
                    champPlayed['wins'] = "{:.0f}%".format(float(champPlayed['wins'])*100.0)
                    champID = getChampId(champPlayed['champ_name'], lang)
                    champPlayed['champ_name_img'] = 'http://ddragon.leagueoflegends.com/cdn/10.14.1/img/champion/{}.png'.format(champID)

def getMapAnalisis(data):
    result = {}
    ids = {'chaos':0,'order':0}

    def getFila(pos,team, ids):
        if pos is not None and pos != "":
            val = 0 if pos=="Jg" else None
            val = 1 if pos=="Top" else val
            val = 2 if pos=="Mid" else val
            val = 3 if pos=="Adc" else val
            val = 4 if pos=="Supp" else val
            inc = 0 if team=="CHAOS" else 5
            return val+inc
        else:
            if team == "CHAOS":
                val = ids['chaos']
                ids['chaos'] += 1
                return val
            else:
                val = ids['order']
                ids['order'] += 1
                return val + 5

    for keyTeam in data:
        for champ in data[keyTeam]:
            fila = getFila(champ['pos'],keyTeam,ids)
            avg = champ['data']['avg']['normales']
            kda = champ['data']['kda']['normales']
            league = champ['data']['league']
            best_league = league['best_league']
            champSel = champ['data']['champs']['normales'][0]
            champSelKda = champSel['kda']
            

            result[fila] = {
                0 : champ['pos'],
                1 : champ['name'],
                2 : "{} ({})".format(avg['plays'],avg['wins']), #play(wins) general
                3 : champ['champ'], #champ name
                4 : "" if champSel['champ_level']==None else champSel['champ_level'], #maestria
                5 : "{}/{}/{}".format(champSelKda['kills'],champSelKda['deaths'],champSelKda['assists']), #kda
                6 : "{} ({})".format(champSel['plays'],champSel['wins']), #play(wins) campeon
                7 : league['enemy_avg']['name'], #enemigos
                8 : best_league['name'] if 'name' in best_league else "", #max league
                #'7' : 0 #puntaje general
            }

    return result