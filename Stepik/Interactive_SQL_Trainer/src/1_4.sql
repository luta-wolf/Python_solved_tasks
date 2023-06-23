-- task 1
SELECT author, title, price
FROM book
WHERE price <= (
        SELECT AVG(price)
        FROM book
        )
ORDER BY price DESC;

-- task 2
SELECT author, title, price
FROM book
WHERE  price - (
    SELECT MIN(price)
    FROM book
    ) <= 150
ORDER BY price;

-- task 3
SELECT author, title, amount
FROM book
WHERE amount IN (
    SELECT amount
    FROM book
    GROUP BY amount
    HAVING COUNT(amount) = 1
    )

-- task 4
SELECT author, title, price
FROM book
WHERE price < ANY (
    SELECT MIN(price) AS price
    FROM book
    GROUP BY author
    )

-- task 5
-- 1
SELECT title, author, amount, (
    SELECT  MAX(amount)
    FROM book
    ) - amount AS Заказ
FROM book
WHERE amount != (
    SELECT MAX(amount)
    FROM book
    )
-- 2
SELECT title, author, amount, (SELECT MAX(amount) FROM book) - amount AS Заказ
FROM book
HAVING Заказ > 0;

-- task 6
-- Вывести название, авторов и цены тех книг,
-- которые больше средей цены всех книг на 20%
SELECT title, author, price
FROM book
WHERE price > (
    SELECT ROUND(AVG(price) + AVG(price) * 0.2, 2)
    FROM book
    )