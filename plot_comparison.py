#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# Lecture des fichiers
df_basic = pd.read_csv('strong_scaling_basic.csv')
df_opti = pd.read_csv('strong_scaling.csv')

# Extraction des données
mpi_basic = df_basic['MPI'].values
fom_basic = df_basic['FOM'].values
time_basic = df_basic['Time(s)'].values

mpi_opti = df_opti['MPI'].values
fom_opti = df_opti['FOM'].values
time_opti = df_opti['Time(s)'].values

# ============================================================
# GRAPHIQUE 1 : Comparaison FOM
# ============================================================
plt.figure(figsize=(12, 7))
plt.plot(mpi_basic, fom_basic, 'o-', color='red', linewidth=2, markersize=8, label='Version basique')
plt.plot(mpi_opti, fom_opti, 'o-', color='blue', linewidth=2, markersize=8, label='Version optimisée')
plt.xlabel('Nombre de processus MPI', fontsize=12)
plt.ylabel('FOM (MLUPS)', fontsize=12)
plt.title('Comparaison des performances - FOM', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('comparison_fom.png', dpi=150)
plt.show()

# ============================================================
# GRAPHIQUE 2 : Comparaison Temps d'exécution
# ============================================================
plt.figure(figsize=(12, 7))
plt.plot(mpi_basic, time_basic, 'o-', color='red', linewidth=2, markersize=8, label='Version basique')
plt.plot(mpi_opti, time_opti, 'o-', color='blue', linewidth=2, markersize=8, label='Version optimisée')
plt.xlabel('Nombre de processus MPI', fontsize=12)
plt.ylabel('Temps d\'exécution (secondes)', fontsize=12)
plt.title('Comparaison des performances - Temps d\'exécution (100 itérations)', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('comparison_time.png', dpi=150)
plt.show()

# ============================================================
# RÉSULTATS DÉTAILLÉS
# ============================================================
print("\n" + "="*60)
print("COMPARAISON DÉTAILLÉE")
print("="*60)

print("\n--- VERSION BASIQUE ---")
for i in range(len(mpi_basic)):
    print(f"MPI={mpi_basic[i]:2d} : FOM={fom_basic[i]:6.2f} MLUPS, Temps={time_basic[i]:6.2f} s")

print("\n--- VERSION OPTIMISÉE ---")
for i in range(len(mpi_opti)):
    print(f"MPI={mpi_opti[i]:2d} : FOM={fom_opti[i]:6.2f} MLUPS, Temps={time_opti[i]:6.2f} s")

# Gain global
gain_fom = fom_opti[-1] / fom_basic[0]
gain_time = time_basic[0] / time_opti[-1]
print(f"\n--- GAIN GLOBAL ---")
print(f"FOM : ×{gain_fom:.1f} (de {fom_basic[0]:.2f} à {fom_opti[-1]:.2f} MLUPS)")
print(f"Temps : ×{gain_time:.1f} (de {time_basic[0]:.2f} à {time_opti[-1]:.2f} s)")

print("\n" + "="*60)
print("Fichiers générés :")
print("  - comparison_fom.png")
print("  - comparison_time.png")
print("="*60)