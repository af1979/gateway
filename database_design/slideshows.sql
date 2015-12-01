CREATE TABLE slideshows (
  id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  category ENUM('celebs', 'movies', 'lifestyle', 'tv') NOT NULL,
  title VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL,
  image_url VARCHAR(255) NOT NULL, # This would be used for the background/cover image
  PRIMARY KEY(id)
) ENGINE=INNODB;