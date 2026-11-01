#1--hiring problem with score---
import math

def secretary_problem(candidates):
    n = len(candidates)
    # Calculate 37% of candidates
    k = math.ceil(n / math.e) #or just say k=37
    
    # Find the best candidate among the observed candidates
    best_score = max(candidates[:k])
    best_number = candidates[:k].index(best_score) + 1
    
    print("Total Candidates =", n)
    print("Candidates Observed =", k)
    print("\nBest Candidate Among First", k, "Candidates")
    print("Candidate Number :", best_number)
    print("Candidate Score :", best_score)
    
    # Selection Phase
    for i in range(k, n):
        if candidates[i] > best_score:
            print("\nSelected Candidate")
            print("Candidate Number :", i + 1)
            print("Candidate Score :", candidates[i])
            return
        else:
            continue
            
    # If no suitable candidate is found
    print("\nNo better candidate was found.")
    print("Selecting the last candidate.")
    print("Candidate Number :", n)
    print("Candidate Score :", candidates[-1])

# Scores of 100 candidates
candidates = [
    45,67,89,56,78,65,91,54,72,88,
    63,57,81,69,74,92,53,61,85,77,
    66,58,83,79,68,71,87,64,55,76,
    82,59,84,73,62,90,70,75,90,60,
    80,86,67,72,88,54,65,79,91,58,
    74,83,69,77,56,81,63,87,71,66,
    92,55,78,84,60,73,89,57,82,68,
    76,94,61,85,70,80,64,90,59,86,
    75,67,93,72,88,54,81,69,77,62,
    95,74,83,58,71,87,65,79,91,87
]
secretary_problem(candidates)


#2----hiring problem with random------



import random
n= 10

canditates=list(range(1,n+1))
random.shuffle(canditates)

best = float('inf')
hires=0

print("Candidates order: ", canditates)

for i in range(n):
    print(f"Interview candidate rank : {canditates[i]}")

    if canditates[i]<best:
        best = canditates[i]
        hires+=1
        print(" -> hired")
    else:
        print(" -> rejected")

print("\nTotal interviews = ", n)
print("Total Hires = ",hires)
