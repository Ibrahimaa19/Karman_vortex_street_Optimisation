#!/bin/bash

DATE=$(date +"%Y%m%d_%H%M%S")
mkdir -p perf

echo "=== Test $DATE ==="

echo "=== perf stat ==="
perf stat -e cycles,instructions,cache-misses,cache-references,L1-dcache-load-misses \
         mpirun -np 2 ./build/top.lbm-exe config.txt &> perf/perf_stat_${DATE}.txt

echo "=== perf record ==="
perf record -e cycles -F 999 -g -o perf/perf_${DATE}.data \
         mpirun -np 2 ./build/top.lbm-exe config.txt &> /dev/null

echo "=== perf report ==="
perf report -i perf/perf_${DATE}.data --stdio &> perf/perf_report_${DATE}.txt

echo "Terminé. Fichiers dans perf/ avec préfixe ${DATE}"