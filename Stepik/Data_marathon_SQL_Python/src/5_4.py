# task 1
import pandas as pd
sum_revenue = game_events['revenue'].sum()
print(sum_revenue)

# task 2
import pandas as pd
max_date = game_events['event_date'].max()
min_date = game_events['event_date'].min()
print(max_date, min_date)

# task 3
import pandas as pd
mean_revenue = game_events['revenue'].mean()
median_revenue = game_events['revenue'].median()
print(mean_revenue, median_revenue)

# task 4
# 1
import pandas as pd
# все строки где user_id == 'f5ef9841
user_events = game_events[game_events['user_id'] == 'f5ef9841']
# все значения из столбца 'event_name'
user_events_names = user_events['event_name']
# количество значений из столбца 'event_name'
user_events_names_count = user_events_names.count()
print(user_events_names_count)

# 2
import pandas as pd
count_events = game_events[game_events['user_id'] == 'f5ef9841']['event_name'].count()
print(count_events)

# task 5
import pandas as pd
count_events = game_events[game_events['event_date'] == '2021-01-15']['event_name'].count()
print(count_events)
