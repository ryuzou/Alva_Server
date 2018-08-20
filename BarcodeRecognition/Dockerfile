FROM python:2.7

RUN apt-get update
RUN apt-get install libopencv-dev libzbar-dev
RUN pip install opencv-python && pip install zbar
COPY ./StartProc.sh ./StartProc.sh

RUN ./StartProc.sh