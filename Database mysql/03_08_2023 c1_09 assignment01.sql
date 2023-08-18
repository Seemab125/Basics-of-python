-- TASKT 1 : Create data base with yourname_rollno.
CREATE DATABASE seemab_c109 ;

USE seemab_c109;
-- TASK 2: Create table with any name

CREATE TABLE gculahore (
                         serialno int,
						DepartmentName varchar (255),
                        StudentsStrength int , 
						Faculty int,
						HODname varchar(255)
				     );
-- TASK 3
INSERT INTO gculahore VALUES ("1","ElectricalEngg", "100", "10", "Danish");
INSERT INTO gculahore VALUES ("2","MEchanicalEngg", "70", "8", "Ali");
INSERT INTO gculahore VALUES ("3","ComputerEngg", "150", "20", "Ghufran");
SELECT * from gculahore ;

CREATE TABLE PunjabUniHostels (
                        numbers int,  
                        DepartmentName varchar(255),
                        HostelNumber int,
                        Rooms int,
                        SuperintendName varchar(255)
                        );
INSERT INTO PunjabUniHostels VALUES ("1","ElectricalEngg", "1", "30", "Ghufran");
INSERT INTO PunjabUniHostels VALUES ("2","EMEchanicallEngg", "2", "25", "umar");
INSERT INTO PunjabUniHostels VALUES ("3","ComputerEngg", "3", "20", "waheed");
SELECT * from PunjabUniHostels ;

-- Task 4:  Write the SQL code to empty the data table.
TRUNCATE gculahore;
SELECT * from gculahore;

TRUNCATE punjabUniHostels;
SELECT * from punjabUniHostels;

-- Task 5:  Write the SQL code to delete the data table.
DROP TABLE gculahore ;
DROP TABLE punjabUniHostels ;

-- Task 6:  Write the SQL code to delete database.

DROP DATABASE seemab_c109;

