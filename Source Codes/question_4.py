import pandas as pd

nobel = pd.read_csv("nobel.csv")

first_woman = nobel[nobel['sex'] == 'Female'].sort_values('year').iloc[0]

first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']

print("First Woman Name:", first_woman_name)
print("First Woman Category:", first_woman_category)