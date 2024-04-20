# this file performs pre-processing for machine learning in the form of feature
# selection and removing correlated features. It can also preform high level
# data cleaning, as there are functions that would the user to remove columns
# that may have been useful for EDA, but aren't useful for ML.
# Another purpose of this file is that it's not per se project specific,
# I can pass datasets for multiple projects through this file and it
# will generate dummy variables and delete unneeded features without
# much customization
import pandas as pd

# data import function


def import_data(csv_file: str) -> object:

    # function to import the data from a CSV file

    data_ml = pd.read_csv(csv_file)

    return (data_ml)


def delete_columns(data: object, column_list: list) -> object:

    data.drop(column_list, inplace=True, axis=1)

    return data


def add_dummies(data: object) -> object:

    # this function generates dummy variables and then
    # deletes the "default" column as we're going to be
    # predicting "paid"
    # this is the only function that's specific for the
    # lending dataset

    # add dummy variables to the data frame

    data = pd.get_dummies(data)

    data.rename(columns={'loan_status_Fully Paid': 'paid'}, inplace=True)
    data.rename(columns={'loan_status_Charged Off': 'default'}, inplace=True)

    columns = ['default']

    data.drop(columns, inplace=True, axis=1)

    return data


def find_correlations(data: object, threshold: float) -> list:

    # identify correlated features and then remove them from the
    # data 'data_ml' data frame

    correlated_features = set()

    # drop the target variable (paid) and others that
    # aren't just included for annualized return calculations
    # not for machine learning

    # columns to drop
    columns = ['paid', 'total_payments', 'net_gain']

    cordata = data.drop(columns, axis=1)

    cor_matrix = cordata.corr()

    for i in range(len(cor_matrix.columns)):
        for j in range(i):
            if abs(cor_matrix.iloc[i, j]) > threshold:
                colname = cor_matrix.columns[i]
                correlated_features.add(colname)

    return list(correlated_features)


def write_data(data: object, file_name: str):

    # writes data to a csv when passed a data frame and a string with the
    # file name

    data.to_csv(file_name, index=False)

    return (print('file processing complete'))


def main():
    ml_data = import_data('data/LC_2015_clean(4)_updated_April2022.csv')

    # list of columns to delete
    column_list = ['issue_d', 'emp_length',
                   'earliest_cr_line', 'addr_state',
                   'annual_inc', 'purpose', 'dti',
                   'total_pymnt', 'lost_principle',
                   'total_pymnt_inv', 'monthly_income',
                   'total_rec_late_fee', 'revol_bal',
                   'monthly_debt_payments',
                   'updated_monthly_debt_payments',
                   'total_rec_int', 'total_rec_prncp']
    data = delete_columns(ml_data, column_list)
    data = add_dummies(data)
    write_data(data, 'data/updated_lc_ML_ready_data_april2022.csv')


if __name__ == '__main__':
    main()
