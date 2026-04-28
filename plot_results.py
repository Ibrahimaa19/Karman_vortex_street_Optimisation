#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# Lecture des fichiers
df_basic = pd.read_csv('strong_scaling_basic.csv')
df_opti = pd.read_csv('strong_scaling.csv')

# Extraction des données
mpi_basic = df_basic['MPI'].values
fom_basic = df_basic['FOM'].values

mpi_opti = df_opti['MPI'].values
fom_opti = df_opti['FOM'].values

# Calcul du speedup (référence = 1 MPI)
ref_basic = fom_basic[0]
ref_opti = fom_opti[0]

speedup_basic = [f / ref_basic for f in fom_basic]
speedup_opti = [f / ref_opti for f in fom_opti]

# Idéal linéaire (pour les MPI de la version optimisée)
ideal = mpi_opti

# ============================================================
# GRAPHIQUE 1 : Speedup (basique vs optimisée + idéal)
# ============================================================
plt.figure(figsize=(12, 7))
plt.plot(mpi_basic, speedup_basic, 'o-', color='red', linewidth=2, markersize=8, label='Version basique')
plt.plot(mpi_opti, speedup_opti, 'o-', color='blue', linewidth=2, markersize=8, label='Version optimisée')
plt.plot(ideal, ideal, 'k--', linewidth=1.5, alpha=0.5, label='Idéal linéaire')
plt.xlabel('Nombre de processus MPI', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.title('Comparaison du Speedup - Version basique vs optimisée', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('comparison_speedup.png', dpi=150)
plt.show()

# ============================================================
# GRAPHIQUE 2 : FOM (basique vs optimisée)
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
# AFFICHAGE DANS LE TERMINAL
# ============================================================
print("\n" + "="*50)
print("RÉSULTATS VERSION BASIQUE")
print("="*50)
print(df_basic.to_string(index=False))

print("\n" + "="*50)
print("RÉSULTATS VERSION OPTIMISÉE")
print("="*50)
print(df_opti.to_string(index=False))

print("\n" + "="*50)
print("SPEEDUP MAX")
print("="*50)
print(f"Basique : {max(speedup_basic):.2f}x")
print(f"Optimisée : {max(speedup_opti):.2f}x")
print("="*50)