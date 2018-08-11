if ! mysql -u root -ppassword -e 'Alva_Server'; then
  mysql -u root -ppassword Alva_Server <  BookShelf_scheme.sql
  mysql -u root -ppassword Alva_Server <  BookData_scheme.sql
fi