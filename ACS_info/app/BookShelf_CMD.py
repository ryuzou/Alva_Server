import flask
from flask import Flask, jsonify, request
import json
import MySQLdb


class BookstaticDB:
    __conn = None
    __cur = None

    def __init__(self):
        self.__conn = MySQLdb.connect(host='rdb', user='root', passwd='password', db='Alva_Server', charset='utf8')
        self.__cur = self.__conn.cursor()
