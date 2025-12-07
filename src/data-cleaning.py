# This script loads raw sales data, applies cleaning steps to ensure consistency and correctness, and outputs a cleaned up .CSV file.

import pandas as pd

# Load the CSV file into a pandas DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)

# Standardize column names by converting them to lowercase and replacing spaces with underscores
def standardize_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

# Strip leading and trailing whitespace from text columns such as product names and categories
def clean_text_fields(df):
    text_columns = ['product_name', 'category']
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].str.strip()
    return df

# Handle missing values in price and quantity. Rows with missing values in these columns are dropped
def handle_missing_values(df):
    df = df.dropna(subset=['price', 'quantity'])
    return df

# Remove rows with negative price or quantity values
def remove_invalid_rows(df):
    df = df[(df['price'] >= 0) & (df['quantity'] >= 0)]
    return df

def main():
    raw_path = 'data/raw/sales_data.csv'
    cleaned_path = 'data/cleaned/sales_data_cleaned.csv'

    df_raw = load_data(raw_path)
    df_clean = standardize_column_names(df_raw)
    df_clean = clean_text_fields(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print(f"Cleaning complete. First few rows:\n{df_clean.head()}")

if __name__ == "__main__":
    main()