import pandas as pd

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print("Error reading file:", e)
        return []
