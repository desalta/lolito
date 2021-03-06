
acciones = {
    'PRIM_RUNA'     : [-272,-468],
    'PRIM_CLAVE'    : [-272,-349],
    'PRIM_RAN1'     : [-272,-253],
    'PRIM_RAN2'     : [-272,-164],
    'PRIM_RAN3'     : [-272,-78],
    'SEC_RUNA'      : [53,-468],
    'SEC_RAN1'      : [53,-356],
    'SEC_RAN2'      : [53,-251],
    'FRAG1'        : [53,-166],
    'FRAG2'        : [53,-120],
    'FRAG3'        : [53,-78],
    'GUARDAR'       : [88,-556],
    'EDITAR'       : [-276,-555]
}

#La runa primaria se muestran todas en el siguiente orden
ruta_prim = {
    'PRE'   : [-197,-465],
    'DOM'   : [-156,-465],
    'BRU'   : [-117,-465],
    'VAL'   : [-77,-465],
    'INS'   : [-37,-465],
}

#La runa secundaria se muestran todas menos la primaria
ruta_sec = {
    'RUN0'   : [136,-465],
    'RUN1'   : [186,-465],
    'RUN2'   : [234,-465],
    'RUN3'   : [285,-465],
}

def get_ruta_sec(pri,sec):
    lista = ['PRE','DOM','BRU','VAL','INS']
    posP = lista.index(pri)
    posS = lista.index(sec)

    if posP<=posS:
        posAux = 0 if posS-1<0 else posS-1
        return(ruta_sec['RUN{}'.format(posAux)])
    else:
        return(ruta_sec['RUN{}'.format(posS)])


runa_prim = {
    'PRE' : {
        'clave'  : {
            'EO'    : [-192,-348],
            'CL'    : [-142,-347],
            'SM'    : [-94,-348],
            'CO'     : [-45,-349],
        },
        'ranura1': {
            'S'     : [-184,-249],
            'T'     : [-119,-249],
            'CP'    : [-52,-249],
        },
        'ranura2': {
            'LC'    : [-185,-163],
            'LT'    : [-119,-162],
            'LL'    : [-53,-166],
        },
        'ranura3': {
            'GG'    : [-185,-76],
            'C'     : [-118,-76],
            'UB'    : [-53,-75],
        },
    },

    'DOM' : {
        'clave'  : {
            'E'     : [-192,-347],
            'D'     : [-143,-348],
            'CO'    : [-92,-346],
            'LE'    : [-44,-347],
        },
        'ranura1': {
            'GB'    : [-184,-252],
            'SS'    : [-118,-252],
            'IS'    : [-52,-252],
        },
        'ranura2': {
            'CZ'    : [-184,-165],
            'PF'    : [-120,-165],
            'CDO'    : [-51,-162],
        },
        'ranura3': {
            'CV'    : [-193,-73],
            'CIN'   : [-143,-76],
            'CIM'   : [-94,-76],
            'CD'    : [-44,-77],
        },
    },

    'BRU' : {
        'clave'  : {
            'IA'    : [-181,-347],
            'CAR'    : [-121,-344],
            'FV'    : [-54,-346],
        },
        'ranura1': {
            'OA'    : [-184,-253],
            'AFM'    : [-119,-252],
            'CN'    : [-51,-252],
        },
        'ranura2': {
            'T'     : [-184,-167],
            'C'     : [-117,-165],
            'CAB'    : [-51,-163],
        },
        'ranura3': {
            'Q'     : [-186,-74],
            'CSA'    : [-119,-75],
            'TC'    : [-52,-76],
        },
    },

    'VAL' : {
        'clave'  : {
            'AP'    : [-181,-347],
            'REP'     : [-121,-344],
            'G'     : [-54,-346],
        },
        'ranura1': {
            'D'     : [-184,-253],
            'FV'    : [-119,-252],
            'GE'    : [-51,-252],
        },
        'ranura2': {
            'A'     : [-184,-167],
            'SA'    : [-117,-165],
            'CO'    : [-51,-163],
        },
        'ranura3': {
            'CE'    : [-186,-74],
            'REV'     : [-119,-75],
            'I'     : [-52,-76],
        },
    },

    'INS' : {
        'clave'  : {
            'AG'    : [-181,-347],
            'LHA'    : [-121,-344],
            'RU'    : [-54,-346],
        },
        'ranura1': {
            'DH'    : [-184,-253],
            'CM'    : [-119,-252],
            'MO'    : [-51,-252],
        },
        'ranura2': {
            'MF'    : [-184,-167],
            'DS'    : [-117,-165],
            'EG'    : [-51,-163],
        },
        'ranura3': {
            'PC'    : [-186,-74],
            'VA'    : [-119,-75],
            'TDT'    : [-52,-76],
        },
    }
}

runa_sec = {
    'PRE' : {
        'S'     : [140,-379],
        'T'     : [207,-381],
        'CP'    : [274,-380],
        'LC'    : [141,-303],
        'LT'    : [206,-302],
        'LL'    : [271,-304],
        'GG'    : [140,-225],
        'C'     : [206,-227],
        'UB'    : [273,-225],
    },

    'DOM' : {
        'GB'    : [140,-379],
        'SS'    : [207,-381],
        'IS'    : [274,-380],
        'CZ'    : [141,-303],
        'PF'    : [206,-302],
        'CDO'    : [271,-304],
        'CV'    : [133,-225],
        'CIN'   : [181,-226],
        'CIM'   : [234,-224],
        'CD'    : [281,-224],
    },

    'BRU' : {
        'OA'    : [140,-379],
        'AFM'    : [207,-381],
        'CN'    : [274,-380],
        'T'     : [141,-303],
        'C'     : [206,-302],
        'CAB'    : [271,-304],
        'Q'     : [140,-225],
        'CSA'    : [206,-227],
        'TC'    : [273,-225],
    },

    'VAL' : {
        'D'     : [140,-379],
        'FV'    : [207,-381],
        'GE'    : [274,-380],
        'A'     : [141,-303],
        'SA'    : [206,-302],
        'CO'    : [271,-304],
        'CE'    : [140,-225],
        'REV'     : [206,-227],
        'I'     : [273,-225],
    },

    'INS' : {
        'DH'    : [140,-379],
        'CM'    : [207,-381],
        'MO'    : [274,-380],
        'MF'    : [141,-303],
        'DS'    : [206,-302],
        'EG'    : [271,-304],
        'PC'    : [140,-225],
        'VA'    : [206,-227],
        'TDT'   : [273,-225],
    },
}

frag = {
    'ranura1': {
        'OP1'    : [140,-161],
        'OP2'    : [207,-163],
        'OP3'    : [274,-162],
    },
    'ranura2': {
        'OP1'    : [142,-117],
        'OP2'    : [206,-119],
        'OP3'    : [274,-116],
    },
    'ranura3': {
        'OP1'    : [140,-73],
        'OP2'    : [206,-74],
        'OP3'    : [272,-73],
    },
}