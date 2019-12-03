import math
import pandas as pd


def count_upper(mass):
    return math.floor(mass / 3) - 2


if __name__ == '__main__':
    test = 1
    
    if test:
        res = count_upper(14)
        print(res)
    else:
        df = pd.read_csv('input.txt', header=None)
        df.columns = ['values']

        df['result'] = df['values'].apply(count_upper)

        print(df['result'].sum())
