# -*- coding: utf-8 -*-
import cv2
import zbar
import threading
import MySQLdb

db = MySQLdb.connect(
    host='db', port=3306, user='root', passwd='password', db='Alva_Server', charset='utf8'
)
db.cursorclass = MySQLdb.cursors.DictCursor

scanner = zbar.ImageScanner()
scanner.parse_config('enable')
cap = cv2.VideoCapture(0)
captured = False


class Barcode_Recognise:
    inited = 0
    cap = None

    def __init__(self):
        if self.inited != 0:
            pass
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        self.cap = cv2.VideoCapture(0)
        captured = False

def Barcode_read():
    ret, frame = cap.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rows, cols = gray_img.shape[:2]
    image = zbar.Image(cols, rows, 'Y800', gray_img.tostring())
    scanner.scan(image)

    for symbol in image:
        cursor.execute('INSERT INTO D_Barcode Barcode VALUES %d', (symbol.data ,))
    cursor.close()

thread = threading.Timer(0.1, Barcode_read)
thread.start()

cap.release()