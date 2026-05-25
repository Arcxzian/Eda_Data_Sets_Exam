def max_female_laureate_decade(df) -> dict | None:
    df = df.copy()
    df['decade'] = (df['year'] // 10) * 10
    decades = df['decade'].unique()
    categories = df['category'].unique()
    best_proportion = -1
    best_decade = None
    best_category = None
    for decade in decades:
        for category in categories:
            is_decade = df['decade'] == decade
            is_category = df['category'] == category
            group = df[is_decade & is_category]
            if len(group) == 0:
                continue
            is_female = group['sex'] == 'Female'
            proportion = float(is_female.mean())
            if proportion > best_proportion:
                best_proportion = proportion
                best_decade = int(decade)
                best_category = str(category)
    return [{best_decade: best_category}]

max_female_dict: dict = max_female_laureate_decade(nobel_dataframe)
decade = list(max_female_dict[0].keys())[0]
category = max_female_dict[0][decade]
print("=" * 55)
print("    Nobel Prize: Highest Female Laureate Proportion")
print("=" * 55)
print(f"  Decade   : {decade}s")
print(f"  Category : {category}")
print("=" * 55)