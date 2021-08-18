FROM python:3.6.9

ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y

#RUN apt install python3.6.9-dev default-libmysqlclient-dev -y

RUN mkdir -p /usr/src/app/tdspeak

WORKDIR /usr/src/app/tdspeak

COPY . /usr/src/app/tdspeak

RUN pip install -r requirements.txt

#CMD ["bash"]

CMD ["uwsgi", "--ini", "tdspeak.ini"]
