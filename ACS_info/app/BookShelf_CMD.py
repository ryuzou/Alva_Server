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

    def GetBookInfo(self, BookFullname=None, BookFullID=None):
        if not BookFullname == None:
            self.__cur.execute("SELECT id from D_Bookdata WHERE book_title = %s", BookFullname)
            BookFullID = self.__cur.fetchall()
        else:
            self.__cur.execute("SELECT book_title from D_Bookdata WHERE id = %s", BookFullID)
            BookFullname = self.__cur.fetchall()
        self.__cur.execute("SELECT Barcode from D_Bookdata WHERE id = %s", BookFullID)
        Barcode = self.__cur.fetchall()
        self.__cur.execute("SELECT book_author from D_Bookdata WHERE id = %s", BookFullID)
        BookAuthor = self.__cur.fetchall()
        self.__cur.execute("SELECT book_genre from D_Bookdata WHERE id = %s", BookFullID)
        BookGenre = self.__cur.fetchall()
        RteDict = {
            "bookid": BookFullID,
            "bookname": BookFullname,
            "barcode": Barcode,
            "author": BookAuthor,
            "genre": BookGenre
        }
        return RteDict

    def GetBookIMG(self, BookFullID):
        self.__cur.execute("SELECT book_img from D_Bookdata WHERE id = %s", BookFullID)
        BookIMG = self.__cur.fetchall()  # todo
        pass

    def GetBookIdealCOD(self, BookFullID):
        self.__cur.execute("SELECT XGrid_Place from D_BookShelf WHERE id = %s", BookFullID)
        BookCod_X = self.__cur.fetchall()
        self.__cur.execute("SELECT YGrid_Place from D_BookShelf WHERE id = %s", BookFullID)
        BookCod_Y = self.__cur.fetchall()
        RetDict = {
            "X": BookCod_X,
            "Y": BookCod_Y
        }
        return RetDict

    def GetBookIDFromName(self, BookFullName):
        pass

    def EstimateBookFullName(self, Name):
        pass

    def GetBookIDFromBarcode(self, Barcode):
        pass


BDB = BookstaticDB()
