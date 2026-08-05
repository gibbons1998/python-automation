import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df.to_csv(output_file, index=False)

    print(f"Cleaned dataset saved to {output_file}")

if __name__ == "__main__":
    clean_csv("data.csv", "clean_data.csv")
