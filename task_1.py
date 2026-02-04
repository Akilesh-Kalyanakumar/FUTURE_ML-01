import pandas as pd



import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linearRegression import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd

df = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\Sample - Superstore.xlsx")

df.head()

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Aggregate daily sales
daily_sales = df.groupby('Order Date')['Sales'].sum().reset_index()

# Sort by date
daily_sales = daily_sales.sort_values('Order Date')

daily_sales.head()

print("VS Code is running Python correctly")


