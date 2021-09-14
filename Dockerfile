FROM mysql:5.7.15

ENV MYSQL_DATABASE=ludiiGames \
    MYSQL_ROOT_PASSWORD=newpassword

RUN apt-get update && \
    apt-get install -y wget unzip

RUN wget https://ludii.games/downloads/database.zip && \
    unzip database.zip && \
    mv database/* /docker-entrypoint-initdb.d/


# Add file from local
# ADD data/ludiiGames.sql /docker-entrypoint-initdb.d

EXPOSE 3306