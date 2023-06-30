# DataGuru

## Library Overview

The **DataGuru** library is designed to provide various data analysis and preprocessing functionalities to simplify common tasks in data science projects. It includes primary functions such as `missingValues`, `findOutliers`, and `analyzeData`. Let's analyze each of these functions in detail:

### `missingValues(data)`

This function computes the missing values statistics for each column in the input data. It generates a DataFrame containing information such as the variable name, total values, total missing values, missing value rate, data type, unique values, and total unique values. The missing data DataFrame is sorted in descending order based on the total number of missing values.

### `findOutliers(data, method='zscore')`

This function detects outliers in numeric columns of the input data. It supports two outlier detection methods: Z-score and IQR (interquartile range). By default, the Z-score method is used. The function iterates over each numeric column and applies the specified outlier detection method. It then collects information about the column, including the mean, standard deviation, outliers, total outliers, and percentage of outliers. The resulting DataFrame is sorted in descending order based on the percentage of outliers.

### `analyzeData(data, numCol, catCol)`

This function performs an analysis on the input data by grouping a numeric column (numCol) based on a categorical column (catCol). It calculates the mean, standard deviation, and percentage of the numeric column for each category. The results are displayed in a DataFrame sorted in descending order based on the mean value. Additionally, a bar plot is generated using Plotly Express, visualizing the mean, standard deviation, and percentage for each category.

## Installation

The latest stable release (and required dependencies) can be installed from PyPI:

`pip install DataGuru`

## Future Enhancements

Planned enhancements for the library, including segregation features in `analyzeData` similar to the "hue" parameter in seaborn, model comparison for regression, classification, and clustering, and data preprocessing capabilities. These additions will provide more flexibility and functionality to the library, enabling users to perform advanced analyses and streamline their data science workflows.

By incorporating these features, the **DataGuru** library aims to simplify common data analysis tasks, automate repetitive code, and enhance the productivity of data science students and practitioners.

## Change Log

### 0.0.1 (12/06/2023)
- First Release
- Features:
  - missingValues
  - findOutliers
  - analyzeData
    
### 0.0.2 (29/06/2023)
- Second Release
    - improved the functionality of missingValues, and findOutliers function.
    - fixed the bugs in the analyzeData function.
