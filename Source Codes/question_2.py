import pandas as pd

nobel_dataframe = pd.read_csv('nobel.csv')

def highest_usa_winner_decade(df) -> int | None:
    df['decade'] = (df['year'] // 10) * 10
    df['is_usa_born'] = df['birth_country'] == 'United States of America'
    decade_ratios = df.groupby('decade')['is_usa_born'].mean()
    return int(decade_ratios.idxmax())
max_decade_usa: int = highest_usa_winner_decade(nobel_dataframe)

max_decade_usa: int = highest_usa_winner_decade(nobel_dataframe)
print("=" * 110)
print("  Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?")
print("-" * 110)
print(f"  {max_decade_usa}s")
print("=" * 110)
