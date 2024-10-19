CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    reorder_level INT DEFAULT 10
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES inventory(id),
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity_sold INT NOT NULL
);
