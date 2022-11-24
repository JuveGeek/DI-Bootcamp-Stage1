-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;
/*
CREATE DATABASE bootcamp
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_Burkina Faso.1252'
    LC_CTYPE = 'French_Burkina Faso.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE students(
	id SERIAL PRIMARY KEY,
	last_name VARCHAR(30) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	birth_date date NOT NULL
);


INSERT INTO students(first_name, last_name, birth_date)
VALUES ('Marc', 'Benichou', '1998-11-02'),
		('Yoan', 'Cohen', '2010-12-03'),
		('Lea', 'Benichou', '1987-07-27'),
		('Amelia', 'Dux', '1996-07-04'),
		('David', 'Grez', '2003-06-14'),
		('Oumar', 'Simpson', '1980-10-03');

INSERT INTO students(last_name, first_name, birth_date)
VALUES ('Juvénal', 'Pilabre', '2000-10-23');


SELECT * 
FROM students;
*/

SELECT (first_name, last_name) from students;

SELECT (first_name, last_name) from students WHERE students.id=2 ;

SELECT (first_name, last_name) from students WHERE students.last_name='Benichou' AND students.first_name='Marc' ;

SELECT (first_name, last_name) from students WHERE students.last_name='Benichou' OR students.first_name='Marc' ;

SELECT (first_name, last_name) from students WHERE students.first_name LIKE '%a%' ;

SELECT (first_name, last_name) from students WHERE students.first_name LIKE 'a%' ;

SELECT (first_name, last_name) from students WHERE students.first_name LIKE '%a' ;

SELECT (first_name, last_name) from students WHERE students.first_name LIKE '__a%' ;

SELECT (first_name, last_name) from students WHERE students.id = 1 OR students.id = 3  ;

SELECT (id, first_name, last_name, birth_date) from students WHERE students.birth_date >  '2000-01-01'  ;



