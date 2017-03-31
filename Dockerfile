FROM        dayback-base
MAINTAINER  msjo91@gmail.com

COPY        . /srv/app
WORKDIR     /srv/app

COPY        .conf-secret/uwsgi-app.ini          /etc/uwsgi/sites/app.ini
COPY        .conf-secret/nginx.conf             /etc/nginx/nginx.conf
COPY        .conf-secret/nginx-app.conf         /etc/nginx/sites-available/app.conf
COPY        .conf-secret/supervisor-app.conf    /etc/supervisor/conf.d/

RUN         ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf

EXPOSE      4040
#CMD         supervisord -n

# docker build -t dayback .