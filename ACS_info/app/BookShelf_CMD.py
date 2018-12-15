import flask
from flask import Flask, jsonify, request
import json
import MySQLdb
import time


class BookstaticDB:
    __conn = None
    __cur = None

    def __testSQLconnection(self, nestnum=0):
        Pnestnum = nestnum + 1
        try:
            MySQLdb.connect(host='rdb', user='root', passwd='password', db='Alva_Server', charset='utf8')
            return 0
        except MySQLdb.Error as e:
            if nestnum >= 10:
                if nestnum >= 10:
                    return -1
                time.sleep(0.2)
            print("mysql connection error :", e)
            self.__testSQLconnection(Pnestnum)

    def __init__(self):
        if self.__testSQLconnection() != 0:
            print("sql error")
        self.__conn = MySQLdb.connect(host='rdb', user='root', passwd='password', db='Alva_Server', charset='utf8')
        self.__cur = self.__conn.cursor()

    def GetBookInfo(self, BookFullname=None, BookFullID=None):
        if not BookFullname == None:
            sql = "SELECT id from D_Bookdata WHERE book_title = %s" % (BookFullname,)
            self.__cur.execute(sql)
            BookFullID = self.__cur.fetchall()
        else:
            sql = "SELECT book_title from D_Bookdata WHERE id = %s" % (BookFullID,)
            self.__cur.execute(sql)
            BookFullname = self.__cur.fetchall()
        sql = "SELECT Barcode from D_Bookdata WHERE id = %s" % (BookFullID,)
        self.__cur.execute(sql)
        Barcode = self.__cur.fetchall()
        sql = "SELECT book_author from D_Bookdata WHERE id = %s" % (BookFullID,)
        self.__cur.execute(sql)
        BookAuthor = self.__cur.fetchall()
        sql = "SELECT book_genre from D_Bookdata WHERE id = %s" % (BookFullID,)
        self.__cur.execute(sql)
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
        sql = "SELECT book_img from D_Bookdata WHERE id = %s" % (BookFullID,)
        self.__cur.execute(sql)
        BookIMG = self.__cur.fetchall()  # todo
        return BookIMG

    def GetBookIdealCOD(self, BookFullID):
        sql = "SELECT XGrid_Place from D_BookShelf WHERE id = %s" % (BookFullID,)
        self.__cur.execute(sql)
        BookCod_X = self.__cur.fetchall()
        sql = "SELECT YGrid_Place from D_BookShelf WHERE id = %s" % (BookFullID,)
        print(sql)
        self.__cur.execute(sql)
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
