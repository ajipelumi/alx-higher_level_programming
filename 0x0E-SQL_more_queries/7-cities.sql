-- This script creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on our MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	PRIMARY KEY (id),
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states (id)
);
