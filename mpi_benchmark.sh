#!/bin/bash

export OMP_NUM_THREADS=1

echo "MPI,FOM" > mpi_benchmark.csv

for mpi in 1 2 4 6 8 10 12 14 16; do
    echo -n "MPI=$mpi ... "
    
    output=$(mpirun -np $mpi --bind-to core ./build/top.lbm-exe config.txt 2>&1)
    fom=$(echo "$output" | grep "FOM:" | awk '{print $2}')
    
    echo "$mpi,$fom" >> final_results.csv
    echo "$fom MLUPS"
done

echo ""
echo "=== MEILLEUR RÉSULTAT ==="
sort -t, -k2 -rn mpi_benchmark.csv | head -1