"""
This file imports the csv file with the Lending Club data and does the
following:
1) High level cleaning as far as fixing data types, E.g. 19.29% is
converted to 0.1929
2) Subsets the data
3) Adds some basic measures E.g. debt to income after the loan is added,
current monthly debt payments, calculates net gain as loan amount - received
interest, principal and late fees. Net gain was calculated in this fashion
as it was a straight forward measure that didn't require using anticipated
principle + interest, as a customer who paid their loan back early would 
"technically" be counted as a loss, since 100% of principle would be paid
back, but less than the anticipated interest would've been paid. 
4) Fills in 0 for NaN in scenarios where it's a simple fix and doesn't
require a lot of analysis. E.g. NaNs for customers without a credit
card balance

Overall this file does a lot of the heavy lifting for subsetting and
cleaning the data in order to make the next level of feature engineering,
cleaning, EDA and machine learning simpler. The subsetted columns are based
on a preliminary analysis of the data, focusing on the columns that Lending
Club would've when the customer first applied for the loan and getting rid of
the columns that contained data gathered over the course of the customer paying
back the loan. 
"""

import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')


def import_data(file_name):

    # function that imports data file with Lending Club approved loan data

    lending = pd.read_csv(file_name, low_memory=False)

    return(lending)


def subset_data(df):

    lending_subset = df[['funded_amnt', 'term', 'int_rate', 'installment',
                         'grade', 'emp_length', 'home_ownership', 'annual_inc',
                         'verification_status', 'issue_d', 'loan_status',
                         'purpose', 'addr_state', 'dti', 'delinq_2yrs',
                         'earliest_cr_line', 'fico_range_low',
                         'inq_last_6mths', 'mths_since_last_delinq',
                         'open_acc', 'pub_rec', 'pub_rec_bankruptcies',
                         'revol_bal', 'revol_util', 'total_acc', 'total_pymnt',
                         'total_pymnt_inv', 'total_rec_prncp', 'total_rec_int',
                         'total_rec_late_fee', 'collections_12_mths_ex_med',
                         'application_type', 'acc_now_delinq',
                         'chargeoff_within_12_mths', 'acc_open_past_24mths',
                         'avg_cur_bal', 'delinq_amnt', 'mo_sin_old_rev_tl_op',
                         'mo_sin_rcnt_rev_tl_op', 'mo_sin_rcnt_tl', 'mort_acc',
                         'mths_since_recent_inq',
                         'mths_since_recent_revol_delinq',
                         'num_accts_ever_120_pd', 'num_il_tl',
                         'num_tl_120dpd_2m', 'pct_tl_nvr_dlq', 'tot_coll_amt',
                         'tot_cur_bal', 'total_bal_ex_mort']]

    return (lending_subset)


def fix_data_types(data):

    # Fix columns that are the wrong data type or have characters we
    # don't need like '%'

    # fix interest rate

    data.loc[:, 'int_rate'] = data.loc[:, 'int_rate'].\
             str.strip('%').astype('float64')
    data.loc[:, 'int_rate'] = data.loc[:, 'int_rate'] / 100

    # fix revolving utilization

    data.loc[:, 'revol_util'] = data.loc[:, 'revol_util'].\
        str.strip('%').astype('float64')
    data.loc[:, 'revol_util'] = data.loc[:, 'revol_util'] / 100

    # extract digit from employment length and
    # create column with employment in months

    data['emp_length'] = data.emp_length.str.extract(r'(\d+)')

    # got errors prior, so we'll drop the rows with "NaN" in
    # emp_length as it's critical to credit scoring

    data.dropna(subset=['emp_length'], inplace=True)

    # reset the data frame index since we deleted rows

    data.reset_index()

    # convert values in employment length column to integers

    data['emp_length'] = data['emp_length'].astype(int)

    # create new column with employment length in months

    data.loc[:, 'emp_length_months'] = data.loc[:, 'emp_length'] * 12

    # convert the DTI column to a decimal

    data.loc[:, 'dti_dec'] = data.loc[:, 'dti'] / 100

    # convert issue date and earliest credit line columns to dates
    # used dt.floor to just extract the date due to receiving out
    # of bounds errors via the typical pandas date conversion methods

    data['issue_d'] = pd.to_datetime(data['issue_d'],
                                     format='%b-%y',
                                     errors='coerce').dt.floor('D')

                                     
    data['earliest_cr_line'] = pd.to_datetime(data['earliest_cr_line'],
                                              format='%b-%y',
                                              errors='coerce').dt.floor('D')

    # create length of credit history column in months

    data['length_of_credit_history'] = ((data['issue_d'] -
                                         data['earliest_cr_line'])
                                        / np.timedelta64(1, 'M'))

    data['length_of_credit_history'] =\
        data['length_of_credit_history'].astype(int)

    return data


def fix_dates(data):

    # common for dates to mistakenly get entered in as
    # "future dates" for earliest credit line this function removes those rows

    data = data[(data['length_of_credit_history'] >= 0)]

    return(data)


def measures(data):

    # calculate monthly income

    data.loc[:, 'monthly_income'] = (data.loc[:, 'annual_inc'] / 12)

    # calculate monthly debt payments

    data.loc[:, 'monthly_debt_payments'] = (data.loc[:, 'dti_dec'] *
                                            data.loc[:, 'monthly_income'])

    # monthly debt payments cost loan

    data.loc[:, 'updated_monthly_debt_payments'] = (data.loc[:,
                                                    'monthly_debt_payments']
                                                    + data.loc[:,
                                                    'installment'])

    # calculate lost principle (defaulted loans)

    data.loc[:, 'lost_principle'] = (data.loc[:, 'funded_amnt']
                                     - data.loc[:, 'total_rec_prncp'])

    # calculate # of payments received per loan

    data.loc[:, 'total_payments'] = (data.loc[:, 'total_pymnt']
                                     / data.loc[:, 'installment'])

    # updated DTI

    data.loc[:, 'post_loan_dti'] = (data.loc[:,
                                    'updated_monthly_debt_payments']
                                    / data.loc[:, 'monthly_income'])

    data.loc[:, 'net_gain'] = ((data.loc[:,'total_rec_prncp'] + data.loc[:,'total_rec_int'] +\
         data.loc[:,'total_rec_late_fee']) -  data.loc[:, 'funded_amnt'])

    return data



def fix_na(data):

    # fill in NaNs with zeroes for those columns as they won't require
    # data transforms E.g. situations like months since last delinquency
    # where having a zero is better than but 30 is better 1, but not as
    # good as having had zero delinquencies.

    # the zeros are customers without credit card balances
    data.loc[:, 'revol_util'].fillna(0, inplace=True)

    # similar to the above, if there are no inquiries, when the
    # credit is pulled no data comes across so a NaN occurs, at
    # least that's the working presumption

    data.loc[:, 'mths_since_recent_inq'].fillna(0, inplace=True)

    # if you have had no significant past dues, there would be nothing
    # to enter, hence the NaNs. This was verified by digging through the data,
    # customers with NaNs here had higher FICO scores and zeroes in
    # related columns

    data.loc[:, 'num_tl_120dpd_2m'].fillna(0, inplace=True)

    return data


def write_file(data, filename):

    data.to_csv(filename, date_format='%Y-%m-%d', index=False)

    return (print('file processing complete'))


def main():
    lending = import_data('data/LC_2015_Data.csv')
    subset = subset_data(lending)
    fixed_data = fix_data_types(subset)
    fixed_data = fix_dates(fixed_data)
    final_data = measures(fixed_data)
    final_data = fix_na(final_data)
    write_file(final_data, 'data/processed_2015_loan_data_april22.csv')


if __name__ == '__main__':
    main()
