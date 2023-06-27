CREATE TABLE fine (
    fine_id SERIAL,
    name VARCHAR(30),
    number_plate VARCHAR(6),
    violation VARCHAR(50),
    sum_fine DECIMAL(8,2),
    date_violation DATE,
    date_payment DATE
    );

CREATE TABLE traffic_violation (
    violation_id SERIAL,
    violation VARCHAR(50),
    sum_fine DECIMAL(8,2)
    );

INSERT INTO fine (name, number_plate, violation, sum_fine, date_violation, date_payment)
VALUES
('Баранов П.Е.',	'Р523ВТ',	'Превышение скорости (от 40 до 60)',	500,	'2020-01-12',	'2020-01-17'),
('Абрамова К.А.',	'О111АВ',	'Проезд на запрещающий сигнал',	1000,	'2020-01-14',	'2020-02-27'),
('Яковлев Г.Р.',	'Т330ТТ',	'Превышение скорости (от 20 до 40)',	500,	'2020-01-23',	'2020-02-23'),
('Яковлев Г.Р.',	'М701АА',	'Превышение скорости (от 20 до 40)',	NULL, 	'2020-01-12',  NULL),
('Колесов С.П.',	'К892АХ',	'Превышение скорости (от 20 до 40)',	 NULL,	'2020-02-01', NULL),
('Баранов П.Е.',	'Р523ВТ',	'Превышение скорости (от 40 до 60)',	NULL ,	'2020-02-14', NULL),
('Абрамова К.А.',	'О111АВ',	'Проезд на запрещающий сигнал',	 NULL,	'2020-02-23', NULL),
('Яковлев Г.Р.',	'Т330ТТ',	'Проезд на запрещающий сигнал',	 NULL,	'2020-03-03', NULL);

INSERT INTO traffic_violation (violation, sum_fine)
VALUES
('Превышение скорости (от 20 до 40)',	500.00),
('Превышение скорости (от 40 до 60)',	1000.00),
('Проезд на запрещающий сигнал',	1000.00);

SELECT * FROM fine;
SELECT * FROM traffic_violation;

-- 3
UPDATE fine AS f, traffic_violation AS tv
SET f.sum_fine =  tv.sum_fine
WHERE f.sum_fine IS NULL AND f.violation = tv.violation;

SELECT *
FROM fine;

-- 4
SELECT name, number_plate, violation
FROM fine
GROUP BY name, number_plate, violation
HAVING COUNT(violation) > 1
ORDER BY name, 2, 3

-- 5
-- 1
UPDATE fine,
    (
    SELECT name, number_plate, violation
    FROM fine
    GROUP BY name, number_plate, violation
    HAVING COUNT(violation) > 1
    ) query_in
SET fine.sum_fine = IF(fine.date_payment IS NULL, fine.sum_fine * 2, fine.sum_fine)
WHERE  fine.name = query_in.name
    AND fine.number_plate = query_in.number_plate
    AND fine.violation = query_in.violation;

SELECT *
FROM fine;

-- 2
UPDATE
    fine f,
    (SELECT name, number_plate, violation
    FROM fine
    GROUP BY name, number_plate, violation
    HAVING COUNT(*) > 1) q_in
SET f.sum_fine = f.sum_fine * 2
WHERE
    (f.name, f.number_plate, f.violation) =
    (q_in.name, q_in.number_plate, q_in.violation) AND
    f.date_payment IS Null;

SELECT * FROM fine;

-- 6
UPDATE fine AS f, payment AS p
SET f.date_payment = p.date_payment,
    f.sum_fine = IF(DATEDIFF(p.date_payment, p.date_violation) < 21, f.sum_fine / 2, f.sum_fine)
WHERE (f.name, f.number_plate, f.violation) = (p.name, p.number_plate, p.violation)
    AND f.date_payment IS NULL;

SELECT name, number_plate, violation, sum_fine, date_violation, date_payment
FROM fine;

-- 7
CREATE TABLE back_payment AS
SELECT name, number_plate, violation, sum_fine, date_violation
FROM fine
WHERE date_payment IS NULL;

SELECT name, number_plate, violation, sum_fine, date_violation
FROM back_payment;

