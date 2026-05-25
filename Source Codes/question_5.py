
import pandas as pd

nobel_dataframe = pd.read_csv('nobel.csv')

def get_repeat_nobel_winners(df: pd.DataFrame) -> list:

    winner_counts = df['full_name'].value_counts()

    repeats = winner_counts[winner_counts >= 2].index.tolist()
    
    return repeats

repeat_list: list[str] = get_repeat_nobel_winners(nobel_dataframe)

print("=" * 110)
print("  Which individuals or organizations have won more than one Nobel Prize throughout the years?")
print("-" * 110)

for winner in repeat_list:
    print(f"  • {winner}")

print("=" * 110)