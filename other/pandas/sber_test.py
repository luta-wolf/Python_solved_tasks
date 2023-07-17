import pandas as pd
data = {
'date': pd.date_range(start='2019-01-01', periods=12,
freq='100D').to_series().sample(frac=1).to_list(),
'customer_id': [101, 102, 103, 101, 102, 104, 105, 103, 101, 102, 106, 107],
'product_id': [1, 2, 3, 2, 3, 1, 2, 1, 3, 3, 1, 2],
'quantity': [3, 1, 2, 1, 3, 2, 2, 3, 1, 2, 1, 3],
'price': [10.5, 15.2, 8.7, 13.4, 9.1, 11.8, 12.5, 7.2, 16.6, 8.9, 10.2, 14.1],
}
df = pd.DataFrame(data)

print(df)
