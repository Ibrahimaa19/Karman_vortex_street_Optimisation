#!/bin/bash

# Ficher de résultats
RESULTS="benchmark_fixed.csv"
echo "Type,MPI,OMP,Total,FOM" > $RESULTS

# Utiliser toujours le meme executable
EXE="./build/top.lbm-exe"

# Configurations (max 8 threads)
CONFIGS="
MPI,8,1,8
MPI,4,1,4
MPI,2,1,2
MPI,1,1,1
OpenMP,1,2,2
OpenMP,1,4,4
OpenMP,1,8,8
Hybrid,4,2,8
Hybrid,2,4,8"

for cfg in $CONFIGS; do
    type=$(echo $cfg | cut -d, -f1)
    mpi=$(echo $cfg | cut -d, -f2)
    omp=$(echo $cfg | cut -d, -f3)
    total=$(echo $cfg | cut -d, -f4)
    
    export OMP_NUM_THREADS=$omp
    export OMP_PLACES=cores
    export OMP_PROC_BIND=close
    
    echo -n "$type $mpi,$omp ... "
    
    output=$(mpirun -np $mpi --bind-to core $EXE config.txt 2>&1)
    fom=$(echo "$output" | grep "FOM:" | awk '{print $2}')
    
    echo "$type,$mpi,$omp,$total,$fom" >> $RESULTS
    echo "FOM=$fom"
done

echo ""
echo "=== RÉSULTATS ==="
column -t -s, $RESULTS