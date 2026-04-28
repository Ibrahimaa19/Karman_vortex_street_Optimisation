#!/bin/bash

export OMP_NUM_THREADS=1

echo "MPI,Time(s),FOM,Special(s),Collision(s),Halo(s),Propagation(s)" > wtime_results.csv

for mpi in 1 2 4 8 16 28; do
    echo -n "Test MPI=$mpi ... "
    
    output=$(mpirun -np $mpi ./build/top.lbm-exe config.txt 2>&1)
    
    time=$(echo "$output" | grep "Total" | awk '{print $3}')
    fom=$(echo "$output" | grep "FOM: " | awk '{print $2}')
    special=$(echo "$output" | grep "Special" | awk '{print $3}')
    collision=$(echo "$output" | grep "Collision" | awk '{print $3}')
    halo=$(echo "$output" | grep "Halo" | awk '{print $3}')
    propagation=$(echo "$output" | grep "Propagation" | awk '{print $3}')
    
    echo "$mpi,$time,$fom,$special,$collision,$halo,$propagation" >> wtime_results.csv
    echo "FOM=$fom, Time=${time}s"
done

cat wtime_results.csv