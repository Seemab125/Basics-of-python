CREATE DATABASE sql3;
USE sql3;

CREATE TABLE students (
              id int,
              stName varchar(255),
              stEmail varchar(255),
              age int,
              gender varchar(255)
              );
SELECT * FROM students;

INSERT INTO students
VALUE (1,'seemab', 'see@gmail.com', 22, 'M');
INSERT INTO students
VALUE (2,'see', 'hanan@gmail.com', 20, 'M');
INSERT INTO students
VALUE (4,'Ali', 'Ali@gmail.com', 22, 'M');
INSERT INTO students
VALUE (5,'Ahmad', 'Ahmad33@gmail.com', 22, 'M');
INSERT INTO students
VALUE (4,'Ali', 'Ali@gmail.com', 22, 'M');
INSERT INTO students
VALUE (5, 'Ghufran', 'Ghufran@gmail.com', 23 , 'M' );
INSERT INTO students
VALUE (7,'A', NULL, 22, 'M');

-- update the students table to set the 'studentName' of the student with 'id' 5 to 'sara'
UPDATE students
SET stName = 'Sara'
where id = '5';

SELECT * FROM students;


-- 2. Increase the 'price' of all items in the 'inventory' table by 10%.

CREATE TABLE inventory (
             id int,
             item varchar(255),
             bill int,
             date varchar(255)
             );
DROP TABLE inventory;
INSERT INTO inventory
VALUES
( 1, 'Apple' , 200, '10:08:2023' ),
( 2, 'Banana' , 100, '11:08:2023' ),
( 3, 'Orange' , 300, '12:08:2023' ),
( 4, 'Mango' , 400, '13:08:2023' ),
( 5, 'Soup' , 50, '10:08:2023' );

SELECT * FROM inventory;

-- now increase price
UPDATE inventory
SET bill = bill * 1.20;


-- 1. Delete all records from the 'products' table where the 'pStatus' is 'Inactive'
CREATE TABLE products (
	id int,
    pName varchar(255) NOT NULL,
    barcode varchar(255) UNIQUE, 
    price int,
    pStatus varchar(255) DEFAULT 'Active'
);

INSERT INTO products 
VALUES (2, 'Fork', 1234, 25, 'Inactive');
INSERT INTO products 
VALUES (2, 'Fork', NULL, 25, 'Active');
INSERT INTO products (id,pName,price)
VALUES (2, 'Bottle', NULL, 20, 'Active');
SELECT * FROM products;

DELETE FROM products WHERE pStatus= 'Inactive';

-- 2. Use the TRUNCATE statement to clear the 'inventory' table
TRUNCATE TABLE inventory;
SELECT * FROM inventory;

-- Where and In Clauses:
-- 1. Retrieve the names of students from the 'students' table whose ages are either 18, 19, or 20.
SELECT * FROM students;
SELECT * FROM students WHERE age >= 18 AND age <=20;

-- 2. Fetch the 'pName' and 'price' of products from the 'products' table where the 'pStatus' is 'Active'.
SELECT pName, price FROM products WHERE pStatus = 'Active';

-- Between Clause:
-- 1. Retrieve the names of students from the 'students' table whose ages are between 25 and 30
SELECT * FROM students WHERE age BETWEEN 25 and 30 ;

-- 2. Get the list of products from the 'inventory' table that have a 'price' between $5 and $15.
SELECT *FROM inventory WHERE bill BETWEEN 50 and 300 ;

-- Is Null and Not Null:
-- 1. Find the emails of students from the 'students' table who haven't provided an email address.
SELECT * FROM students WHERE stEmail IS NULL ;

-- 2. Retrieve the 'pName' of products from the 'products' table that have a null 'barcode'.
SELECT * FROM products WHERE barcode IS NULL ;

-- Unique and Auto_Increment:
-- 1. Design a table named 'orders' with an auto-increment 'order_id' as a primary key.

CREATE TABLE orders (
             order_id int,
             order_name varchar(255),
             order_price int
             );
             
INSERT INTO orders
VALUES (1, 'camera', 2000);
INSERT INTO orders
VALUES (2, 'boat', 3000);
SELECT * FROM orders;
ALTER TABLE orders MODIFY COLUMN order_id int AUTO_INCREMENT;
