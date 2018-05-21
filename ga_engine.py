# -*- utf-8 -*-
from mpi4py import MPI
from ga_functions import *
import random
MASTER = 0

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


if rank == MASTER:
    cities = {
        # load cities from file or stdin
        'A': (0,0),
        'B': (1,1),
        'C': (2,2),
        'D': (3,3),
        'E': (4,4),
        'F': (5,5),
    }
    size = 10
    mutation_probability = 0.01
    info = {
        'cities': cities,
        'size': size,
        'mutation_probability': mutation_probability,
        'iterations': 100,
    }
else:
    info = None

info = comm.bcast(info, root=MASTER)

cities_names = info['cities'].keys()

paths = [''.join(random.sample(cities_names, len(cities_names))) for _ in range(info['size'])]

for i in range(info['iterations']):
     paths = mutate(paths, info['mutation_probability'])
     paths = cross(paths)
     paths = reproduce(paths, info['cities'])
 
     best, average, worst = find_path_statistics(paths, cities)
     
     print(paths, best, average, worst)






#results = comm.gather(ranks, root=MASTER)
