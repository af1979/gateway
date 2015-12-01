CREATE TABLE slides (
  id int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  slideshow_id int(11) NOT NULL,
  title VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  PRIMARY KEY(id),
  CONSTRAINT(fk_slides_slideshows_id) FOREIGN KEY(slideshow_id)
      REFERENCES slideshows(id)
      ON DELETE CASCADE
) ENGINE=INNODB;