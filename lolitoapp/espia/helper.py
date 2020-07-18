import json

def getChampId(champName,lang):
    lang = "esAR" if lang is None else lang
    file = './espia/champs/champion_{}.json'.format(lang)
    with open(file) as json_file:
        dataJson = json.load(json_file)

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

            ##### Corregir porcentajes y traer Imgen de champs frecuentes
            for league in champ['data']['champs']:
                for champPlayed in champ['data']['champs'][league]:
                    champPlayed['wins'] = "{:.0f}%".format(float(champPlayed['wins'])*100.0)
                    champID = getChampId(champPlayed['champ_name'], lang)
                    champPlayed['champ_name_img'] = 'http://ddragon.leagueoflegends.com/cdn/10.14.1/img/champion/{}.png'.format(champID)

            #### Agrego % perdidas
            for keyAvg in champ['data']['avg']:
                avg = champ['data']['avg'][keyAvg]
                avg['loss'] = "{:.1f}%".format(100-float(avg['wins'][0:-1]))
