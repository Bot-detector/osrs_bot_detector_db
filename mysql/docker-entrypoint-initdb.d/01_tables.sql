USE playerdata;

-- playerdata.Players definition-- playerdata.Labels definition

CREATE TABLE Labels (
    id int NOT NULL AUTO_INCREMENT,
    label varchar(50) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY Unique_label (label)
);

INSERT INTO `Labels` (id, label) VALUES (0, "UNKOWN");

CREATE TABLE Players (
    id int NOT NULL AUTO_INCREMENT,
    name text NOT NULL,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime DEFAULT NULL,
    possible_ban tinyint(1) NOT NULL DEFAULT '0',
    confirmed_ban tinyint(1) NOT NULL DEFAULT '0',
    confirmed_player tinyint(1) NOT NULL DEFAULT '0',
    label_id int NOT NULL DEFAULT '0',
    label_jagex int NOT NULL DEFAULT '0',
    ironman tinyint DEFAULT NULL,
    hardcore_ironman tinyint DEFAULT NULL,
    ultimate_ironman tinyint DEFAULT NULL,
    normalized_name text,
    PRIMARY KEY (id),
    UNIQUE KEY Unique_name (name (50)),
    KEY FK_label_id (label_id),
    KEY confirmed_ban_idx (confirmed_ban),
    KEY normal_name_index (normalized_name (50)),
    KEY Players_label_jagex_IDX (label_jagex),
    KEY Players_possible_ban_IDX (possible_ban, confirmed_ban),
    CONSTRAINT FK_label_id FOREIGN KEY (label_id) REFERENCES Labels (id) ON DELETE RESTRICT ON UPDATE RESTRICT
);