import pandas as pd
import string
import random

# Number of rows
num_rows = 100

# Create column names A to Z
columns = list(string.ascii_uppercase)

# Generate random integer data
data = {
    col: [random.randint(1, 100) for _ in range(num_rows)]
    for col in columns
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("sample_data.csv", index=False)

print(df.head())