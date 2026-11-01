#1-------Set Covering Approx------

universe = {1, 2, 3, 4, 5}

sets = {
    "S1": {1, 2, 3},
    "S2": {2, 4},
    "S3": {3, 4, 5},
    "S4": {5}
}

uncovered = set(universe)
selected = []

while uncovered:

    best_set = max(
        sets,
        key=lambda s: len(sets[s] & uncovered)
    )

    selected.append(best_set)

    uncovered -= sets[best_set]

    del sets[best_set]

print("Selected sets:", selected)
print("All elements are covered.")



#2------Subset Sum Approx-----

numbers = [3, 5, 7, 10, 12]

target = 15

numbers.sort(reverse=True)

subset = []
total = 0

for num in numbers:

    if total + num <= target:
        subset.append(num)
        total += num

print("Numbers:", numbers)
print("Target:", target)
print("Selected subset:", subset)
print("Subset sum:", total)




#3-----Vertex Cover Approx---



edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D")
]

cover = []

while edges:

    u, v = edges[0]

    cover.append(u)
    cover.append(v)

    edges = [
        edge for edge in edges
        if u not in edge and v not in edge
    ]

print("Vertex Cover:", cover)
print("Number of vertices:", len(cover))
