-- DB schema
CREATE DATABASE Bolt
CHARACTER SET utf8mb4
COLLATE utf8mb4_hungarian_ci;


CREATE TABLE Products (
	ID int,
    Name varchar(255),
	Kcal int,
    Price int,
    Restricted bool
);

CREATE TABLE Employees(
	ID int,
    Name varchar(255),
    Wage int,
    Position varchar(255),
    Password text
);