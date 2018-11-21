FROM python:3.6

ARG project_dir=/app/

WORKDIR $project_dir

ADD requirements.txt /requirements/
ADD uwsgi.ini /init/

RUN apt-get install -y default-libmysqlclient-dev gcc

RUN pip install greenlet
RUN CFLAGS="-I/usr/local/include/python3.6m/greenlet" UWSGI_PROFILE="asyncio" pip install uwsgi
RUN pip install -r ../requirements/requirements.txt

CMD ["uwsgi","--ini","/init/uwsgi.ini"]