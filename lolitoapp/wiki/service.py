# Get builds by champ,pos,name
QUERY1 = 'SELECT * FROM builds WHERE id_champ = ? and pos = ? and name = ? LIMIT 1'


def addItemsX(build, nameX, keyX, max):
    result = []
    for i in range(1, max + 1):
        name = nameX.format(i)
        if (name in build) and (build[name] is not None) and (build[name].strip() != ""):
            key = keyX.format(i)
            result.append({key: build[name]})
    return result


def prepareBuilds(build):
    result = {}
    result['trinket'] = {'wr': build['trinket_wr'], 'img': build['trinket_img']}
    result['skill'] = {'wr': build['skill_order_wr'], 'data': build['skill_order_data'].split(";")}
    result['summoners'] = {'wr': build['summoners_wr']}
    result['start_build'] = {'wr': build['start_build_wr']}
    result['full_build'] = {'wr': build['full_build_wr']}
    result['runes'] = {'wr': build['runes_wr']}

    result['summoners']['items'] = addItemsX(build, "summoners{}_img", "img", 2)
    result['start_build']['items'] = addItemsX(build, "start_build{}_img", "img", 6)
    result['full_build']['items'] = addItemsX(build, "full_build{}_img", "img", 6)
    result['runes']['items'] = addItemsX(build, "runes{}_img", "img", 11)

    return result


def prepareData(champ, pos, dbWiki):
    champ = dbWiki.getFirst('champs', 'name', champ)
    statics = dbWiki.getFirst('statics', 'id_champ', champ['id'])
    buildH = dbWiki.getQuery(QUERY1, [champ['id'], pos, 'highest'])[0]
    buildF = dbWiki.getQuery(QUERY1, [champ['id'], pos, 'frecuent'])[0]
    champ['role'] = pos.capitalize()
    data = {
        'champ': champ,
        'statics': statics,
        'buildH': prepareBuilds(buildH),
        'buildF': prepareBuilds(buildF),
    }
    return data
