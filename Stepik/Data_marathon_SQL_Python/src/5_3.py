# task 1
import pandas as pd
my_df = df
print(my_df)

# task 2
import pandas as pd
df_column_type = df['type']
print(df_column_type)

# task 3
import pandas as pd
column_name = 'user_id'
game_events_users = game_events[column_name]
print(game_events_users)

# task 4
import pandas as pd
game_events_unique_users = game_events['user_id'].unique()
print(game_events_unique_users)

# task 5
import pandas as pd
game_events_unique_users = game_events['user_id'].nunique()
print(game_events_unique_users)

# task 6
import pandas as pd
my_game_events = game_events[game_events['event_name'] == 'app_first_launch']
print(my_game_events)

# task 7
import pandas as pd
my_game_events = game_events[game_events['user_id'] == 'f5ef9841']
print(my_game_events)

# task 8
import pandas as pd
my_game_events = game_events[game_events['event_date'] > '2021-01-14']
print(my_game_events)

# task 9
import pandas as pd
my_game_events = game_events[game_events['revenue'] >= 7.49]
print(my_game_events)
