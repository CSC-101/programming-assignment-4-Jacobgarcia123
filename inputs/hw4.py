def print_county_info(counties):
    for county in counties:
        print(f"County: {county['County']}, State: {county['State']}")
        print(f" Education (Bachelors Degree or Higher):{county['Education.Bachelor\'s Degree or Higher']}%")
        print(f" Income(Persons Below Poverty Level): {county['Income.Persons Below Poverty Level']}%")
        print(f" Total Population: {county['Population']}")
        print(f" Ethnicities:")
        print(f" Asian Alone: {county['Ethnicities.Asian Alone']}%")
        print(f" Black Alone: {county['Ethnicities.Black Alone']}%")
        print(f" White Alone: {county['Ethnicities.White Alone']}%")

