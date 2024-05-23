-- Create unique_id table on server
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id),
    UNIQUE (id)
);
