CREATE DATABASE Practice;
USE Practice;

--Create table Vehicle
CREATE TABLE Vehicle(
	VehicleID INT,
	make VARCHAR(50),
	model VARCHAR(50),
	year INT,
	dailyRate DECIMAL(10, 2),
	Status BIT,
	passengerCapacity INT,
	engineCapacity INT
	PRIMARY KEY(VehicleID),
);

--Inserting values to Vehicle
INSERT INTO Vehicle(vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
VALUES
(1, 'Toyota', 'Camry', 2002, 50.00, 1, 4, 1450),
(2, 'Honda', 'Civic', 2023, 45.00 , 1, 7, 1500),
(3, 'Ford', 'Focus', 2022, 48.00, 0, 4, 1400),
(4, 'Nissan', 'Altima', 2023, 52.00, 7, 7, 1200),
(5, 'Chevrolet', 'Malibu', 2022, 47.00, 1, 4, 1800),
(6, 'Hyundai', 'Sonata', 2023, 49.00, 0, 7, 1400),
(7, 'BMW', '3 Series', 2023, 60.00, 1, 7, 2499),
(8, 'Mercedes', 'C-Class', 2022, 58.00, 1, 8, 2599),
(9, 'Audi', 'A4', 2022, 55.00, 0, 4, 2500),
(10, 'Lexus', 'ES', 2023, 54.00, 1, 4, 2500);

select * from Vehicle;

--Create table Customer
CREATE TABLE Customer(
	customerID INT,
	firstName VARCHAR(50),
	lastName VARCHAR(50),
	email VARCHAR(100),
	phoneNumber VARCHAR(30),
	PRIMARY KEY(customerID)
);

--Inserting values to Customer
INSERT INTO Customer(customerID, firstName, lastName, email, phoneNumber)
VALUES
(1, 'John', 'Doe', 'johndoe@example.com', '555-555-5555'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '555-123-4567'),
(3, 'Robert', 'Johnson', 'robert@example.com', '555-789-1234'),
(4, 'Sarah', 'Brown', 'sarah@example.com', '555-456-7890'),
(5, 'David', 'Lee', 'david@example.com', '555-987-6543'),
(6, 'Laura', 'Hall', 'laura@example.com', '555-234-5678'),
(7, 'Michael', 'Davis', 'michael@example.com', '555-876-5432'),
(8, 'Emma', 'Wilson', 'emma@example.com', '555-432-1098'),
(9, 'William', 'Taylor', 'william@example.com', '555-321-6547'),
(10, 'Olivia', 'Adams', 'olivia@example.com', '555-765-4321');

select * from customer;

--Create table Lease
CREATE TABLE Lease(
	leaseID INT,
	vehicleID INT,
	customerID INT,
	startDate DATE,
	endDate DATE,
	Type VARCHAR(20)
	PRIMARY KEY(leaseID)
	FOREIGN KEY (vehicleID) References Vehicle(VehicleID),
	FOREIGN KEY (CustomerID) References Customer(CustomerID)
);

--Inserting values to Lease
INSERT INTO Lease(leaseID, vehicleID, customerID, startDate, endDate, type)
VALUES
(1, 1, 1, '2023-01-01', '2023-01-05', 'Daily'),
(2, 2, 2, '2023-02-15', '2023-02-28', 'Monthly'),
(3, 3, 3, '2023-03-10', '2023-03-15', 'Daily'),
(4, 4, 4, '2023-04-20', '2023-04-30' , 'Monthly'),
(5, 5, 5, '2023-05-05', '2023-05-10', 'Daily'),
(6, 4, 3, '2023-06-15', '2023-06-30', 'Monthly'),
(7, 7, 7, '2023-07-01', '2023-07-10', 'Daily'),
(8, 8, 8, '2023-08-12', '2023-08-15', 'Monthly'),
(9, 3, 3, '2023-09-07', '2023-09-10', 'Daily'),
(10, 10, 10, '2023-10-10', '2023-10-31', 'Monthly');

select * from lease;

--Create table Payment
CREATE TABLE Payment(
	paymentID INT,
	leaseID INT,
	paymentDate DATE,
	amount DECIMAL(10, 2),
	PRIMARY KEY(paymentID),
	FOREIGN KEY (leaseID) References Lease(leaseID)
);

--Inserting values to Payment
INSERT INTO Payment(paymentID, leaseID, paymentDate, amount)
VALUES
(1, 1, '2023-01-03', 200.00),
(2, 2, '2023-02-20', 1000.00),
(3, 3, '2023-03-12', 75.00),
(4, 4, '2023-04-25', 900.00),
(5, 5, '2023-05-07', 60.00),
(6, 6, '2023-06-18', 1200.00),
(7, 7, '2023-07-03', 40.00),
(8, 8, '2023-08-14', 1100.00),
(9, 9, '2023-09-09', 80.00),
(10, 10, '2023-10-25', 1500.00);

select * from Payment;