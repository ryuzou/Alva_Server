FROM python:3.7

ARG project_dir=/app/

WORKDIR $project_dir

ADD requirements.txt /requirements/

RUN pip install flask
RUN pip install -r ../requirements/requirements.txt

CMD ["python", "reply.py"]