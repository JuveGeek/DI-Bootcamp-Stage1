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
FROM customer;

SELECT (first_name, last_name) AS full_name
FROM customer;

SELECT 
	DISTINCT (create_date)
FROM customer;
	
SELECT *
FROM customer
ORDER BY first_name DESC;
	
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT address,phone 
FROM customer
INNER JOIN address
ON customer.address_id=address.address_id;

SELECT *
FROM film
WHERE film_id=15 OR film_id=150;

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Ace Goldfinger';


SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'Ac%';

SELECT *
from film
ORDER BY replacement_cost DESC
LIMIT 10;

SELECT payment_date, amount
FROM payment 
INNER JOIN customer
ON payment.customer_id=customer.customer_id
ORDER by payment.customer_id;

SELECT *
FROM inventory
INNER JOIN film
ON inventory.film_id=film.film_id
WHERE inventory.film_id!=film.film_id;

SELECT *
FROM city
INNER JOIN country
ON country.country_id=city.country_id;

