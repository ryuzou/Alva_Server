FROM mysql:5.7
MAINTAINER docker-db

COPY ./my.cnf /etc/mysql/my.cnf
COPY ./BookShelf_scheme.sql /usr/local/lib/SQL_schfiles/BookShelf_scheme.sql
COPY ./BookData_scheme.sql /usr/local/lib/SQL_schfiles/BookData_scheme.sql
COPY ./DBSet.sh /docker-entrypoint-initdb.d/DBSet.sh
