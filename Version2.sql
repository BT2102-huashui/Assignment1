CREATE DATABASE IF NOT EXISTS version2;
CREATE TABLE IF NOT EXISTS version2.administrator (
	id INT PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    gender ENUM('Female', 'Male') NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    password VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS version2.payment (
	id INT PRIMARY KEY NOT NULL,
    fee_amount DOUBLE(20,2) NOT NULL,
    payment_date DATE NOT NULL,
    create_DATE DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS version2.customer (
	id INT PRIMARY KEY NOT NULL,
    password VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    gender ENUM('Female', 'Male') NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email_address VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS version2.item (
	id INT PRIMARY KEY NOT NULL,
    category ENUM('Lights', 'Locks') NOT NULL,
    model ENUM('Light1', 'Light2', 'SmartHome1', 'Safe1', 'Safe2', 'Safe3') NOT NULL,
    request_status ENUM('Sub', 'Sub and Wait', 'Pro', 'Appr', 'Can', 'Com') NOT NULL,
    service_status ENUM('Waiting', 'Progress', 'Completed') NOT NULL,
    purchase_status ENUM('Yes', 'No') NOT NULL,
    purchase_date DATE NOT NULL,
    customer_id INT NOT NULL,
    admin_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES version2.customer(id),
    FOREIGN KEY (admin_id) REFERENCES version2.administrator(id)
);
CREATE TABLE IF NOT EXISTS version2.request (
	id INT PRIMARY KEY NOT NULL,
    date DATE NOT NULL,
    request_status ENUM('Sub', 'Sub and Wait', 'Pro', 'Appr', 'Can', 'Com'),
    customer_id INT NOT NULL,
    admin_id INT NOT NULL,
    item_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES version2.customer(id),
    FOREIGN KEY (admin_id) REFERENCES version2.administrator(id),
    FOREIGN KEY (item_id) REFERENCES version2.item(id)
);