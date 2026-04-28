#!/bin/bash
# strong_scaling.sh

echo "MPI,FOM,Time(s)" > strong_scaling.csv

for mpi in 1 2 4 6 8 10 12 14 16; do
    echo -n "MPI=$mpi ... "
    export OMP_NUM_THREADS=1
    
    # Exécuter et capturer la sortie complète
    output=$( { time mpirun -np $mpi --bind-to core ./build/top.lbm-exe config_test.txt; } 2>&1 )
    
    # Extraire FOM
    fom=$(echo "$output" | grep "FOM:" | awk '{print $2}')
    
    # Extraire le temps réel (format 0m0.000s ou 0.000s)
    real_time=$(echo "$output" | grep "real" | awk '{print $2}' | sed 's/[ms]//g' | tr ',' '.')
    
    # Si format avec 'm' (minutes)
    if [[ $real_time == *"m"* ]]; then
        minutes=$(echo $real_time | cut -d'm' -f1)
        seconds=$(echo $real_time | cut -d'm' -f2)
        real_time=$(echo "$minutes * 60 + $seconds" | bc)
    fi
    
    echo "$mpi,$fom,$real_time" >> strong_scaling.csv
    echo "FOM=$fom, Time=${real_time}s"
done

cat strong_scaling.csv