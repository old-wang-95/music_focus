FROM docker.io/atmaniak/firefox-python3
MAINTAINER wang0624@foxmail.com

RUN ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip
RUN apt-get -y update && apt-get install fonts-wqy-zenhei

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt -i https://pypi.doubanio.com/simple/

COPY . /music_focus

EXPOSE 8000

CMD cd /music_focus/admin && sh start.sh
