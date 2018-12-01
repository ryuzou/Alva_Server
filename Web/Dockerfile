FROM php:7-apache
COPY php.ini /usr/local/etc/php/
RUN apt-get update \
  && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev libmcrypt-dev
#RUN apt-get install -y software-properties-common \
#  && add-apt-repository -y ppa:certbot/certbot \
#  && apt-get update \
#  && apt-get install -y python-certbot-apache
RUN docker-php-ext-install pdo_mysql mysqli mbstring gd iconv

ENV APACHE_DOCUMENT_ROOT=/var/www/html/Alva
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf
