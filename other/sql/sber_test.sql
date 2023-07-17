CREATE TABLE shop(
    id SERIAL,
    date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(8,2)
);

INSERT INTO shop(date, customer_id, product_id, quantity, price)
VALUES
('2020-05-15', 101, 1, 3, 10.5),
('2019-07-20', 102, 2, 1, 15.2),
('2020-12-01', 103, 3, 2,  8.7),
('2019-01-01', 101, 2, 1, 13.4),
('2019-04-11', 102, 3, 3,  9.1),
('2020-02-05', 104, 1, 2, 11.8),
('2021-06-19', 105, 2, 2, 12.5),
('2022-01-05', 103, 1, 3,  7.2),
('2021-09-27', 101, 3, 1, 16.6),
('2019-10-28', 102, 3, 2,  8.9),
('2020-08-23', 106, 1, 1, 10.2),
('2021-03-11', 107, 2, 3, 14.1);

SELECT * FROM shop
ORDER BY 2, 4;

-- Общая выручка магазина за каждый год:
SELECT EXTRACT(YEAR  FROM  date) AS year, SUM(quantity * price) AS revenue
FROM shop
GROUP BY 1
ORDER BY 1;

-- Количество уникальных клиентов, которые сделали заказы в каждом году.
SELECT EXTRACT(YEAR  FROM  date) AS year, COUNT(DISTINCT  customer_id) AS customer
FROM shop
GROUP BY 1
ORDER BY 1;

-- Общее количество товаров, проданных в каждом году.
SELECT EXTRACT(YEAR  FROM  date) AS year, SUM(quantity) AS goods
FROM shop
GROUP BY 1
ORDER BY 1;

-- Средняя стоимость заказа каждого клиента за каждый год.
SELECT EXTRACT(YEAR  FROM  date) AS year, customer_id, AVG(quantity * price) AS average_order
FROM shop
GROUP BY 1, 2
ORDER BY 1;

-- Общая выручка магазина за каждый месяц.
SELECT EXTRACT(MONTHS  FROM  date) AS month, SUM(quantity * price) AS revenue
FROM shop
GROUP BY 1
ORDER BY 1;

-- Общая выручка магазина за каждый месяц для каждого отдельного продукта.
SELECT EXTRACT(MONTHS  FROM  date) AS month, product_id, SUM(quantity * price) AS revenue
FROM shop
GROUP BY 1, 2
ORDER BY 1;
