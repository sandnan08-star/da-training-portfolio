CREATE TABLE products_sandbox AS SELECT * FROM products;

INSERT INTO products_sandbox (product_id, product_name, unit_cost, list_price)
VALUES (99999, 'Test', 5.99, 10.99);

select * from products_sandbox where product_id = 99999;

UPDATE products_sandbox
SET list_price = 11.99
WHERE product_id = 99999;

DELETE FROM products_sandbox
WHERE product_id = 99999;