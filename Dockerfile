FROM ubuntu

ENV PYTHONUNBUFFERED 1

ADD . .

RUN apt update

RUN apt install -y python3 python3-pip

RUN pip install -r requirements.txt

RUN python3 download.py

EXPOSE 5000

CMD uwsgi --http 0.0.0.0:5000 --module app:app