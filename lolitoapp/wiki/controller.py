#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from helper import database
from wiki import service


def getwiki():
    dbWiki = database.DataBase('./wiki/wiki.db')
    champs = dbWiki.getAll('champs')
    return render_template('wiki.html', champs=champs)


def getchamp(champ, pos):
    dbWiki = database.DataBase('./wiki/wiki.db')
    champs = dbWiki.getAll('champs')
    data = service.prepareData(champ, pos, dbWiki)
    return render_template("wiki.html", champs=champs, data=data)
