#!/bin/bash
docker build  -t apache-pgy  .
docker container run -d  --name "PGY1" -p 8088:8088 apache-pgy
#docker container run -d  --name "PGY1" -p 80:8088 apache-pgy ##Alternatieve oplossing op lokale poort 80 en 8088 bij Dockers

#usefull commands
#docker ps -a
#docker exec -it cont_ID /bin/bash
#docker stop cont_ID
#docker container prune
