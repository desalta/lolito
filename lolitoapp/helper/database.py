#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sqlite3


class DataBase:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.path = path

    def _getCon(self):
        return self.db

    def _closeConnection(self):
        self.db.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self._closeConnection()

    ############################################################### DATABASE

    @staticmethod
    def getDb(path):
        if os.path.isfile(path):
            return DataBase(path)
        else:
            return DataBase(path).createTables()

    def deleteDb(self):
        os.remove(self.path)

    def createTables(self):
        db = sqlite3.connect(self.path)
        db.execute(
            '''CREATE TABLE "champs" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT, "name" TEXT UNIQUE, "url" TEXT,"img" TEXT, "pos" TEXT )''')
        db.execute(
            '''CREATE TABLE "statics" ( "id" INTEGER, "id_champ" INTEGER, "league" TEXT, "role_rate" TEXT, "win_rate" TEXT, "play_rate" TEXT, "ban_rate" TEXT, "pagp" TEXT, "gold_earned" TEXT, "kills" TEXT, "deaths" TEXT, "assists" TEXT, "damage_dealt" TEXT, "damage_taken" TEXT, "minions_killed" TEXT, "place" TEXT, "damage_composition" TEXT, PRIMARY KEY("id") )''')
        db.execute(
            '''CREATE TABLE "builds" ( "id" INTEGER,"id_champ" INTEGER, "name" TEXT,"league" TEXT, "pos" TEXT,"trinket_wr" TEXT,"trinket_name_en" TEXT,"trinket_name_es" TEXT,"trinket_img" TEXT,"summoners_wr" TEXT,"summoners1_name_en" TEXT,"summoners1_name_es" TEXT,"summoners1_img" TEXT,"summoners2_name_en" TEXT,"summoners2_name_es" TEXT,"summoners2_img" TEXT,"start_build_wr" TEXT,"start_build1_name_en" TEXT,"start_build1_name_es" TEXT,"start_build1_img" TEXT,"start_build2_name_en" TEXT,"start_build2_name_es" TEXT,"start_build2_img" TEXT,"start_build3_name_en" TEXT,"start_build3_name_es" TEXT,"start_build3_img" TEXT,"start_build4_name_en" TEXT,"start_build4_name_es" TEXT,"start_build4_img" TEXT,"start_build5_name_en" TEXT,"start_build5_name_es" TEXT,"start_build5_img" TEXT,"start_build6_name_en" TEXT,"start_build6_name_es" TEXT,"start_build6_img" TEXT,"full_build_wr" TEXT,"full_build1_name_en" TEXT,"full_build1_name_es" TEXT,"full_build1_img" TEXT,"full_build2_name_en" TEXT,"full_build2_name_es" TEXT,"full_build2_img" TEXT,"full_build3_name_en" TEXT,"full_build3_name_es" TEXT,"full_build3_img" TEXT,"full_build4_name_en" TEXT,"full_build4_name_es" TEXT,"full_build4_img" TEXT,"full_build5_name_en" TEXT,"full_build5_name_es" TEXT,"full_build5_img" TEXT,"full_build6_name_en" TEXT,"full_build6_name_es" TEXT,"full_build6_img" TEXT,"skill_order_wr" TEXT,"skill_order_data" TEXT,"runes_wr" TEXT,"runes1_name_en" TEXT,"runes1_name_es" TEXT,"runes1_img" TEXT,"runes2_name_en" TEXT,"runes2_name_es" TEXT,"runes2_img" TEXT,"runes3_name_en" TEXT,"runes3_name_es" TEXT,"runes3_img" TEXT,"runes4_name_en" TEXT,"runes4_name_es" TEXT,"runes4_img" TEXT,"runes5_name_en" TEXT,"runes5_name_es" TEXT,"runes5_img" TEXT,"runes6_name_en" TEXT,"runes6_name_es" TEXT,"runes6_img" TEXT,"runes7_name_en" TEXT,"runes7_name_es" TEXT,"runes7_img" TEXT,"runes8_name_en" TEXT,"runes8_name_es" TEXT,"runes8_img" TEXT,"runes9_name_en" TEXT,"runes9_name_es" TEXT,"runes9_img" TEXT,"runes10_name_en" TEXT,"runes10_name_es" TEXT,"runes10_img" TEXT,"runes11_name_en" TEXT,"runes11_name_es" TEXT,"runes11_img" TEXT,PRIMARY KEY("id") )''')
        db.execute(
            '''CREATE TABLE "items" ( "id" INTEGER, "url_en" TEXT, "url_es" TEXT, "img" TEXT, "name_en" TEXT, "name_es" TEXT, PRIMARY KEY("id") )''')
        db.close()
        return self

    ############################################################### QUERYS

    # return data={"id_champ":1,"name":"akali"}
    def getAll(self, table):
        cursorObj = self.db.cursor()
        result = []

        command = 'SELECT * FROM {}'.format(table)
        sqlresult = cursorObj.execute(command)
        if sqlresult is not None:
            for row in sqlresult:
                resultItem = {}
                for i in range(len(sqlresult.description)):
                    resultItem[sqlresult.description[i][0]] = row[i]
                result.append(resultItem)
        return result

    # return data={"id_champ":1,"name":"akali"}
    def getFirst(self, table, column, value):
        cursorObj = self.db.cursor()

        command = 'SELECT * FROM {} WHERE {} = ? LIMIT 1'.format(table, column)
        sqlresult = cursorObj.execute(command, (value,))
        if sqlresult is not None:
            for row in sqlresult:
                result = {}
                for i in range(len(sqlresult.description)):
                    result[sqlresult.description[i][0]] = row[i]
                return result
        return None

    def getQuery(self, query, values):
        cursorObj = self.db.cursor()
        result = []

        sqlresult = cursorObj.execute(query, values)
        for row in sqlresult:
            resultItem = {}
            for i in range(len(sqlresult.description)):
                resultItem[sqlresult.description[i][0]] = row[i]
            result.append(resultItem)

        return result

    # data={"id_champ":1,"name":"akali"}
    def insert(self, table, data):
        cursorObj = self.db.cursor()

        columns = ""
        values = ""
        variables = []

        for k, v in data.items():
            columns += k + ","
            values += "?,"
            variables.append(v)

        command = 'INSERT INTO {} ({}) VALUES({})'.format(table, columns[:-1], values[:-1])
        cursorObj.execute(command, (variables))
        self.db.commit()

    # data={"id_champ":1,"name":"akali"}
    def update(self, table, data, id):
        cursorObj = self.db.cursor()

        columns = ""
        variables = []
        for k, v in data.items():
            columns += k + " = ?, "
            variables.append(v)

        command = 'UPDATE {} SET {} WHERE ID = {}'.format(table, columns[:-2], id)
        cursorObj.execute(command, variables)
        self.db.commit()