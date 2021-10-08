CREATE DATABASE IF NOT EXISTS bt2102;
USE bt2102;
CREATE TABLE IF NOT EXISTS administrator (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    gender ENUM('Female', 'Male') NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    password VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS customer (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    password VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    gender ENUM('Female', 'Male') NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email_address VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS item (
	id INT PRIMARY KEY NOT NULL,
    category ENUM('Lights', 'Locks') NOT NULL,
    product_id INT DEFAULT NULL,
    model ENUM('Light1', 'Light2', 'SmartHome1', 'Safe1', 'Safe2', 'Safe3') NOT NULL,
    purchase_status ENUM('Yes', 'No') NOT NULL,
    purchase_date DATE DEFAULT NULL,
    customer_id INT DEFAULT NULL,
    admin_id INT DEFAULT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (admin_id) REFERENCES administrator(id)
);
CREATE TABLE IF NOT EXISTS request (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    request_status ENUM('Sub', 'Sub and Wait', 'Pro', 'Appr', 'Can', 'Com') DEFAULT NULL,
    service_status ENUM('Waiting', 'Progress', 'Completed') NOT NULL DEFAULT 'Waiting',
    customer_id INT NOT NULL,
    admin_id INT NOT NULL,
    item_id INT NOT NULL,
	fee_amount float(20,2) DEFAULT NULL,
    payment_date DATE DEFAULT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (admin_id) REFERENCES administrator(id),
    FOREIGN KEY (item_id) REFERENCES item(id)
);