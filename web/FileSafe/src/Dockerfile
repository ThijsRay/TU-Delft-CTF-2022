FROM alpine:3.16

RUN apk --no-cache --update \
    add apache2 \
    apache2-ssl \
    curl \
    php8-apache2 \
    php8-bcmath \
    php8-bz2 \
    php8-calendar \
    php8-common \
    php8-ctype \
    php8-curl \
    php8-dom \
    php8-gd \
    php8-iconv \
    php8-mbstring \
    php8-mysqli \
    php8-mysqlnd \
    php8-openssl \
    php8-pdo_mysql \
    php8-pdo_pgsql \
    php8-pdo_sqlite \
    php8-phar \
    php8-session \
    php8-xml \
    && mkdir /htdocs

EXPOSE 80

ADD httpd.conf /etc/apache2/httpd.conf
ADD php.ini /etc/php8/php.ini
ADD CTF /var/www/CTF

HEALTHCHECK CMD wget -q --no-cache --spider localhost

ENTRYPOINT ["httpd", "-D", "FOREGROUND"]
