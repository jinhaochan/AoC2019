import math
import pandas as pd


def recursive_count_upper(mass):
    if mass < 0:
        return 0

    return mass + recursive_count_upper(math.floor(mass / 3) - 2)

if __name__ == '__main__':
    test = 0 

    if test:
        res = recursive_count_upper(100756)
        print(res - 100756)
    else:
        df = pd.read_csv('input.txt', header=None)
        df.columns = ['values']

        df['result'] = df['values'].apply(lambda x: recursive_count_upper(x) - x)

        print(df['result'].sum())
