FROM php:7-apache
COPY php.ini /usr/local/etc/php/
RUN apt-get update \
  && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev libmcrypt-dev
#RUN apt-get install -y software-properties-common \
#  && add-apt-repository -y ppa:certbot/certbot \
#  && apt-get update \
#  && apt-get install -y python-certbot-apache
RUN docker-php-ext-install pdo_mysql mysqli mbstring gd iconv
