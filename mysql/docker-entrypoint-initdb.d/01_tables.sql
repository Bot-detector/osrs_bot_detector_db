USE playerdata;

CREATE TABLE Players (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    possible_ban BOOLEAN,
    confirmed_ban BOOLEAN,
    confirmed_player BOOLEAN,
    label_id INTEGER,
    label_jagex INTEGER,
    ironman BOOLEAN,
    hardcore_ironman BOOLEAN,
    ultimate_ironman BOOLEAN,
    normalized_name TEXT
);

CREATE TABLE Labels (
    id int NOT NULL AUTO_INCREMENT,
    label varchar(50) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY Unique_label (label) USING BTREE
)
;