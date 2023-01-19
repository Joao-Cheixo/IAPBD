CREATE TABLE IF NOT EXISTS `autor_has_reference` (
 autor_id_autor int(11) NOT NULL,
 reference_id_reference int(11) NOT NULL,
 PRIMARY KEY (autor_id_autor,reference_id_reference),
 KEY fk_autor_has_reference_reference1_idx (reference_id_reference),
 KEY fk_autor_has_reference_autor1_idx (autor_id_autor),
 CONSTRAINT fk_autor_has_reference_autor1 FOREIGN KEY (autor_id_autor) REFERENCES autor (id_autor),
 CONSTRAINT fk_autor_has_reference_reference1 FOREIGN KEY (reference_id_reference) REFERENCES reference (id_reference)
)
ENGINE=InnoDB DEFAULT CHARSET =latin1 COLLATE =latin1_bin;

CREATE TABLE IF NOT EXISTS `bac_feat` (
 features_id_features int(11) NOT NULL,
 bacterias_idbacterias int(11) NOT NULL,
 PRIMARY KEY (features_id_features, bacterias_idbacterias),
 KEY fk_bac_feat_bacterias1_idx (bacterias_idbacterias),
 CONSTRAINT fk_bac_feat_bacterias1 FOREIGN KEY (bacterias_idbacterias) REFERENCES bacterias (idbacterias),
 CONSTRAINT fk_bac_feat_features1 FOREIGN KEY (features_id_features) REFERENCES features (id_features)
)
ENGINE=InnoDB DEFAULT CHARSET =latin1 COLLATE =latin1_bin;

CREATE TABLE IF NOT EXISTS `bac_ref_ann` (
 reference_id_reference int(11) NOT NULL,
 bacterias_idbacterias int(11) NOT NULL,
 annotations_id_annotations int(11) NOT NULL,
 PRIMARY KEY (reference_id_reference, bacterias_idbacterias, annotations_id_annotations),
 KEY fk_bac_ref_ann_bacterias1_idx (bacterias_idbacterias),
 KEY fk_bac_ref_ann_annotations1_idx (annotations_id_annotations),
 CONSTRAINT fk_bac_ref_ann_annotations1 FOREIGN KEY (annotations_id_annotations) REFERENCES annotations (id_annotations),
 CONSTRAINT fk_bac_ref_ann_bacterias1 FOREIGN KEY (bacterias_idbacterias) REFERENCES bacterias (idbacterias),
 CONSTRAINT fk_bac_ref_ann_reference1 FOREIGN KEY (reference_id_reference) REFERENCES reference (id_reference)
)
ENGINE=InnoDB DEFAULT CHARSET =latin1 COLLATE =latin1_bin;



