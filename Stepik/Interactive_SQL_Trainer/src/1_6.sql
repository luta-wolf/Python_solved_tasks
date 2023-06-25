-- Создание таблицы
CREATE TABLE trip(
    trip_id SERIAL,
    name VARCHAR(30),
    city VARCHAR(25),
    per_diem DECIMAL(8,2),
    date_first DATE,
    date_last DATE
    );

INSERT INTO trip(name, city, per_diem, date_first, date_last)
VALUES
('Баранов П.Е.', 'Москва', '700', '2020-01-12', '2020-01-17'),
('Абрамова К.А.', 'Владивосток', '450', '2020-01-14', '2020-01-27'),
('Семенов И.В.', 'Москва', '700', '2020-01-23', '2020-01-31'),
('Ильиных Г.Р.', 'Владивосток', '450', '2020-01-12', '2020-02-02'),
('Колесов С.П.', 'Москва', '700', '2020-02-01', '2020-02-06'),
('Баранов П.Е.', 'Москва', '700', '2020-02-14', '2020-02-22'),
('Абрамова К.А.', 'Москва', '700', '2020-02-23', '2020-03-01'),
('Лебедев Т.К.', 'Москва', '700', '2020-03-03', '2020-03-06'),
('Колесов С.П.', 'Новосибирск', '450', '2020-02-27', '2020-03-12'),
('Семенов И.В.', 'Санкт-Петербург', '700', '2020-03-29', '2020-04-05'),
('Абрамова К.А.', 'Москва', '700', '2020-04-06', '2020-04-14'),
('Баранов П.Е.', 'Новосибирск', '450', '2020-04-18', '2020-05-04'),
('Лебедев Т.К.', 'Томск', '450', '2020-05-20', '2020-05-31'),
('Семенов И.В.', 'Санкт-Петербург', '700', '2020-06-01', '2020-06-03'),
('Абрамова К.А.', 'Санкт-Петербург', '700', '2020-05-28', '2020-06-04'),
('Федорова А.Ю.', 'Новосибирск', '450', '2020-05-25', '2020-06-04'),
('Колесов С.П.', 'Новосибирск', '450', '2020-06-03', '2020-06-12'),
('Федорова А.Ю.', 'Томск', '450', '2020-06-20', '2020-06-26'),
('Абрамова К.А.', 'Владивосток', '450', '2020-07-02', '2020-07-13'),
('Баранов П.Е.', 'Воронеж', '450', '2020-07-19', '2020-07-25');

SELECT * FROM trip;

-- task 1
SELECT name, city, per_diem, date_first, date_last
FROM trip
WHERE name LIKE '%а %'
ORDER BY date_last DESC;

-- task 2
SELECT DISTINCT name
FROM trip
WHERE city = 'Москва'
ORDER BY name;

-- task 3
SELECT city, COUNT(city) AS Количество
FROM trip
GROUP BY city
ORDER BY city;

-- task 4
SELECT city, COUNT(city) AS Количество
FROM trip
GROUP BY city
ORDER BY 2 DESC
LIMIT 2;

-- task 5
SELECT name, city, DATEDIFF(date_last, date_first) + 1 AS Длительность
FROM trip
WHERE city NOT IN ('Москва', 'Санкт-Петербург')
ORDER BY 3 DESC;

-- task 6
SELECT name, city, date_first, date_last
FROM trip
WHERE (
    SELECT MIN(DATEDIFF(date_last, date_first))
    FROM trip
    ) = DATEDIFF(date_last, date_first)

-- task 7
SELECT name, city, date_first, date_last
FROM trip
WHERE MONTH(date_first) = MONTH(date_last)
ORDER BY city, name

-- task 8
SELECT MONTHNAME(date_first) AS Месяц, COUNT(DATEDIFF(date_last, date_first)) AS Количество
FROM trip
GROUP BY MONTHNAME(date_first)
ORDER BY 2 DESC, 1

-- task 9
-- 1
SELECT name, city, date_first, (DATEDIFF(date_last, date_first)  + 1) * per_diem  AS Сумма
FROM trip
WHERE MONTHNAME(date_first) IN ('February', 'March')
ORDER BY name, Сумма DESC

-- 2
select name, city, date_first, per_diem*(datediff(date_last,date_first)+1) as Сумма from trip
where MONTH(date_first) in (2,3) and YEAR(date_first) = 2020
order by name, Сумма desc;

-- task 10
-- WHERE для доп.условия выборки строк,
-- HAVING - доп. условие для выборки в колонках.
-- 1
SELECT name, SUM((DATEDIFF(date_last, date_first) + 1) * per_diem) AS Сумма
FROM trip
WHERE name IN (
    SELECT name
    FROM trip
    GROUP BY name
    HAVING COUNT(name) > 3)
GROUP BY 1
ORDER BY 2 DESC;
-- 2
SELECT name, SUM((DATEDIFF(date_last,date_first) + 1) * per_diem) AS Сумма
FROM trip
GROUP BY name
HAVING COUNT(name) > 3
ORDER BY 2 DESC;