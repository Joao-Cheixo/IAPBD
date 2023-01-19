SET foreign_key_checks = 0;

ALTER TABLE locus modify id_locus INT NOT NULL AUTO_INCREMENT;

ALTER TABLE annotations modify id_annotations INT NOT NULL AUTO_INCREMENT;

ALTER TABLE bacterias modify idbacterias INT NOT NULL AUTO_INCREMENT;

ALTER TABLE features modify id_features INT NOT NULL AUTO_INCREMENT;

ALTER TABLE reference modify id_reference INT NOT NULL AUTO_INCREMENT;

ALTER TABLE sequencia modify id_sequencia INT NOT NULL AUTO_INCREMENT;

select * from bacterias;

select * from features;