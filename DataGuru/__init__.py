import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats

'''------------------------------------------------------ Missing Values------------------------------------------------------'''


def missingValues(data):
    variable_name = []
    total_value = []
    total_missing_value = []
    missing_value_rate = []
    unique_value_list = []
    total_unique_value = []
    data_type = []

    for col in data.columns:
        variable_name.append(col)
        data_type.append(data[col].dtype)
        total_value.append(data[col].shape[0])
        total_missing_value.append(data[col].isnull().sum())
        missing_value_rate.append(
            round(data[col].isnull().sum() / data[col].shape[0], 4))
        unique_value_list.append(data[col].unique())
        total_unique_value.append(len(data[col].unique()))

    missing_data = pd.DataFrame({
        "Variable": variable_name,
        "Total Value": total_value,
        "Total Missing Value": total_missing_value,
        "Missing Value Rate": missing_value_rate,
        "Data Type": data_type,
        "Unique Value": unique_value_list,
        "Total Unique Value": total_unique_value
    })

    missing_data = missing_data.set_index("Variable")
    missing_data = missing_data[missing_data["Total Missing Value"] > 0]
    return missing_data.sort_values("Total Missing Value", ascending=False)


'''------------------------------------------ detect Outliers -----------------------------------------------------'''


def detect_outliers_zscore(data):
    z_scores = stats.zscore(data)
    threshold = 3
    outliers_mask = np.abs(z_scores) > threshold
    return outliers_mask


def detect_outliers_iqr(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers_mask = (data < lower_bound) | (data > upper_bound)
    return outliers_mask


def findOutliers(data, method='zscore'):
    numeric_columns = data.select_dtypes(include=np.number).columns.tolist()
    outliers_data = pd.DataFrame(
        columns=['Column', 'Mean', 'Standard Deviation', 'Outliers'])

    for col in numeric_columns:
        mean = np.mean(data[col])
        std = np.std(data[col])
        outliers = []

        if method == 'zscore':
            outliers_mask = detect_outliers_zscore(data[col])
        elif method == 'iqr':
            outliers_mask = detect_outliers_iqr(data[col])
        else:
            raise ValueError("Invalid outlier detection method.")

        outliers = data[col][outliers_mask]

        if len(outliers) > 0:
            outliers = outliers.sort_values()
            outliers_data = outliers_data.append({
                'Column': col,
                'Mean': mean,
                'Standard Deviation': std,
                'Outliers': outliers,
            }, ignore_index=True)

    if outliers_data.empty:
        return outliers_data
    else:
        outliers_data['Total Outliers'] = outliers_data['Outliers'].apply(len)
        outliers_data['Percentage of Outliers'] = (
            outliers_data['Total Outliers'] / data.shape[0]) * 100
        outliers_data.reset_index(drop=True, inplace=True)
        outliers_data.sort_values(
            by='Percentage of Outliers', ascending=False, inplace=True)
        return outliers_data


'''------------------------------------------------------- analyze the Data -------------------------------------------------------------'''


def analyze_column(data, numCol, catCol):
    grouped_data = data.groupby(catCol)
    mean = grouped_data[numCol].mean()
    std = grouped_data[numCol].std()
    total = grouped_data.size().sum()
    percentage = grouped_data.size() / total * 100

    result_df = pd.DataFrame(
        {'Mean': mean, 'Standard Deviation': std, 'Percentage': percentage})
    return result_df


def analyzeData(data, numCol, catCol):
    analysis_result = analyze_column(data, numCol, catCol)
    analysis_result = analysis_result.sort_values('Mean', ascending=False)
    print(f"Analysis for column '{numCol}':")
    print(analysis_result)
    print()

    fig = px.bar(analysis_result, x=analysis_result.index, y=[
                 'Mean', 'Standard Deviation', 'Percentage'], labels={'value': 'Value', 'variable': 'Metric'})

    texts = [analysis_result['Mean'],
             analysis_result['Standard Deviation'], analysis_result['Percentage']]
    for i, t in enumerate(texts):
        fig.data[i].text = t.round(2).astype(str) + '%'
        fig.data[i].textposition = 'outside'

    fig.update_layout(
        title={
            'text': f"Analysis for column '{catCol}'",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        yaxis_title=numCol,
        xaxis_title=catCol,
        barmode='group',
        legend_title='Metric',
        autosize=False,
        width=1200,
        height=500
    )

    fig.show()
