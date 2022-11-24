-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;
/*
CREATE DATABASE dvdrental
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_Burkina Faso.1252'
    LC_CTYPE = 'French_Burkina Faso.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	*/
	
SELECT * 
FROM language
LEFT OUTER JOIN film
ON language.language_id=film.language_id;

SELECT film, description, title, name
FROM language
RIGHT OUTER JOIN film
ON language.language_id=film.language_id; 

SELECT film, description, title, name
FROM language
LEFT OUTER JOIN film
ON language.language_id=film.language_id; 
/*
CREATE TABLE new_film(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);
*/
INSERT INTO new_film(name)
VALUES
	('Avatar'),
    ('Avenger');
/*
CREATE TABLE customer_review(
	review_id SERIAL PRIMARY KEY NOT NULL,
	film_id INTEGER,
	language_id INTEGER,
	title VARCHAR(20),
	score INTEGER,
	review_text VARCHAR(30),
	last_update date,
	FOREIGN KEY(film_id) REFERENCES film(film_id) ,
	FOREIGN KEY(language_id) REFERENCES language(language_id)
);


INSERT INTO customer_review(film_id , language_id, title , score ,review_text , last_update)
VALUES (1,1, 'Alice aux pays',4, 'nothing much', '2030-10-10' )

INSERT INTO customer_review(film_id , language_id, title , score ,review_text , last_update)
VALUES (7,6, 'SIMba',4, 'nothing much', '2030-10-10' )
*/



