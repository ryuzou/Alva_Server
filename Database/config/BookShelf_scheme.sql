CREATE TABLE D_BookShelf (
  `book_id` int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `XGrid_Place` int(10) NOT NULL DEFAULT '0',
  `YGrid_Plave` int(10) NOT NULL DEFAULT '0',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  /* index(book_id) */
) ENGINE=InnoDB;