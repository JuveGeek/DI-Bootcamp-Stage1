-- Database: public

-- DROP DATABASE IF EXISTS public;

CREATE DATABASE public
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_Burkina Faso.1252'
    LC_CTYPE = 'French_Burkina Faso.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	

ALTER TABLE items
ADD	id_item SERIAL PRIMARY KEY,
ADD	type_item VARCHAR(30) NOT NULL,
ADD	price_item INTEGER NOT NULL;


ALTER TABLE customers
ADD id_customer SERIAL PRIMARY KEY,
ADD nom_customer VARCHAR(30) NOT NULL,
ADD prenom_customer VARCHAR(30) NOT NULL;


INSERT INTO items(type_item, price_item) 
VALUES ('Small Desk',100),
	   ('Large Desk',300),
	   ('Fan',80);
	   
INSERT INTO customers(nom_customer, prenom_customer) 
VALUES ('Greg', 'Jones'),
	   ('Sandra', 'Jones'),
	   ('Scott', 'Scott'),
	   ('Trevor', 'Green'),
	   ('Melanie', 'Johnson');



SELECT * 
FROM items;

SELECT * 
FROM items
WHERE items.price_item > 80;

SELECT * 
FROM items
WHERE items.price_item < 300;



SELECT * 
FROM customers
WHERE customers.nom_customer = 'Smith' ;

SELECT * 
FROM customers
WHERE customers.nom_customer = 'Jones' ;

SELECT * 
FROM customers
WHERE customers.nom_customer != 'Scott' ;






