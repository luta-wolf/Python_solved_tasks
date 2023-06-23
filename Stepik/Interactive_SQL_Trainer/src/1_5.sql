-- task 1
CREATE TABLE supply(
    supply_id SERIAL,
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8,2),
    amount INT
    );

-- task 2
INSERT INTO supply(title, author, price, amount)
VALUES    ('Лирика', 'Пастернак Б.Л.', 518.99, 2),
        ('Черный человек', 'Есенин С.А.', 570.20, 6),
        ('Белая гвардия', 'Булгаков М.А.', 540.50, 7),
        ('Идиот', 'Достоевский Ф.М.', 360.80, 3);

-- task 3
INSERT INTO book (title, author, price, amount)
SELECT title, author, price, amount
FROM supply
WHERE  author NOT IN ('Булгаков М.А.', 'Достоевский Ф.М.');

SELECT title, author, price, amount
FROM book;

-- task 4
INSERT INTO book (title, author, price, amount)
            SELECT title, author, price, amount
            FROM supply
            WHERE author NOT IN (
                SELECT DISTINCT author
                FROM book);

SELECT *
FROM book;

-- task 5
UPDATE book
SET price = price * 0.9
WHERE amount BETWEEN 5 AND 10;

SELECT *
FROM book;

-- task 6
UPDATE book
SET price = IF(buy = 0, price * 0.9, price),
    buy = IF(buy > amount, amount,  buy);

SELECT *
FROM book;

-- task 7
-- 1
UPDATE book, supply
SET book.amount = book.amount + supply.amount,
    book.price = (book.price + supply.price) / 2
WHERE book.author = supply.author AND book.title = supply.title;

SELECT *
FROM book;
-- 2
update book b, supply s
set b.amount = b.amount + s.amount, b.price = (b.price + s.price)/2
where b.title = s.title;

select * from book;

-- task 8
DELETE FROM supply
WHERE author IN (
    SELECT author
    FROM book
    GROUP BY author
    HAVING SUM(amount) > 10
    );

SELECT *
FROM supply;

-- task 9
CREATE TABLE ordering
SELECT author, title, (
    SELECT ROUND(AVG(amount))
    FROM book
    ) AS amount
FROM book
WHERE amount < (
    SELECT ROUND(AVG(amount))
    FROM book
    );

SELECT *
FROM ordering