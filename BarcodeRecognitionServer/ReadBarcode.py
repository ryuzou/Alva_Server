# -*- coding: utf-8 -*-
import cv2
import zbar
import MySQLdb
from time import sleep

scanner = zbar.ImageScanner()

scanner.parse_config('enable')

cap = cv2.VideoCapture(0)

connect = MySQLdb.connect(
    # host='db', port=3306, user='root', passwd='password', db='Alva_Server', charset='utf8'
    host='127.0.0.1', port=3306, user='root', passwd='password', db='Alva_Server', charset='utf8'
)
cursor = connect.cursor()

while True:

    ret, frame = cap.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    x, y = 220, 140
    # ROI no hidari ue

    w, h = 200, 200
    # ROI no width, height

    roi = gray_img[y:y + h, x:x + w]

    rows, cols = roi.shape[:2]
    image = zbar.Image(cols, rows, 'Y800', roi.tostring())
    scanner.scan(image)

    for symbol in image:
        sqltext1 = "insert into D_Barcode_log (barcode) VALUES ('"
        sqltext2 = "')"
        sqltext = sqltext1 + symbol.data + sqltext2
        cursor.execute(sqltext)
        print symbol.data

    connect.commit()
    if cv2.waitKey(1) == 27:
        break
cap.release()

cursor.close()
connect.close()  # データベースオジェクトを閉じる
# end with esc
