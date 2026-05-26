import pandas as pd

# I-load ang dataset
nobel = pd.read_csv("nobel.csv")

# I-filter ang mga babae at i-sort ayon sa taon
first_woman = nobel[nobel['sex'] == 'Female'].sort_values('year').iloc[0]

# I-save sa mga required variables
first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']

# Pwede mong i-print para makita ang resulta
print("First Woman Name:", first_woman_name)
print("First Woman Category:", first_woman_category)