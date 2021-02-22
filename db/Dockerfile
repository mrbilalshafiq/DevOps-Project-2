FROM mysql:5.7
ENV MYSQL_DATABASE=db
ENV MYSQL_ROOT_PASSWORD=root
COPY ./Create.sql /docker-entrypoint-initdb.d
