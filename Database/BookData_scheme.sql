CREATE TABLE `D_Bookdata` (
  `barcode` int primary key,
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `book_id` int(10)
  `exist_S` int(1) DEFAULT '0',
  `book_title` varchar DEFAULT '0',
  `book_genre` varchar DEFAULT '0',
  `book_author` varchar DEFAULT '0',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_book_id
    FOREIGN KEY (book_id)
    REFERENCE D_Bookshelf (id)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;