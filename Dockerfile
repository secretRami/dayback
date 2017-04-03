FROM        dayback-base
MAINTAINER  msjo91@gmail.com

COPY        . /srv/app
WORKDIR     /srv/app

COPY        .conf-secret/uwsgi-app.ini /etc/uwsgi/sites/app.ini

# docker build -t dayback .