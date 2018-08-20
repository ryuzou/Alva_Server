CREATE TABLE `D_Bookdata` (
  `barcode` int primary key,
  `id` int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `book_id` int(10),
  `exist_S` int(1) DEFAULT '0',
  `book_title` varchar(100) DEFAULT 'NOT INPUTED',
  `book_genre` varchar(15) DEFAULT 'NOT INPUTED',
  `book_author` varchar(15) DEFAULT 'NOT INPUTED',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (book_id)
    REFERENCE D_Bookshelf(id) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;