# Import necessary libraries
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os

# Function to load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to preprocess the dataset
def preprocess_data(df):
    # Separate target column (if exists)
    if 'target' in df.columns:
        X = df.drop('target', axis=1)  # Features
        y = df['target']               # Target/label
    else:
        X = df
        y = None

    # Identify numeric and categorical features
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = X.select_dtypes(include=['object']).columns.tolist()

    # Pipeline for numeric data: fill missing values + scale
    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),  # Fill missing numeric values with mean
        ('scaler', StandardScaler())                  # Scale numeric features to standard normal distribution
    ])

    # Pipeline for categorical data: fill missing values + one-hot encode
    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Fill missing categorical values with the most frequent
        ('encoder', OneHotEncoder(handle_unknown='ignore'))    # Encode categories as binary variables
    ])

    # Combine numeric and categorical pipelines
    preprocessor = ColumnTransformer([
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

    # Apply transformations
    X_processed = preprocessor.fit_transform(X)

    return X_processed, y

# Function to save processed data to CSV
def save_transformed_data(X_processed, output_path):
    # If the result is a sparse matrix (from OneHotEncoder), convert to dense
    output_df = pd.DataFrame(
        X_processed.toarray() if hasattr(X_processed, 'toarray') else X_processed
    )
    
    # Save to CSV
    output_df.to_csv(output_path, index=False)
    print(f"✅ Transformed data saved to: {output_path}")

# Main function to run the ETL pipeline
def main():
    input_file = "raw_data.csv"          # Input file name
    output_file = "processed_data.csv"   # Output file name

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Input file '{input_file}' not found.")
        return

    print("🔄 Running data pipeline...")

    # Load and process the data
    df = load_data(input_file)
    X_processed, _ = preprocess_data(df)
    
    # Save the output
    save_transformed_data(X_processed, output_file)

    print("✅ Data pipeline completed.")

# Run main if executed as script
if __name__ == "__main__":
    main()
