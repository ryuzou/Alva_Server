# -*- coding: utf-8 -*-
import cv2
import zbar
from Communicate import UDP_connection

scanner = zbar.ImageScanner()

scanner.parse_config('enable')

cap = cv2.VideoCapture(0)

captured = False
UDP = UDP_connection()
UDP.Config(web)

while True:

    try:
        if UDP.Recieve()[-1] == "read":
            pass
        elif UDP.Recieve()[-1] == "end":
            break
    except:
        continue

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
        # print('%s' % symbol.data)
        UDP.Send(symbol.data)


cap.release()