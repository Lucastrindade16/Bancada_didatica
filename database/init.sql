DROP TABLE IF EXISTS 'data';

CREATE TABLE 'data' (
    'data_id' INTEGER PRIMARY KEY /*/ AUTO_INCREMENT */,
    'timestamp' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    'topic' VARCHAR(45),
    'variable' VARCHAR(45),
    'value' VARCHAR(45)
);