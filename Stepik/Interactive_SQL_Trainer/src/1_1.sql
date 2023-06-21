--task 1 /* Создаем таблицу*/
-- MySQL
-- CREATE TABLE book (
--     book_id INT PRIMARY KEY AUTO_INCREMENT,
--     title VARCHAR(50),
--     author VARCHAR(30),
--     price DECIMAL(8, 2),
--     amount INT
-- )
-- PostgerSQL 1
CREATE TABLE book (
    book_id SERIAL,
    title VARCHAR(50),
    author VARCHAR(30),
    price DECIMAL(8, 2),
    amount INT
);
-- PostgerSQL 2
-- CREATE TABLE book (
--     book_id INT PRIMARY KEY,
--     title VARCHAR(50),
--     author VARCHAR(30),
--     price DECIMAL(8, 2),     -- DECIMAL(8,2) 8 знаков до ,  2 знака после  + и - и (,) не учитываются
--     amount INT
-- );

--task 2 Вставка записи в таблицу
INSERT INTO book (title, author, price, amount)
VALUES  ('Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3);

--task 2 Вставка записи в таблицу
INSERT INTO book (title, author, price, amount)
VALUES  ('Белая гвардия', 'Булгаков М.А.',540.50 ,5),
        ('Идиот', 'Достоевский Ф.М.', 460.00, 10),
        ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2);