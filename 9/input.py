
import pandas as pd

df = pd.read_csv('california_housing_test.csv')

print(df[
    (df['population'] > 0) &
    (df['population'] < 500)
].median_house_value.mean())

min_population = df.population.min()
print(df[
    df['population'] == min_population
].households.max())