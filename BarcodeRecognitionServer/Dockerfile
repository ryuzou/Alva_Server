FROM python:2.7

RUN apt-get update
RUN apt-get -y install libopencv-dev libzbar-dev setserial curl
RUN pip install opencv-python && pip install zbar
RUN pip install MySQL-python
RUN pip install mysql-connector-python
RUN pip install mysql-connector-python-rf
COPY ./StartProc.sh /usr/local/lib/Alva/StartProc.sh
COPY ./ReadBarcode.py /usr/local/lib/Alva/ReadBarcode.py
COPY ./debug-loop.sh /usr/local/lib/Alva/debug-loop.sh