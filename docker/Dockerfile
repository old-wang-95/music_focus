FROM python:3.7.0
MAINTAINER wang0624@foxmail.com

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt -i https://pypi.doubanio.com/simple/

COPY . /music_focus

EXPOSE 8000

CMD cd /music_focus/admin && sh start.sh
