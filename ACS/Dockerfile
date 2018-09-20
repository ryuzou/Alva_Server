FROM python:3.6

ARG project_dir=/app/

WORKDIR $project_dir

ADD requirements.txt /requirements/

RUN apt-get install -y default-libmysqlclient-dev gcc

RUN pip install flask
RUN pip install -r ../requirements/requirements.txt

CMD ["python", "reply.py"]