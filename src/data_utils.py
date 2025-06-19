import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo

def load_and_combine_data(repo_id=19):
    """
    Fetches a dataset from the UCI ML Repository and combines features and targets.
    """
    dataset = fetch_ucirepo(id=repo_id)
    X = dataset.data.features
    y = dataset.data.targets
    combined_data = pd.concat([X, y], axis=1)
    return combined_data

def save_data_to_excel(dataframe, filename="car_evaluation_data.xlsx"):
    """
    Saves a Pandas DataFrame to an Excel file.
    """
    dataframe.to_excel(filename, index=False)
    print(f"Los datos se han guardado en {filename}")

def save_data_to_csv(dataframe, filename="DATA_FORMATEADA.csv", encoding="ISO-8859-1"):
    """
    Saves a Pandas DataFrame to a CSV file with specified encoding.
    """
    dataframe.to_csv(filename, index=False, encoding=encoding)
    print(f"Los datos se han guardado en {filename} con codificación {encoding}.")

def preprocess_data(dataframe):
    """
    Performs preprocessing steps on the car evaluation dataframe:
    - Changes data types of 'doors' and 'persons' to category.
    - Renames categories for 'lug_boot'.
    - Consolidates categories for 'doors'.
    - Renames 'lug_boot' column to 'trunk'.
    """
    df = dataframe.copy()

    # Change data types
    if 'doors' in df.columns:
        df['doors'] = df['doors'].astype('category')
    if 'persons' in df.columns:
        df['persons'] = df['persons'].astype('category')

    # Rename 'lug_boot' categories
    if 'lug_boot' in df.columns:
        df["lug_boot"] = np.where(df["lug_boot"] == "small", "pequeño", df["lug_boot"])
        df["lug_boot"] = np.where(df["lug_boot"] == "med", "mediano", df["lug_boot"])
        df["lug_boot"] = np.where(df["lug_boot"] == "big", "grande", df["lug_boot"])

    # Consolidate 'doors' categories
    if 'doors' in df.columns:
        df["doors"] = np.where(df["doors"] == "2", "3 a menos", df["doors"])
        df["doors"] = np.where(df["doors"] == "3", "3 a menos", df["doors"])
        df["doors"] = np.where(df["doors"] == "4", "4 a más", df["doors"])
        df["doors"] = np.where(df["doors"] == "5more", "4 a más", df["doors"])

    # Rename 'lug_boot' column
    if 'lug_boot' in df.columns:
        df.rename({'lug_boot': 'trunk'}, axis=1, inplace=True)

    return df
