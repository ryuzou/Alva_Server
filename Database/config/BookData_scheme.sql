CREATE TABLE D_Bookdata (
  `barcode` int ,
  `id` int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `book_id` int(10) UNIQUE KEY,
  `exist_S` int(1) DEFAULT '0',
  `book_title` varchar(1000) DEFAULT 'NOT INPUTED',
  `book_genre` varchar(1000) DEFAULT 'NOT INPUTED',
  `book_author` varchar(1000) DEFAULT 'NOT INPUTED',
  `bookimage_path` varchar(1000) DEFAULT 'NULL',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  /* FOREIGN KEY (book_id) REFERENCES D_Bookshelf(book_id) ON DELETE CASCADE ON UPDATE CASCADE */
) ENGINE=InnoDB;