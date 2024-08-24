import pandas as pd
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Assuming negative values should be set to NaN
    df = df.applymap(lambda x: float('nan') if x < 0 else x)
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)

def process_all_files(data_dir, output_dir):
    files = os.listdir(data_dir)
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(data_dir, file)
            df = load_data(file_path)
            cleaned_df = clean_data(df)
            output_path = os.path.join(output_dir, f"cleaned_{file}")
            save_cleaned_data(cleaned_df, output_path)
