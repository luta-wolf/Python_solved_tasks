-- task 1
SELECT *
FROM book;

-- task 2
SELECT author, title, price
FROM book;

-- task 3
SELECT title AS Название, author AS Автор
FROM book;

-- task 4
SELECT title, amount, amount * 1.65 AS pack
FROM book;

-- task 5
SELECT title, author, amount, ROUND(price - price * 0.3 , 2) AS new_price
FROM book;

-- task 6
SELECT author, title,
       ROUND(IF(author = 'Булгаков М.А.', price * 1.1, IF(author = 'Есенин С.А.', price * 1.05, price)) , 2)
           AS  new_price
FROM book;

