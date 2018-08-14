if ! mysql -u root -ppassword -e "use Alva_Server"; then
  mysql -u root -ppassword -e "create database Alva_Server"
  mysql -u root -ppassword Alva_Server <  /usr/local/lib/SQL_schfiles/BookShelf_scheme.sql
  mysql -u root -ppassword Alva_Server <  /usr/local/lib/SQL_schfiles/BookData_scheme.sql
fi