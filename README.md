# DATA-PIPELINE-DEVELOPMENT (INTERNSHIP(TASK-1))

**COMPANY**  : CODTECH IT SOLUTIONS
**NAME**     : POLASANI PURUSHOTHAM REDDY
**INTERN ID**: CT08DN1100
**DOMAIN**   : DATA SCIENCE
**DURATION** : 8 WEEEKS
**MENTOR**   : NEELA SANTOSH



# DESCRIPTION:
  Data Pipeline Project - Internship Task

  This project implements a **Data Pipeline** for **Extract, Transform, Load (ETL)** operations using Python, Pandas, and Scikit-learn libraries. It is designed to   automate the process of loading raw data, preprocessing it by handling missing values, scaling numeric features, encoding categorical variables, and finally        saving the transformed data for further use such as model training or analysis.

The project is structured to be easily extendable and reusable for various datasets with similar preprocessing needs. This pipeline is a crucial step in any data science or machine learning workflow, ensuring data quality and consistency.

## Features

  - **Data Loading**: Reads raw CSV data from a file.
  - **Data Preprocessing**:
      - Imputation of missing values for numeric and categorical data.
      - Scaling numeric data to standardize feature ranges.
      - One-hot encoding of categorical features to convert them into numeric format.
  - **Data Saving**: Saves the processed data into a new CSV file.
  - **Error Handling**: Checks if the input file exists and informs the user if it does not.
  - **Modular Design**: Functions are modular to allow easy extension or replacement.
  


## Project Structure:

  ├── data_pipeline.py # Python script containing the ETL pipeline code
  ├── raw_data.csv # Sample input dataset with missing values and categorical data
  ├── processed_data.csv # Output dataset after preprocessing (generated after running)
  └── README.md # Project documentation (this file)

## Dependencies:
  pandas: For data manipulation and CSV reading/writing.

  scikit-learn: For data preprocessing utilities like imputation, scaling, encoding, and pipeline management. 

## Code Explanation:
  **load_data(file_path)**: Reads the CSV file into a Pandas DataFrame.
  **preprocess_data(df)**:
    Separates the features (X) and target (y) columns.
    Identifies numeric and categorical columns.
  **creates separate pipelines for numeric and categorical data**:
    Numeric pipeline fills missing values with the mean and scales features.
    Categorical pipeline fills missing values with the most frequent value and one-hot encodes categories.
    Combines pipelines using ColumnTransformer to process all features simultaneously.

  **save_transformed_data(X_processed, output_path)**: Converts the transformed data to a DataFrame and saves it as a CSV.

  **main() function**: Orchestrates loading, preprocessing, and saving the data while checking for input file existence.

✅, 🔄, ❌ - Symbols can be copied from Emojipedia,Get Emoji  websites


# Usage Instructions:
  **Prepare the Input Data**:
    The input file raw_data.csv should contain your raw dataset with columns including both numeric and categorical features. The file must be placed in the        
    project root directory.

**Run the Data Pipeline Script**:
   python data_pipeline.py
   
**Output**:

  After running, a new file processed_data.csv will be generated. This file contains the preprocessed data where missing values are imputed, numeric features are     scaled, and categorical variables are one-hot encoded. This file is ready for further machine learning tasks or analysis.



# OUTPUT:

![Image](https://github.com/user-attachments/assets/5232f591-1560-426a-be91-43d2d5b5cbd3)


