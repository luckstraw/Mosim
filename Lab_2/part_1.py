population = 100000
growth_rate = 0.01

for year in range(1, 11):
    population += population * growth_rate
    print(f"Year {year}: Population = {int(population)}")

print("\n\n\n")