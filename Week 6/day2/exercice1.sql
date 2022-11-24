-- Database: public

-- DROP DATABASE IF EXISTS public;
/*
CREATE DATABASE public
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_Burkina Faso.1252'
    LC_CTYPE = 'French_Burkina Faso.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;*/
	
	SELECT type_item, price_item 
	FROM items 
	ORDER BY price_item ASC;
	
	SELECT * 
	FROM items 
	WHERE price_item >= 80
	ORDER BY price_item DESC;
	
	SELECT nom_customer, prenom_customer
	FROM customers
	ORDER BY prenom_customer ASC
	LIMIT 3;
	
	SELECT nom_customer
	FROM customers
	ORDER BY nom_customer DESC
	
	
	
	
	