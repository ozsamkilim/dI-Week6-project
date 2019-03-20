DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS phone_call;

CREATE TABLE user (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL,
	password TEXT NOT NULL
);

CREATE TABLE customer (
	customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	phone VARCHAR(255),
	email VARCHAR(255),
	address1 VARCHAR(255),
	address2 VARCHAR(255),
	postal_code VARCHAR(255),
	city VARCHAR(255),
	country VARCHAR(255),
	added_by VARCHAR(255)


);

-- CREATE TABLE phone_call (
-- ...
-- );





INSERT INTO user (username, password)
	VALUES ('admin', 'password');


INSERT INTO customer (customer_id,first_name,last_name,phone,email,address1,address2,postal_code,city,country,added_by)
	VALUES (1, 'yoss', "boss","098765","yoss@boss.co.uk","tlv","tlvvv","ghdks","tlv","israel","admin");











