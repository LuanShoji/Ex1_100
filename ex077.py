t = ("Palio", "Fox", "Polo", "Honda Civic", "Suzuki Swift", "Gol", "CB500F")
for c in t:
    print(f"\nNa palavra {c} temos", end=" ")
    for a in c:
        if a in "aeiou":
            print(a, end=" ")

