FROM        ubuntu:16.04
MAINTAINER  msjo91@gmail.com

COPY        . /srv/app
WORKDIR     /srv/app

RUN         apt-get -y update
RUN         apt-get -y install python3
RUN         apt-get -y install python3-pip
RUN         apt-get -y install nginx
RUN         apt-get -y install supervisor

RUN         pip3 install --upgrade pip
RUN         pip3 install --upgrade setuptools
RUN         pip3 install -r requirements.txt
RUN         pip3 install uwsgi

COPY        .conf-secret/uwsgi-app.ini          /etc/uwsgi/sites/app.ini
COPY        .conf-secret/nginx.conf             /etc/nginx/nginx.conf
COPY        .conf-secret/nginx-app.conf         /etc/nginx/sites-available/app.conf
COPY        .conf-secret/supervisor-app.conf    /etc/supervisor/conf.d/

RUN         ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf

EXPOSE      4040
#CMD         supervisord -n

# docker build -t dayback .