mkdir tempdir


echo "FROM ubuntu" >tempdir/Dockerfile
echo "USER root" >>tempdir/Dockerfile
echo "LABEL author    PeterGythiel" >>tempdir/Dockerfile
echo "RUN apt-get update " >>tempdir/Dockerfile
echo "RUN apt-get -y install  apache2 psmisc " >>tempdir/Dockerfile
echo 'RUN echo "ServerName DevNet_PGY" >> /etc/apache2/apache2.conf' >>tempdir/Dockerfile
echo "RUN apt-get -y install apache2-utils " >>tempdir/Dockerfile
echo "RUN apt clean " >>tempdir/Dockerfile
echo "RUN a2enmod rewrite" >>tempdir/Dockerfile
echo "EXPOSE 8088" >>tempdir/Dockerfile

echo "COPY files/index.html /var/www/html/" >>tempdir/Dockerfile
echo "RUN service apache2 restart" >>tempdir/Dockerfile
#CMD [“apache2ctl”, “-D”, “FOREGROUND”]" >>tempdir/Dockerfile
echo "ENTRYPOINT apache2ctl -D FOREGROUND" >>tempdir/Dockerfile

cd tempdir
docker build -t pgy-jenkin-apache .
docker run -t -d -p 8088:8088 --name "Jenkins-PGY-Apache" pgy-jenkin-apache
docker ps -a