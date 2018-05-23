# -*- utf-8 -*-
from mpi4py import MPI
from ga_functions import *
from utils import parse_input
import random
import sys

MASTER = 0

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


if rank == MASTER:
    input_data = sys.stdin.read()
    info = parse_input(input_data)    
else:
    info = None

info = comm.bcast(info, root=MASTER)

cities_names = info['cities'].keys()
paths = [''.join(random.sample(cities_names, len(cities_names))) for _ in range(int(info['size']))]

global_best = (float("inf"), '')

for i in range(int(info['iterations'])):
     paths = mutate(paths, info['mutation_probability'])
     paths = cross(paths)
     paths = reproduce(paths, info['cities'])
     
     best, average, worst = find_path_statistics(paths, info['cities'])
     if best[0] < global_best[0]:
         global_best = best
     
     
     #print(paths, best, average, worst)

results = comm.gather({'rank': rank, 'result': global_best}, root=MASTER)

if rank == MASTER:
    for result in results:
        print(result)
