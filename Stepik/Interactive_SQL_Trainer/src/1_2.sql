-- task 1
SELECT *
FROM book;

-- task 2
SELECT author, title, price
FROM book;

-- task 3
SELECT title AS Название,
       author AS Автор
FROM book;

-- task 4
SELECT title,
       amount,
       amount * 1.65 AS pack
FROM book;

-- task 5
SELECT title,
       author,
       amount,
       ROUND(price - price * 0.3 , 2) AS new_price
FROM book;

-- task 6
SELECT author,
       title,
       ROUND(IF(author = 'Булгаков М.А.', price * 1.1, IF(author = 'Есенин С.А.', price * 1.05, price)) , 2)
           AS  new_price
FROM book;

-- task 7
SELECT author,
        title,
        price
FROM book
WHERE amount < 10;

-- task 8
SELECT title,
       author,
       price,
       amount
FROM book
WHERE (price < 500 OR price > 600) AND price * amount >= 5000;

-- task 9
SELECT title,
       author
FROM book
WHERE price BETWEEN 540.50 AND 800 AND amount IN (2, 3, 5, 7)

-- task 10
SELECT author,
       title
FROM book
WHERE amount BETWEEN 2 AND 14
ORDER BY author DESC, title;

-- task 11
SELECT title,
       author
FROM book
WHERE title LIKE '_% %_' AND author LIKE '%С.%'
ORDER BY title;

-- task 12
SELECT title,
       author,
       price,
       amount
FROM book
WHERE price > 500 AND author LIKE '%А.%'
GROUP BY 1, 2, 3, 4