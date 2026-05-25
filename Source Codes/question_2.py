import pandas as pd

nobel_dataframe = pd.read_csv('nobel.csv')

def highest_usa_winner_decade(df) -> int | None:
    df['decade'] = (df['year'] // 10) * 10
    total_decade = df.groupby('decade').size()
    usa_born = df[df['birth_country'] == 'United States of America']
    usa_decade = usa_born.groupby('decade').size()
    ratio = (usa_decade / total_decade)
    return ratio.idxmax()

max_decade_usa: int = highest_usa_winner_decade(nobel_dataframe)
print("=" * 110)
print("  Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?")
print("-" * 110)
print(f"  {max_decade_usa}s")
print("=" * 110)