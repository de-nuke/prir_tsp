import sys
from utils import parse_input
from ga_functions import *
from itertools import permutations

text = sys.stdin.read()

info = parse_input(text)

cities = info['cities'].keys()

paths = list(permutations(cities, len(cities)))

best = float("inf")
best_path = 'dupa'
for path in paths:
    dist = path_distance(path, info['cities'])
    if dist < best:
        best = dist
        best_path = path
print(best, best_path)
