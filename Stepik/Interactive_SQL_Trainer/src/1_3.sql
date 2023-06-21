-- task 1
-- 1
SELECT DISTINCT amount
FROM book;
-- 12
SELECT amount
FROM book
GROUP BY amount;

-- task 2
SELECT author AS Автор,
       COUNT(amount) AS Различных_книг,
       SUM(amount) AS Количество_экземпляров
FROM book
GROUP BY author;

-- task 3
SELECT author,
       MIN(price) AS Минимальная_цена,
       MAX(price) AS Максимальная_цена,
       AVG(price) AS Средняя_цена
FROM book
GROUP BY author;

-- task 4
SELECT author,
       SUM(price * amount) AS Стоимость,
       ROUND((SUM(price * amount) * 18 / 100) / (1 + 18 / 100) ,2) AS НДС,
       ROUND(SUM(price * amount) / (1 + 18 / 100) ,2) AS Стоимость_без_НДС
FROM book
GROUP BY author;

-- task 5
SELECT MIN(price) AS Минимальная_цена,
        MAX(price) AS Максимальная_цена,
        ROUND(AVG(price), 2) AS Средняя_цена
FROM book;

-- task 6
SELECT ROUND(AVG(price), 2) AS Средняя_цена,
       SUM(price * amount) AS Стоимость
FROM book
WHERE amount BETWEEN 5 AND 14;

-- task 7
--1
SELECT author,
       SUM(price * amount) AS Стоимость
FROM book
WHERE title <> 'Идиот' AND title <> 'Белая гвардия'
GROUP BY author
HAVING SUM(price * amount) > 5000
ORDER BY Стоимость DESC;
--2
SELECT author, SUM(price * amount) AS Стоимость FROM book
WHERE title NOT IN ('Идиот', 'Белая Гвардия')
GROUP BY author
HAVING SUM(price * amount) > 5000
ORDER BY Стоимость DESC;

-- task 8
SELECT author, COUNT(title)
FROM book
WHERE amount > 5
GROUP BY author