from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import json
import ssl
import threading
import time

from . import jsonfile

def getSoupUrl(url):
    try:
        print("request: "+url + "...\n")
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
        with urllib.request.urlopen(req) as response:
            html = response.read()
            soup = BeautifulSoup(html, "html.parser")
            print("request: "+url + " ... terminado :) \n")
            return soup
    except:
        print("request: "+url + " ... error :) \n")
        return None


def getJson(url):
    print(url + " ...")
    try:
        context = ssl._create_unverified_context()
        res = urllib.request.urlopen(url, context=context)
        res_body = res.read()
        return json.loads(res_body.decode("utf-8"))
    except:
        return None

def getLocalData():
    #Get data of game
    data = getJson('https://127.0.0.1:2999/liveclientdata/allgamedata')
    jsonfile.saveJson('./espia/logs','localdata',20,data)
    #data = jsonfile.readJson("./espia/logs/localdata 20-07-2020 16'30'24.json")
    if data is None:
       return None 

    result = {'ORDER': [], 'CHAOS': []}
    for play in data['allPlayers']:
        if not play['isBot']:
            result[play['team']].append({
                'name': play['summonerName'],
                'champ': play['championName'],
                'pos': play['position'],
                'skin' : play['skinID'],
                'champ_img' : ""
            })

    return result


def getStatChamp(server, name):
    soup = getSoupUrl('https://www.leagueofgraphs.com/es/summoner/{}/{}'.format(server, name))
    result = {}

    if soup is None:
        return result

    test = soup.find(id="profileBasicStats")
    if test is None:
        return result

    start_time = time.time()
    print ("stats INI: {}".format(name))
    ############################# LIGA
    league = result['league'] = {}

    best_league = league['best_league'] = {}
    if (len(soup.select('.summoner-rankings .best-league .winsNumber')) > 0):
        best_league['img'] = "http:" + soup.select('.summoner-rankings .best-league .img-align-block img')[0]['src']
        best_league['name'] = soup.select('.summoner-rankings .best-league .leagueTier')[0].text.replace('\n', '').strip()
        best_league['mode'] = soup.select('.summoner-rankings .best-league .queue')[0].text.replace('\n', '').strip()
        best_league['rank'] = soup.select('.summoner-rankings .best-league .rank .highlight')[0].text.replace('\n', '').strip()
        best_league['toprank'] = soup.select('.summoner-rankings .best-league .topRankPercentage')[0].text.replace('\n', '').strip()
        best_league['points'] = soup.select('.summoner-rankings .best-league .leaguePoints')[0].text.replace('\n', '').strip()
        best_league['wins'] = soup.select('.summoner-rankings .best-league .winsNumber')[0].text.replace('\n', '').strip()
        best_league['losses'] = soup.select('.summoner-rankings .best-league .lossesNumber')[0].text.replace('\n', '').strip()

    other_league = league['other_league'] = {}
    if (len(soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .winsNumber')) > 0):
        other_league['img'] = "http:" + soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .img-align-block img')[0]['src']
        other_league['name'] = soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .leagueTier')[0].text.replace('\n', '').strip()
        other_league['mode'] = soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .queueName')[0].text.replace('\n', '').strip()
        other_league['rank'] = soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .rankLine .highlight-dark-only')[0].text.replace('\n', '').strip()
        other_league['toprank'] = soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .topRankPercentage')[0].text.replace('\n', '').strip()
        other_league['points'] = soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .leaguePoints')[0].text.replace('\n', '').strip()
        other_league['wins'] = soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .winsNumber')[0].text.replace('\n', '').strip()
        other_league['losses'] = soup.select('.summoner-rankings .other-league:not(.averageEnnemyLine) .lossesNumber')[0].text.replace('\n', '').strip()

    enemy_avg = league['enemy_avg'] = {}
    enemy_avg['img'] = "http:" + soup.select('.summoner-rankings .other-league.averageEnnemyLine .img-align-block img')[0]['src']
    enemy_avg['name'] = soup.select('.summoner-rankings .other-league.averageEnnemyLine .leagueTier')[0].text.replace(
        '\n', '').strip()

    ############################# TAGS
    result['tags'] = []
    for tag in soup.select('.tags-box .tag'):
        result['tags'].append({'text': tag.text.replace('\n', '').strip(), 'color': tag['class'][len(tag['class']) - 1]})

    ############################# AVG 
    avg = result['avg'] = {}

    aux = soup.find(id="profileBasicStats").find('div', {'data-tab-id': 'championsData-ranked'}).findAll('div', {'class': 'pie-chart-container'})
    avg['ranked'] = {
        'plays': aux[0].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip(),
        'wins': aux[1].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip()
    }

    aux = soup.find(id="profileBasicStats").find('div', {'data-tab-id': 'championsData-soloqueue'}).findAll('div', {'class': 'pie-chart-container'})
    avg['soloqueue'] = {
        'plays': aux[0].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip(),
        'wins': aux[1].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip()
    }

    aux = soup.find(id="profileBasicStats").find('div', {'data-tab-id': 'championsData-flex'}).findAll('div', {'class': 'pie-chart-container'})
    avg['flexible'] = {
        'plays': aux[0].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip(),
        'wins': aux[1].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip()
    }

    aux = soup.find(id="profileBasicStats").find('div', {'data-tab-id': 'championsData-all-queues'}).findAll('div', {'class': 'pie-chart-container'})
    avg['normales'] = {
        'plays': aux[0].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip(),
        'wins': aux[1].find('div', {'class': 'pie-chart'}).text.replace('\n', '').strip()
    }

    ############################# AVG KDA
    avg = result['kda'] = {}

    aux = soup.find(id="profileKda").find('div', {'data-tab-id': 'championsData-ranked'})
    avg['ranked'] = {
        'kills': aux.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
        'deaths': aux.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
        'assists': aux.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
    }

    aux = soup.find(id="profileKda").find('div', {'data-tab-id': 'championsData-soloqueue'})
    avg['soloqueue'] = {
        'kills': aux.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
        'deaths': aux.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
        'assists': aux.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
    }

    aux = soup.find(id="profileKda").find('div', {'data-tab-id': 'championsData-flex'})
    avg['flexible'] = {
        'kills': aux.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
        'deaths': aux.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
        'assists': aux.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
    }

    aux = soup.find(id="profileKda").find('div', {'data-tab-id': 'championsData-all-queues'})
    avg['normales'] = {
        'kills': aux.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
        'deaths': aux.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
        'assists': aux.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
    }

    ############################# CHAMPS FAVORITOS
    avg = result['champs'] = {}

    aux = soup.find(id="favchamps").find('div', {'data-tab-id': 'championsData-ranked'}).findAll('tr')
    avg['ranked'] = []
    for item in aux:
        if item.find('div', {'class': 'name'}) is not None:
            avg['ranked'].append({
                'champ_img' : None,
                'champ_name': item.find('div', {'class': 'name'}).text.replace('\n', '').strip(),
                'champ_level': None if item.find('img', {'class': 'championMasteryLevelIcon'}) is None else item.find('img', {'class': 'championMasteryLevelIcon'})['alt'][-1],
                'champ_level_img': None if item.find('img', {'class': 'championMasteryLevelIcon'}) is None else "http:" + item.find('img', {'class': 'championMasteryLevelIcon'})['src'],
                'kda': {
                    'kills': item.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
                    'deaths': item.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
                    'assists': item.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
                },
                'plays': item.findAll('td')[1].find('progressbar')['data-value'],
                'wins': item.findAll('td')[2].find('progressbar')['data-value'][:5]
            })

    aux = soup.find(id="favchamps").find('div', {'data-tab-id': 'championsData-soloqueue'}).findAll('tr')
    avg['soloqueue'] = []
    for item in aux:
        if item.find('div', {'class': 'name'}) is not None:
            avg['soloqueue'].append({
                'champ_img': None,
                'champ_name': item.find('div', {'class': 'name'}).text.replace('\n', '').strip(),
                'champ_level': None if item.find('img', {'class': 'championMasteryLevelIcon'}) is None else
                item.find('img', {'class': 'championMasteryLevelIcon'})['alt'][-1],
                'champ_level_img': None if item.find('img',{'class': 'championMasteryLevelIcon'}) is None else "http:" + item.find('img', {'class': 'championMasteryLevelIcon'})['src'],
                'kda': {
                    'kills': item.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
                    'deaths': item.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
                    'assists': item.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
                },
                'plays': item.findAll('td')[1].find('progressbar')['data-value'],
                'wins': item.findAll('td')[2].find('progressbar')['data-value'][:5]
            })

    aux = soup.find(id="favchamps").find('div', {'data-tab-id': 'championsData-flex'}).findAll('tr')
    avg['flexible'] = []
    for item in aux:
        if item.find('div', {'class': 'name'}) is not None:
            avg['flexible'].append({
                'champ_img': None,
                'champ_name': item.find('div', {'class': 'name'}).text.replace('\n', '').strip(),
                'champ_level': None if item.find('img', {'class': 'championMasteryLevelIcon'}) is None else
                item.find('img', {'class': 'championMasteryLevelIcon'})['alt'][-1],
                'champ_level_img': None if item.find('img',{'class': 'championMasteryLevelIcon'}) is None else "http:" + item.find('img', {'class': 'championMasteryLevelIcon'})['src'],
                'kda': {
                    'kills': item.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
                    'deaths': item.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
                    'assists': item.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
                },
                'plays': item.findAll('td')[1].find('progressbar')['data-value'],
                'wins': item.findAll('td')[2].find('progressbar')['data-value'][:5]
            })

    aux = soup.find(id="favchamps").find('div', {'data-tab-id': 'championsData-all-queues'}).findAll('tr')
    avg['normales'] = []
    for item in aux:
        if item.find('div', {'class': 'name'}) is not None:
            avg['normales'].append({
                'champ_img': None,
                'champ_name': item.find('div', {'class': 'name'}).text.replace('\n', '').strip(),
                'champ_level': None if item.find('img', {'class': 'championMasteryLevelIcon'}) is None else
                item.find('img', {'class': 'championMasteryLevelIcon'})['alt'][-1],
                'champ_level_img': None if item.find('img',{'class': 'championMasteryLevelIcon'}) is None else "http:" + item.find('img', {'class': 'championMasteryLevelIcon'})['src'],
                'kda': {
                    'kills': item.find('span', {'class': 'kills'}).text.replace('\n', '').strip(),
                    'deaths': item.find('span', {'class': 'deaths'}).text.replace('\n', '').strip(),
                    'assists': item.find('span', {'class': 'assists'}).text.replace('\n', '').strip()
                },
                'plays': item.findAll('td')[1].find('progressbar')['data-value'],
                'wins': item.findAll('td')[2].find('progressbar')['data-value'][:5]
            })

    elapsed_time = time.time() - start_time
    print ("stats END: {} time:{}".format(name,elapsed_time))
    return result

def setDataChampInThread(server,name,champ):
    champ['data'] = getStatChamp(server,name)

def getLiveData(server, localdata):
    thread_list = []
    for team in localdata:
        for champ in localdata[team]:
            name = urllib.parse.quote(champ['name'])
            #setDataChampInThread(server,name,champ)
            print('abriendo thread para buscar: '+name)
            t = threading.Thread(target=setDataChampInThread, args=(server, name,champ))
            thread_list.append(t)
            t.start()

    for thread in thread_list:
        thread.join()
    
    print("join all ...")

def getMockdata():
    with open('./espia/allspydata.json') as json_file:
        data = json.load(json_file)
    localdata = data
