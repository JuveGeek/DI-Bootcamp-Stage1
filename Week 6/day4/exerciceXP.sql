-- Database: hr.backup

-- DROP DATABASE IF EXISTS "hr.backup";
/*
CREATE DATABASE "hr.backup"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_Burkina Faso.1252'
    LC_CTYPE = 'French_Burkina Faso.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
*/

SELECT first_name AS FirstName, last_name AS LastName
FROM employees;
	
SELECT distinct department_id
FROM employees;

SELECT *
FROM employees 
ORDER BY first_name DESC;
;
	
SELECT first_name FirstName, last_name, salary, (15*salary/100) AS PF
FROM employees;

SELECT employee_id, first_name FirstName, last_name, salary
FROM employees
ORDER BY salary ASC;

SELECT sum(salary) AS total
FROM employees;

SELECT min(salary) AS minimum, max(salary) AS maximum
FROM employees;

SELECT AVG(salary) AS total
FROM employees;

SELECT count(employees) AS nombreEmployees
FROM employees;

SELECT UPPER(first_name) AS Employees_firstname
FROM employees;

SELECT SUBSTRING(first_name,1,3) 
FROM employees;
	
SELECT  (first_name|| ' ' ||last_name) AS Employee
FROM employees;
	
SELECT first_name , last_name, length(first_name)+length(last_name) AS Fullname_length
FROM employees;

SELECT first_name ~ '^[0-9\.]+$'
FROM employees ;
	
SELECT *
FROM employees
LIMIT 10;

SELECT first_name , last_name, salary
FROM employees
WHERE salary BETWEEN 10000 AND 15000;

SELECT first_name , last_name, hire_date
FROM employees
WHERE employees.hire_date > '1987-01-01' AND employees.hire_date < '1987-12-31' ;
	
SELECT first_name
FROM employees
WHERE first_name LIKE '%e%'
AND first_name LIKE '%c%';
	
SELECT last_name, job_title, salary
FROM employees
INNER JOIN jobs
ON employees.job_id = jobs.job_id
WHERE job_title IN ('Shipping Clerks', 'Programmers')
AND salary NOT IN (4500,10000, 15000);	
	
SELECT last_name FROM employees WHERE last_name LIKE '______';

SELECT last_name FROM employees WHERE last_name LIKE '__e%';

SELECT job_title
FROM employees
INNER JOIN jobs
ON employees.job_id = jobs.job_id;
	
SELECT * 
FROM employees 
WHERE last_name IN('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD');	
	
	
	
	
	