import pandas as pd

nobel = pd.read_csv('nobel.csv')


def get_top_gender_and_country(data):
    top_gender = data['sex'].value_counts().idxmax()
    top_country = data['birth_country'].value_counts().idxmax()
    return top_gender, top_country


top_gender, top_country = get_top_gender_and_country(nobel)
print("\n")
print("="*50)
print("What is the most awarded gender and birth country?")
print("="*50)
print(f"Top Gender:  {top_gender}")
print(f"Top Country: {top_country}")
print("="*50)
