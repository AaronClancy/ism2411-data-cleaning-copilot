# This script loads raw sales data, applies cleaning steps to ensure consistency and correctness, and outputs a cleaned up .CSV file.

import pandas as pd

# Load the CSV file into a pandas DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)

# Standardize column names by converting them to lowercase and replacing spaces with underscores
def standardize_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

