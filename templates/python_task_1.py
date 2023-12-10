import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here

df = pd.read_csv('dataset-1.csv')
def generate_car_matrix(dataset):
result_df = data.pivot(index='id_1', columns='id_2', values='car')
result_df.fillna(0, inplace=True)
result_df.values[[range(len(result_df))], [range(len(result_df))]] = 0
return result_df
new_df = generate_car_matrix(df)
print(new_df)


    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
df = pd.read_csv('dataset-1.csv')
def generate_car_matrix(dataset):
result_df = data.pivot(index='id_1', columns='id_2', values='car')
result_df.fillna(0, inplace=True)
result_df.values[[range(len(result_df))], [range(len(result_df))]] = 0
return result_df
new_df = generate_car_matrix(df)
print(new_df)

    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
import pandas as pd
def get_bus_indexes(df):
mean_bus = df['bus'].mean()
indices = df[df['bus'] > 2 * mean_bus].index.tolist()
return sorted(indices)

    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

def filter_routes(df):
route_avg = df.groupby('route')['truck'].mean()
routes_greater_than_7 = route_avg[route_avg > 7].index.tolist()
return sorted(routes_greater_than_7)


    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

def multiply_matrix(result_df):
modified_df = result_df.copy()
modified_df = modified_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
modified_df = modified_df.round(1)
return modified_df

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    def check_time_completeness(df):
df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
df['duration'] = df['end_timestamp'] - df['start_timestamp']
grouped = df.groupby(['id', 'id_2'])
completeness_check = grouped.apply(lambda x: (
(x['duration'].min() >= pd.Timedelta(days=1)) and
(x['duration'].max() <= pd.Timedelta(days=1, seconds=1)) and
(x['start_timestamp'].dt.dayofweek.nunique() == 7)
))
return completeness_check

    return pd.Series()
