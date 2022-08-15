FROM ubuntu 
USER root
LABEL author    PeterGythiel
RUN apt-get update 
RUN apt-get -y install  apache2 psmisc 
RUN echo "ServerName DevNet_PGY" >> /etc/apache2/apache2.conf
RUN apt-get -y install apache2-utils 
RUN apt clean 
RUN a2enmod rewrite
EXPOSE 8088

COPY files/index.html /var/www/html/
RUN service apache2 restart
#CMD [“apache2ctl”, “-D”, “FOREGROUND”]
ENTRYPOINT apache2ctl -D FOREGROUND

