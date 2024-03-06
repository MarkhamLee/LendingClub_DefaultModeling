import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class EDA:

    def calc_performance(self, df: object):

        # this method takes a data frame with loan information as an input
        # and then calculates high level performance metrics with respect
        # to investment gains.

        columns = ['total_loan_value', 'total_net_gains', 'avg_interest rate',
                   'avg_loan_amount', 'avg_gains($)', 'avg_gains(%)',
                   'annualized_return']

        self.perf_df = pd.DataFrame(columns=columns)

        self._output_list = []

        # this function calculates high level data like average interest,
        # loan size, net gains and annualized returns

        # calculate total loan value
        total_loans = df['funded_amnt'].sum()

        # calculate total gains
        total_gains = df['net_gain'].sum()

        # default rate
        # default_rate = df['paid'].mean()

        # calculate average interest rate
        avg_interest_rate = 100 * df['int_rate'].mean()

        # calculate average loan size
        avg_loan_size = df['funded_amnt'].mean()

        # calculate average gains in terms of dollars earned
        avg_gains = df['net_gain'].mean()

        # calculate average gains in terms of %
        avg_gains_per = 100 * (avg_gains/avg_loan_size)

        avg_total_payments = df['total_payments'].mean()

        gains_dec = avg_gains_per / 100

        # multiply total payments by 30 to get the approximate # of days
        days = avg_total_payments * 30

        # calculate annualized return
        annualized_return = (((1 + gains_dec) ** (365/days)) - 1) * 100

        # add calculations to output list

        self._output_list = [total_loans, total_gains, avg_interest_rate,
                             avg_loan_size, avg_gains, avg_gains_per,
                             annualized_return]

        return self.add_df(self._output_list, self.perf_df,)

    def add_df(self, data: object, df: object) -> object:

        # provided with a list and a data frame this method will
        # insert that list as a row in that data frame

        # convert list to series

        list_series = pd.Series(data, index=df.columns)

        df = df.append(list_series, ignore_index=True)

        self._df = df.round(3)

        return self._df

    def find_correlations(self, data: object, threshold: float) -> list:

        # identify correlated features and then remove them from the
        # data 'data_ml' data frame

        self._correlated_features = set()

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
                    self._correlated_features.add(colname)

        return list(self._correlated_features)

    def subset_data(self, data: object, removal_list: list) -> object:

        self._data = data

        # this function will remove the correlated features from the dataset
        # inputs: data frame, removal list from prior function
        # this and the other function will built to be reusable for a
        # variety of projects and to avoid errors related to typing
        # in column name by hand this column can also be generally
        # used to remove any column from a data frame

        self._data.drop(removal_list, inplace=True,  axis=1)

        return self._data

    def add_column(self, col_list: list, data: object, position: int,
                   title: str) -> object:

        self._data = data

        self._data.insert(position, title, col_list, True)

        return self._data

    def update_index(self, add_list: list, df: object) -> object:

        df_index = []

        performance_df = pd.DataFrame(columns=['avg_interest_rate',
                                               'avg_loan_amount',
                                               'avg_interest_received',
                                               'avg_gains($)',
                                               'avg_gains(%)',
                                               'avg_total_payments',
                                               'annualized_return'])

        # update existing index list with new elements,
        # requires passing a list of values for
        # the index, as well as data rame being adjusted

        df_index.extend(add_list)

        # update performance data frame index

        df = df.index = df_index

        return performance_df

    # function that will append two data frames together
    def append_df(self, df1: object, df2: object) -> object:

        df1 = df1.append(df2, ignore_index=True)

        return df1

    # function that will create two side by side violin plots showing
    # the distribution of a variable on the Y axis vs a categorical
    # variable on the x axis. This function is used by passing a data frame,
    # plus the column label for the x and y axis.
    def violin_plot(self, x: object, y: object, data: object, title: str):

        ax = sns.violinplot(x=x, y=y, inner='quartile', data=data)
        ax.set_title(title, fontsize=16)

        return ax

    # data frame for counting # of items of a particular category
    # e.g. % defaults vs. paid off for loans
    def categorical_count(self, data: object, category: str) -> list:

        # generate a new df with a count of each category

        cat_count = pd.DataFrame(data[category].value_counts())

        # reset index and fix column labels

        cat_count = cat_count.reset_index()

        cat_count.rename(columns={category: 'count'}, inplace=True)
        cat_count.rename(columns={'index': category}, inplace=True)

        # calculate # of items so we can calculate % of total

        total_items = len(data)

        # add % of total

        cat_count['per_of_total'] = cat_count['count'] / total_items

        return cat_count

    # this function will put a range of values into bins,
    # useful for doing things like comparing an outcome (like loan status)
    # vs an income or interest rate range
    # the input variables are data = the data frame, freq = intervals the vales
    # sliced by. Value is the column in the data frame we're putting into bins
    def make_bins(self, data: object, freq: float, value) -> object:

        # get minimum and maximum values
        lowest = data[value].min()
        highest = data[value].max()

        # create bins
        bins = pd.interval_range(start=lowest, freq=freq, end=highest,
                                 closed='left')

        bin_column = value + '_bin'

        data[bin_column] = pd.cut(data[value], bins=bins)

        # group by bins and use .mean() to get the default rate for each
        bin_df = data.groupby(bin_column).mean()
        bin_df = bin_df.round(3)

        return bin_df

        # this function will generate line plots
    def line_plot(self, data: object, x: object, y: object,
                  title: str) -> object:

        sns.lineplot(data=data, x=x, y=y)
        plt.title(title)

    def default_by_category(self, data: object, category: str) -> object:

        data = pd.get_dummies(data, columns=['loan_status'])

        # update the column names
        data.rename(columns={'loan_status_Charged Off': 'default'},
                    inplace=True)
        data.rename(columns={'loan_status_Fully Paid': 'paid'}, inplace=True)

        # group by category
        data = data.groupby(category).mean()

        return data
