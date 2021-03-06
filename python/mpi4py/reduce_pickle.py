#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Jérémie DECOCK (http://www.jdhp.org)

# run:
#   mpirun -np 4 python3 reduce_pickle.py
#     or
#   mpiexec -n 4 python3 reduce_pickle.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

data = rank

result = comm.reduce(data, op=MPI.SUM, root=0)

print("process", rank, ":", data, result)

