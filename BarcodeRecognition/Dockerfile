FROM python:2.7

RUN apt-get update
RUN apt-get -y install libopencv-dev libzbar-dev
RUN pip install opencv-python && pip install zbar
COPY ./StartProc.sh /usr/local/lib/Alva/StartProc.sh
COPY ./ReadBarcode.py /usr/local/lib/Alva/ReadBarcode.py

CMD sh /usr/local/lib/Alva/StartProc.sh