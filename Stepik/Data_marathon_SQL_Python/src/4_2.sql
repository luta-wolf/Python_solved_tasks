-- task 1
SELECT user_id, SUM(revenue)
FROM game_events
GROUP BY user_id
-- task 2
SELECT user_id, event_date, SUM(revenue)
FROM game_events
GROUP BY user_id, event_date

-- task 3
-- 1
SELECT user_id, event_date, COUNT(event_name)
FROM game_events
GROUP BY user_id, event_date
-- 2
SELECT user_id, event_date, COUNT(event_name)
FROM game_events
GROUP BY 1, 2

-- task 4
SELECT user_id, SUM(revenue)
FROM game_events
WHERE event_date = '2021-01-13'
GROUP BY user_id

-- task 5
SELECT event_date, COUNT(DISTINCT user_id)
FROM game_events
GROUP BY event_date

-- task 6
SELECT user_id, MIN(event_date), MAX(event_date) FROM game_events
GROUP BY user_id

-- task 7
SELECT event_date, event_name, COUNT(event_name)
FROM game_events
GROUP BY event_date, event_name

-- task 8
SELECT event_date, event_name, COUNT(event_name)
FROM game_events
WHERE event_date >= '2021-01-14'
GROUP BY event_date, event_name

-- task 9
SELECT event_date, SUM(revenue) AS total_revenue, COUNT(DISTINCT user_id) AS cnt_users
FROM game_events
WHERE event_date <= '2021-01-15'
GROUP BY 1

-- task 9
SELECT event_date, SUM(revenue)/ COUNT(DISTINCT user_id) AS avg_revenue
FROM  game_events
WHERE event_date <= '2021-01-15'
GROUP BY 1
