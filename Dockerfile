FROM mysql:5.7.15


ENV MYSQL_DATABASE=test-ludeme \
    MYSQL_ROOT_PASSWORD=newpassword

# add file
ADD data/ludiiGames.sql /docker-entrypoint-initdb.d

EXPOSE 3306