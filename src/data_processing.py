import pandas as pd

def load_crime_data(file_path: str) -> pd.DataFrame:
    """Load and clean crime statistics CSV."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
    return df

def load_unemployment_data(file_path: str) -> pd.DataFrame:
    """Load and clean unemployment CSV."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def load_loadshedding_data(file_path: str) -> pd.DataFrame:
    """Load and clean load-shedding CSV."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df

def merge_datasets(crime_df, unemployment_df, load_df):
    """Merge datasets on province/year for combined analysis."""
    merged = pd.merge(crime_df, unemployment_df, on=['province', 'year'], how='outer')
    return merged
