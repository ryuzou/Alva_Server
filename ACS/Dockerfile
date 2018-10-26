FROM python:3.6

ARG project_dir=/app/

WORKDIR $project_dir

ADD requirements.txt /requirements/
ADD uwsgi.ini /init/

RUN apt-get install -y default-libmysqlclient-dev gcc

RUN pip install flask flask-cors
RUN pip install -r ../requirements/requirements.txt

CMD ["uwsgi","--ini","/init/uwsgi.ini"]