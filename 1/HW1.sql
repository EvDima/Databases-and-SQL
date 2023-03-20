SELECT * FROM mobile_phones;

CREATE TABLE mobile_phones (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(45),
    manufacturer VARCHAR(45),
    product_count INT,
    price INT);
    
INSERT INTO mobile_phones (product_name, manufacturer, product_count, price)
VALUES 
('iPhone X','Apple','3','76000'),
('iPhone 8','Apple','2','51000'),
('Galaxy S9','Samsung','2','56000'),
('Galaxy S8','Samsung','1','41000'),
('P20 Pro','Huawei','5','36000');


SELECT product_name, manufacturer, price
FROM mobile_phones
WHERE product_count > 2;


SELECT * FROM mobile_phones
WHERE manufacturer = 'Samsung';

    