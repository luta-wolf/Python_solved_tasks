-- task 1
SELECT SUM(revenue) / COUNT(DISTINCT user_id) AS arpu
FROM game_events

-- task 2
-- 1
import pandas as pd
arpu = game_events['revenue'].sum()/game_events['user_id'].nunique()
print(arpu)
import pandas as pd
-- 2
arpu = game_events.revenue.sum()/game_events.user_id.nunique()
print(arpu)
