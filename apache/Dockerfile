FROM debian:buster-slim

RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi-py3 \
    python3 python3-pip && apt-get clean

RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

COPY apache2.conf /etc/apache2/
COPY sites-available /etc/apache2/sites-available

RUN a2enmod headers

CMD  /usr/sbin/apache2ctl -D FOREGROUND
