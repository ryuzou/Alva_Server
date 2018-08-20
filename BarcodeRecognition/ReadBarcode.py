# -*- coding: utf-8 -*-
import cv2
import zbar
scanner = zbar.ImageScanner()
scanner.parse_config('enable')
cap = cv2.VideoCapture(0)
captured = False

while True:

    ret, frame = cap.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rows, cols = gray_img.shape[:2]
    image = zbar.Image(cols, rows, 'Y800', gray_img.tostring())
    scanner.scan(image)

    for symbol in image:
        #print('%s' % symbol.data)
        f = open('/usr/local/lib/Alva/barcode.txt', 'w')
        f.write('%s' % symbol.data)
        f.close()
        captured = True

    if captured:
        break

    if cv2.waitKey(1) == 27:
        break

cap.release()

cv2.destroyAllWindows()