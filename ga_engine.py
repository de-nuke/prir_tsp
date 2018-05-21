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
    size = 3
    mutate = 0.01
    info = {
        'cities': cities,
        'size': size,
        'mutate': mutate,
    }
else:
    info = None

info = comm.bcast(info, root=MASTER)

cities_names = info['cities'].keys()

paths = [''.join(random.sample(cities_names, len(cities_names))) for _ in range(info['size'])]

print(paths)

paths = crossover(paths)
print(paths)

#results = comm.gather(ranks, root=MASTER)
#print("Po barierze")
#print("rank = {} -> {}".format(rank, results))



#print('rank',rank,paths)
